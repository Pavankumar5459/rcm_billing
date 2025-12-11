import streamlit as st
from utils.navigation import show_navbar
from utils.ui_components import centered_header, section_title, info_block
from utils.data_engine import load_provider_data, compute_denial_distribution

show_navbar()
centered_header("Denials Dashboard")

df = load_provider_data()

if df is None or df.empty:
    st.error("Provider dataset not found.")
    st.stop()

denials = compute_denial_distribution(df)

section_title("Estimated Denial Categories")

st.bar_chart(denials.set_index("category")["rate"])

info_block("""
These denial rates are modeled using:
- CPT complexity  
- Utilization patterns  
- Medicare adjudication trends  
- Common RCM denial drivers  
""")

section_title("Denial Summary Table")
st.dataframe(denials)
