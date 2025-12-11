
import streamlit as st
from utils.navigation import show_navbar
from utils.data_engine import load_provider_data
from utils.cms_metrics import compute_claim_volume, compute_avg_allowed, compute_payment_rate, compute_denial_rate
from utils.ui_components import kpi_card

show_navbar()

FOLDER_ID = "1_S50S0Spc9hfYLpNrbTxNYiQr2XiLpj1"

st.title("RCM KPI Dashboard (RY25)")

df = load_provider_data(FOLDER_ID)
if df is None:
    st.error("Provider dataset missing.")
    st.stop()

col1, col2, col3, col4 = st.columns(4)
kpi_card("Total Claims", compute_claim_volume(df))
kpi_card("Avg Allowed Amount", compute_avg_allowed(df))
kpi_card("First Pass Payment Rate", str(compute_payment_rate(df)) + "%")
kpi_card("Denial Rate", str(compute_denial_rate(df)) + "%")

st.subheader("Top CPT Codes")
if "cpt_code" in df and "line_count" in df:
    st.dataframe(
        df.groupby("cpt_code")["line_count"]
        .sum()
        .sort_values(ascending=False)
        .head(10)
    )
