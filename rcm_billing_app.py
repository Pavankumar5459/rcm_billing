import streamlit as st
import os
from utils.navigation import show_navbar

# -------------------------------------
# Load CSS theme
# -------------------------------------
def load_css():
    css_path = "styles/hanvion_theme.css"
    if os.path.exists(css_path):
        with open(css_path) as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# -------------------------------------
# MAIN APPLICATION ENTRY
# -------------------------------------
def main():

    st.set_page_config(
        page_title="Hanvion Health – RCM Platform",
        layout="wide",
        initial_sidebar_state="expanded"
    )

    load_css()
    show_navbar()

    st.title("Hanvion Health – Revenue Cycle Management Platform")
    st.subheader("Interactive Education • Analytics • Simulators (RY25 Medicare)")

    st.markdown("---")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("### **RCM Overview**")
        st.write("Explore the complete revenue cycle workflow from eligibility to payment posting.")

    with col2:
        st.markdown("### **Coverage, Eligibility & Prior Authorization**")
        st.write("Learn how payers determine benefits and the workflow for authorizations.")

    with col3:
        st.markdown("### **Claims, Denials & Appeals**")
        st.write("Understand claim creation, adjudication, denials, and resolution pathways.")

    st.markdown("---")

    col4, col5 = st.columns(2)

    with col4:
        st.markdown("### **RCM KPI Dashboard (RY25)**")
        st.write("Real-world CMS analytics with claims performance, FPR, denial rate, and AR aging.")

    with col5:
        st.markdown("### **Simulators**")
        st.write("Interactive tools for PA outcomes, claims adjudication, and access modeling.")

    st.markdown("---")
    st.caption("Powered by Hanvion Health • Reporting Year 2025 CMS Medicare Utilization")


if __name__ == "__main__":
    main()
