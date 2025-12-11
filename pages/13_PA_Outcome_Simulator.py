
import streamlit as st
from utils.navigation import show_navbar
from utils.simulation_engine import simulate_prior_auth

show_navbar()

st.title("Prior Authorization Outcome Simulator")

complexity = st.slider("Case Complexity (1=low, 5=high)", 1, 5, 2)
docs = st.slider("Documentation Quality (1–10)", 1, 10, 8)

result = simulate_prior_auth(complexity, docs)

st.subheader("PA Approval Probability")
st.write("### " + str(result) + "%")
