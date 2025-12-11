import streamlit as st

def switch(page_name):
    st.switch_page(f"pages/{page_name}.py")

def show_navbar():
    st.markdown("""
        <style>
        .topnav {
            background-color: #0A1E3A;
            overflow: hidden;
            padding: 12px 15px;
            border-radius: 6px;
            margin-bottom: 25px;
        }
        .topnav a {
            float: left;
            color: #ffffff;
            text-align: center;
            padding: 10px 16px;
            text-decoration: none;
            font-size: 16px;
            font-weight: 600;
        }
        .topnav a:hover {
            color: #4BB4FF;
        }
        </style>
    """, unsafe_allow_html=True)

    cols = st.columns([1,1,1,1,1,1,1,1])

    with cols[0]:
        if st.button("Home"):
            switch("1_RCM_Overview")

    with cols[1]:
        if st.button("Coverage"):
            switch("2_Coverage_and_Eligibility")

    with cols[2]:
        if st.button("PA"):
            switch("3_Prior_Authorization")

    with cols[3]:
        if st.button("Claims"):
            switch("4_Claims_Lifecycle")

    with cols[4]:
        if st.button("Denials"):
            switch("5_Denials_Management")

    with cols[5]:
        if st.button("KPI"):
            switch("10_RCM_KPI_Dashboard")

    with cols[6]:
        if st.button("AR Aging"):
            switch("11_AR_Aging_Dashboard")

    with cols[7]:
        if st.button("Provider"):
            switch("12_Provider_Performance")
