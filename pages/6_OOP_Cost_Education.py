import streamlit as st
from utils.navigation import show_navbar
from utils.ui_components import centered_header, section_title, info_block

show_navbar()
centered_header("Out-of-Pocket Cost Education")

section_title("Understanding Patient Financial Responsibility")
st.write("""
Out-of-pocket (OOP) costs determine what a patient pays before and after insurance.
Understanding this is essential for patient communication and accurate cost estimates.
""")

section_title("Key Terms")
info_block("""
**Deductible:** Amount the patient pays before insurance starts covering services.  
**Copay:** Fixed amount due per visit or service.  
**Coinsurance:** Percentage the patient pays after meeting deductible.  
**Out-of-Pocket Maximum:** The most a patient will pay in a year.  
""")

section_title("Example")
st.write("""
A patient with:
- $1,000 deductible  
- 20% coinsurance  
- $25 copay  
Will pay different amounts depending on whether the deductible is met.

Clear explanations help build trust and reduce billing confusion.
""")
