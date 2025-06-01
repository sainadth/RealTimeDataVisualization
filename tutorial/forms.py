import streamlit as st
# Form prevents re-runs until submit
with st.form("user_form"):
    st.write("User Registration Form")
    
    name = st.text_input("Full Name:")
    email = st.text_input("Email:")
    age = st.number_input("Age:", min_value=0, max_value=120)
    city = st.selectbox("City:", ["NYC", "LA", "Chicago"])
    
    # Form submit button
    submitted = st.form_submit_button("Register")
    
    if submitted:
        st.success(f"Welcome {name}!")
        st.write(f"Email: {email}")
        st.write(f"Age: {age}")
        st.write(f"City: {city}")