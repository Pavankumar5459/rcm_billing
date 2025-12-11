import streamlit as st
from utils.navigation import show_navbar
from utils.ui_components import centered_header, section_title, info_block, timeline_step

show_navbar()
centered_header("Coverage & Eligibility")

section_title("Insurance Verification Basics")
st.write("""
Coverage and Eligibility verification is the first gate in ensuring a claim
gets paid. Errors here cause **the highest volume of avoidable denials**.
""")

section_title("Key Concepts")
info_block("""
**• Eligibility:** Confirms the patient has active insurance coverage.  
**• Benefits:** Determines what the plan covers and what the patient must pay.  
**• Deductible:** Amount patient must pay before insurance begins contributing.  
**• Copay:** Fixed amount due for a visit or service.  
**• Coinsurance:** Percentage the patient pays after meeting deductible.  
""")

section_title("Eligibility Workflow")
timeline_step(1, "Collect Patient Information", "Demographics, insurance card, subscriber details.")
timeline_step(2, "Verify Coverage", "Check active status, plan type, termination date.")
timeline_step(3, "Check Benefits", "Copay, coinsurance, deductible remaining.")
timeline_step(4, "Identify PA Requirements", "Some services require authorization.")
timeline_step(5, "Communicate Patient Responsibility", "Clear up front understanding improves collections.")
