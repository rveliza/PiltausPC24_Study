import streamlit as st

cols_settings = [20, 80]

st.title("Flight Controls")

st.image("images/flight_controls.png")


st.write("## Primary Flight Control System")
with st.expander("Ailerons"):
    st.markdown(""" 
    * 25$\degree$ up, 15$\degree$ down
    * 2 static dischargers per aileron
    """)

with st.expander("Elevator"):
    st.markdown("""
    * 25$\degree$ up, 15$\degree$ down
    * 2 static dischargers per aileron
""")
    
with st.expander("Rudder"):
    st.markdown("""
    * On Ground: 28$\degree$ in either direction    
    * In Flight: 
        * Flaps 0$\degree$ - +/- 20$\degree$
        * Flaps 8$\degree$ - +/- 26$\degree$
        * Flaps 15$\degree$ and 33$\degree$ - +/- 28$\degree$    
    * If one engine is inoperative, the UMS provides a command signal to drive the rudder limiter actuator to the  full +/-\$degree# position so that the full rudder trabel is permitted.
    * WOW at landing signals the UMS to drive the rudder limiter actuator to the full +/-\$degree$ position where it remains through removal of electrical power from the aircraft
    * 2 static dischargers
""")


st.write("## Lights and Switches")

col1, col2 = st.columns(cols_settings)
with col1:
    st.image("images/trim_sec_stab_sw.png", use_column_width=True)
with col2:
    with st.expander("SEC STAB TRIM "):
        st.markdown("""
* Channel 2
* ENABLE (guarded): 
    - Illuminates the ON indicator
    - Deenergizes the stabilizer trim switches on the control wheels
* SEC STAB TRIM (split): Must be depressed/held simultaneously to activate settings:
    - DN: Trims aircraft nose down
    - UP: Trims aircraft nose up
                    """)


col1, col2 = st.columns(cols_settings)
with col1:
    st.image("images/trim_aileron_sw.png", use_column_width=True)
with col2:
    with st.expander("AIL TRIM"):
        st.markdown("""
* LWD: Moves the left aileron tab to trim left
* RWD: Moves the left aileron tab to trim right
                    """)
        
col1, col2 = st.columns(cols_settings)
with col1:
    st.image("images/trim_rud_knob.png", use_column_width=True)
with col2:
    with st.expander("RUD TRIM"):
        st.markdown("""
* NL: Moves rudder nose left to 24$\degree$
* NR: Moves rudder nose right to 22$\degree$
                    """)
        
flap_bt_pos = st.radio("Flaps Emerg Pwer PB", options=["OFF", "FLAPS", "ON"], label_visibility="collapsed", horizontal=True)

emer_flap_selection = {
    "OFF": {"img": "images/flaps_emer_pb_off.png", "desc": "Normal electrical power supply to the flaps system via the right bus"},
    "FLAPS": {"img": "images/flaps_emer_pb_flaps.png", "desc": "FLAPS automatically illuminates to indicate only the essential bus is providing power, but is not connected to the flaps system"},
    "ON": {"img": "images/flaps_emer_pb_on.png", "desc": "When the pushbutton is pressed, ON illuminates indicating the essential bus is connected to the flaps system.  This allows emergency extension of the flaps."}
}
col1, col2 = st.columns(cols_settings)
with col1:
    st.image(emer_flap_selection[flap_bt_pos]["img"], use_column_width=True)
with col2:
    with st.expander("FLAPS EMERGENCY POWER PUSHBUTON"):
        st.markdown(F"""
{emer_flap_selection[flap_bt_pos]["desc"]}
                    """)


        
col1, col2 = st.columns(cols_settings)
with col1:
    st.image("images/flap_lever.png", use_column_width=True)
with col2:
    with st.expander("FLAP LEVER"):
        st.markdown("""
* 0$\degree$
    - Flaps indicator and digital numbers are cyan during ground ops.
* 8$\degree$
    - Takeoff position - flaps indicator and digital readouts are green during ground ops.
    - Minimum retraction until ice is removed from the flaps.
* 15$\degree$
    - Takeoff position - flaps indicator and digital readouts are green during ground ops.
    - Maximum extension during icing conditions
* 33$\degree$
    - Flaps indicator and digital numbers are cyan during ground ops.
                    """)
        

