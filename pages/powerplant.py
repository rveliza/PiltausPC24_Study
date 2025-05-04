import streamlit as st

st.title("Powerplant")

st.write("## Question Bank")

with st.expander("How many compressors are in the engine?"):
    st.write("""
* 1 LP comppressor
* 3 IP compressors
* 1 HP compressor""")
    
with st.expander("What is the EXACT technology of the engine?"):
    st.write("""
At takeoff power, the exhaust nozzle provides a 3$\degree$ vector due to an aerodynamic phenomenon known as the Coanda effect.  As the aircraft approaches cruise, the vector is parralel with the engine centerline.""")
    
with st.expander("What connects the Accesory Gearbox to the engine?"):
    st.write("""

* Tower Shaft""")
    
with st.expander("How much oil capacity is there between the FULL OIL and ADD OIL marks in the engine's sight glass?"):
    st.write("""
* 1 quart""")
    
with st.expander("How many exciters are in the engine?"):
    st.write("""
* 2 exciters
    - 1 for engine start on ground
    - 2 for engine start in flight""")

with st.expander("What is the main control of the engine?"):
    st.write("""
* FADEC""")
    
with st.expander("Where are the FADEC's located?"):
    st.write("""
* 2 engine ECU's (1 per engine) mounted on the pressure bulkhead in the rear compartment.""")
    
with st.expander("What powers the ECU's?"):
    st.write("""
* Essential bus""")
    
with st.expander("What are the sensors that the FADEC uses?"):
    st.write("""
* TT2 sensor - Temperature inputs
* PT2 sensor - Inlet pressure inputs
* N1 sensor - high power settings to provide speed inputs
* N2 sensor - low power settings to provide speed inputs
* ITT Probes - 6 probes that average the temperature.""")
    
with st.expander("What are the stops in the throttle quadrant?"):
    st.write("""
* Hard stops:
    - Idle
    - ATR
* Soft stops:
    - MCT
    - T/O""")

with st.expander("What is the low pressure shaft trip sensor for?"):
    st.write("""
* In case the LP shaft separates, it pulls a trigger the trip sensor cable, pulling the sutoff solenoid on the FCU therefore stopping fuel flow to the engine and shutting it down.""")
    
with st.expander("How is the engine ignition controlled with the engine rotary knobs?"):
    st.write("""
* OFF - No ignition
* DRY MOTOR - ignition off, starter on
* RUN - One igniter on
* IGN - Both igniters on""")
    
with st.expander("What causes the L/R ENG Fail CAS message?"):
    st.write("""
* N1 dropped 15% for 0.5 seconds""")
    

with st.expander("When is the ATR automatically activated?"):
    st.write("""
* When the throttles are at T/O and an engine fails""")
    
with st.expander("At how many minutes after takeoff does the ATR Disarm CAS message appear?"):
    st.write("""
* 5 minutes""")
    
