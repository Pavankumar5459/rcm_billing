import streamlit as st

st.set_page_config(layout="wide")
st.title("Claims Lifecycle")

st.markdown("""
The claims lifecycle represents the financial journey of a healthcare service from clinical documentation 
to payer reimbursement. Understanding this process is essential for preventing denials and optimizing cash flow.
""")

st.markdown("---")
st.header("Claims Lifecycle Stages")

st.subheader("1. Clinical Documentation")
st.markdown("""
Providers document diagnoses, procedures, medications, and all services rendered.  
Accurate documentation is the foundation of correct coding and billing.
""")

st.subheader("2. Medical Coding")
st.markdown("""
- ICD-10: Diagnosis codes  
- CPT: Procedure codes  
- HCPCS: Supply, drug, and device codes  
- Modifiers: Clarify circumstances of service  
""")

st.subheader("3. Charge Capture")
st.markdown("""
Translation of services into billable charges.  
Missed charges lead to revenue leakage.
""")

st.subheader("4. Claim Creation")
st.markdown("""
Claims are generated using standardized formats:
- CMS-1500 (professional claims)  
- UB-04 (facility claims)  
""")

st.subheader("5. Claim Submission")
st.markdown("""
Claims are sent to the payer through a clearinghouse, which performs initial edits for errors.
""")

st.subheader("6. Adjudication")
st.markdown("""
The payer determines:
- What is covered  
- What is denied  
- Allowed amount  
- Provider reimbursement  
- Patient responsibility  
""")

st.subheader("7. Payment Posting")
st.markdown("""
Payments, adjustments, and patient liabilities are posted using the ERA (Electronic Remittance Advice).
""")

st.subheader("8. Denial Management")
st.markdown("""
Denied claims are analyzed, corrected, and resubmitted.  
Common denial categories: eligibility, coding, medical necessity, authorization.
""")

st.subheader("9. Patient Billing")
st.markdown("""
Patients are billed for their portion after insurance payments.  
Clear statements reduce confusion and improve collections.
""")

st.markdown("---")
st.header("What Makes a Claim 'Clean'?")

st.markdown("""
A clean claim is one that contains no errors, requires no manual intervention, and is processed on the 
first submission. Clean claim rates are a critical RCM performance metric.
""")

st.markdown("""
**Clean claims require:**
- Correct patient information  
- Verified eligibility  
- Accurate coding  
- Valid authorization  
- Correct modifiers  
- Supported documentation  
- Correct payer ID  
""")

st.markdown("---")
st.header("Why Claims Lifecycle Knowledge Matters")

st.markdown("""
Understanding each step of the claims lifecycle allows RCM professionals to reduce denials, increase 
reimbursement, and improve the financial health of the organization.
""")
