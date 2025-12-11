import streamlit as st
import pandas as pd
import altair as alt
from pathlib import Path

st.set_page_config(layout="wide")
st.title("Medicare Provider Analytics")

st.markdown("""
This dashboard provides sample Medicare-style provider analytics.  
It automatically loads data from the **sample_data** folder with no file upload required.
""")

# -------------------------------------------------
# Auto-load data
# -------------------------------------------------
df_path = Path("sample_data/provider_sample.csv")

if df_path.exists():
    df = pd.read_csv(df_path)
    st.success("Provider sample dataset loaded successfully.")
else:
    st.error("Provider sample dataset not found in /sample_data.")
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
st.header("Provider Specialty Distribution")

if "specialty" in df.columns:
    specialty_counts = df["specialty"].value_counts().reset_index()
    specialty_counts.columns = ["specialty", "count"]

    chart = (
        alt.Chart(specialty_counts.head(15))
        .mark_bar()
        .encode(
            x="count:Q",
            y=alt.Y("specialty:N", sort="-x"),
            tooltip=["specialty", "count"]
        )
    )
    st.altair_chart(chart, use_container_width=True)
else:
    st.info("Specialty column not found in dataset.")

st.markdown("---")
st.header("Top HCPCS Codes")

if "hcpcs_code" in df.columns:
    hcpcs_counts = df["hcpcs_code"].value_counts().reset_index()
    hcpcs_counts.columns = ["HCPCS Code", "Count"]

    st.dataframe(hcpcs_counts.head(20), use_container_width=True)

    chart = (
        alt.Chart(hcpcs_counts.head(15))
        .mark_bar()
        .encode(
            x="Count:Q",
            y=alt.Y("HCPCS Code:N", sort="-x"),
            tooltip=["HCPCS Code", "Count"]
        )
    )
    st.altair_chart(chart, use_container_width=True)
else:
    st.info("HCPCS code column not found in dataset.")

st.markdown("---")
st.header("Allowed vs Paid Amount (Scatter Plot)")

if "allowed_amount" in df.columns and "paid_amount" in df.columns:
    df2 = df.dropna(subset=["allowed_amount", "paid_amount"])

    scatter = (
        alt.Chart(df2)
        .mark_circle(size=60, opacity=0.7)
        .encode(
            x="allowed_amount:Q",
            y="paid_amount:Q",
            tooltip=list(df.columns)
        )
    )
    st.altair_chart(scatter, use_container_width=True)

st.markdown("---")
st.write("This is a simplified analytics module. Replace sample_data with CMS datasets for deeper analysis.")
