import streamlit as st

st.set_page_config(layout="wide")

st.title("Patient Access & Insurance Reimbursement Journey")

st.markdown("""
This interactive page walks through the **full patient access pathway** for high-cost therapies.  
It explains every administrative and financial step required to secure coverage—from scheduling and eligibility  
to prior authorization, claims submission, denials, and appeals.

The goal is to help **patients, providers, and access teams** understand how coverage decisions are made  
and what documentation is needed at each stage.
""")

st.markdown("---")

# Timeline steps content
steps = [
    {
        "title": "1. Scheduling and Patient Intake",
        "content": """
The access journey begins when the patient is scheduled for an appointment.  
Front-office staff collect demographics, insurance card images, and confirm contact information.

Key data collected:
- Full name, DOB, address  
- Primary and secondary insurance  
- Referring provider (if applicable)  
- Reason for visit / diagnosis  

This step sets the foundation for correct eligibility checks and benefit verification.
"""
    },
    {
        "title": "2. Eligibility and Benefits Investigation",
        "content": """
Insurance is verified to determine whether the patient has **active coverage**, what services are covered,  
and what the **patient's out-of-pocket costs** will be (copay, deductible, coinsurance).

Common findings:
- Deductible remaining  
- Prior authorization required  
- Step therapy required  
- Plan exclusions for certain specialty therapies  

This step prevents avoidable denials and ensures patients are informed before treatment begins.
"""
    },
    {
        "title": "3. Out-of-Pocket Cost Estimation",
        "content": """
The provider or access team calculates the patient’s estimated financial responsibility.

Components include:
- Deductible  
- Copay  
- Coinsurance  
- Out-of-pocket maximum status  

For high-cost therapies, accurate cost counseling builds trust and supports informed decisions.
"""
    },
    {
        "title": "4. Prior Authorization Requirements Review",
        "content": """
Most specialty and infused therapies require **prior authorization**.

PA checks include:
- Diagnosis alignment with clinical criteria  
- Required labs or test results  
- Step therapy completion  
- Treatment history  
- FDA labeling and coverage policies  

Without PA approval, therapy will not be reimbursed.
"""
    },
    {
        "title": "5. Clinical Documentation Collection",
        "content": """
The provider gathers the medical records needed to demonstrate **medical necessity**.

Typical documents:
- Chart notes  
- Diagnosis records  
- Lab/imaging results  
- Previous therapies tried and failed  
- Provider attestation  

Strong documentation increases PA approval likelihood.
"""
    },
    {
        "title": "6. Prior Authorization Submission",
        "content": """
The PA request is submitted to the payer via portal, fax, EHR integration, or specialty pharmacy.

Submission includes:
- Clinical documentation packet  
- Treatment plan  
- HCPCS/CPT codes  
- ICD-10 diagnosis codes  
- Provider credentials  

Payer response time ranges from 24 hours to 30 days depending on urgency and therapy type.
"""
    },
    {
        "title": "7. Payer Review and Determination",
        "content": """
The payer evaluates:
- Medical necessity  
- FDA indication match  
- Plan-specific policies  
- Prior therapy history  
- Coverage limitations  

Possible outcomes:
- Approved  
- Denied  
- Partially approved  
- Request for additional information (“medical necessity review”)
"""
    },
    {
        "title": "8. Therapy Administration and Claim Creation",
        "content": """
Once approved, therapy can be administered (infusion, injection, specialty drug fulfillment).

Billing team creates the claim:
- HCPCS / CPT procedure codes  
- ICD-10 diagnosis codes  
- NDC number (if drug billed)  
- Units and dosage  
- Place of service  

Accurate coding ensures correct reimbursement.
"""
    },
    {
        "title": "9. Claim Submission and Adjudication",
        "content": """
Claims are submitted to the payer using CMS-1500 or UB-04 formats.  
The payer adjudicates based on:

- Plan benefits  
- Allowed amount  
- Provider contract  
- Documentation requirements  
- Modifiers used  

Outcome:
- Paid  
- Partially paid  
- Denied  
"""
    },
    {
        "title": "10. Denials and Appeals",
        "content": """
If denied, the access team analyzes the payer denial reason and resubmits an appeal.

Common denial categories:
- Medical necessity  
- Authorization missing/invalid  
- Coding mismatch  
- Coverage exclusion  

Appeal packet includes:
- Letter of medical necessity  
- Provider attestation  
- Supporting clinical documents  
- Corrected claim (if applicable)  

Successful appeals protect revenue and ensure patient access to therapy.
"""
    },
    {
        "title": "11. Final Reimbursement and Patient Billing",
        "content": """
Once adjudicated, the payer issues reimbursement to the provider or specialty pharmacy.

Final steps:
- Payment posting  
- Adjustment posting  
- Patient statement generation  
- Financial counseling if high balance  

Clear communication strongly affects patient satisfaction and overall experience.
"""
    }
]

# Timeline display
for step in steps:
    with st.expander(step["title"], expanded=False):
        st.markdown(step["content"])

st.markdown("---")

st.markdown("""
This patient access journey reflects real-world workflows used by specialty pharmacies, provider offices,
payer access teams, and pharmaceutical reimbursement support programs.

It is designed to help patients and clinicians understand what is required to secure coverage for
**high-cost therapies** and avoid avoidable delays or denials.
""")
