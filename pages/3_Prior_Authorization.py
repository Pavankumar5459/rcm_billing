from utils.navigation import show_navbar
show_navbar()
import streamlit as st

st.set_page_config(layout="wide")
st.title("Prior Authorization")

st.markdown("""
Prior Authorization (PA) is a cost-control process used by payers to determine whether a planned procedure, 
medication, or service is medically necessary. Failure to obtain PA results in denials and lost revenue.
""")

st.markdown("---")
st.header("When Is Prior Authorization Required?")

st.markdown("""
- High-cost medications  
- Diagnostic imaging (MRI, CT)  
- Specialty procedures  
- Infusion therapies  
- Certain DME (Durable Medical Equipment)  
- Out-of-network services  
""")

st.markdown("---")
st.header("Prior Authorization Workflow")

st.markdown("""
1. Provider determines need for service  
2. Clinical documentation gathered  
3. Authorization request submitted to payer  
4. Payer reviews medical necessity criteria  
5. Approval, denial, or request for more information  
6. Authorization stored in EHR  
7. Claim submitted with PA reference number  
""")

st.markdown("---")
st.header("Why Payers Require PA")

col1, col2 = st.columns(2)
with col1:
    st.subheader("From a Cost-Management Perspective")
    st.markdown("""
    - Prevents overuse of expensive services  
    - Ensures adherence to clinical guidelines  
    - Controls spending on specialty care  
    """)

with col2:
    st.subheader("From an RCM Perspective")
    st.markdown("""
    - Missing PA leads to full claim denial  
    - Retroactive authorization often not available  
    - Delays treatment and reimbursement  
    """)

st.markdown("---")
st.header("Common PA Denials")

st.markdown("""
- Missing or invalid authorization  
- Procedure not covered under plan  
- Incorrect clinical documentation  
- PA expired before date of service  
- Service rendered at non-approved facility  
""")

st.markdown("---")
st.header("Best Practices for Preventing PA Issues")

st.markdown("""
- Create standardized authorization checklists  
- Verify payer-specific rules during scheduling  
- Track submitted and pending authorizations  
- Maintain real-time communication with providers  
- Document authorization numbers clearly  
""")
