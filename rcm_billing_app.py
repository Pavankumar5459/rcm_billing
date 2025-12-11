import streamlit as st
from utils.navigation import show_navbar
from utils.ui_components import centered_header

# -----------------------------------------------------------
# PAGE CONFIG
# -----------------------------------------------------------
st.set_page_config(
    page_title="Hanvion Health – RCM Education Platform",
    page_icon="💠",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Hide sidebar completely
hide_sidebar = """
<style>
[data-testid="stSidebar"] {display: none;}
</style>
"""
st.markdown(hide_sidebar, unsafe_allow_html=True)

# Top Navigation Bar
show_navbar()

# -----------------------------------------------------------
# HOME PAGE UI
# -----------------------------------------------------------

centered_header("Hanvion Health – Revenue Cycle Intelligence Platform")

st.write(
    """
Welcome to the **Hanvion RCM Education Platform**.  
Explore interactive modules that teach and visualize:

- End-to-end Revenue Cycle Management  
- Coverage & Eligibility  
- Prior Authorization  
- Claims Lifecycle & Adjudication  
- Denials Management  
- KPI Dashboards & Analytics  
- AR Aging  
- Provider Performance  
- Real-world RCM Simulators  
    """
)

st.write("---")

# -----------------------------------------------------------
# EDUCATIONAL MODULE CARDS
# -----------------------------------------------------------

def module_card(title, description, page):
    cols = st.columns([3, 1])
    with cols[0]:
        st.subheader(title)
        st.write(description)
    with cols[1]:
        st.page_link(page, label="Open Module", use_container_width=True)
    st.write("")


st.markdown("### Educational Modules")

module_card(
    "RCM Overview",
    "Learn the end-to-end revenue cycle workflow.",
    "pages/1_RCM_Overview.py",
)

module_card(
    "Coverage & Eligibility",
    "Understand payer benefits, verification rules, and patient responsibility.",
    "pages/2_Coverage_and_Eligibility.py",
)

module_card(
    "Prior Authorization",
    "Review authorization workflows and common reasons for denial.",
    "pages/3_Prior_Authorization.py",
)

module_card(
    "Claims Lifecycle",
    "See how claims move through submission, adjudication, and payment.",
    "pages/4_Claims_Lifecycle.py",
)

module_card(
    "Denials Management",
    "Identify major denial types, root causes, and appeal strategies.",
    "pages/5_Denials_Management.py",
)

module_card(
    "OOP Cost Education",
    "Learn about copays, deductibles, coinsurance, and patient responsibility.",
    "pages/6_OOP_Cost_Education.py",
)


st.write("---")
st.markdown("### Analytics Dashboards")

module_card(
    "KPI Dashboard",
    "Track key RCM metrics including denial rate, clean claim rate, and financial KPIs.",
    "pages/10_RCM_KPI_Dashboard.py",
)

module_card(
    "AR Aging Dashboard",
    "Visualize accounts receivable buckets and collection patterns.",
    "pages/11_AR_Aging_Dashboard.py",
)

module_card(
    "Provider Performance",
    "Analyze provider utilization, RVUs, geographic adjustments, and payment patterns.",
    "pages/13_Provider_Performance.py",
)


st.write("---")
st.markdown("### Simulators")

module_card(
    "RCM Timeline Simulator",
    "Simulate the patient's journey from scheduling → eligibility → PA → claim → payment.",
    "pages/7_RCM_Timeline_Simulator.py",
)

module_card(
    "Access Simulator",
    "Evaluate eligibility, documentation completeness, and approval probability.",
    "pages/8_RCM_Access_Simulator.py",
)

module_card(
    "PA Outcome Simulator",
    "Simulate prior authorization results and payer decision steps.",
    "pages/14_PA_Outcome_Simulator.py",
)

module_card(
    "Claims Adjudication Simulator",
    "Simulate payer adjudication, denials, appeals, and payment accuracy.",
    "pages/15_Claims_Adjudication_Simulator.py",
)


# -----------------------------------------------------------
# FOOTER
# -----------------------------------------------------------
st.write("---")
st.caption("Hanvion Health © 2025 • Revenue Cycle Education & Intelligence Platform")

