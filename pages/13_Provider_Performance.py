import streamlit as st
from utils.navigation import show_navbar
from utils.ui_components import centered_header, section_title
from utils.data_engine import load_provider_data, provider_performance

show_navbar()
centered_header("Provider Performance Dashboard")

df = load_provider_data()

if df is None or df.empty:
    st.error("Provider dataset missing.")
    st.stop()

perf = provider_performance(df)

section_title("Top Performing Providers (Total Payments)")
st.dataframe(perf["top_providers"])

section_title("Highest Volume Providers (Service Count)")
st.dataframe(perf["high_volume"])

section_title("Average Allowed Amount by Provider Type")
st.bar_chart(perf["allowed_by_type"])
