import streamlit as st
from utils.navigation import show_navbar

show_navbar()

st.title("Denials Management")
st.write("""Denials represent lost revenue unless corrected promptly.""")