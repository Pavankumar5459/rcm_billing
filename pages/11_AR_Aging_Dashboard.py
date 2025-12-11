
import streamlit as st
from utils.navigation import show_navbar
from utils.data_engine import load_provider_data, compute_ar_aging

show_navbar()

FOLDER_ID = "1_S50S0Spc9hfYLpNrbTxNYiQr2XiLpj1"

st.title("AR Aging Dashboard")

df = load_provider_data(FOLDER_ID)
if df is None:
    st.error("Provider dataset missing.")
    st.stop()

aging = compute_ar_aging(df)

st.subheader("AR Aging Distribution")
if aging:
    st.bar_chart(aging)
else:
    st.warning("AR aging cannot be computed.")
