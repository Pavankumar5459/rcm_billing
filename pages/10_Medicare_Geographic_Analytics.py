import streamlit as st
import pandas as pd
import altair as alt
from pathlib import Path

st.set_page_config(layout="wide")
st.title("Medicare Geographic Analytics")

st.markdown("""
This dashboard provides geographic-level Medicare insights using a sample dataset.  
Data loads automatically from the **sample_data** directory without any file uploads.
""")

# -------------------------------------------------
# Auto-load data
# -------------------------------------------------
geo_path = Path("sample_data/geo_sample.csv")

if geo_path.exists():
    df = pd.read_csv(geo_path)
    st.success("Geographic sample dataset loaded successfully.")
else:
    st.error("Geographic sample CSV not found in /sample_data.")
    st.stop()

st.markdown("---")
st.subheader("Dataset Preview")
st.dataframe(df.head(), use_container_width=True)

st.markdown("---")
st.subheader("Dataset Summary")

col1, col2, col3 = st.columns(3)
col1.metric("Rows", df.shape[0])
col2.metric("Columns", df.shape[1])
col3.metric("Missing Values", df.isna().sum().sum())

st.markdown("---")
st.header("Allowed Amount by State")

if "state" in df.columns and "allowed_amount" in df.columns:
    allowed_state = df.groupby("state")["allowed_amount"].sum().reset_index()

    chart = (
        alt.Chart(allowed_state)
        .mark_bar()
        .encode(
            x="allowed_amount:Q",
            y=alt.Y("state:N", sort="-x"),
            tooltip=["state", "allowed_amount"]
        )
    )
    st.altair_chart(chart, use_container_width=True)
else:
    st.info("State or allowed_amount column missing.")

st.markdown("---")
st.header("Paid Amount by State")

if "state" in df.columns and "paid_amount" in df.columns:
    paid_state = df.groupby("state")["paid_amount"].sum().reset_index()

    chart = (
        alt.Chart(paid_state)
        .mark_bar(color="#2563EB")
        .encode(
            x="paid_amount:Q",
            y=alt.Y("state:N", sort="-x"),
            tooltip=["state", "paid_amount"]
        )
    )
    st.altair_chart(chart, use_container_width=True)

st.markdown("---")
st.header("Top HCPCS Codes Nationally")

if "hcpcs_code" in df.columns and "allowed_amount" in df.columns:
    hcpcs_top = (
        df.groupby("hcpcs_code")["allowed_amount"]
        .sum()
        .reset_index()
        .sort_values("allowed_amount", ascending=False)
    )

    st.dataframe(hcpcs_top.head(20), use_container_width=True)

st.markdown("---")
st.write("This module scales automatically when real CMS datasets are added.")
