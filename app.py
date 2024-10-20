import streamlit as st

# Calculator functions
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Cannot divide by zero!"

# Streamlit app
st.title("Simple Calculator")

# User input
operation = st.selectbox("Select operation:", ["Add", "Subtract", "Multiply", "Divide"])

num1 = st.number_input("Enter first number:")
num2 = st.number_input("Enter second number:")

if st.button("Calculate"):
    if operation == "Add":
        result = add(num1, num2)
        st.write(f"{num1} + {num2} = {result}")
    elif operation == "Subtract":
        result = subtract(num1, num2)
        st.write(f"{num1} - {num2} = {result}")
    elif operation == "Multiply":
        result = multiply(num1, num2)
        st.write(f"{num1} * {num2} = {result}")
    elif operation == "Divide":
        result = divide(num1, num2)
        st.write(f"{num1} / {num2} = {result}")
