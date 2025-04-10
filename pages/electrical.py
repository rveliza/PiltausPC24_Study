import streamlit as st

col_settings = [20, 80]

st.title("Electrical")

st.write("## Lights and Switches")

nicad_lion = st.radio("Batt type", ("NiCad", "Li-ion"), index=0, horizontal=True, label_visibility="collapsed")

batt_volt, batt_amps = ("24V", "44A") if nicad_lion == "NiCad" else ("26.4V", "40A")

with st.expander("Batteries"):
    st.markdown(f"""
{batt_volt}DC/{batt_amps} {nicad_lion} batteries provide power to the aircraft for a minimum of 60 minutes
""")




col1, col2 = st.columns(col_settings)
with col1:
    st.image("images/bat_1_sw.png", use_column_width=True)
with col2:
    with st.expander("BAT 1 Switch"):
        st.markdown("""
* BAT 1: Energizes Battery Contactor BC1 to closed
* OFF: De-energizes Battery Contactor BC1 to open 
                    
Bat 1 is in the left nose bay and provides power to the left and essential busses""")
        
col1, col2 = st.columns(col_settings)
with col1:
    st.image("images/bat_2_sw.png", use_column_width=True)
with col2:
    with st.expander("BAT 2 Switch"):
        st.markdown("""
* BAT 2: Energizes Battery Contactor BC2 to closed
* OFF: De-energizes Battery Contactor BC2 to open
                    
Bat 2 is in the rear right-wing fairing and provides power to the right bus for engine starts
                    
###### Notte: Bat 2 should not be turned on until ready to start the engine, or rapid depletion of the batteries will occur""")
        
col1, col2 = st.columns(col_settings)
with col1:
    st.image("images/gen_1_sw.png", use_column_width=True)
with col2:
    with st.expander("GEN 1 Switch"):
        st.markdown("""
* GEN 1: Arms associated PCU to operate in START mode or GENERATE mode as subsequently requested
* OFF: Disarms associated PCU - next selection to ON restarts the PCU
                    """)
        
col1, col2 = st.columns(col_settings)
with col1:

    st.image("images/gen_2_sw.png", use_column_width=True)
with col2:
    with st.expander("GEN 2 Switch"):
        st.markdown("""
* GEN 2: Arms associated PCU to operate in START mode or GENERATE mode as subsequently requested
* OFF: Disarms associated PCU - next selection to ON restarts the PCU
                    """)


off_avail_on = st.radio("off_avail_on", ("OFF", "AVAIL", "ON"), index=0, horizontal=True, label_visibility="collapsed")

gpu_data = {
    "OFF": {"image": "images/gpu_off_btn.png", "title": "GPU OFF", "desc": """GPU is not requested and no expternal power source is available"""},
    "AVAIL": {"image": "images/gpu_avail_btn.png", "title": "GPU AVAIL", "desc": """
    GPU is not requested but an external power source is connected and available.
    * If pressed: Closes GPC and GPU supplies power"""},
    "ON": {"image": "images/gpu_on_btn.png", "title": "GPU ON", "desc": """
    GPU is connected and supplying power to the aircraft\n
    * Pushing the button for 2 seconds opens the GPC and GPU stops supplying power"""},
}

col1, col2 = st.columns(col_settings)
with col1:
    st.image(gpu_data[off_avail_on]["image"], use_column_width=True)
with col2:
    with st.expander(gpu_data[off_avail_on]["title"], expanded=True):
        st.markdown(gpu_data[off_avail_on].get("desc", ""))
        


elec_op_mode = st.selectbox("Operating Mode", options=["Normal Operation - 2 generators", "Pre Departure Mode", "Quiet Power mode", "Ground Power Mode", "Pre-Start MMode", "Engine Start - Battery Only", "Single Generator - Second Engine Pre-Start Mode", "Cross-Generator Start #2 Engine Running, #1 Starting)", "GPU Start", "Single Generator After GPU Start", "Single Generator - Left OFF / Fail", "Single Generator - Right OFF / Fail", "Dual Generator Failure"])

st.write(elec_op_mode)


with st.expander("Essential Bus"):
    st.markdown("""
* Pilot PFD - DU 1
* Upper MFD - DU 2 
* Captain side PFD controller
* Cockpit Voice / Flight Data Recorder""")
    

with st.expander("EPDU 2"):
    st.markdown("""
* Lower MFD - DU 3
* Copilot PFD - DU 4 
* Copilot side PFD controller
* Cursor Control Device - CCD
* Electronic Stanby Instrument System EPDU2""")
    
