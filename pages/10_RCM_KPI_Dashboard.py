import streamlit as st
import plotly.express as px
from utils.navigation import show_navbar
from utils.data_engine import load_provider_data, compute_kpis, compute_ar_aging, RY_DEFAULT
from utils.ui_components import kpi_card, section_header

show_navbar()

st.title(f"RCM KPI Dashboard – CMS Medicare (Reporting Year {RY_DEFAULT})")
st.caption("Data Source: CMS Medicare Physician & Other Practitioners (RY25 Release)")

df = load_provider_data()

if df is None:
    st.warning("Provider dataset not available. Please upload provider_RY25.csv.")
    st.stop()

# ------------------------------------
# KPI Cards
# ------------------------------------
kpis = compute_kpis(df)

col1, col2, col3 = st.columns(3)
with col1: kpi_card("Total Claims", f"{kpis['total_claims']:,}")
with col2: kpi_card("Denial Rate", f"{kpis['denial_rate']}%")
with col3: kpi_card("Clean Claim (FPR) Rate", f"{kpis['fpr_rate']}%")

col4, col5, col6 = st.columns(3)
with col4: kpi_card("Service Volume", f"{kpis['service_volume']:,}")
with col5: kpi_card("Avg Allowed Amount", f"${kpis['avg_allowed']:,}")
with col6: kpi_card("Dataset Year Filter", f"RY{RY_DEFAULT}")

# ------------------------------------
# Claims Volume Chart
# ------------------------------------
section_header("Claims Distribution by Allowed Amount")
fig = px.histogram(df, x="allowed_amount", nbins=40, title="Allowed Amount Histogram")
st.plotly_chart(fig, use_container_width=True)

# ------------------------------------
# Provider Performance
# ------------------------------------
section_header("Top 20 Providers by Service Volume")
if "service_count" in df.columns and "rndrng_prvdr_type" in df.columns:
    summary = df.groupby("rndrng_prvdr_type")["service_count"].sum().nlargest(20)
    fig2 = px.bar(summary, title="Top Provider Types by Volume")
    st.plotly_chart(fig2, use_container_width=True)

# ------------------------------------
# AR Aging Simulation
# ------------------------------------
section_header("Estimated AR Aging Buckets (Based on CMS Payment Ratios)")
aging = compute_ar_aging(df)

if aging:
    fig3 = px.bar(
        x=list(aging.keys()),
        y=list(aging.values()),
        labels={"x": "Aging Bucket", "y": "% of Claims"},
        title="Estimated AR Aging Distribution"
    )
    st.plotly_chart(fig3, use_container_width=True)
else:
    st.info("AR aging cannot be computed due to missing payment fields.")
