import streamlit as st
import pandas as pd
import numpy as np

# Create sample data
df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie', 'Diana'],
    'Age': [25, 30, 35, 28],
    'City': ['NYC', 'LA', 'Chicago', 'Miami'],
    'Salary': [50000, 60000, 70000, 55000]
})

# Display options
st.dataframe(df)  # Interactive table
st.table(df)      # Static table
st.write(df)      # Auto-formatted display