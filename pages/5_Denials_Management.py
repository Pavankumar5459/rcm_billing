from utils.navigation import show_navbar
show_navbar()
import streamlit as st

st.set_page_config(layout="wide")
st.title("Denials Management")

st.markdown("""
Denials occur when payers do not approve part or all of a claim.  
Effective denials management ensures that organizations recover lost revenue and prevent future denials.
""")

st.markdown("---")
st.header("Types of Denials")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Hard Denials")
    st.markdown("""
    Cannot be corrected or resubmitted.  
    Results in permanent loss of revenue.
    """)

with col2:
    st.subheader("Soft Denials")
    st.markdown("""
    Can be corrected with additional documentation or coding adjustments.
    """)

st.markdown("---")
st.header("Common Denial Categories")

st.markdown("""
- Eligibility-related  
- Authorization missing  
- Coding errors  
- Non-covered services  
- Bundling or rebundling issues  
- Medical necessity not met  
""")

st.markdown("---")
st.header("Denial Resolution Workflow")

st.markdown("""
1. Identify denial reason  
2. Review payer explanation (EOB/ERA)  
3. Correct coding or documentation  
4. Submit appeal or corrected claim  
5. Track payer response  
""")

st.markdown("---")
st.header("Preventing Denials")

st.markdown("""
- Verify eligibility before service  
- Confirm authorization rules  
- Ensure accurate documentation  
- Use coding audits  
- Monitor denial trends  
""")

st.markdown("---")
st.header("Why Denials Management Matters")

st.markdown("""
A robust denials strategy recovers lost revenue, reduces rework, and improves overall financial performance.
""")
