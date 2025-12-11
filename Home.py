import streamlit as st
from PIL import Image

st.set_page_config(page_title="Hanvion Health RCM", layout="wide")

logo = Image.open("hanvion_logo.png")
st.image(logo, width=200)

st.title("Hanvion Health – Patient Access & Revenue Cycle Navigator")

st.write(
    '''
Welcome to the **Hanvion Health RCM Dashboard**, a patient-access intelligence platform designed to:
- Explain coverage pathways  
- Support prior authorization  
- Assist providers with documentation  
- Troubleshoot denials  
- Estimate patient out-of-pocket cost  
- Simplify complex insurance workflows  
'''
)

st.info("Use the left sidebar to navigate through the full RCM workflow.")
