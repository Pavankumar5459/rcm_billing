import streamlit as st
from utils.navigation import show_navbar

show_navbar()

st.title("Prior Authorization (PA)")
st.write("""PA ensures the payer approves clinical necessity before services are rendered.""")