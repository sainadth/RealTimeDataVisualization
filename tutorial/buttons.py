import streamlit as st
import pandas as pd
import numpy as np
# Simple button
if st.button("Click me!"):
    st.write("Button was clicked! 🎉")

# Button with custom styling
if st.button("Primary Button", type="primary"):
    st.success("Primary button clicked!")

# Conditional buttons
name = st.text_input("Enter name:")
if name:
    if st.button(f"Greet {name}"):
        st.write(f"Hello, {name}! 👋")

df = pd.DataFrame({
    "Age": np.random.randint(20, 60, 20),
    "Salary": np.random.randint(40000, 120000, 20),
    "City": np.random.choice(["Houston", "Dallas", "Austin"], 20)
})

# Download button
csv_data = df.to_csv(index=False)
st.download_button(
    label="Download CSV",
    data=csv_data,
    file_name="sample_data.csv",
    mime="text/csv"
)