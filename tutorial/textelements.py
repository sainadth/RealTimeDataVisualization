import streamlit as st
st.title("Main Title")
st.header("Section Header")
st.subheader("Subsection Header")
st.text("Fixed-width text")
st.markdown("**Bold** and *italic* text")
st.caption("Small caption text")
st.code("print('Hello World')", language="python")

# Special formats
st.latex(r"\sum_{i=1}^{n} x_i^2")
st.json({"name": "John", "age": 30})