import streamlit as st
import pandas as pd
import numpy as np

# Create a sample DataFrame with Age and City columns
df = pd.DataFrame({
    "Age": np.random.randint(0, 100, 50),
    "City": np.random.choice(["NYC", "LA", "Chicago", "Miami"], 50),
    "Name": [f"Person {i}" for i in range(50)]
})

# Add content to sidebar
st.sidebar.title("Settings Panel")
st.sidebar.markdown("---")

# Sidebar widgets
st.sidebar.header("Filters")
min_age = st.sidebar.slider("Minimum Age:", 0, 100, 18)
max_age = st.sidebar.slider("Maximum Age:", 0, 100, 65)
cities = st.sidebar.multiselect("Cities:", 
                               ["NYC", "LA", "Chicago", "Miami"])

# Sidebar form
with st.sidebar.form("settings_form"):
    st.header("User Preferences")
    theme = st.selectbox("Theme:", ["Light", "Dark"])
    notifications = st.checkbox("Enable notifications")
    submitted = st.form_submit_button("Save Settings")
    
    if submitted:
        st.sidebar.success("Settings saved!")

# Use sidebar values in main area
filtered_data = df[(df['Age'] >= min_age) & (df['Age'] <= max_age)]
if cities:
    filtered_data = filtered_data[filtered_data['City'].isin(cities)]
st.dataframe(filtered_data)