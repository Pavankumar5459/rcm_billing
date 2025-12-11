import streamlit as st
from utils.navigation import show_navbar

show_navbar()

st.title("Claims Lifecycle")
st.write("""The claim lifecycle describes the path from claim creation to reimbursement.""")