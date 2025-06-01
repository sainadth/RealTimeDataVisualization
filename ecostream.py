#===============================================================================#
# Setup: Import libraries, load environment variables, and configure Streamlit page
import streamlit as st
import pandas as pd
import json
import requests
import os
from dotenv import load_dotenv
from streamlit_folium import st_folium
import folium
from folium.plugins import MarkerCluster
import plotly.graph_objects as go
from contextlib import contextmanager
import matplotlib.pyplot as plt  # Import for color palette
import about  
import pytz  # Add this import for timezone conversion

#===============================================================================#
# Setup
load_dotenv()
PURPLE_AIR_API_KEY = os.getenv("PURPLE_AIR_API_KEY")
st.set_page_config(page_title="EcoStream", layout="wide")
#===============================================================================#


#===============================================================================#
# Title
_, title_col, _ = st.columns([0.1, 9.8, 0.1])
with title_col:
    st.markdown(
        """
        <h1 style="text-align: center;
                font-size: 60px;
                font-weight: bold;
                text-shadow: 1px 1px 2px rgba(0,0,0,0.2);">
            EcoStream
        </h1>
        """,
        unsafe_allow_html=True
    )
#===============================================================================#


#===============================================================================#
# Helpers: Utility functions for loading sensor data, caching, API calls, and sensor selection logic
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

@st.cache_data
def create_loc_dict(df):
    return {(row['name']): [row['latitude'], row['longitude'] ] for _, row in df.iterrows()}

def get_data(sensor_index):
    url = f"https://api.purpleair.com/v1/sensors/{sensor_index}/history"
    params = {"fields": "pm2.5_alt", "start_timestamp": int((pd.Timestamp.now() - pd.Timedelta(days=3)).timestamp())}
    try:
        res = requests.get(url, headers={"X-API-Key": PURPLE_AIR_API_KEY}, params=params)
        res.raise_for_status()
        return res.json()
    except Exception as e:
        print(f"API error: {e}")
        return None

def toggle_sensor_selection(sensor_name):
# Function to toggle sensor selection (single mode only)
    st.session_state.highlighted_sensor = sensor_name  # Highlight the selected sensor
    lat, lon = sensor_loc_dict.get(sensor_name)
    if lat and lon:
        st.session_state.zoom = 14  # Adjust zoom level for better focus
        st.session_state.la = lat
        st.session_state.lo = lon
#===============================================================================#


#===============================================================================#
# Styling: Custom CSS for Streamlit UI elements and horizontal layout context manager
st.markdown("""
            <style>
                /* Hide Streamlit main menu (hamburger) */
                #MainMenu {visibility: hidden;}
                /* Hide Streamlit footer */
                footer {visibility: hidden;}
                /* Hide the top toolbar (floating) */
                header {visibility: hidden;}
                div.block-container{
                    padding-top:1rem;
                }
            
                .stApp {
                    # background-color: rgb(246 248 250);
                }
            
                .stSidebar {
                    background-color: rgb(246 248 250);
                    font-family: 'Arial', sans-serif;
                    # color: #FFFFFF;
                    border-radius: 10px;
                    padding: 1rem;
                }

                .stSidebar img {
                    width: 100px;
                    height: auto;
                    margin-bottom: 1rem;
                    # background-color: #ffffff;
                    border-radius: 10px;
                    padding: 0.5rem;
                }
            
                .stSidebar button {
                    text-align: left;
                }
            
                section[data-testid="stSidebar"] button {
                    width: 100%;
                    display: flex !important;
                    align-items: left !important;
            justify-content: left !important;
                    font-weight: bold !important;
                    padding: 0.75rem 1.5rem !important;
                }
                section[data-testid="stSidebar"] button[kind="tertiary"]:hover {
                    color: #FFFFFF !important;
                    background-color: #31383f !important;
                }
                   
            </style>""",
            unsafe_allow_html=True
)

HORIZONTAL_STYLE = """
<style class="hide-element">
    /* Hides the style container and removes the extra spacing */
    .element-container:has(.hide-element) {
        display: none;
    }
    /*
        The selector for >.element-container is necessary to avoid selecting the whole
        body of the streamlit app, which is also a stVerticalBlock.
    */
    div[data-testid="stVerticalBlock"]:has(> .element-container .horizontal-marker) {
        display: flex;
        flex-direction: row !important;
        flex-wrap: wrap;
        gap: 0.5rem;
        align-items: center;
    }
    /* Buttons and their parent container all have a width of 704px, which we need to override */
    div[data-testid="stVerticalBlock"]:has(> .element-container .horizontal-marker) div {
        width: max-content !important;
    }
    /* Just an example of how you would style buttons, if desired */
    /*
    div[data-testid="stVerticalBlock"]:has(> .element-container .horizontal-marker) button {
        border-color: red;
    }
    */
</style>
"""

