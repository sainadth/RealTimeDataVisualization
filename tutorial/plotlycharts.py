import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
import pandas as pd

# Create a DataFrame with columns matching the plotly scatter plot arguments
df = pd.DataFrame({
    "Age": np.random.randint(20, 60, 20),
    "Salary": np.random.randint(40000, 120000, 20),
    "City": np.random.choice(["Houston", "Dallas", "Austin"], 20)
})

# Scatter plot
fig = px.scatter(
    df, 
    x="Age", 
    y="Salary",
    color="City",
    title="Age vs Salary by City"
)
st.plotly_chart(fig, use_container_width=True)

# Custom plotly chart
fig = go.Figure()
fig.add_trace(go.Scatter(x=[1,2,3,4], y=[10,11,12,13]))
st.plotly_chart(fig)