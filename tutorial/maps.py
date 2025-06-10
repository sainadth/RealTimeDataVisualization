import streamlit as st
import pandas as pd
import plotly.express as px

# Simple map with coordinates
map_data = pd.DataFrame({
    'lat': [37.76, 37.77, 37.78, 37.79],
    'lon': [-122.4, -122.41, -122.42, -122.43],
    'size': [20, 30, 40, 50]
})

st.map(map_data)

# Plotly map
fig = px.scatter_map(
    map_data,
    lat="lat",
    lon="lon",
    size="size",
    mapbox_style="open-street-map"
)
st.plotly_chart(fig)