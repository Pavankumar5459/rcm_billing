import streamlit as st
from utils.navigation import show_navbar
from utils.ui_components import centered_header, section_title
from utils.data_engine import load_provider_data, simulate_ar_aging

show_navbar()
centered_header("AR Aging Dashboard")

df = load_provider_data()

if df is None or df.empty:
    st.error("Provider dataset missing.")
    st.stop()

ar_df = simulate_ar_aging(df)

section_title("AR Aging Buckets")

st.bar_chart(ar_df.set_index("bucket")["amount"])

section_title("AR Distribution Table")
st.dataframe(ar_df)

