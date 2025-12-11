import streamlit as st
import pandas as pd
import altair as alt
from pathlib import Path

st.set_page_config(layout="wide")
st.title("Medicare Provider Analytics")

st.markdown("""
This dashboard provides an overview of Medicare provider utilization patterns using a sample dataset.  
You may replace the sample file with CMS Physician Public Use File (PUF) data for deeper analysis.
""")

st.markdown("---")
st.header("Data Loading")

provider_path = Path("sample_data/provider_sample.csv")

if provider_path.exists():
    df = pd.read_csv(provider_path)
    st.success("Provider sample dataset loaded successfully.")
else:
    st.error("Provider sample dataset not found. Please check your file path.")
    st.stop()

st.write("### Preview of Dataset")
st.dataframe(df.head(), use_container_width=True)

st.markdown("---")
st.header("Basic Dataset Information")

col1, col2, col3 = st.columns(3)
col1.metric("Rows", df.shape[0])
col2.metric("Columns", df.shape[1])
col3.metric("Missing Values", df.isna().sum().sum())

st.markdown("---")
st.header("Provider Summary")

# If dataset contains these columns:
potential_cols = ["provider", "specialty", "allowed_amount", "paid_amount", "hcpcs_code"]

for col in potential_cols:
    if col not in df.columns:
        st.warning(f"Column missing: {col}")

if "specialty" in df.columns:
    specialty_counts = df["specialty"].value_counts().reset_index()
    specialty_counts.columns = ["specialty", "count"]

    st.subheader("Providers by Specialty")

    chart = (
        alt.Chart(specialty_counts.head(15))
        .mark_bar()
        .encode(
            x=alt.X("count:Q"),
            y=alt.Y("specialty:N", sort="-x"),
            tooltip=["specialty", "count"],
        )
    )
    st.altair_chart(chart, use_container_width=True)

st.markdown("---")
st.header("HCPCS Utilization")

if "hcpcs_code" in df.columns:
    hcpcs_counts = df["hcpcs_code"].value_counts().reset_index()
    hcpcs_counts.columns = ["HCPCS Code", "Count"]

    st.write("### Top HCPCS Codes")
    st.dataframe(hcpcs_counts.head(20), use_container_width=True)

    chart = (
        alt.Chart(hcpcs_counts.head(15))
        .mark_bar()
        .encode(
            x=alt.X("Count:Q"),
            y=alt.Y("HCPCS Code:N", sort="-x"),
            tooltip=["HCPCS Code", "Count"],
        )
    )
    st.altair_chart(chart, use_container_width=True)

st.markdown("---")
st.header("Allowed vs Paid Amount Analysis")

if "allowed_amount" in df.columns and "paid_amount" in df.columns:
    df2 = df.dropna(subset=["allowed_amount", "paid_amount"])

    scatter = (
        alt.Chart(df2)
        .mark_circle(size=60)
        .encode(
            x="allowed_amount:Q",
            y="paid_amount:Q",
            tooltip=list(df2.columns),
        )
    )
    st.altair_chart(scatter, use_container_width=True)

    st.markdown("""
    A strong correlation between allowed and paid amounts indicates consistent reimbursement patterns.  
    Outliers may represent bundling issues, modifiers, or unusual claim adjudication scenarios.
    """)

st.markdown("---")
st.write("This module can be expanded with more detailed analytics once full CMS data is added.")
