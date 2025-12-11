
import streamlit as st
import pandas as pd
from utils.data_loader import load_geo

st.title("🌎 Geographic Reimbursement Explorer")

mode = st.radio("Select Data Mode:", ["Sample Dataset", "Upload Full Dataset"])

upload = None
if mode == "Upload Full Dataset":
    upload = st.file_uploader("Upload Full Geo CSV")

df = load_geo(sample=(mode=="Sample Dataset"), upload=upload)

if df is None:
    st.error("No dataset loaded.")
else:
    st.success(f"Dataset loaded with {len(df):,} rows")

    states = st.multiselect("State", sorted(df["Rndrng_Prvdr_State_Abrvtn"].dropna().unique()))
    if states:
        df = df[df["Rndrng_Prvdr_State_Abrvtn"].isin(states)]

    st.write("### Total Allowed Amount by State")
    state_spend = df.groupby("Rndrng_Prvdr_State_Abrvtn")["Avg_Mdcr_Alowd_Amt"].sum().sort_values(ascending=False)
    st.bar_chart(state_spend.head(20))