@contextmanager
def st_horizontal():
    st.markdown(HORIZONTAL_STYLE, unsafe_allow_html=True)
    with st.container():
        st.markdown('<span class="hide-element horizontal-marker"></span>', unsafe_allow_html=True)
        yield
#===============================================================================#


#===============================================================================#
# Data & State: Load sensor data, create lookup dictionaries, and initialize Streamlit session state
df_sensors = load_sensors()
sensor_dict = create_dict(df_sensors)
sensor_loc_dict = create_loc_dict(df_sensors)

# Session init
st.session_state.setdefault("sensors_selected", [])
st.session_state.setdefault("sensor_data_selected", [])
st.session_state.setdefault("update_chart", False)
st.session_state.setdefault("last_clicked_location", None)
st.session_state.setdefault("la", 27.8)  # Default latitude
st.session_state.setdefault("lo", -97.3)  # Default longitude
st.session_state.setdefault("zoom", 10)  # Default longitude
st.session_state.setdefault("last_click_time", None)
st.session_state.setdefault("highlighted_sensor", None)  # Track the highlighted sensor
#===============================================================================#


#===============================================================================#
# Sidebar: Render sidebar with navigation buttons and handle page switching
st.logo(image="images/logo.png", size="large")
dashboard_clicked = st.sidebar.button("Dashboard", type="tertiary", key="dashboard_btn", icon="🏠")
about_clicked = st.sidebar.button("About", type="tertiary" ,key="about_btn", icon="ℹ️")

# Determine which page to show
if "page" not in st.session_state:
    st.session_state.page = "Dashboard"

if dashboard_clicked:
    st.session_state.page = "Dashboard"

if about_clicked:
    st.session_state.page = "About"

if st.session_state.page == "About":
    about.show_about()
    st.stop()
#===============================================================================#


#===============================================================================#
# Main content: Define layout columns for chart and map
chart_col, map_col = st.columns([3, 2])
#===============================================================================#


#===============================================================================#
# Map: Display interactive map with clustered sensor markers and custom icons
m = folium.Map(location=[st.session_state.la, st.session_state.lo], zoom_start=st.session_state.zoom, control_scale=True)
marker_cluster = MarkerCluster().add_to(m)
custom_icon_url = "https://cdn-icons-png.flaticon.com/512/684/684908.png"  # Example custom marker icon URL

for _, row in df_sensors.iterrows():
    folium.Marker(
        location=[row['latitude'], row['longitude']],
        popup=folium.Popup(f"""
                            <b>Sensor:</b> {row['name'].replace('_', ' ')}
                            <br>
                            <b>Index:</b> {row['sensor_index']}
                            <br>
                            <b>Location:</b> {row['latitude']}, {row['longitude']}
                           """,
                           max_width=300),
        tooltip=f"{row['name'].replace('_', ' ')}",
        icon=folium.CustomIcon(custom_icon_url, icon_size=(30, 30))  # Use custom marker icon with specified size
    ).add_to(marker_cluster)

with map_col:
    st.subheader("Map of Nearby Sensors")
    st_data = st_folium(m, height=400)
#===============================================================================#


#===============================================================================#
# Timeout logic: Reset selection if user is inactive for a set period
TIMEOUT_SECONDS = 15

if (
    "last_click_time" in st.session_state and
    st.session_state.last_click_time is not None and
    (pd.Timestamp.now() - st.session_state.last_click_time).total_seconds() > TIMEOUT_SECONDS
):
    st.session_state.last_clicked_location = None
    st.session_state.last_click_time = None
    st.session_state.update_chart = True
    st.session_state.highlighted_sensor = None  # Reset highlighted sensor

REFRESH_INTERVAL = 60  # Refresh every 10 minutes

