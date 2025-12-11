
import streamlit as st
from utils.navigation import show_navbar
from utils.simulation_engine import simulate_claim

show_navbar()

st.title("Claims Adjudication Simulator")

payment_accuracy = st.slider("Payment Accuracy Score (0–100)", 0, 100, 80)
coding_quality = st.slider("Coding Quality Score (0–100)", 0, 100, 90)
auth_status = st.selectbox("Authorization Status", ["Approved", "Missing"])

outcome = simulate_claim(payment_accuracy, coding_quality, auth_status)

st.subheader("Claim Outcome")
st.write("### " + str(outcome))
