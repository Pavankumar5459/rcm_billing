import streamlit as st

st.set_page_config(layout="wide")
st.title("RCM Timeline Simulator")

st.markdown("""
This interactive simulator walks through the typical timeline of a healthcare encounter from initial scheduling 
to final payment resolution. Use it to understand where errors often occur and how they impact reimbursement.
""")

st.markdown("---")
st.header("Select a Stage of the Revenue Cycle")

steps = {
    "1. Scheduling and Registration": {
        "description": """
The patient is scheduled and demographic information is collected.  
Accurate registration sets the foundation for clean billing.
""",
        "risks": [
            "Incorrect name or date of birth",
            "Wrong insurance information",
            "Missing contact details"
        ],
        "rcm_impact": """
Errors at this step can cause eligibility failures and claim rejections later in the cycle.
"""
    },
    "2. Coverage and Eligibility": {
        "description": """
Insurance coverage is verified and benefits are reviewed before service.  
This includes checking active coverage, copays, deductibles, and prior authorization requirements.
""",
        "risks": [
            "Terminated coverage",
            "Incorrect payer billed",
            "Prior authorization requirement missed"
        ],
        "rcm_impact": """
Inadequate eligibility verification leads to denials, self-pay reclassification, and delayed cash flow.
"""
    },
    "3. Prior Authorization": {
        "description": """
For certain services and medications, payers require prior authorization confirming medical necessity.
""",
        "risks": [
            "Authorization not obtained",
            "Expired authorization",
            "Service performed at a non-approved location"
        ],
        "rcm_impact": """
Missing or invalid authorization commonly results in full claim denial, often non-recoverable.
"""
    },
    "4. Clinical Encounter and Documentation": {
        "description": """
The patient is seen by the provider. All diagnoses, procedures, and treatments are documented.
""",
        "risks": [
            "Insufficient clinical detail",
            "Documentation not matching level of service",
            "Missing procedure notes"
        ],
        "rcm_impact": """
Poor documentation leads to under-coding, over-coding, or denials related to medical necessity.
"""
    },
    "5. Coding and Charge Capture": {
        "description": """
Medical coders or providers assign ICD-10, CPT, and HCPCS codes, and charges are captured.
""",
        "risks": [
            "Incorrect diagnosis or procedure codes",
            "Missing modifiers",
            "Uncaptured services or missed charges"
        ],
        "rcm_impact": """
Coding errors can cause denials, rework, audit risk, and reduced reimbursement.
"""
    },
    "6. Claim Creation and Submission": {
        "description": """
The claim is generated (CMS-1500 or UB-04) and submitted to the payer, often through a clearinghouse.
""",
        "risks": [
            "Formatting errors",
            "Incomplete claim fields",
            "Wrong payer routing"
        ],
        "rcm_impact": """
Submission issues delay payment and increase the need for resubmission and follow-up.
"""
    },
    "7. Payer Adjudication": {
        "description": """
The payer reviews the claim against coverage rules, fee schedules, and clinical policies.
""",
        "risks": [
            "Coverage exclusions",
            "Fee schedule discrepancies",
            "Claim incorrectly denied"
        ],
        "rcm_impact": """
Adjudication outcomes determine provider reimbursement and patient out-of-pocket costs.
"""
    },
    "8. Payment Posting and Reconciliation": {
        "description": """
Payments, adjustments, and patient responsibilities are posted using the remittance advice.
""",
        "risks": [
            "Incorrect payment posting",
            "Contractual adjustments misapplied",
            "Secondary payer not billed"
        ],
        "rcm_impact": """
Posting errors distort financial reports and can leave collectible revenue unresolved.
"""
    },
    "9. Denials and Appeals": {
        "description": """
Denied claims are reviewed, corrected, and appealed if appropriate.
""",
        "risks": [
            "Appeal deadlines missed",
            "Root cause not fixed",
            "Insufficient appeal documentation"
        ],
        "rcm_impact": """
Weak denials management leads to permanent revenue loss and high write-offs.
"""
    },
    "10. Patient Billing and Collections": {
        "description": """
The patient is billed for their portion after payer processing.  
Clear communication helps avoid confusion and dissatisfaction.
""",
        "risks": [
            "Confusing statements",
            "Incorrect balance",
            "No payment options offered"
        ],
        "rcm_impact": """
Poor patient billing processes result in slow collections, bad debt, and patient complaints.
"""
    }
}

selected_step = st.selectbox(
    "Choose a step to view details",
    list(steps.keys())
)

data = steps[selected_step]

st.markdown(f"### {selected_step}")
st.markdown(data["description"])

st.subheader("Common Risks at This Stage")
for r in data["risks"]:
    st.markdown(f"- {r}")

st.subheader("Impact on Revenue Cycle")
st.markdown(data["rcm_impact"])

st.markdown("---")
st.markdown("Use the dropdown to explore how each stage in the RCM timeline affects reimbursement and patient experience.")
