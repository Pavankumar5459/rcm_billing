import streamlit as st
from utils.navigation import show_navbar
from utils.ui_components import centered_header, section_title, timeline_step

show_navbar()
centered_header("RCM Timeline Simulator")

section_title("Simulate a Patient's Journey")

st.write("""
This simulator walks through the high-level journey a patient encounters in the revenue cycle.
""")

timeline_step(1, "Scheduling", "Patient books visit. Provider collects insurance details.")
timeline_step(2, "Eligibility Verification", "Insurance plan, copay, deductible confirmed.")
timeline_step(3, "Prior Authorization", "If required, provider submits clinical documentation.")
timeline_step(4, "Service Delivery", "Provider sees the patient and documents the visit.")
timeline_step(5, "Coding", "Visit is coded using CPT, HCPCS, ICD-10.")
timeline_step(6, "Claim Submission", "Claim sent electronically to payer.")
timeline_step(7, "Adjudication", "Payer reviews coding, coverage, medical necessity.")
timeline_step(8, "Payment or Denial", "Based on policy, coding rules, and documentation.")
timeline_step(9, "Appeals & Collections", "If denied, provider can appeal for reconsideration.")
