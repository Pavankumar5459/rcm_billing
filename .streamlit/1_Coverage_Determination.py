import streamlit as st

st.title("🧭 Coverage Determination Engine")

st.write("""
This tool walks through how payers decide whether a therapy is **approved**, **denied**, or **pending more information**.
""")

with st.expander("Step 1: Patient & Benefit Verification"):
    st.write("""
- Verify patient demographics  
- Confirm active insurance  
- Validate eligibility dates  
""")

with st.expander("Step 2: Medical Necessity Check"):
    icd = st.text_input("Diagnosis (ICD-10)")
    st.write("Payers evaluate if the ICD-10 supports medical necessity.")

with st.expander("Step 3: Prior Authorization Required?"):
    st.write("Most specialty + infusion medications require PA under the medical benefit.")

with st.expander("Step 4: Clinical Review"):
    st.write("""
Payer nurses review:
- Diagnosis  
- Provider notes  
- Previous treatments  
- Lab results  
""")

decision = st.selectbox("Final Determination:", ["Approved", "Denied", "Need More Info"])

if decision == "Approved":
    st.success("Therapy approved ✔ Coverage confirmed.")
elif decision == "Denied":
    st.error("Claim denied ❌ See Denial Resolver page.")
else:
    st.warning("Payer requires additional documents.")
