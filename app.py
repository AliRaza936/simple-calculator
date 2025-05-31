# calculator_app.py

import streamlit as st

st.title("🧮 Simple Calculator")

# Input numbers
num1 = st.number_input("Enter first number", format="%.2f")
num2 = st.number_input("Enter second number", format="%.2f")

# Operation selection
operation = st.selectbox("Choose operation", ["Add", "Subtract", "Multiply", "Divide"])

# Compute result
if st.button("Calculate"):
    if operation == "Add":
        result = num1 + num2
        st.success(f"Result: {num1} + {num2} = {result}")
    elif operation == "Subtract":
        result = num1 - num2
        st.success(f"Result: {num1} - {num2} = {result}")
    elif operation == "Multiply":
        result = num1 * num2
        st.success(f"Result: {num1} × {num2} = {result}")
    elif operation == "Divide":
        if num2 == 0:
            st.error("Error: Division by zero.")
        else:
            result = num1 / num2
            st.success(f"Result: {num1} ÷ {num2} = {result}")
