import streamlit as st

st.title("Indicating & Recording")

cols_settings = [20, 80]

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


with st.expander("Excessive Attitude Declutter"):
    st.markdown("""
* < +/- 65$\degree$ Roll Angle > +/- 63$\degree$
* < +/- 30$\degree$ Pitch Angle > +/- 28$\degree$
* < +/- 20$\degree$ Pitch Angle > +/- 18$\degree$ """)
    

with st.expander("Cockpit Voice / Flight Data Recorder"):
    st.markdown("""
* Essencial Bus Powered
* 2 hours of audio,
* 25 hours or ARINC 429 data
* 20 hours of ARINC 717 data """)
    
st.write("## Lights and Switches")

col1, col2 = st.columns(cols_settings)
with col1:
    st.image("images/cvr_test.png", use_column_width=True)
with col2:
    with st.expander("CVR TEST/ERASE"):
        st.markdown("""
* Test - Press to initiate CVR test for 5 seconds to illuminate the switch
* CVR TEST - Illuminates when the test is initiated
    * CAS messages related to CVR or FDR should not display
* Erase - Press and hold for at least 8 seconds to delete stored data
    * Aircraft must be on the ground
    * CVR Erase message displays until process is complete
                    """)
        

st.write("## Question Bank")

with st.expander("The ACE$^{tm}$ avionics system monitors flight instruments on both PFDs and displays a/an _________ next to the item when it is detects a miscompare"):
    st.markdown("""? (question mark)""")

with st.expander("Flight alerting system (FAS) annunciators appear on each PFD and are cleared with the master warning pushbutton. True or False?"):
    st.markdown("""False""")

with st.expander("The main purpose of SmarView SVS is bot to provide and increase situational awareness.  True or False?"):
    st.markdown("""True""")

with st.expander("The ____ is an independent system that provides critiacl flight altitude and heading data in the event of total display failure"):
    st.markdown("""ESIS""")

with st.expander("Caustion CAS messages can only be scrolled after acknowledging with the master caution push button. True or False?"):
    st.markdown("""True""")

with st.expander("A link within the ECL to automaticall open the assiciated synoptic page is provided when the ECL is displayed on the _______"):
    st.markdown(""" Lower MFD""")

with st.expander("To test the CVFDR, press the CVR TEST/ERASE button for ________ seconds to illuminate the switch."):
    st.markdown("""5""")
