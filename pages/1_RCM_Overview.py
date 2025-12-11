import streamlit as st
from utils.navigation import show_navbar

show_navbar()

st.title("Revenue Cycle Management (RCM) Overview")
st.write("""The Revenue Cycle represents the complete financial journey of a patient encounter — 
from scheduling and insurance verification to claims submission, adjudication, and payment posting.""")