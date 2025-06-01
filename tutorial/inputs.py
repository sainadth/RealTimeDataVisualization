import streamlit as st

name = st.text_input("Enter your name:", "John Doe")
bio = st.text_area("Tell us about yourself:", height=100)
password = st.text_input("Password:", type="password")

# Display results
st.write(f"Hello, {name}!")
st.write(f"Bio: {bio}")

# Validation
if len(password) < 8:
    st.error("Password must be at least 8 characters")
else:
    st.success("Password is valid")