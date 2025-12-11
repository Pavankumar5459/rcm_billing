import streamlit as st
from utils.navigation import show_navbar
from utils.ui_components import centered_header, section_title, timeline_step, info_block

show_navbar()
centered_header("Claims Lifecycle")

section_title("The Life of a Healthcare Claim")
timeline_step(1, "Charge Capture", "Translate services into billable CPT/HCPCS codes.")
timeline_step(2, "Claim Creation", "Build an EDI 837 claim with codes, units, modifiers, NPI.")
timeline_step(3, "Claim Scrubbing", "Check for coding errors, missing data, payer rules.")
timeline_step(4, "Claim Submission", "Sent electronically to payer.")
timeline_step(5, "Adjudication", "Payer verifies coverage, coding accuracy, medical necessity.")
timeline_step(6, "Payment or Denial", "Determined using fee schedules and payer rules.")
timeline_step(7, "Appeals", "Correct errors or challenge clinical denials.")
timeline_step(8, "Collections", "Patient and payer balances are pursued.")

info_block("""
Understanding this lifecycle is essential for preventing denials and accelerating payment.
""")
