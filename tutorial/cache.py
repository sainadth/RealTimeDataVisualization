import streamlit as st
import pandas as pd
import numpy as np
@st.cache_data
def load_large_dataset():
    """This function will only run once, then cache the result"""
    # Simulate expensive operation
    import time
    time.sleep(2)  # Pretend this takes time
    
    # Load or generate data
    df = pd.DataFrame({
        'x': np.random.randn(10000),
        'y': np.random.randn(10000),
        'category': np.random.choice(['A', 'B', 'C'], 10000)
    })
    return df

@st.cache_data
def process_data(df, category_filter):
    """Cache processed data based on parameters"""
    return df[df['category'] == category_filter]

# Use cached functions
df = load_large_dataset()  # Fast after first run
category = st.selectbox("Category:", ['A', 'B', 'C'])
filtered_df = process_data(df, category)
st.dataframe(filtered_df.head())