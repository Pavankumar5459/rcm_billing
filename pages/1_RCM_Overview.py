import streamlit as st

st.set_page_config(layout="wide")

# Title
st.title("Revenue Cycle Management (RCM) Overview")

st.markdown("""
Revenue Cycle Management (RCM) is the end-to-end financial process that healthcare organizations use 
to track patient encounters from initial registration to final payment.  
This module provides a structured, professional overview of the full RCM lifecycle.
""")

st.markdown("---")

# Section 1: What is RCM?
st.header("What Is Revenue Cycle Management?")
st.markdown("""
Revenue Cycle Management is the coordination of administrative and clinical functions that contribute to 
capturing, managing, and collecting patient service revenue.  

RCM connects **clinical care**, **documentation**, **coding**, **billing**, **payer rules**, and **collections** 
into a unified financial process.
""")

st.markdown("""
Key components include:
- Insurance verification and coverage checks  
- Prior authorization when required  
- Accurate clinical documentation  
- Correct medical coding (ICD-10, CPT, HCPCS)  
- Clean claim submission  
- Payment posting and denial review  
- Appeals and follow-up on unpaid claims  
""")

st.markdown("---")

# Section 2: Why RCM Matters
st.header("Why RCM Matters")
col1, col2 = st.columns(2)

with col1:
    st.subheader("For Healthcare Organizations")
    st.markdown("""
    - Ensures timely reimbursement  
    - Reduces claim denials and rework  
    - Improves financial stability  
    - Supports compliance and audit readiness  
    - Enables operational efficiency  
    """)

with col2:
    st.subheader("For Patients")
    st.markdown("""
    - Accurate insurance coverage determination  
    - Correct out-of-pocket estimates  
    - Fewer billing surprises  
    - Faster claim resolution  
    - Better understanding of benefit limitations  
    """)

st.markdown("---")

# Section 3: The End-to-End RCM Lifecycle
st.header("The End-to-End RCM Lifecycle")

st.markdown("""
Below is the standard RCM workflow followed across hospitals, clinics, and physician practices.
""")

st.markdown("""
**1. Patient Access and Registration**  
Collection of demographics, insurance details, and eligibility verification.

**2. Coverage & Eligibility**  
Determining active coverage, payer rules, deductibles, copays, and benefits.

**3. Prior Authorization (if required)**  
Submitting medical necessity documentation to obtain approval before services.

**4. Clinical Encounter**  
Patient receives services; provider documents findings and treatment.

**5. Coding**  
ICD-10 for diagnoses; CPT/HCPCS for procedures and medications; modifiers applied when needed.

**6. Charge Capture**  
Translating clinical activity into billable charges.

**7. Claim Creation & Submission**  
CMS-1500 or UB-04 created; sent to clearinghouse or payer.

**8. Adjudication**  
Payer reviews coverage rules, coding accuracy, medical necessity, and contractual agreements.

**9. Payment Posting**  
Allowed amounts, patient responsibility, adjustments, and payment are recorded.

**10. Denials Management**  
Incorrect, incomplete, or non-covered claims are reviewed and corrected.

**11. Appeals & Follow-up**  
Additional documentation submitted; claim reconsidered.

**12. Patient Billing & Collections**  
Statements generated for patient responsibility after insurance payment.

""")

st.markdown("---")

# Section 4: Common RCM Challenges
st.header("Common Challenges in Revenue Cycle")

st.markdown("""
Even well-structured RCM teams face operational and financial challenges.  
Below are the most frequent issues that impact revenue leakage.
""")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    **Common Operational Issues**
    - Incomplete patient information  
    - Incorrect insurance coverage details  
    - Missing prior authorizations  
    - Documentation gaps  
    - Incorrect coding  
    """)

with col2:
    st.markdown("""
    **Financial Impact Areas**
    - Increased claim rejections  
    - Denials due to coding or benefit limitations  
    - Payment delays  
    - Reduced reimbursement  
    - Higher administrative costs  
    """)

st.markdown("---")

# Section 5: How This Dashboard Helps
st.header("How This Dashboard Helps You Learn RCM")

st.markdown("""
This platform is designed to give you both **educational clarity** and **data-driven insight** using 
real Medicare datasets.

You will learn:
- Core RCM concepts step by step  
- How payers determine reimbursement  
- Medicare Part B utilization patterns  
- Geographic differences in healthcare spending  
- How coding impacts payments  
- How eligibility and authorization affect claim success  

Use the navigation to continue learning each component in depth.
""")

st.markdown("---")

st.markdown("Navigate to the next module using the sidebar to continue your learning journey.")
