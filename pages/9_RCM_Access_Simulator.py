import streamlit as st

st.set_page_config(layout="wide")

# -------------------------------------------------
# Simulator Steps
# -------------------------------------------------
steps = [
    {
        "title": "1. Patient Intake",
        "description": """
The journey begins with the patient entering the healthcare system.  
The clinic collects demographics, insurance details, referring provider information,  
and reason for visit.

Accurate intake ensures clean downstream processing.
"""
    },
    {
        "title": "2. Eligibility & Benefits Verification",
        "description": """
The access team verifies whether the patient's insurance is active and what benefits apply.

Key checks:
- Active coverage for the date of service  
- Deductible balance  
- Copay/coinsurance  
- Therapy coverage restrictions  
- Prior authorization requirements  

This prevents avoidable denials later.
"""
    },
    {
        "title": "3. Out-of-Pocket Estimation",
        "description": """
The provider office estimates what the patient will owe.  
This is especially important for high-cost therapies.

Factors:
- Deductible remaining  
- Copay amounts  
- Coinsurance rules  
- Out-of-pocket maximum status  
"""
    },
    {
        "title": "4. Prior Authorization Review",
        "description": """
Most specialty drugs require prior authorization.

The team confirms:
- Diagnosis alignment  
- FDA label/coverage criteria  
- Step therapy requirements  
- Lab/imaging requirements  
- Provider credentials  

This determines what clinical proofs must be submitted.
"""
    },
    {
        "title": "5. Clinical Documentation Assembly",
        "description": """
Medical necessity must be clearly documented.

Documentation typically includes:
- Chart notes  
- Diagnosis and staging  
- Previous therapies tried/failed  
- Test results  
- Treatment rationale  

Good documentation improves approval rate.
"""
    },
    {
        "title": "6. Prior Authorization Submission",
        "description": """
The PA packet is submitted through payer portals, fax, EHR, or specialty pharmacy channels.

Includes:
- HCPCS/CPT codes  
- ICD-10 diagnosis codes  
- Provider NPI/credentials  
- Medical necessity packet  
"""
    },
    {
        "title": "7. Payer Review",
        "description": """
The payer evaluates medical necessity, benefit rules, clinical guidelines, and plan documentation.

Possible outcomes:
- Approved  
- Denied  
- Partially approved  
- Additional info requested  
"""
    },
    {
        "title": "8. Therapy Administration",
        "description": """
After approval, therapy can be administered or fulfilled by a specialty pharmacy.

Documentation of dosage, units, and site of care must be exact.
"""
    },
    {
        "title": "9. Claim Creation & Submission",
        "description": """
Billing creates a claim with correct codes and submits it to the payer.

Claim accuracy requires:
- Procedure codes (HCPCS/CPT)  
- Diagnosis codes (ICD-10)  
- Drug units  
- Modifiers  
- Place of service  

Clean claims get reimbursed faster.
"""
    },
    {
        "title": "10. Claim Adjudication",
        "description": """
The payer processes the claim based on:
- Plan benefits  
- Allowed amount  
- Provider contract  
- Prior authorization status  
- Coding consistency  

Possible results:
- Paid  
- Underpaid  
- Denied  
"""
    },
    {
        "title": "11. Denials & Appeals",
        "description": """
If denied, the access team reviews the payer's reason and prepares an appeal.

Appeal components:
- Letter of medical necessity  
- Clinical packet  
- Provider attestation  
- Corrected claim  

Successful appeals restore reimbursement and patient access.
"""
    }
]

# -------------------------------------------------
# Session State Initialization
# -------------------------------------------------
if "step_index" not in st.session_state:
    st.session_state.step_index = 0

# Helper functions
def next_step():
    if st.session_state.step_index < len(steps) - 1:
        st.session_state.step_index += 1

def prev_step():
    if st.session_state.step_index > 0:
        st.session_state.step_index -= 1

# -------------------------------------------------
# UI Layout
# -------------------------------------------------
current = st.session_state.step_index
step = steps[current]

st.subheader(f"Step {current+1} of {len(steps)}")
st.markdown(f"### {step['title']}")
st.markdown(step["description"])

st.markdown("---")

col1, col2, col3 = st.columns([1,1,6])

with col1:
    if current > 0:
        st.button("Back", on_click=prev_step)

with col2:
    if current < len(steps) - 1:
        st.button("Next", on_click=next_step)

st.markdown("---")

st.write("""
This simulator reflects real-world patient access workflows used by provider offices,
specialty pharmacies, payer utilization management teams, and pharmaceutical reimbursement hubs.
""")
