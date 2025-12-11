import streamlit as st
from utils.navigation import show_navbar
from utils.ui_components import centered_header, section_title, timeline_step, info_block

show_navbar()
centered_header("RCM Overview")

section_title("What is Revenue Cycle Management?")
st.write("""
Revenue Cycle Management (RCM) is the end-to-end financial process that ensures healthcare
providers get paid for the services they deliver. It covers every step from scheduling to
final collections.
""")

section_title("Full RCM Workflow")
timeline_step(1, "Patient Access", "Scheduling, registration, coverage & eligibility checks.")
timeline_step(2, "Authorization", "Review prior authorization requirements and obtain approvals.")
timeline_step(3, "Service Delivery", "Clinical encounter, documentation, and coding readiness.")
timeline_step(4, "Coding & Charge Entry", "Translate documentation into CPT/ICD codes.")
timeline_step(5, "Claim Submission", "Generate and submit EDI 837 claim to the payer.")
timeline_step(6, "Payer Adjudication", "Payer reviews coding, coverage, medical necessity.")
timeline_step(7, "Payment Posting", "Payment posted using 835 ERA or manual posting.")
timeline_step(8, "Denials & Appeals", "Fix errors, resubmit claims, or appeal medical denials.")
timeline_step(9, "Collections", "Follow-up on aged AR and patient balances.")

info_block("""
Understanding each stage helps prevent denials, accelerate reimbursement,
and improve financial performance.
""")
