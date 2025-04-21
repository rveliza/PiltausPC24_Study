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
    
st.write("## Secondary Flight Controls")
st.write("Trims, Flaps, Spoilers")

st.image("images/flaps_diag.png")

with st.expander("Flap System"):
    st.markdown("""
* Right Bus Powered
* Electromechanically actuated
* Double slotted
* Main and auxiliary flap panels
    * Two main flap panels are interconnected by a torque tube.
    * Each flap panel group incorporates inboard, middle and outboard hinges.
    * The inboard hinge supports the main and auxiliary flap panels
    * Outboard hinge supports only the main flap panel
    * Flap actuators are located at the inboard and outboard hinges
* Full travel time for full actuator rotation of 94.3$\degree$ is 17.2 seconds in either direction.
* UMS channel DCPU 2A is for control
* DCPU 2b is the monitoring channel:
    * Loss of motion
    * Uncommanded movement
    * Skew
    * Asymmetry
                
* Flaps Inhibit
    * VFE exceedance
        * Takeoff - 200 kt
        * Landing = 175 kt
        * Failed pitch trim - 160 kt
    * Flap control lever in intermediate position for more than 3 seconds.
""")
    
st.image("images/spoilers_diag.png")

with st.expander("Spoiler System"):
    st.markdown("""
* Four spoiler panels per side, each with its own actuator.
    * Two inner panels - Ground Spoilers
        * Operate only in ground
    * Two outer panels - Multi Function Spoilers
        * Airbrakes
        * Low speed roll control enhancement
        * Lift dump during landing rollout and during RTO.
    * Electrical power for the spoiler system is supplied by both the left and the right buses to ensure that at least partial capability remains available in case of loss of power to either bus.
""")
    
st.image("images/pitch_trim_diag.png")

with st.expander("Pitch Trim System"):
    st.markdown("""
* Range: 10$\degree$ up - 5$\degree$ down
* Pitch Trim Actuator:
    * Motor 1 - Primary pitch trim (channel 1) - Essential Bus
    * Motor 2 - Secondary pitch trim (channel 2) - EPDU 4
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
    "OFF": {"img": "images/flaps_emer_pb_off.png", "desc": "Normal electrical power supply to the flaps system via the right bus - EPDU 4"},
    "FLAPS": {"img": "images/flaps_emer_pb_flaps.png", "desc": "Emergency Mode, emergency contactors EC1 and EC2 have operated and only the essential bus is powered. FLAPS automatically illuminates to indicate only the essential bus is providing power, but is not connected to the flaps system"},
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
    - Moving the control wheel more than 27 $\dgree$ results in a blendig or mixing of the roll assist and airbrakes as follows on the downward wing:
        - Flaps 8 or 15 - Roll assist moves MFS smoothly
        - Flapps 33 -MFS commands are on a UMS for landing
* OUT
    - MFS extend to 35$\degree$
    - AIRBRK annunciator displays in black with green background
    * 4.5 seconds / 8$\degree$ per second.
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
        * Airpeed < 175 kt
        * Flaps extended
    * The full deflection of 35$\degree$ on the extended MFS is reached when control wheel deflection reaches 72$\degree$ at speeds < 140 kt.
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
* Sequence:
    * Outer MFS: Signalled on touchdown. Deploys aprox in 0.75 secs.
    * Outer GS: Signalled on touchdown.  Deploys aprox in 2.2 seconds
    * Inner MFS: Signalled 2 seconds after touchdown.  Deploys aprox in 0.75 secs.
    * Inner GS: Signalled 2 seconds after touchdownd Deploys aprox in 1 second.
""")
    
with st.expander("Lift Dump - Takeoff"):
    st.markdown("""
* Moving the throttles above idle when lift dump is active:
    * Automatic termination of the lift dump function
    * MFS and GS retract to 0$\degree$
    * Lift dump annunciator extinguises
""")
    
with st.expander("Pitch Trim Inhibit"):
    st.markdown("""
When the primary pitch trim system fails, automatic pitch trim compensation for airbrake operation is not available. When this is the case, airbrake operation is inhibited above 250 kt and the airbrakes cannot be extended
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