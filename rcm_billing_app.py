import streamlit as st
from pathlib import Path

st.set_page_config(page_title="Hanvion Health – RCM Education Platform", layout="wide")

css_path = Path("styles/hanvion_theme.css")
if css_path.exists():
    with open(css_path) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.markdown("""
<div style="background: linear-gradient(90deg, #0EA5E9, #2563EB); 
            padding: 36px; border-radius: 12px; margin-bottom: 30px;">
    <h1 style="color:white; margin:0;">Hanvion Health – Revenue Cycle Management Education Platform</h1>
    <p style="color:white; font-size:18px; margin:4px 0 0;">
        Learn the healthcare revenue cycle through structured educational modules 
        and explore Medicare provider and geographic analytics.
    </p>
</div>
""", unsafe_allow_html=True)

col1, col2 = st.columns([1,1])
with col1:
    if st.button("Start Learning RCM"):
        st.switch_page("pages/1_RCM_Overview.py")
with col2:
    if st.button("Explore Medicare Analytics"):
        st.switch_page("pages/9_Medicare_Provider_Analytics.py")

st.markdown("---")
st.subheader("Revenue Cycle Education Modules")