col1, col2 = st.columns(cols_settings)
with col1:
    st.image("images/airbrake_lever.png", use_column_width=True)
with col2:
    with st.expander("AIRBRAKE LEVER"):
        st.markdown("""
* IN
    - Airbraking
    - Roll assitance
    - Blended airbraking and roll assistance
    - Lift dump
    - If throttles are moved above MCT and lever moved out of IN:
        - MFS remain at o $\degree$
        - AIRBRK annunciator displays in black with cyan background
        - CAS Takeoff CONFIG in cyan
        
* 1/2
    - MFS extend to 20$\degree$
    - AIRBRK annunciator displays in green with black background
    - If throttles are moved above MCT:
        - MFS auto rettract to 0$\degree$
        - AIRBRK annunciator displays in black with cyan background
        - CAS Takeoff CONFIG in cyan
    - Moving the control wheel more than 27 $\dgree$ results in a bliendig or mixing of the roll assist and airbrakes as follows on the downward wing:
        - Flaps 8 or 15 - Roll assist moves MFS smoothly
        - Flapps 33 -MFS commands are on a UMS for landing
* OUT
    - MFS extend to 35$\degree$
    - AIRBRK annunciator displays in black with green background
                    """)
        
with st.expander("Airbrake - Throttles T/O"):
    st.markdown("""
- If throttles are moved above MCT and lever moved out of IN:
        - MFS remain at o $\degree$
        - AIRBRK annunciator displays in black with cyan background
        - CAS Takeoff CONFIG in cyan
- If throttles are moved above MCT:
        - MFS auto rettract to 0$\degree$
        - AIRBRK annunciator displays in black with cyan background
        - CAS Takeoff CONFIG in cyan
""")
    

with st.expander("Airbrake - Automatic Speed Protection"):
    st.markdown("""
- Aircraft speed > Mach 0.751:
    * Throttles - position ignored
    * MFS - automatically extend
    * AIRBRK displays
- Aircraft speed < Mach 0.74:
    * MFS - automatically retract to 0 $\degree$
    * AIRBRK extinguishes
""")
    
with st.expander("Roll Assist"):
    st.markdown("""
    * MFS exxtend between 0$\degree$ and 35$\degree$ on the donward moving wing when:
        * Control wheel more than 27$\degree$
        * Airpees < 175 kt
        * Flaps extended
""")
    
with st.expander("Blended Roll Assist and Airbrake"):
    st.markdown("""
- Moving the control wheel more than 27 $\dgree$ results in a bliendig or mixing of the roll assist and airbrakes as follows on the downward wing:
        - Flaps 8 or 15 - Roll assist moves MFS smoothly
        - Flapps 33 -MFS commands are on a UMS for landing
""")
    
with st.expander("Lift Dump"):
    st.markdown("""
* Trottles at IDLE with speed > 45 kt and one of the following:
    * Both WOW
    * One WOW and whells spinning
    * No WOW and tree wheels spinning
* When the above conditions are satisfied:
    * MFS and GS extend fully to 35 $\degree# and 50$\degree$ and remain unitl speed < 45 kt.
    * Lift Dump annunciator displays
* Lift dump is also commanded when a rejected takeoff is activated above 45 kt by movint the trottles to IDLE
""")
    
with st.expander("Lift Dump - Takeoff"):
    st.markdown("""
* Moving the throttles above idle when lift dump is active:
    * Automatic termination of the lift dump function
    * MFS and GS retract to 0$\degree$
    * Lift dump annunciator extinguises
""")
    

############################## QUESTION BANK
st.write("## Question Bank")

with st.expander("When a STAB Trim Fail message displays, pressing ENABLE causes ___________ to illuminate on the pushbutton and removes power from the trim switches on the _______________"):
    st.write("ON - Control Wheel")

with st.expander("The selectable flap positions are _____________"):
    st.write("0$\degree$, 8$\degree$, 15$\degree$, 33$\degree$")


with st.expander("If a dual generator failure occurs, the flaps can only be used after pressing the FLAP EMER PWR pushutton"):
    st.write("True")

with st.expander("The __________ function is automatic when the aircraft touches down with throttles in the IDLE position"):
    st.write("Lift Dump")

with st.expander("Landing with the airbrakes extended is permitted provided the aircraft is on a stable approach and the airbrakes are retracted before 25 ft AGL"):
    st.write("False")