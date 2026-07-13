import streamlit as st
from my_pages import home, calculator, dashboard

st.set_page_config(
    page_title="My Multi-Page App",
    page_icon="🚀",
    layout="wide"
)

st.sidebar.title("📋 Main Menu")

selected_page = st.sidebar.radio(
    "Select Page",
    ["🏠 Home", "🧮 Calculator", "📊 Dashboard"]
)

if selected_page == "🏠 Home":
    home.show()

elif selected_page == "🧮 Calculator":
    calculator.show()

elif selected_page == "📊 Dashboard":
    dashboard.show()