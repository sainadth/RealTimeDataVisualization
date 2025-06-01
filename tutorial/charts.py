import streamlit as st
import numpy as np
import pandas as pd


# Sample data
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['Series A', 'Series B', 'Series C']
)

# Built-in charts
st.line_chart(chart_data)
st.area_chart(chart_data)
st.bar_chart(chart_data)

# Single column chart
st.bar_chart(chart_data['Series A'])