import streamlit as st
import pandas as pd


def show():
    st.title("📊 Dashboard")

    data = {
        "Month": ["January", "February", "March", "April"],
        "Sales": [25000, 32000, 28000, 41000]
    }

    df = pd.DataFrame(data)

    st.dataframe(df, width="stretch")
    st.bar_chart(df.set_index("Month"))