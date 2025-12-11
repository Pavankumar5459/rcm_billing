import streamlit as st
import pandas as pd
import altair as alt
from pathlib import Path

st.set_page_config(layout="wide")

st.title("Billing & Denials Insights")

st.markdown("""
This module explains how billing works and uses sample CMS-style datasets  
to demonstrate denial patterns, allowed vs paid gaps, and service utilization trends.
""")

st.markdown("---")

# -----------------------------------------------------------
# LOAD SAMPLE DATA FILES
# -----------------------------------------------------------

prov_path = Path("sample_data/provider_sample.csv")
geo_path = Path("sample_data/geo_sample.csv")

if not prov_path.exists():
    st.error("provider_sample.csv missing from sample_data folder")
    st.stop()

if not geo_path.exists():
    st.error("geo_sample.csv missing from sample_data folder")
    st.stop()

prov = pd.read_csv(prov_path)
geo = pd.read_csv(geo_path)

st.success("Billing datasets loaded successfully.")

# -----------------------------------------------------------
# BASIC PREVIEW
# -----------------------------------------------------------

with st.expander("View Raw Provider Dataset"):
    st.dataframe(prov.head(), use_container_width=True)

with st.expander("View Geographic Dataset"):
    st.dataframe(geo.head(), use_container_width=True)

st.markdown("---")

# -----------------------------------------------------------
# ALLOWED VS. PAID ANALYSIS
# -----------------------------------------------------------

st.header("Allowed Amount vs. Paid Amount")

if "allowed_amount" in prov.columns and "paid_amount" in prov.columns:
    summary = prov[["allowed_amount", "paid_amount"]].dropna()
    summary["gap"] = summary["allowed_amount"] - summary["paid_amount"]

    col1, col2, col3 = st.columns(3)
    col1.metric("Average Allowed", f"${summary['allowed_amount'].mean():.2f}")
    col2.metric("Average Paid", f"${summary['paid_amount'].mean():.2f}")
    col3.metric("Average Gap", f"${summary['gap'].mean():.2f}")

    chart = (
        alt.Chart(summary.sample(min(500, len(summary))))
        .mark_circle(size=60, opacity=0.6)
        .encode(
            x="allowed_amount:Q",
            y="paid_amount:Q",
            tooltip=["allowed_amount", "paid_amount", "gap"]
        )
    )
    st.altair_chart(chart, use_container_width=True)
else:
    st.info("Sample dataset does not include allowed_amount and paid_amount fields.")

st.markdown("---")

# -----------------------------------------------------------
# DENIAL-LIKE ANALYSIS
# Paid amount = 0 or null = likely denial
# -----------------------------------------------------------

st.header("Denial Pattern Detection")

if "paid_amount" in prov.columns:
    prov["denied"] = prov["paid_amount"].fillna(0) == 0
    denial_rate = prov["denied"].mean() * 100

    st.metric("Estimated Denial Rate", f"{denial_rate:.2f}%")

    denial_chart = (
        alt.Chart(prov)
        .mark_bar()
        .encode(
            x="denied:N",
            y="count()"
        )
    )
    st.altair_chart(denial_chart, use_container_width=True)

    st.markdown("""
    A “denied claim” in this simplified dataset is any record where **paid amount = 0**.  
    In real RCM systems, denial codes (CARC/RARC) provide more detail.
    """)
else:
    st.info("Dataset missing paid_amount field to calculate denial rate.")

st.markdown("---")

# -----------------------------------------------------------
# SERVICE UTILIZATION
# -----------------------------------------------------------

st.header("Service Utilization by HCPCS Code")

if "hcpcs_code" in prov.columns:
    code_counts = prov["hcpcs_code"].value_counts().reset_index()
    code_counts.columns = ["HCPCS Code", "Count"]

    chart = (
        alt.Chart(code_counts.head(15))
        .mark_bar()
        .encode(
            x="Count:Q",
            y=alt.Y("HCPCS Code:N", sort="-x"),
            tooltip=["HCPCS Code", "Count"]
        )
    )
    st.altair_chart(chart, use_container_width=True)
else:
    st.info("Dataset missing HCPCS codes.")

st.markdown("---")

st.write("""
This module provides a simplified but realistic view of how billing datasets  
can be used to detect denial patterns, measure reimbursement gaps,  
and analyze utilization trends.  
Replace the sample_data folder with CMS datasets to extend functionality.
""")
