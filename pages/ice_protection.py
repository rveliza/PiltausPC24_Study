import streamlit as st

col_settings = [20, 80]

st.title("Ice Protection")

col1, col2 = st.columns(col_settings)
with col1:
    st.image("images/windshield_knob.png")
with col2:
    with st.expander("WINDSHIELD"):
        st.markdown("""
* OFF: Disables Windshield
* AUTO HI: Turns on high power heating automatically when ice is detected, and turns off automatically when ice is no longer detected.  DOES NOT HEAT SIDE WINDOWS
* LOW + SIDE: Mainly used to defog side windows.  Heats main and side windows at low heating power
* MAN HI: Heats main windwhields at high power
                    """)
        
col1, col2 = st.columns(col_settings)
with col1:
    st.image("images/ips_knob.png")
with col2:
    with st.expander("IPS"):
        st.markdown("""
* MAN: Manual control via synoptic page
* AUTO: Automatic determination of icing conditions and activation of IPS
* AUTO NAI: Manually activates both NAI systems while maintaining all other IPS sybsystems in AUTO
* ALL ON: Manually activates all IPS subsystems
                    """)
        
col1, col2 = st.columns(col_settings)
with col1:
    st.image("images/swps_ice_knob.png")
with col2:
    with st.expander("Stall Warning Protection System Ice Mode"):
        st.markdown("""
* RESET: Reset Mode 1 to Mode 0 (pull, turn, hold for more than two seconds)
* AUTO: Automatic operation
* OVRD > 1: Resets Mode 2 to Mode 1 (pull, turn)
                    """)
        
col1, col2 = st.columns(col_settings)
with col1:
    st.image("images/ws_emer_button.png")
with col2:
    with st.expander("WS EMER PWR"):
        st.markdown("""
* PRESSED: 
    - LED illuminates ON
    - Emergency power from the battery if the WSH power fails
    - operates for 100 seconds
    - :orange[**CAUTION**]: operation of the system on the ground can permanently damage the windshield.  When the aircraft is energized make sure it is not illuminated
                    """)



st.write("## Question Bank")

with st.expander("What indications do we get when ice is detected and not on ground?"):
    st.write("""
* :blue[**ICE**] below the configuration summary window
* 2 :blue[**ICE**] in the IPS summary window.  One for each ice detector
* :blue[**ICE**] at the bottom ev every synoptic page
* :blue[**ICE**] at the top left of the PFD.  Changes to :orange[**ICE**] when in Mode 2""")
    
with st.expander("What indications de we get when ice is detected on the ground?"):
    st.write("""* None""")

with st.expander("What happens if a single ice detector fails?"):
    st.write("""
* :blue[**Ice Detector Fail**] CAS in flight    
  :orange[**Ice Detector Fail**] CAS on ground""")
    
with st.expander("What happens if both ice detectors fail?"):
    st.write("""
* :orange[**L+R ICE DTECT Fail**] CAS message
* Automatic IPS mode will not be available, only Manual Mode""")
    
with st.expander("What are the main components of the Anti-Ice Deice system?"):
    st.write("""
* Nacelle Anti-Ice System: PRSOV controls supply of bleed air, spring-loaded open for availability during electrical failures
* Wing Anti-Ice System:
    - Two Wing Ati-Ice Valves spring loaded to closed.
* Horizontal Stabilizer Deice System:
    - Ejector Flow Control Valve: allows bleed air to flow and inflate de pneumatic deice boots.  When de-energized it applies vacuum pressure to hold boots in deflated position
* Windshield Heat System:
    - Main Windows: 2 heated zones per window.  Zone 2 has the heating elements (EPDU1 and EPDU2)     
""")
    
with st.expander("Describe the ICE Modes"):
    st.write("""
* Ice mode 0: Non-icing conditions
* Ice mode 1:
    - Icing conditions are encontered + 70 seconds
    - Unlatches automatically when TAT > 15$\degree$ for more than 10 minutes
    - Unlatches manually commanding a reset during non-icing conditions
* Ice mode 2:
    - :orange[**ICE**]
    - The ice detectors have detected ice and the WAI system did not operate properly.
    - Latched until landing unless a manually commanded reset.
    - The SPWS will advance LSA, shaker and pusher speeds
    - Maintain speed above dynamic speed bug
""")