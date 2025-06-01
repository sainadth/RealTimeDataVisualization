import streamlit as st
# Container groups related elements
with st.container():
    st.write("This is inside a container")
    st.write("All elements are grouped together")
    
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Metric 1", "100")
    with col2:
        st.metric("Metric 2", "200")

# Empty placeholder for dynamic content
placeholder = st.empty()

# Later in your code, update the placeholder
if st.button("Update"):
    placeholder.success("Content updated!")