import streamlit as st
# Equal width columns
col1, col2 = st.columns(2)

with col1:
    st.header("Column 1")
    st.write("This is the first column")
    st.button("Button 1")

with col2:
    st.header("Column 2")
    st.write("This is the second column")
    st.button("Button 2")

# Different width columns
col1, col2, col3 = st.columns([1, 2, 1])

with col1:
    st.write("Narrow")
with col2:
    st.write("Wide column")
with col3:
    st.write("Narrow")