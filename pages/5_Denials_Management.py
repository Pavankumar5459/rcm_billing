import streamlit as st
from utils.navigation import show_navbar
from utils.ui_components import centered_header, section_title, info_block

show_navbar()
centered_header("Denials Management")

section_title("Major Denial Categories")
info_block("""
**1. Eligibility Denials:** Coverage inactive or plan mismatch.  
**2. Authorization Denials:** Missing PA or expired approval.  
**3. Coding Denials:** Incorrect CPT/ICD, missing modifiers, unbundling.  
**4. Medical Necessity:** Insufficient documentation for the service.  
**5. Timely Filing:** Claim not submitted within payer rules.  
""")

section_title("Appeal Strategies")
st.write("""
- Include detailed clinical notes  
- Use correct appeal forms  
- Reference payer policies  
- Submit within time limits  
- Support claims with evidence-based guidelines  
""")

section_title("Root Cause Prevention")
st.write("""
Effective denials management includes:  
- Training staff  
- Automating eligibility  
- Pre-claim scrubbing  
- Strong documentation workflows  
""")
