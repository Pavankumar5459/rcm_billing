import streamlit as st

st.set_page_config(layout="wide")
st.title("Claims Lifecycle")

st.markdown("""
The Claims Lifecycle represents the full financial journey of a healthcare encounter—from documentation 
to reimbursement. Understanding this lifecycle helps reduce denials and streamline revenue operations.
""")

st.markdown("---")
st.header("1. Clinical Documentation")

st.markdown("""
Accurate documentation by providers is the foundation of successful billing.  
Documentation must support medical necessity, coding, and payer requirements.
""")

st.markdown("""
Examples of required documentation:
- Diagnoses  
- Procedures  
- Medications  
- Time-based services  
- Imaging and lab reports  
""")

st.markdown("---")
st.header("2. Medical Coding")

st.markdown("""
Coding translates clinical work into standardized billing codes.
""")

col1, col2 = st.columns(2)
with col1:
    st.subheader("ICD-10-CM")
    st.markdown("Represents diagnoses and conditions.")

with col2:
    st.subheader("CPT / HCPCS")
    st.markdown("""
    CPT: Procedures performed  
    HCPCS: Drugs, supplies, and additional services  
    """)

st.markdown("---")
st.header("3. Charge Capture")

st.markdown("""
Charge capture ensures that all provider services are converted into billable charges.  
Missed charges result in lost revenue.
""")

st.markdown("---")
st.header("4. Claim Creation")

st.markdown("""
Claims are generated using standard formats:
- CMS-1500 (professional claims)  
- UB-04 (facility claims)  
""")

st.markdown("""
Claims must include:
- Patient demographics  
- Insurance information  
- Diagnosis codes  
- Procedure codes  
- Provider information  
""")

st.markdown("---")
st.header("5. Claim Submission")

st.markdown("""
Claims are transmitted to the payer through a clearinghouse.  
Clearinghouses check for formatting errors before submitting to the payer.
""")

st.markdown("---")
st.header("6. Payer Adjudication")

st.markdown("""
Payers evaluate the claim based on:
- Coverage rules  
- Medical necessity  
- Allowed amounts  
- Fee schedules  
- Coordination of benefits  
""")

st.markdown("""
Possible outcomes:
- Paid  
- Partially paid  
- Denied  
- Additional information requested  
""")

st.markdown("---")
st.header("7. Payment Posting")

st.markdown("""
Payments and adjustments are posted using an ERA (Electronic Remittance Advice).  
Patient responsibility (copay, deductible, coinsurance) is also recorded.
""")

st.markdown("---")
st.header("8. Denial Management")

st.markdown("""
Denied claims must be corrected and resubmitted.  
This is one of the most resource-intensive RCM tasks.
""")

st.markdown("""
Common denial reasons include:
- Eligibility issues  
- Missing authorization  
- Coding errors  
- Non-covered services  
""")

st.markdown("---")
st.header("9. Patient Billing")

st.markdown("""
Patients receive a statement for their share of the cost after insurance processes the claim.  
Clear communication improves patient satisfaction and reduces confusion.
""")

st.markdown("---")
st.header("Why Understanding the Claims Lifecycle Matters")

st.markdown("""
- Improves clean claim rates  
- Reduces rework  
- Speeds up reimbursement  
- Supports better compliance  
""")
