
import streamlit as st
from utils.navigation import show_navbar
from utils.simulation_engine import simulate_access

show_navbar()

st.title("Patient Access Simulator")

coverage = st.slider("Coverage Score (0–100)", 0, 100, 80)
auth_required = st.checkbox("Prior Authorization Required?", True)
network = st.selectbox("Network Status", ["INN", "OON"])

result = simulate_access(coverage, auth_required, network)

st.subheader("Access Success Probability")
st.write("### " + str(result) + "%")