if (
    "last_refresh_time" not in st.session_state or
    (pd.Timestamp.now() - st.session_state.last_refresh_time).total_seconds() > REFRESH_INTERVAL
):
    # Fetch latest data for each selected sensor and update sensor_data_selected
    refreshed_sensor_data = []
    for sensor_index, sensor_name in st.session_state.sensors_selected:
        data = get_data(sensor_index)
        if data and 'data' in data and data['data']:
            try:
                df = pd.DataFrame(data['data'], columns=['timestamp', 'value'])
                df['timestamp'] = pd.to_datetime(df['timestamp'], unit='s').dt.tz_localize('UTC').dt.tz_convert('America/Chicago')
                refreshed_sensor_data.append(df)
            except Exception as e:
                print(f"Error refreshing data for sensor {sensor_name}: {e}")
                refreshed_sensor_data.append(pd.DataFrame(columns=['timestamp', 'value']))
        else:
            refreshed_sensor_data.append(pd.DataFrame(columns=['timestamp', 'value']))
    st.session_state.sensor_data_selected = refreshed_sensor_data
    st.session_state.update_chart = True
    st.session_state.last_refresh_time = pd.Timestamp.now()
#===============================================================================#


#===============================================================================#
# Handle clicks: Process map marker clicks, fetch sensor data, and update session state
clicked = st_data.get("last_object_clicked")

if clicked and clicked != st.session_state.last_clicked_location:
    st.session_state.last_clicked_location = clicked
    st.session_state.last_click_time = pd.Timestamp.now()
    lat, lon = clicked["lat"], clicked["lng"]
    sensor_info = sensor_dict.get((lat, lon))

    if sensor_info:
        sensor_index, sensor_name = sensor_info[0], sensor_info[1].strip()
        existing_sensor_indices = [s[0] for s in st.session_state.sensors_selected]

        if sensor_index in existing_sensor_indices:
            index = existing_sensor_indices.index(sensor_index)
            del st.session_state.sensors_selected[index]
            del st.session_state.sensor_data_selected[index]

        data = get_data(sensor_index)

        if data and 'data' in data and data['data']:
            print(f"Sensor {sensor_name} data fetched successfully.", len(data['data']))
            try:
                df = pd.DataFrame(data['data'], columns=['timestamp', 'value'])
                df['timestamp'] = pd.to_datetime(df['timestamp'], unit='s').dt.tz_localize('UTC').dt.tz_convert('America/Chicago')
                st.session_state.sensors_selected.append([sensor_index, sensor_name])
                st.session_state.sensor_data_selected.append(df)
                st.session_state.update_chart = True  # Ensure update_chart is set
            except Exception as e:
                print(f"Error processing data for sensor {sensor_name}: {e}")
        else:
            print(f"No valid data found for sensor {sensor_name}. Data structure: {data}")
            with chart_col:
                st.toast("No data for this sensor.", icon="⚠️")
    else:
        print("No sensor information found for the clicked location.")
    print("Dirty flag status:", st.session_state.update_chart)


# Prepare chart data
if st.session_state.update_chart:
    print("Processing chart data...")
    dfs = [df.assign(sensor=st.session_state.sensors_selected[i][1])
           for i, df in enumerate(st.session_state.sensor_data_selected)
           if not df.empty and df.shape[1] > 0]
    if dfs:
        combined = pd.concat(dfs, ignore_index=True)
        combined = combined.groupby(['timestamp', 'sensor']).mean().reset_index()
        pivot_data = combined.pivot(index='timestamp', columns='sensor', values='value')
        pivot_data = pivot_data.dropna(how='all').ffill().bfill().tail(500)
        st.session_state.pivot_data = pivot_data
        print(f"Updated pivot_data: {st.session_state.pivot_data.shape}")
    else:
        st.session_state.pivot_data = None
        print("No valid dataframes to process.")
    st.session_state.update_chart = False
else:
    print("Chart data is up-to-date.")

# Ensure update_chart is set when new data is fetched
if "pivot_data" not in st.session_state or st.session_state.pivot_data is None:
    st.session_state.update_chart = True
    print("update_chart flag set due to missing or empty pivot_data.")

