import streamlit as st
import pandas as pd
import altair as alt
from pathlib import Path

st.set_page_config(layout="wide")
st.title("Medicare Geographic Analytics")

st.markdown("""
This module provides geographic insights into Medicare utilization patterns based on sample data.  
Geographic analysis highlights how reimbursement and service volume vary across states.
""")

st.markdown("---")
st.header("Data Loading")

geo_path = Path("sample_data/geo_sample.csv")

if geo_path.exists():
    df = pd.read_csv(geo_path)
    st.success("Geographic sample data loaded successfully.")
else:
    st.error("Geo dataset not found. Please verify the file location.")
    st.stop()

st.write("### Preview of Dataset")
st.dataframe(df.head(), use_container_width=True)

st.markdown("---")
st.header("Dataset Information")

col1, col2, col3 = st.columns(3)
col1.metric("Rows", df.shape[0])
col2.metric("Columns", df.shape[1])
col3.metric("Missing Values", df.isna().sum().sum())

st.markdown("---")

expected_columns = ["state", "allowed_amount", "paid_amount", "hcpcs_code"]
for col in expected_columns:
    if col not in df.columns:
        st.warning(f"Missing expected column: {col}")

st.header("Allowed Amount by State")

if "state" in df.columns and "allowed_amount" in df.columns:
    state_summary = df.groupby("state")["allowed_amount"].sum().reset_index()

    chart = (
        alt.Chart(state_summary)
        .mark_bar()
        .encode(
            x=alt.X("allowed_amount:Q", title="Total Allowed Amount"),
            y=alt.Y("state:N", sort="-x"),
            tooltip=["state", "allowed_amount"],
        )
    )
    st.altair_chart(chart, use_container_width=True)

st.markdown("---")
st.header("Paid Amount by State")

if "paid_amount" in df.columns:
    state_paid = df.groupby("state")["paid_amount"].sum().reset_index()

    chart_paid = (
        alt.Chart(state_paid)
        .mark_bar(color="#2563EB")
        .encode(
            x="paid_amount:Q",
            y=alt.Y("state:N", sort="-x"),
            tooltip=["state", "paid_amount"],
        )
    )
    st.altair_chart(chart_paid, use_container_width=True)

st.markdown("---")
st.header("Top HCPCS Codes by State")

if "hcpcs_code" in df.columns:
    top_hcpcs = (
        df.groupby("hcpcs_code")["allowed_amount"]
        .sum()
        .reset_index()
        .sort_values(by="allowed_amount", ascending=False)
    )

    st.write("### Top HCPCS Codes Nationally")
    st.dataframe(top_hcpcs.head(20), use_container_width=True)

st.markdown("---")
st.write("This module is designed to scale with full CMS data for live analytic dashboards.")
