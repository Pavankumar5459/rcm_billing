import streamlit as st
from utils.navigation import show_navbar
from utils.ui_components import centered_header, section_title, info_block

show_navbar()
centered_header("Access Simulator")

section_title("Simulate Eligibility & Access Outcomes")

st.write("""
This simulator estimates whether a patient is likely to be approved at the access stage.
It considers eligibility, documentation, and clinical requirements.
""")

# Inputs
plan_active = st.selectbox("Active Insurance Coverage?", ["Yes", "No"])
ded_met = st.selectbox("Deductible Met?", ["Yes", "No"])
docs_ready = st.selectbox("Documentation Complete?", ["Yes", "No"])
clinical_match = st.selectbox("ICD-10 Supports CPT?", ["Yes", "No"])

section_title("Result")

if plan_active == "No":
    info_block("❌ Access Denied: No active insurance coverage.")
elif docs_ready == "No":
    info_block("❌ Access Denied: Missing documentation required.")
elif clinical_match == "No":
    info_block("❌ Access Denied: Diagnosis does not support service.")
else:
    info_block("✅ Access Approved: PA or claim likely to move forward successfully.")
