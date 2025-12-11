
import streamlit as st
from utils.navigation import show_navbar
from utils.denial_engine import classify_denial, denial_appeal_recommendation

show_navbar()

st.title("Billing & Denials Insights")

reason = st.text_input("Enter denial reason text")

if reason:
    category = classify_denial(reason)
    action = denial_appeal_recommendation(category)

    st.write("### Category: " + str(category))
    st.write("**Recommended Action:** " + str(action))
