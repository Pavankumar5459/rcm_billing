import streamlit as st
from utils.navigation import show_navbar
from utils.ui_components import centered_header, section_title, info_block

show_navbar()
centered_header("Billing & Denials Insights")

section_title("Common Billing Issues")
info_block("""
- Missing or incorrect modifiers  
- Incomplete documentation  
- Service billed without prior authorization  
- Incorrect place of service code  
- Coding not supported by clinical notes  
""")

section_title("Top Denial Drivers")
info_block("""
1. Eligibility issues  
2. Authorization missing or invalid  
3. Medical necessity not supported  
4. Incorrect coding or bundling  
5. Timely filing exceeded  
""")

section_title("How to Reduce Denials")
st.write("""
- Automate eligibility checks  
- Confirm PA before service  
- Use scrubbers to catch errors before submission  
- Train providers on documentation standards  
- Analyze payer patterns using dashboards  
""")
