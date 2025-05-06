import streamlit as st

cols_settings = [20, 80]

st.title("Communications")

st.write("## Lights and Switches")

col1, col2 = st.columns(cols_settings)
with col1:
    st.image("images/comms_mic_select_knob.png")
with col2:
    with st.expander("MIC SELECT Knob"):
        st.markdown("""
* Left: Connects microphone to pilot audio panel
* OFF: No connection
* Right: Connects microphone to the copilot audio panel

**Note:** For single-pilot operations set the knob to LEFT
                    """)
        
############ EMERG COM !
col1, col2 = st.columns(cols_settings)
with col1:
    st.image("images/comms_emerg_com1_btn.png")
with col2:
    with st.expander("MIC SELECT Knob"):
        st.markdown("""
* Changes the active COM frequency to 121.5 MHz (or to configured emergency frequency)
* Inhibits the frequency transfer function and removes the swap icon from the softkey
* Pressing agian changes the stby frequency in COM 1 to 121.5 MHz
* Perssing again returns frequency selection back to its original functionality and the active and stanby frequencies remain unchanged
                    """)
        
############### KMA 29 Audio Panel
col1, col2 = st.columns(cols_settings)
with col1:
    st.image("images/comms_kma29_panel.png")
with col2:
    with st.expander("KMA29 Audio Panel"):
        st.markdown("""
* Number 1 audio panel: essential bus
    * Only audio panel available when in dual generator failure
* Number 2 audio panel: right bus
                    
* ICS:
    * ISO: Pilot is isolated from the intercom and is connected only to the aircraft radio system.  Neither the copilot nor the passengers hear aircraft radio receptions or pilot transmissions
    * ALL: The pilot, copilot and passengers hear the aircraft radio and intercom
    * CREW: The pilot and copilot are connected on one intercom channel and hear the aircraft radios.  The passengers do not hear the aircraft radios.
                    """)

        

########### Question Bank
st.write("## Question Bank")
with st.expander("How many static dischargers in the PC-24? "):
    st.write("16")

with st.expander("When the EMER COM 1 121.5 switch is pressed, emergency tuning is activated and the active COM 1 frequency changes to 121.5 Mhz. True or False?"):
    st.write("True")

with st.expander("Pressing the PTT pushbutton for more than _____ seconds will cause a 'STUCK MIC' message in the radio tuning window"):
    st.write("32")

with st.expander("As a safety precaution, the _______ system stops transmitting if the refueling door is open."):
    st.write("HF")

with st.expander("Where are the MIC SELECT knob and the hand microphone?"):
    st.write("Aft center console")


