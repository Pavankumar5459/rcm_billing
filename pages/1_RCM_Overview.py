import streamlit as st

st.set_page_config(layout="wide")

st.title("RCM Overview")

st.markdown("""
This module provides a clear explanation of the end-to-end revenue cycle,  
from patient intake through final reimbursement.  
It is designed for training users who need to understand the complete workflow  
supporting patient access and financial clearance.
""")

st.markdown("---")

st.header("What Is the Revenue Cycle?")

st.markdown("""
The revenue cycle is the full administrative and financial process that a patient encounter follows.  
It includes scheduling, eligibility verification, prior authorization, documentation, coding, billing,  
payers' adjudication, reimbursement, and appeals.

A strong revenue cycle ensures:
- Accurate claims  
- Faster reimbursement  
- Fewer denials  
- Clear communication to patients  
""")

st.markdown("---")

sections = [
    ("1. Scheduling & Registration",
     "Collect demographics, insurance information, referral details, and reason for visit."),

    ("2. Eligibility & Benefits Verification",
     "Confirm coverage, network status, deductible, copay, and coinsurance."),

    ("3. Prior Authorization",
     "Determine if the service or therapy requires payer approval before treatment."),

    ("4. Documentation & Coding",
     "Ensure correct ICD-10 diagnosis codes, CPT/HCPCS procedure codes, and medical necessity documentation."),

    ("5. Claim Creation",
     "Generate the claim with all required codes, modifiers, units, and provider details."),

    ("6. Claim Submission & Adjudication",
     "Submit electronically to the payer. The payer evaluates coverage, contracts, and benefit rules."),

    ("7. Payment Posting",
     "Payer issues payment or denial. Payments are posted and matched to accounts."),

    ("8. Denials & Appeals",
     "Analyze denial reasons and submit appeal packets or corrected claims."),

    ("9. Patient Billing",
     "Generate statements based on remaining balances, copays, and deductibles.")
]

for title, text in sections:
    with st.expander(title):
        st.write(text)

st.markdown("---")

st.write("Use the navigation menu or Home page to explore detailed modules on each component of the revenue cycle.")
