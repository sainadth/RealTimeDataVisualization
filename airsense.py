import time
import streamlit as st
import pandas as pd
import json
import requests
import os
from dotenv import load_dotenv
from streamlit_folium import st_folium
import folium
from folium.plugins import MarkerCluster
import altair as alt

# Setup
load_dotenv()
PURPLE_AIR_API_KEY = os.getenv("PURPLE_AIR_API_KEY")
st.set_page_config(page_title="Airsense", layout="wide")  # Ensure wide layout

# Helpers
@st.cache_data
def load_sensors():
    with open('sensors/nearbysensors.json', 'r') as f:
        sensors_data = json.load(f)
    df = pd.DataFrame(sensors_data)
    df = df[['sensor_index', 'name', 'latitude', 'longitude']].dropna()
    df['name'] = df['name'].str.strip()
    return df

@st.cache_data
def create_dict(df):
    return {(row['latitude'], row['longitude']): [row['sensor_index'], row['name']] for _, row in df.iterrows()}

def get_data(sensor_index):
    url = f"https://api.purpleair.com/v1/sensors/{sensor_index}/history"
    params = {"fields": "pm2.5_alt", "start_timestamp": int((pd.Timestamp.now() - pd.Timedelta(days=3)).timestamp())}
    try:
        res = requests.get(url, headers={"X-API-Key": PURPLE_AIR_API_KEY}, params=params)
        res.raise_for_status()
        return res.json()
    except Exception as e:
        st.error(f"API error: {e}", icon="🚨")
        return None

# Data & State
_, titleCol, _ = st.columns([1, 3, 1])
with titleCol:
    # st.image("assets/logo.png", width=200)
    st.markdown(
        """
        <h1 style="text-align: center; color: #2c3e50;">Airsense</h1>
        <p style="text-align: center; color: #34495e;">Monitor your air quality with ease</p>
        """,
        unsafe_allow_html=True
    )
    
# Load sensors
df_sensors = load_sensors()

# Create sensor dictionary
sensor_dict = create_dict(df_sensors)

# add line break
st.markdown("<br>", unsafe_allow_html=True)

charcol, mapcol = st.columns([3, 2])

# Map
m = folium.Map(location=[27.8, -97.3], zoom_start=10)
marker_cluster = MarkerCluster().add_to(m)
for _, row in df_sensors.iterrows():
    folium.Marker(
        location=[row['latitude'], row['longitude']],
        popup=folium.Popup(f"<b>Sensor:</b> {row['name']}<br><b>Index:</b> {row['sensor_index']}", max_width=300),
        tooltip=f"Sensor: {row['name']}"  # Tooltip to activate on hover
    ).add_to(marker_cluster)

with mapcol:
    st_data = st_folium(m, width=500, height=350)  # Reduce map dimensions to fit

# Session init
st.session_state.setdefault("sensors_selected", [])
st.session_state.setdefault("sensor_data_selected", [])
st.session_state.setdefault("chart_dirty", False)
st.session_state.setdefault("last_clicked_location", None)
dirty_time = 0

# Handle clicks
clicked = st_data.get("last_object_clicked")
if clicked and clicked != st.session_state.last_clicked_location:
    st.session_state.last_clicked_location = clicked
    lat, lon = clicked["lat"], clicked["lng"]
    sensor_info = sensor_dict.get((lat, lon))

    if sensor_info:
        sensor_index, sensor_name = sensor_info[0], sensor_info[1].strip()
        existing_sensor_indices = [s[0] for s in st.session_state.sensors_selected]

        # Check if the sensor is already selected
        if sensor_index in existing_sensor_indices:
            # Remove existing data for the sensor
            index = existing_sensor_indices.index(sensor_index)
            del st.session_state.sensors_selected[index]
            del st.session_state.sensor_data_selected[index]

        # Fetch new data and append it
        data = get_data(sensor_index)
        if data and 'data' in data and data['data']:
            print(f"Sensor {sensor_name} data fetched successfully.", len(data['data']))
            df = pd.DataFrame(data['data'], columns=['timestamp', 'value'])
            df['timestamp'] = pd.to_datetime(df['timestamp'], unit='s')
            st.session_state.sensors_selected.append([sensor_index, sensor_name])
            st.session_state.sensor_data_selected.append(df)
            st.session_state.chart_dirty = True  # Ensure chart_dirty is set
        else:
            with charcol:
                st.info("No data for this sensor.", icon="⚠️")
    print("Dirty", st.session_state.chart_dirty)

