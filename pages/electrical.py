import streamlit as st

st.title("Electrical")

with st.expander("Essential Bus"):
    st.markdown("""
* Pilot PFD - DU 1
* Upper MFD - DU 2 
* Captain side PFD controller""")
    

with st.expander("EPDU 2"):
    st.markdown("""
* Lower MFD - DU 3
* Copilot PFD - DU 4 
* Copilot side PFD controller
* Cursor Control Device - CCD
* Electronic Stanby Instrument System EPDU2""")