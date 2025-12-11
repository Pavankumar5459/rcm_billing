
import streamlit as st
from utils.navigation import show_navbar
from utils.data_engine import load_provider_data
from utils.provider_engine import provider_summary, provider_score

show_navbar()

FOLDER_ID = "1_S50S0Spc9hfYLpNrbTxNYiQr2XiLpj1"

st.title("Provider Performance Dashboard")

df = load_provider_data(FOLDER_ID)
if df is None:
    st.error("Provider dataset missing.")
    st.stop()

st.subheader("Top Provider Types by Payment")
summary = provider_summary(df)
st.dataframe(summary)

st.subheader("Top Provider Efficiency Scores")
score_df = provider_score(df).head(25)
st.dataframe(score_df)
