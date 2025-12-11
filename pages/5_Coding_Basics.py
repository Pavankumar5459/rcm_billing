import streamlit as st

st.set_page_config(layout="wide")
st.title("Medical Coding Basics")

st.markdown("""
Medical coding assigns standardized codes to diagnoses, procedures, and services.  
Accurate coding ensures correct reimbursement and reduces claim denials.
""")

st.markdown("---")
st.header("1. ICD-10-CM Coding (Diagnoses)")

st.markdown("""
ICD-10-CM codes describe the patient’s condition.

Examples:
- E11.9 — Type 2 diabetes mellitus without complications  
- I10 — Essential hypertension  
- J06.9 — Upper respiratory infection  
""")

st.markdown("---")
st.header("2. CPT Coding (Procedures)")

st.markdown("""
CPT codes represent clinical procedures and services.

Categories:
- Evaluation and Management (99202–99499)  
- Surgery (10021–69990)  
- Radiology (70010–79999)  
- Pathology and Laboratory (80047–89398)  
- Medicine (90281–99607)  
""")

st.markdown("---")
st.header("3. HCPCS Level II Coding")

st.markdown("""
HCPCS codes identify:
- Medications  
- Supplies  
- Durable Medical Equipment (DME)  
- Ambulance services  
""")

Examples:
- J-code drugs (e.g., J3490)  
- A-code supplies (e.g., A9270)  

st.markdown("---")
st.header("4. Modifiers")

st.markdown("""
Modifiers provide additional details about a service.

Common examples:
- 25 — Significant, separately identifiable E/M service  
- 59 — Distinct procedural service  
- RT/LT — Right or left side  
- 76 — Repeat procedure by same provider  
""")

st.markdown("---")
st.header("5. Why Coding Accuracy Matters")

st.markdown("""
- Ensures correct reimbursement  
- Prevents avoidable denials  
- Supports compliance  
- Improves data accuracy  
- Reduces payer audits  
""")
