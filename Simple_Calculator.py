import streamlit as st

# Title of the app
st.title("⌨ Simple Calculator")

# Input fields for numbers
num1 = st.number_input("Enter the first number", value=0.0)
num2 = st.number_input("Enter the second number", value=0.0)

# Dropdown for operation
operation = st.selectbox("Select an operation", ["Add", "Subtract", "Multiply", "Divide"])

# Perform calculation based on the selected operation
if st.button("Calculate"):
    if operation == "Add":
        result = num1 + num2
    elif operation == "Subtract":
        result = num1 - num2
    elif operation == "Multiply":
        result = num1 * num2
    elif operation == "Divide":
        if num2 != 0:
            result = num1 / num2
        else:
            result = "Error: Division by zero"
    
    # Display the result
    st.success(f"Result: {result}")


st.write("\n\n")

st.write("***⛔ Created By Jabbar Jatoi***")