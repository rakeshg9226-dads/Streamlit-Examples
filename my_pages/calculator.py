import streamlit as st


def show():
    st.title("🧮 Calculator")

    number1 = st.number_input("Enter first number")
    number2 = st.number_input("Enter second number")

    operation = st.selectbox(
        "Select operation",
        ["Addition", "Subtraction", "Multiplication", "Division"]
    )

    if st.button("Calculate"):
        if operation == "Addition":
            result = number1 + number2

        elif operation == "Subtraction":
            result = number1 - number2

        elif operation == "Multiplication":
            result = number1 * number2

        else:
            if number2 == 0:
                st.error("Cannot divide by zero.")
                return

            result = number1 / number2

        st.success(f"Result: {result}")