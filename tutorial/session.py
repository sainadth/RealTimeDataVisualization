import streamlit as st
# Initialize session state
if 'counter' not in st.session_state:
    st.session_state.counter = 0

if 'user_name' not in st.session_state:
    st.session_state.user_name = ""

# Display current values
st.write(f"Counter: {st.session_state.counter}")
st.write(f"User: {st.session_state.user_name}")

# Buttons to modify state
col1, col2, col3 = st.columns(3)

with col1:
    if st.button("Increment"):
        st.session_state.counter += 1

with col2:
    if st.button("Decrement"):
        st.session_state.counter -= 1

with col3:
    if st.button("Reset"):
        st.session_state.counter = 0