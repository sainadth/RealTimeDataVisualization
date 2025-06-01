import streamlit as st

# Single metric
st.metric(
    label="Temperature",
    value="70°F",
    delta="1.2°F"
)

# Multiple metrics in columns
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Revenue", "$1.2M", "12%")
    
with col2:
    st.metric("Users", "1,234", "-5%")
    
with col3:
    st.metric("Conversion", "3.2%", "0.8%")