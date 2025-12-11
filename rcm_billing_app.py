import streamlit as st
import os

# Load theme CSS
def load_css():
    css_path = "styles/hanvion_theme.css"
    if os.path.exists(css_path):
        with open(css_path) as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# -----------------------------------------
#      MAIN DASHBOARD HOME PAGE
# -----------------------------------------

def main():

    st.set_page_config(
        page_title="Hanvion RCM Education Platform",
        layout="wide"
    )

    load_css()

    st.title("Hanvion Health – RCM Education Platform")
    st.subheader("Interactive learning + analytics for Revenue Cycle Management")

    st.write("Use the left navigation bar to explore:")

    cols = st.columns(3)

    with cols[0]:
        st.markdown("### RCM Overview")
        st.write("Learn end-to-end revenue cycle workflow.")
    
    with cols[1]:
        st.markdown("### Coverage & Eligibility")
        st.write("How payers determine benefits and patient responsibility.")

    with cols[2]:
        st.markdown("### Prior Authorization")
        st.write("Understand approvals, denials, and P2P workflows.")

    col2 = st.columns(3)

    with col2[0]:
        st.markdown("### Claims Lifecycle")
        st.write("Creation → submission → adjudication progression.")

    with col2[1]:
        st.markdown("### Denials Management")
        st.write("Root cause analysis + recovery strategies.")

    with col2[2]:
        st.markdown("### KPI Dashboards")
        st.write("Real-time metrics for AR, lag, FPR, denials, and more.")

    st.markdown("---")
    st.markdown("Powered by **Hanvion Health AI**")


if __name__ == "__main__":
    main()