# Show chart using Plotly
with chart_col:
    st.subheader("Sensor Data Overview")
    if "pivot_data" in st.session_state and st.session_state.pivot_data is not None:
        df = st.session_state.pivot_data.reset_index()
        fig = go.Figure()

        # Generate a color palette
        color_palette = plt.cm.tab10.colors  # Use a colormap with distinct colors
        color_map = {sensor[1]: f"rgb({int(r*255)}, {int(g*255)}, {int(b*255)})"
                     for sensor, (r, g, b) in zip(st.session_state.sensors_selected, color_palette)}

        for i, sensor in enumerate(st.session_state.sensors_selected):
            sensor_name = sensor[1]
            sensor_data = df[['timestamp', sensor_name]].dropna()
            
            # opacity logic
            opacity = 1.0
            if st.session_state.highlighted_sensor is not None and st.session_state.highlighted_sensor != sensor_name:
                opacity = 0.2


            fig.add_trace(go.Scatter(
                x=sensor_data['timestamp'],
                y=sensor_data[sensor_name],
                mode='lines',
                name=sensor_name,
                line=dict(color=color_map[sensor_name], width=2),
                opacity=opacity,  # Adjust opacity based on selection
                customdata=[sensor_name.replace("_", " ")] * len(sensor_data),
                showlegend=False,
                hovertemplate="<b>Sensor:</b> %{customdata}<br><b>PM2.5:</b> %{y}<br><b>Time:</b> %{x}<extra></extra>"
            ))

        # Calculate the overall average
        overall_average = df.drop(columns=['timestamp']).mean().mean()
        print(f"Overall average PM2.5: {overall_average}")  # Log the overall average

        # Add a horizontal line for the overall average
        fig.add_trace(go.Scatter(
            x=[df['timestamp'].min(), df['timestamp'].max()],
            y=[overall_average, overall_average],
            mode='lines',
            name='Overall Average',
            showlegend=False,
            line=dict(color='black', width=2, dash='dash'),  # Dashed black line for average
            hovertemplate="<b>Overall Average PM2.5:</b> %{y}<extra></extra>"
        ))

        # Update chart layout with styles
        fig.update_layout(
            xaxis=dict(
                title=dict(
                    text="Time",
                    font=dict(size=20, color="#333")  # Corrected title font for x-axis
                ),
                showgrid=True,  # Enable gridlines
                gridcolor="lightgrey",  # Gridline color
                zeroline=False
            ),
            yaxis=dict(
                title=dict(
                    text="PM2.5 Level",
                    font=dict(size=20, color="#333")  # Corrected title font for y-axis
                ),
                showgrid=True,  # Enable gridlines
                gridcolor="lightgrey",  # Gridline color
                zeroline=False
            ),
            height=400,
            plot_bgcolor="white",  # Background color of the plot area
            margin=dict(l=40, r=40, t=40, b=40)  # Adjust margins
        )
        st.plotly_chart(fig, use_container_width=True)

        st.markdown(
            """
            <div>
                <h4>Sensors</h4>
            </div>
            """
            ,unsafe_allow_html=True
        )
        # Adding legend elements for each sensor
        with st_horizontal():
            for sensor, trace in zip(st.session_state.sensors_selected, fig.data):
                sensor_name = sensor[1]
                color = color_map[sensor_name]  # Use the explicitly assigned color
                print(f"Sensor: {sensor_name}, Color: {color}")
                
                st.write(
                    f"<span style='color: {color};'>▬</span>",
                    unsafe_allow_html=True
                )

                # Render the button with the label color matching the sensor's color
                if st.button(
                    f"{sensor_name.replace('_', ' ')}",
                    type="tertiary",
                    key=f"select_{sensor_name}",
                    help="Click to highlight this sensor",
                    use_container_width=True
                ):
                    toggle_sensor_selection(sensor_name)
                    st.rerun()

                if st.button(
                    label="",
                    type="tertiary",
                    key=f"delete_{sensor_name}",
                    help="Click to delete this sensor",
                    use_container_width=True,
                    icon=":material/delete:"
                ):
                    index = [s[1] for s in st.session_state.sensors_selected].index(sensor_name)
                    del st.session_state.sensors_selected[index]
                    del st.session_state.sensor_data_selected[index]
                    st.session_state.update_chart = True
                    print(f"Deleted sensor: {sensor_name}")
                    st.rerun()
            st.write(
                f"<span style='color: black;'>▬ ▬ Average</span>",
                unsafe_allow_html=True
            )
    else:
        # If no data is available, show a message
        st.markdown(
            """
            <div style="height: 400px; display: flex; justify-content: center; align-items: center; background-color: #f9f9f9; border: 2px dashed #ddd; border-radius: 10px;">
                <h2 style="color: #888;">🚫 No sensors selected</h2>
            </div>
            """,
            unsafe_allow_html=True
        )
#===============================================================================#