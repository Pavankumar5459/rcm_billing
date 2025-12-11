import streamlit as st

st.set_page_config(layout="wide")
st.title("Out-of-Pocket Cost Education")

st.markdown("""
Out-of-pocket (OOP) costs are the portion of healthcare expenses that patients must pay themselves.  
Understanding these concepts is critical for patient counseling, financial clearance, and accurate billing.
""")

st.markdown("---")
st.header("Core Out-of-Pocket Concepts")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Deductible")
    st.markdown("""
    The amount a patient must pay each year before the insurance plan starts to pay for covered services.
    """)

    st.subheader("Copay")
    st.markdown("""
    A fixed amount the patient pays at the time of service (for example: 25 dollars for a visit).
    """)

with col2:
    st.subheader("Coinsurance")
    st.markdown("""
    A percentage of the allowed amount the patient must pay after the deductible is met 
    (for example: 20 percent of the approved charge).
    """)

    st.subheader("Out-of-Pocket Maximum")
    st.markdown("""
    The maximum amount a patient will pay in a plan year.  
    After this is reached, the plan typically pays 100 percent of covered services.
    """)

st.markdown("---")
st.header("Example Scenario")

st.markdown("""
Consider this simple example to understand how out-of-pocket costs work.

- Allowed amount for service: 1,000 dollars  
- Deductible: 500 dollars  
- Coinsurance: 20 percent  
- Deductible not yet met this year  
""")

st.subheader("Step-by-step Calculation")

st.markdown("""
1. **Deductible applied**  
   - Patient pays the first 500 dollars  
   - Remaining allowed amount: 500 dollars  

2. **Coinsurance applied on the remaining amount**  
   - Patient pays 20 percent of 500 dollars = 100 dollars  
   - Payer pays 400 dollars  

3. **Total out-of-pocket for this visit**  
   - 500 dollars (deductible) + 100 dollars (coinsurance) = 600 dollars  
""")

st.markdown("---")
st.header("How Out-of-Pocket Costs Affect RCM")

st.markdown("""
- Determines patient balance after insurance  
- Impacts payment plans and collections  
- Influences patient satisfaction and trust  
- Requires clear communication at or before the time of service  
""")

st.markdown("---")
st.header("Best Practices for Discussing Costs With Patients")

st.markdown("""
- Use clear, non-technical language  
- Explain deductible, copay, and coinsurance separately  
- Provide estimates before services when possible  
- Encourage patients to review their Explanation of Benefits (EOB)  
- Document financial counseling in the record  
""")