# Prepare chart data
if st.session_state.chart_dirty:
    print("Processing data...\n\n\n")
    dirty_time = 2
    dfs = [df.assign(sensor=st.session_state.sensors_selected[i][1])
           for i, df in enumerate(st.session_state.sensor_data_selected)
           if not df.empty and df.shape[1] > 0]
    print(f"Dataframes to process: {len(dfs)}")
    if dfs:
        combined = pd.concat(dfs, ignore_index=True)
        combined = combined.groupby(['timestamp', 'sensor']).mean().reset_index()
        pivot_data = combined.pivot(index='timestamp', columns='sensor', values='value')
        pivot_data = pivot_data.dropna(how='all').ffill().bfill().tail(500)
        print(f"Pivot data shape: {pivot_data.shape}")
        print(pivot_data.head())
        st.session_state.pivot_data = pivot_data
        st.session_state.chart_dirty = False  # Reset chart_dirty after processing
    else:
        st.session_state.pivot_data = None  # Handle case where no valid data exists

# Show chart
with charcol:
    print("Loading chart...\n\n\n")
    with st.spinner("Loading chart..."):
        time.sleep(dirty_time)
        dirty_time = 0
        st.subheader("Sensor Data Overview")
        if "pivot_data" in st.session_state and st.session_state.pivot_data is not None:
            df = st.session_state.pivot_data.reset_index()
            selection = alt.selection_point(fields=['sensor'], bind='legend')

            chart = alt.Chart(df).transform_fold(
                fold=df.columns[1:],
                as_=['sensor', 'PM2.5']
            ).mark_line().encode(
                x=alt.X("timestamp:T", title="Time", axis=alt.Axis(labelOverlap=True, tickCount=6)),
                y=alt.Y("PM2.5:Q", title="PM2.5 Level"),
                color=alt.Color('sensor:N', title="Sensor"),
                opacity=alt.condition(selection, alt.value(1), alt.value(0.05)),
                tooltip=[
                    alt.Tooltip("timestamp:T", title="Timestamp", format="%Y-%m-%d %H:%M:%S"),  # Full timestamp with time
                    alt.Tooltip("PM2.5:Q", title="PM2.5 Level"),
                    alt.Tooltip("sensor:N", title="Sensor")
                ]
            ).add_params(
                selection
            ).configure_view(
                strokeWidth=0
            ).configure_legend(
                orient='bottom',
                direction='horizontal',
                titleFontSize=20,
                labelFontSize=20,
                padding=10,
                titleAlign="center",
                labelBaseline="middle",
            )

            st.altair_chart(chart, use_container_width=True)  # Ensure chart uses container width
            st.session_state.chart = chart  # Update chart in session state
        else:
            st.markdown(
                """
                <div style="height: 300px; display: flex; justify-content: center; align-items: center;">
                    <h2>No sensors selected</h2>
                </div>
                """,
                unsafe_allow_html=True
            )
            
# Footer
st.markdown(
    '''
    <style>
        .footer {
            position: fixed;
            bottom: 0;
            left: 0;
            width: 100%;
            background-color: #f9f9f9;
            text-align: center;
            padding: 10px 0;
            font-size: 0.9rem;
            color: #7f8c8d;
            box-shadow: 0px -2px 5px rgba(0, 0, 0, 0.1);
        }
    </style>
    <div class="footer">
        Powered by PurpleAir API | Developed with ❤️ using Streamlit
    </div>
    ''', 
    unsafe_allow_html=True
)