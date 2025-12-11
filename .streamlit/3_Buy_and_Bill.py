import streamlit as st

st.title("💉 Buy-and-Bill Infusion Workflow")

st.write("""
This workflow explains how specialty infused therapies (like UPLIZNA) move through reimbursement.
""")

steps = [
    "1. Benefits Verification (medical benefit)",
    "2. Prior Authorization submission",
    "3. Site-of-Care (SOC) eligibility clearance",
    "4. Buy-and-bill acquisition (J-code processing)",
    "5. Infusion scheduling",
    "6. Claim submission",
    "7. Remittance + Appeals if needed"
]

for s in steps:
    st.checkbox(s)
