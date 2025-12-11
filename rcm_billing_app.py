import streamlit as st

# -------------------------------------------------
# STREAMLIT CONFIG
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
    [data-testid="stSidebar"] {display: none !important;}
    [data-testid="stSidebarNav"] {display: none !important;}
    [data-testid="collapsedControl"] {display: none !important;}
    .block-container {padding-left: 2rem !important; padding-right: 2rem !important;}
</style>
""", unsafe_allow_html=True)

# -------------------------------------------------
# HEADER
# -------------------------------------------------
st.markdown("""
<div style="
    background: linear-gradient(90deg, #0EA5E9, #2563EB);
    padding: 30px;
    border-radius: 12px;
    margin-bottom: 20px;">
    <h1 style="color: white; margin-bottom: 5px;">
        Hanvion Health – RCM Education Platform
    </h1>
    <p style="color: white; font-size: 16px;">
        Interactive modules and analytics explaining patient access, insurance reimbursement, denials, and billing workflows.
    </p>
</div>
""", unsafe_allow_html=True)

# -------------------------------------------------
# EDUCATION MODULES
# -------------------------------------------------
st.subheader("Educational Modules")

col1, col2 = st.columns(2)

modules = [
    ("RCM Overview", "Learn the complete revenue cycle workflow.",
        "pages/1_RCM_Overview.py"),

    ("Coverage & Eligibility", "Understand benefit checks and patient responsibility.",
        "pages/2_Coverage_and_Eligibility.py"),

    ("Prior Authorization", "Learn authorization workflows and payer criteria.",
        "pages/3_Prior_Authorization.py"),

    ("Claims Lifecycle", "Understand how claims are created, submitted, and adjudicated.",
        "pages/4_Claims_Lifecycle.py"),

    ("Denials Management", "Learn denial categories, root causes, and appeals.",
        "pages/6_Denials_Management.py"),

    ("Out-of-Pocket Cost Education", "Teach patients about deductibles, copays, and coinsurance.",
        "pages/7_OOP_Cost_Education.py"),

    ("RCM Timeline Simulator", "Interactive step-by-step revenue cycle walkthrough.",
        "pages/8_RCM_Timeline_Simulator.py"),

    ("Patient Access Journey Simulator", "Simulated workflow: eligibility → PA → claims → appeals.",
        "pages/9_RCM_Access_Simulator.py"),

    ("Billing & Denials Data Insights", 
     "Use Medicare datasets to understand denial patterns, payment gaps, and service utilization.",
     "pages/10_Billing_and_Denials_Insights.py")
]

# -------------------------------------------------
# DISPLAY MODULE CARDS
# -------------------------------------------------
for idx, (title, desc, path) in enumerate(modules):
    with (col1 if idx % 2 == 0 else col2):
        st.markdown(f"""
        <div style="border:1px solid #E5E7EB; padding:18px; border-radius:10px;
                    background:#FFFFFF; margin-bottom:20px;">
            <h3 style="margin:0 0 6px 0;">{title}</h3>
            <p style="margin:0 0 12px 0; color:#475569;">{desc}</p>
        </div>
        """, unsafe_allow_html=True)

        st.page_link(path, label="Open Module")

st.markdown("---")
st.write("Select any module above to start learning about the patient access and reimbursement process.")
