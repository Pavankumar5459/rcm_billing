import streamlit as st
from utils.navigation import show_navbar
from utils.ui_components import centered_header, section_title, timeline_step, info_block

show_navbar()
centered_header("Prior Authorization")

section_title("What is a Prior Authorization?")
st.write("""
A Prior Authorization (PA) is a payer requirement to review clinical documentation
before approving a service. High-cost therapies often require PA.
""")

section_title("Why Do Payers Require PA?")
info_block("""
• Ensure medical necessity  
• Control cost of specialty medications  
• Reduce inappropriate utilization  
""")

section_title("PA Workflow")
timeline_step(1, "Order Received", "Provider decides service or drug is clinically needed.")
timeline_step(2, "Check PA Rules", "Payer and plan determine if authorization is required.")
timeline_step(3, "Submit Documentation", "Provider sends clinical notes, ICD codes, labs, imaging.")
timeline_step(4, "Payer Review", "Clinical reviewers evaluate medical necessity.")
timeline_step(5, "Decision", "Approval, denial, or request for additional information.")
timeline_step(6, "Appeal (if needed)", "Peer-to-peer or written appeal.")

info_block("""
Strong documentation is the #1 reason PAs get approved.
""")
