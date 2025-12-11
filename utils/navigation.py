import streamlit as st

# ---- NAVIGATION BAR ----
def show_navbar():
    st.markdown("""
        <style>
        /* Remove Streamlit default padding */
        .block-container {
            padding-top: 1rem;
        }

        /* NAVBAR CONTAINER */
        .hanvion-navbar {
            background-color: #0A1E3A;
            padding: 12px 20px;
            border-radius: 6px;
            margin-bottom: 25px;
        }

        .hanvion-navbar a {
            color: #FFFFFF;
            font-weight: 600;
            margin-right: 25px;
            text-decoration: none;
            font-size: 16px;
        }

        .hanvion-navbar a:hover {
            color: #4BB4FF;
        }
        </style>

        <div class="hanvion-navbar">
            <a href="/?page=Home">Home</a>
            <a href="/?page=RCM_Overview">RCM Overview</a>
            <a href="/?page=Coverage_Eligibility">Coverage & Eligibility</a>
            <a href="/?page=Prior_Authorization">Prior Authorization</a>
            <a href="/?page=Claims_Lifecycle">Claims Lifecycle</a>
            <a href="/?page=Denials_Management">Denials</a>
            <a href="/?page=KPI_Dashboard">KPI Dashboard</a>
            <a href="/?page=AR_Aging">AR Aging</a>
            <a href="/?page=Provider_Performance">Provider Performance</a>
        </div>
    """, unsafe_allow_html=True)
