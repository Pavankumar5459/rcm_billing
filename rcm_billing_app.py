import streamlit as st
from pathlib import Path

# -------------------------------------------------
# Page Config
# -------------------------------------------------
st.set_page_config(
    page_title="Hanvion Health – RCM Education Platform",
    layout="wide"
)

# -------------------------------------------------
# REMOVE SIDEBAR COMPLETELY
# -------------------------------------------------
st.markdown("""
<style>
    [data-testid="stSidebar"] {display: none;}
    [data-testid="stSidebarNav"] {display: none;}
    [data-testid="collapsedControl"] {display: none;}
</style>
""", unsafe_allow_html=True)

# -------------------------------------------------
# HEADER SECTION
# -------------------------------------------------
st.markdown("""
<div style="
    background: linear-gradient(90deg, #0EA5E9, #2563EB);
    padding: 32px;
    border-radius: 12px;
    margin-bottom: 20px;">
    <h1 style="color: white; margin-bottom: 6px;">
        Hanvion Health – RCM Education Platform
    </h1>
    <p style="color: white; font-size: 17px; margin: 0;">
        Interactive educational modules and Medicare analytics for understanding the healthcare revenue cycle.
    </p>
</div>
""", unsafe_allow_html=True)

# -------------------------------------------------
# HORIZONTAL MENU
# -------------------------------------------------
menu_options = [
    "Home",
    "RCM Overview",
    "Coverage & Eligibility",
    "Prior Authorization",
    "Claims Lifecycle",
    "Coding Basics",
    "Denials Management",
    "Out-of-Pocket Costs",
    "RCM Timeline Simulator",
    "Provider Analytics",
    "Geographic Analytics"
]

menu_selection = st.selectbox(
    "Navigation",
    menu_options,
    key="main_menu"
)

# -------------------------------------------------
# PAGE ROUTING
# -------------------------------------------------
page_routes = {
    "RCM Overview": "pages/1_RCM_Overview.py",
    "Coverage & Eligibility": "pages/2_Coverage_and_Eligibility.py",
    "Prior Authorization": "pages/3_Prior_Authorization.py",
    "Claims Lifecycle": "pages/4_Claims_Lifecycle.py",
    "Coding Basics": "pages/5_Coding_Basics.py",
    "Denials Management": "pages/6_Denials_Management.py",
    "Out-of-Pocket Costs": "pages/7_OOP_Cost_Education.py",
    "RCM Timeline Simulator": "pages/8_RCM_Timeline_Simulator.py",
    "Provider Analytics": "pages/9_Medicare_Provider_Analytics.py",
    "Geographic Analytics": "pages/10_Medicare_Geographic_Analytics.py"
}

if menu_selection != "Home":
    st.switch_page(page_routes[menu_selection])

# -------------------------------------------------
# HOME PAGE CONTENT
# -------------------------------------------------

st.markdown("""
<hr style="margin-top: 10px; margin-bottom: 25px;">
""", unsafe_allow_html=True)

st.subheader("Welcome to the Hanvion RCM Learning and Analytics Platform")

st.markdown("""
This platform provides a full educational journey through the healthcare revenue cycle.  
It includes interactive learning modules, real Medicare-style analytics, and a guided simulator  
to understand how coverage, coding, documentation, and payer rules shape reimbursement.
""")

st.markdown("---")
st.header("Educational Modules")

cols = st.columns(2)

modules = [
    ("RCM Overview", "Learn the end-to-end revenue cycle workflow."),
    ("Coverage & Eligibility", "Understand payer benefits, verification rules, and patient responsibility."),
    ("Prior Authorization", "Review authorization workflows and common reasons for denial."),
    ("Claims Lifecycle", "See how claims move from submission to adjudication."),
    ("Coding Basics", "ICD-10, CPT, HCPCS coding principles and compliance."),
    ("Denials Management", "Identify denial reasons and improve financial performance."),
    ("Out-of-Pocket Costs", "Deductible, copay, coinsurance, and patient balance education."),
    ("RCM Timeline Simulator", "Interactive tool walking through each step in the revenue cycle.")
]

for idx, (title, desc) in enumerate(modules):
    with cols[idx % 2]:
        st.markdown(f"""
        <div style="border: 1px solid #E5E7EB; padding: 16px; border-radius: 10px; 
                    background: #FFFFFF; margin-bottom: 16px;">
            <h3 style="margin: 0 0 6px 0;">{title}</h3>
            <p style="margin: 0 0 10px 0; color: #475569;">{desc}</p>
            <a href="javascript:void(0)" onclick="window.parent.location.href='?main_menu={title.replace(' ', '%20')}'">
                <button style="padding: 8px 15px; border-radius: 6px; 
                               background: #2563EB; color: white; border: none;">
                    Open Module
                </button>
            </a>
        </div>
        """, unsafe_allow_html=True)

st.markdown("---")
st.header("Medicare Analytics Dashboards")

cols2 = st.columns(2)

analytics = [
    ("Provider Analytics", "Analyze Medicare utilization patterns, HCPCS codes, and reimbursement data."),
    ("Geographic Analytics", "Explore Medicare spending and utilization across states.")
]

for idx, (title, desc) in enumerate(analytics):
    with cols2[idx % 2]:
        st.markdown(f"""
        <div style="border: 1px solid #E5E7EB; padding: 16px; border-radius: 10px; 
                    background: #FFFFFF; margin-bottom: 16px;">
            <h3 style="margin: 0 0 6px 0;">{title}</h3>
            <p style="margin: 0 0 10px 0; color: #475569;">{desc}</p>
            <a href="javascript:void(0)" onclick="window.parent.location.href='?main_menu={title.replace(' ', '%20')}'">
                <button style="padding: 8px 15px; border-radius: 6px; 
                               background: #2563EB; color: white; border: none;">
                    Open Dashboard
                </button>
            </a>
        </div>
        """, unsafe_allow_html=True)

st.markdown("---")
st.write("Use the navigation at the top to explore any module.")
