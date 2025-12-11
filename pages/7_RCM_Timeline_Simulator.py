
import streamlit as st
from utils.navigation import show_navbar

show_navbar()

st.title("RCM Timeline Simulator")

st.write("Simulates the timeline of a patient claim journey across eligibility → PA → claim → adjudication → payment.")

steps = [
    "1. Appointment scheduled",
    "2. Eligibility checked",
    "3. Prior Authorization submitted",
    "4. Service performed",
    "5. Claim submitted",
    "6. Claim adjudicated",
    "7. Payment posted / denial issued"
]

st.subheader("RCM Timeline Steps")
for s in steps:
    st.write("• " + s)
