import streamlit as st

cols_settings = [20, 80]

st.title("Lighting")

st.write("## Lights and Switches")

col1, col2 = st.columns(cols_settings)
with col1:
    st.image("images/light_test_btn.png")
with col2:
    with st.expander("COCKPIT LAMP TEST"):
        st.markdown("""
* LH Panel (2): CVR TEST / ERASE, AURAL DISABLE
* Glareshield (8): Master Warning, Master Caution, FIRE XTING, ENG ISOL
* Center Pedestal (5): SEC STAB TRIM, EMER COM 1, WS EMER PWR, FLAPS EMER PWR, DUMP
* OVHD Panel (2): BUS TIE, EXT PWR
                    """)

col1, col2 = st.columns(cols_settings)
with col1:
    st.image("images/light_logo_sw.png")
with col2:
    with st.expander("LOGO / NAV"):
        st.markdown("""
* LOGO: Logo and Nav lights are selected to ON
* NAV: Nav lights are selected ON (one LED each)
                    """)     
        
col1, col2 = st.columns(cols_settings)
with col1:
    st.image("images/light_strobe_sw.png")
with col2:
    with st.expander("STROBE / BEACON"):
        st.markdown("""
* STROBE: only the white anti-collision lights ont the wing tips and tail cone are ON
* BEACON: red pulsating beacon lights on wing tips and tail cone are ON

**NOTE:** Strobe lights and the Beacon lights cannot be operated simultaneously.    
**NOTE:** The white anti-collision and read beacon lights flash at a frequency of about 45 flashes per minute.  All flash at the same time
                    """)     
        

col1, col2 = st.columns(cols_settings)
with col1:
    st.image("images/light_taxi_sw.png")
with col2:
    with st.expander("TAXI"):
        st.markdown("""
* TAXI: a taxi light module at each wing root in the belly fairing (5 LED's), and a taxi light module in each wing tip (2 LED's), are turned ON    
                    
    **Note:** Left wing fairing taxi light is powered by the essential bus
                    """)     


col1, col2 = st.columns(cols_settings)
with col1:
    st.image("images/light_landing_sw.png")
with col2:
    with st.expander("LANDING / PULSE"):
        st.markdown("""
* LANDING: Landing lights operate continuously.    
    - **Note:** Lights will NOT flash when the TCAS signal is received    
    - **Note:** Left landing light runs from essential bus
* PULSE: If installed, the LH and RH lanlding lights pulse alternately.
* OFF: A TCAS alert will cause the landing lights to flash.  Selecting the switch to ON will activate the landing lights steady and terminate the flashing behavior.
                    """)     


col1, col2 = st.columns(cols_settings)
with col1:
    st.image("images/light_recog_sw.png")
with col2:
    with st.expander("RECOG / PULSE"):
        st.markdown("""
* RECOG: recognition lights in each wing tip operate continuously (2 LED's).  TCAS function is inhibitted.
* PULSE: if installed, the LH and RH recognition lights pulse alternately
* OFF: a TCAS alert will cause the recognition lights to flash
                    """)   

col1, col2 = st.columns(cols_settings)
with col1:
    st.image("images/light_emer_sw.png")
with col2:
    with st.expander("EMER LTS"):
        st.markdown("""
* OFF: Deactivates the system.  If aircraft power is on, the emergency lights indicator illuminates, alerting the crew that the system is neither on nor armed.
* ARM: Arms the system for automatic operation.  A loss of electrical power activates the emergency lighting system and remains active fro approximately five minutes
* ON: Switches the lights on, can be used for testing the system
                    """)     
          
        


        



########################### Question Bank
st.write("## Question Bank")
with st.expander("When the aircraft is not powered, pressing the BAGGAGE LIGHTS switch in the cargo door frame illuminates the baggage/cargo and cargo door lights.  True of false?"):
    st.write("True")

with st.expander("When the CABIN LIGHTS switch is in the AUTO position, the upwash, sownwash, and entry-hallway lights illuminate at _____ brightness"):
    st.write("50%")

with st.expander("The baggage/cargo and cargo door lights remain illuminated for ________ minutes to allow for loading/unloading"):
    st.write("five")

with st.expander("The ENTRANCE LIGHT switch in the main cabin door frame can only power the entry-hallway lighting when the aircraft has power.  True or False?"):
    st.write("False")