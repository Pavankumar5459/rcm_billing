
import streamlit as st
import pandas as pd
from utils.data_loader import load_provider

st.title("🧪 Provider Drug Utilization Explorer")

mode = st.radio("Select Data Mode:", ["Sample Dataset", "Upload Full Dataset"])

upload = None
if mode == "Upload Full Dataset":
    upload = st.file_uploader("Upload Full Provider CSV")

df = load_provider(sample=(mode=="Sample Dataset"), upload=upload)

if df is None:
    st.error("No dataset loaded.")
else:
    st.success(f"Dataset loaded with {len(df):,} rows")

    states = st.multiselect("State", sorted(df["Rndrng_Prvdr_State_Abrvtn"].dropna().unique()))
    if states:
        df = df[df["Rndrng_Prvdr_State_Abrvtn"].isin(states)]

    hcpcs = st.multiselect("HCPCS", sorted(df["HCPCS_Cd"].dropna().unique()))
    if hcpcs:
        df = df[df["HCPCS_Cd"].isin(hcpcs)]

    st.write("### Filtered Results")
    st.dataframe(df.head(200))

    st.write("### Top 20 by Allowed Amount")
    top20 = df.sort_values("Avg_Mdcr_Alowd_Amt", ascending=False).head(20)
    st.bar_chart(top20.set_index("HCPCS_Cd")["Avg_Mdcr_Alowd_Amt"])
