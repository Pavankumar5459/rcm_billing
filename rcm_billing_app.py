import streamlit as st

st.set_page_config(layout="wide")

# ---- HIDE STREAMLIT DEFAULT SIDEBAR ----
hide_sidebar_style = """
    <style>
        section[data-testid="stSidebar"] {display: none;}
        div[data-testid="collapsedControl"] {display: none;}
    </style>
"""
st.markdown(hide_sidebar_style, unsafe_allow_html=True)

import streamlit as st

# -------------------------------------------------------
# BASIC PAGE SETUP
# -------------------------------------------------------
st.set_page_config(
    page_title="Hanvion RCM Education",
    layout="wide"
)

# -------------------------------------------------------
# SIDEBAR NAVIGATION (simple & clean)
# -------------------------------------------------------
st.sidebar.title("Hanvion RCM Training")

pages = {
    "RCM Overview": "overview",
    "Coverage & Eligibility": "eligibility",
    "Prior Authorization": "pa",
    "Claims Lifecycle": "claims",
    "Denials Management": "denials",
    "Cost & Billing": "billing",
    "Posting Payments": "payments",
    "Revenue Cycle Summary": "summary",
    "EHR Challenge": "ehr"
}

selected = st.sidebar.radio("Navigate", list(pages.keys()))
page = pages[selected]

# -------------------------------------------------------
# PAGE CONTENT FUNCTIONS
# -------------------------------------------------------

def page_overview():
    st.title("RCM Overview")
    st.write("""
### What is Revenue Cycle Management?

Revenue Cycle Management (RCM) refers to the full financial process used by healthcare organizations to:

1. Capture patient information  
2. Verify insurance  
3. Obtain authorizations  
4. Code the visit  
5. Submit claims  
6. Manage denials  
7. Collect payments  

A strong RCM process improves **cash flow, reduces denials, and shortens Days in AR**.
    """)

def page_eligibility():
    st.title("Coverage & Eligibility")
    st.write("""
### Insurance Eligibility Verification

Eligibility is the **first step** in avoiding claim denials.

It confirms:
- Insurance plan is active  
- Patient is eligible for services  
- Deductible, copay, coinsurance  
- Prior authorization requirements  

Eligibility failures lead to **front-end denials**.
    """)

def page_pa():
    st.title("Prior Authorization")
    st.write("""
### Prior Authorization Basics

Prior authorization is required when insurers need medical justification **before** approving the service.

Common examples:
- MRI / CT  
- Specialty medications  
- Surgeries  
- High-cost biologics  

If PA is not obtained, the claim may be **denied or billed to the patient**.
    """)

def page_claims():
    st.title("Claims Lifecycle")
    st.write("""
### How a Claim Moves Through the Lifecycle

1. **Charge Capture**  
2. **Coding (ICD-10, CPT/HCPCS)**  
3. **Claim Scrubbing**  
4. **Submission to Payer**  
5. **Adjudication**  
6. **Payment or Denial**  
7. **Patient Billing**  

This is the backbone of revenue cycle performance.
    """)

def page_denials():
    st.title("Denials Management")
    st.write("""
### Understanding Claim Denials

Top denial categories:
- Missing information  
- Eligibility issues  
- Authorization not obtained  
- Coding errors  
- Timely filing  

A strong denial management team **reduces write-offs** and improves payer relationships.
    """)

def page_billing():
    st.title("Cost & Billing")
    st.write("""
### Costs, Billing, and Patient Responsibility

Patients may owe:
- Deductibles  
- Copays  
- Coinsurance  
- Non-covered services  

Clear cost communication reduces:
- Surprise billing  
- Patient dissatisfaction  
- Bad debt  

Providers often use **ABN (Advance Beneficiary Notice)** for Medicare.
    """)

def page_payments():
    st.title("Posting Payments")
    st.write("""
### Payment Posting Process

Payment posting ensures the financial records match payer remittances.

Includes:
- ERA / EOB reconciliation  
- Applying patient payments  
- Handling adjustments  
- Identifying underpayments  

Accurate posting drives **clean AR reports and KPI accuracy**.
    """)

def page_summary():
    st.title("Revenue Cycle Summary")
    st.write("""
### Full RCM Summary

The entire revenue cycle includes:

1. Scheduling  
2. Registration  
3. Eligibility Verification  
4. Authorization  
5. Coding  
6. Claim Submission  
7. Denial Management  
8. Payment Posting  
9. Patient Collections  

This summary helps visualize the **end-to-end financial workflow**.
    """)

def page_ehr():
    st.title("EHR Challenge")
    st.write("""
### Mini EHR Simulation (Simple Version)

Provide the following:

- Patient DOB  
- Insurance Provider  
- Type of Service  
- ICD-10 Code  
- Additional Notes  

This teaches how front-desk and clinical staff capture data for billing.
    """)

    # Simple form
    with st.form("ehr_form"):
        dob = st.date_input("Patient DOB")
        insurance = st.text_input("Insurance Provider")
        service = st.text_input("Service Type")
        icd_code = st.text_input("ICD-10 Code")
        notes = st.text_area("Additional Notes")

        submitted = st.form_submit_button("Submit")

        if submitted:
            st.success("Data captured successfully! (Simulation only)")


# -------------------------------------------------------
# PAGE ROUTER
# -------------------------------------------------------

if page == "overview":
    page_overview()
elif page == "eligibility":
    page_eligibility()
elif page == "pa":
    page_pa()
elif page == "claims":
    page_claims()
elif page == "denials":
    page_denials()
elif page == "billing":
    page_billing()
elif page == "payments":
    page_payments()
elif page == "summary":
    page_summary()
elif page == "ehr":
    page_ehr()
