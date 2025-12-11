import streamlit as st
from utils.navigation import show_navbar

show_navbar()

st.title("Understanding Out-of-Pocket (OOP) Costs")
st.write("""Explains deductible, coinsurance, allowed amounts and patient responsibility.""")