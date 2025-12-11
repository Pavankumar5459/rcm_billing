import streamlit as st
from utils.navigation import show_navbar
from utils.ui_components import centered_header, kpi_card, section_title
from utils.data_engine import load_provider_data, compute_kpis

show_navbar()
centered_header("RCM KPI Dashboard")

# Load CMS Provider Data
df = load_provider_data()

if df is None or df.empty:
    st.error("Provider dataset not found.")
    st.stop()

# Compute KPIs
kpis = compute_kpis(df)

col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Medicare Payments", f"${kpis['total_payments']:,.0f}")
col2.metric("Total Services", f"{kpis['total_services']:,.0f}")
col3.metric("Avg Allowed Amount", f"${kpis['avg_allowed']:.2f}")
col4.metric("Estimated Denial Rate", f"{kpis['denial_rate']:.1f}%")

st.write("---")
section_title("Service Volume by HCPCS / CPT")

top_codes = df.groupby("hcpcs_code")["service_count"].sum().sort_values(ascending=False).head(20)
st.bar_chart(top_codes)

section_title("Payments by Provider Type")
pt = df.groupby("provider_type")["payment_amount"].sum().sort_values(ascending=False).head(15)
st.bar_chart(pt)
