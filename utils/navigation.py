import streamlit as st

# Navigation configuration
NAV_ITEMS = [
    ("Home", "rcm_billing_app.py"),
    ("RCM Overview", "pages/1_RCM_Overview.py"),
    ("Coverage & Eligibility", "pages/2_Coverage_and_Eligibility.py"),
    ("Prior Authorization", "pages/3_Prior_Authorization.py"),
    ("Claims Lifecycle", "pages/4_Claims_Lifecycle.py"),
    ("Denials Management", "pages/5_Denials_Management.py"),
    ("KPI Dashboard", "pages/10_RCM_KPI_Dashboard.py"),
    ("AR Aging", "pages/11_AR_Aging_Dashboard.py"),
    ("Provider Performance", "pages/13_Provider_Performance.py"),
]

SIMULATOR_ITEMS = [
    ("Access Simulator", "pages/8_RCM_Access_Simulator.py"),
    ("PA Outcome Simulator", "pages/14_PA_Outcome_Simulator.py"),
    ("Claims Simulator", "pages/15_Claims_Adjudication_Simulator.py"),
    ("Timeline Simulator", "pages/7_RCM_Timeline_Simulator.py"),
]


def show_navbar():
    """Render the top navigation bar with dropdown menu."""
    st.markdown(
        """
        <style>
        .topnav {
            background-color: #0047AB;
            overflow: hidden;
            padding: 12px 20px;
            border-radius: 6px;
            margin-bottom: 25px;
        }
        .topnav a {
            float: left;
            color: white;
            text-align: center;
            padding: 10px 18px;
            text-decoration: none;
            font-size: 16px;
            font-weight: 500;
        }
        .dropdown {
            float: left;
            overflow: hidden;
        }
        .dropdown .dropbtn {
            cursor: pointer;
            color: white;
            background-color: inherit;
            border: none;
            outline: none;
            padding: 10px 18px;
            font-size: 16px;
            font-weight: 500;
        }
        .dropdown-content {
            display: none;
            position: absolute;
            background-color: #E8F0FF;
            min-width: 180px;
            border-radius: 6px;
            margin-top: 4px;
            z-index: 1;
            box-shadow: 0px 4px 10px rgba(0,0,0,0.2);
        }
        .dropdown-content a {
            float: none;
            color: #0047AB;
            padding: 10px 14px;
            text-decoration: none;
            display: block;
            text-align: left;
            font-weight: 500;
        }
        .dropdown-content a:hover {
            background-color: #dce7ff;
        }
        .dropdown:hover .dropdown-content {
            display: block;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    nav_html = '<div class="topnav">'

    # Add primary nav buttons
    for label, page in NAV_ITEMS:
        nav_html += f'<a href="/?page={page}">{label}</a>'

    # Add dropdown for simulators
    nav_html += """
        <div class="dropdown">
            <button class="dropbtn">Simulators ▾</button>
            <div class="dropdown-content">
    """

    for label, page in SIMULATOR_ITEMS:
        nav_html += f'<a href="/?page={page}">{label}</a>'

    nav_html += """
            </div>
        </div>
    </div>
    """

    st.markdown(nav_html, unsafe_allow_html=True)
