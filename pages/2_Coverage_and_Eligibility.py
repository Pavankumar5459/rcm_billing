import streamlit as st

st.set_page_config(layout="wide")
st.title("Coverage and Eligibility")

st.markdown("""
Coverage and Eligibility verification ensures that services are billed correctly and that the payer will 
contribute to the cost of care. This step prevents unnecessary claim rejections and establishes accurate 
patient financial responsibility.
""")

st.markdown("---")
st.header("Key Concepts")

st.markdown("""
**Coverage** refers to the specific services an insurance plan will pay for under the patient's benefits.

**Eligibility** verifies whether the patient has active insurance during the date of service.
""")

st.subheader("What Is Verified During Eligibility?")
st.markdown("""
- Active/Inactive insurance status  
- Plan type: HMO, PPO, EPO, Medicare, Medicaid  
- Coverage dates  
- Deductibles (met vs remaining)  
- Copay amounts  
- Coinsurance percentage  
- Out-of-pocket maximum  
- Prior authorization requirements  
- Service-specific limitations  
""")

st.markdown("---")
st.header("Eligibility Verification Workflow")

st.markdown("""
1. **Collect insurance card details**  
2. **Verify benefits using payer portal or clearinghouse**  
3. **Check demographic accuracy**  
4. **Identify preauthorization requirements**  
5. **Determine patient financial responsibility**  
6. **Document eligibility results in the EHR**  
7. **Communicate cost expectations to the patient**  
""")

st.markdown("---")
st.header("Common Causes of Eligibility-Related Denials")

col1, col2 = st.columns(2)
with col1:
    st.subheader("Operational Issues")
    st.markdown("""
    - Incorrect member ID  
    - Terminated or inactive plan  
    - Wrong payer selection  
    - COB (Coordination of Benefits) not updated  
    """)

with col2:
    st.subheader("Financial Impact")
    st.markdown("""
    - Claim rejections  
    - Payment delays  
    - Higher patient balances  
    - Avoidable write-offs  
    """)

st.markdown("---")
st.header("Why Eligibility Matters")

st.markdown("""
Eligibility verification prevents costly rework, improves claim acceptance rates, and increases patient 
satisfaction by setting appropriate financial expectations.
""")
