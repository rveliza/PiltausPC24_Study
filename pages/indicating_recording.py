import streamlit as st

st.title("Indicating & Recording")

with st.expander("Display Units"):
    st.markdown("""
* DU 1 - Pilot PFD - Essential Bus - AGM1 - MAU1 - IRU
* DU 2 - Upper MFD - Essential Bus - AGM1 - MAU1
* DU 3 - Lower MFD - EPDU 2 - AGM2 - MAU2
* DU 4 - Copilot PFD - EPDU 2 - AGM2 - MAU2 - AHRS""")
    
with st.expander("Primary Flight Display Controllers"):
    st.markdown("""
* Captain side PFD controller - Essential Bus
* Copilot side PFD controller - EPDU 2
                
###### NOTE: Pushing the PFD button directs the focus of the PFD controller to the opposite side PFD""")
    
with st.expander("Composite Primary Flight Display"):
    st.markdown("""
Displays when only one DU remains enabled, when all other DUs are turned off using the DRCP.
* Flight information
* CAS messages
* System summary
* Radio tuning""")


with st.expander("Excessive attitude declutter"):
    st.markdown("""
* < +/- 65$\degree$ Roll Angle > +/- 63$\degree$
* < +/- 30$\degree$ Pitch Angle > +/- 28$\degree$
* < +/- 20$\degree$ Pitch Angle > +/- 18$\degree$ """)