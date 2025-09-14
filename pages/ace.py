import streamlit as st
cols_settings = [20, 80]


st.title("ACE")

st.write("## Lights and Switches")

col1, col2 = st.columns(cols_settings)

with col1:
    st.image("images/autothrottle_pb.png")
with col2:
    with st.expander("AUTO THROTTLE"):
        st.markdown("""
* On Ground:    
    * Armed when pressed
        * LED does not illuminate
        * AT is displayed on the PFD
    * Active when both thrust levers are advanced above 50% N1
""")
        
col1, col2 = st.columns(cols_settings)
with col1:
    st.image("images/bank_pb.png")
with col2:
    with st.expander("BANK"):
        st.markdown("""
* Illuminated:
    * LOW: 17$\degree$ of bank
    * If heading mode is active a magenta arc is is displayed on the attitude sphere int the PFD.
* Not Illuminated:
    * HIGH: 27$\degree$ of bank
""")
        
col1, col2 = st.columns(cols_settings)
with col1:
    st.image("images/l_r_pb.png")
with col2:
    with st.expander("L / R"):
        st.markdown("""
* Default setting at power up is L
* Pressing the switch toggles between L and R
* Coupled approach:
    * Both arrows illuminate below 1,200 feet RA
    * Pushing the button has no effect
""")
        
col1, col2 = st.columns(cols_settings)
with col1:
    st.image("images/speaker_pa_pb.png")
with col2:
    with st.expander("SPEAKER / PA"):
        st.markdown("""
* ON:
    * Cockipt speaker ON
    * Headesets ON
* OFF:
    * Cockpit speaker OFF
    * Headsets ON
* PA:
    * When selected on either panel, pushing either PTT button transmits over the PA.
    * Left side has priority over right side if both are pressed at the same time.
""")

col1, col2 = st.columns(cols_settings)
with col1:
    st.image("images/ics_pb.png")
with col2:
    with st.expander("INTERCOM SELECTOR"):
        st.markdown("""
* ISO:
    * Pilot isolated from intercom and connected only to the radio system
    * Entertainment 1 inputs are muted
    * Copilot hears passengers intercom and entertainment 1
    * Passengers hear copilot and entertainment 2
    * Neither copilor nor passengers hear pilot transmissions or radio receptions
    * This selection must be made for communications when:
        * On standby bus (PDC mode) operations
    * Copilot may select other modes
* ALL:
    * Pilot, copilot, and passengers hear the selected radio and intercom
    * Pilot and copilot hear entertainment 1
    * Passengers hear entertainment 2
    * Copilot cannot select other mode
* CREW:
    * Pilot and copilot hear the selected radio and intercom
    * Pilot and copilot hear entertainment 1
    * Passengers hear neither radio nor intercom transmissions
    * Passengers hear entertainment 2
    * Copilot cannot select other mode
""")
    
st.write("## Question Bank")

with st.expander("To what displays does the AGM1 provide graphics to?"):
    st.write("DU1, DU2")

with st.expander("To what displays does the AGM2 provide graphics to?"):
    st.write("DU3, DU4")

with st.expander("What are the two important failure circumstances that require reversion control?"):
    st.write("""
* Failure of the DU (blank screen)
* Failure of AGM (Red X accross the entire screen)
    - If failure on one of the PFD's the other AGM may be selected
    - NAV information shown will be based on NAV sensor selected on the other display
""")
    
with st.expander("When does the CVR operate?"):
    st.write("Automatically when electrical power from the essential bus is available")

with st.expander("How can you delete the data from the CVR?"):
    st.write("""
* Parking break set
* WOW
* CVR is recording (one engine running)
""")
    
with st.expander("For how long will the FDR record?"):
    st.write("25 hours")

with st.expander("What are the main components of the AHRS system?"):
    st.write("""
* IRS
    - Alignment from 5 minutes (low latitudes) up to 17 minutes (high latitudes)
    - Aircraft must not be moved during alignment or cycle will be restarted 30 seconds after all motion stops
* 2 AHRS
    - AHRS 2: attitude and heading for PFD2
    - AHRS 3: data for dual yaw damper functions
* Magnetometer
""")

with st.expander("How many AFCS systems does the aircraft have?"):
    st.write("2 systems")    

with st.expander("Where are the AFCS hosted?"):
    st.write("""
* Primary AFCS in MAU1
* Secondary AFCS in MAU2
* The active system swaps every power cycle, and the other is standing by
""")
    
with st.expander("How many servos are there for the AFCS?"):
    st.write("""
* 1 for roll
* 1 for pitch
* 2 for yaw
""")
    
with st.expander("What powers the servos?"):
    st.write("""
* yaw 1: essential bus
* yaw 2: right bus
* roll and pitch: dual powered by essential bus and righ bus
""")
    
with st.expander("Normal disconnection of Autopilot?"):
    st.write("""
* Quick Disconnect
* AP on flight controller
* Any pitch trim on control wheel
* Stick shaker activation

* Indications: triple cavalry charge and AP flash red on PFD for 2.5 secs.
""")
    
with st.expander("Abnormal disconnection of Autopilot?"):
    st.write("""
* AP elevator or AP aileron servo failure
* AP monitor failure
* left bus or dual gen failure, depending on APEX build
""")
    
with st.expander("What does the YD do?"):
    st.write("""
* Durtch roll damping
* stability augmentation
* turn coordination
""")
    
with st.expander("How can you disengage the autopilot without disengaging the YD?"):
    st.write("""
* AP button of Flight Controller
* Trim switch on any control wheel
""")
    
with st.expander("Describe the AYT:"):
    st.write("""
* Moves the rudder to drive the sideslip to 0 and then offloads the the rudder force by moving the trim tab
* In case of one engine inop, it will maintain half trapezoid
""")
    
with st.expander("How does the AYT engage?"):
    st.write("Automatically with YD engagement")


with st.expander("What happens to the AYT when the trim switch is moved in a control wheel?"):
    st.write("""
* AYT will disengage
* Auto Yaw Trim Off CAS message
""")
    
with st.expander("What are the modes of operation of the Autothrottles?"):
    st.write("""
* Thrust:
    - Takeoff: throttles set to takeoff thurst
    - FLC climb: throttles set to clmb thrust or below
    - FLC descent: throttles set to idle thust or above
* Speed Hold:
    - All other modes, including VS, ALT, ASEL, GS
    - Throttles are set to maintain manual of FMS speed
* Hold:
    - Holds thust levers in a fixed position during takeoff beginning at 60kt until 400 ft above the runway   
""")
    
with st.expander("How is the AT activated during takeoff"):
    st.write("""
    * AT sets takeoff power if:
        - speed below 60kt
        - both thrust levers advance above 50% N1
""")
    
with st.expander("What do the autothrottles do during EDM?"):
    st.write("""
* FLC: idle
* ASEL or alt: 175 kts
""")
    
with st.expander("""When is the EDM activated?"""):
    st.write("5 secondes after CAB ALT HI CAS message is triggered")
    
with st.expander("""Describe EDM when activated"""):
    st.write("""
* FD - FLC and HDG
* FD - Left 90$\degree$ turn (max 13$\degree$ bank)
* FD - Sets manual speed target to VMO/MMO
* FD - sets altitude to 15,000 feet
* If not enganged, engages the AT and sets them to IDLE
* AP turns the aircraft 90$\degree$ to the left and descends
* @ 15,000 ft the AP capture the altitude
* FD sets manual speed to 175 kts
""")
    
with st.expander("""Once activated, how can you cancell the EDM?"""):
    st.write("""
* AP Quick Disconnect
* Manual trim
* AP of flight controller
* TCS for 2 secs, AP keeps engaged and EDM reverts to ROL and PIT
""")
    
with st.expander("What is the function of the Rudder Bias?"):
    st.write("""
* Assist pilots with compensating yaw resulting from asymmetric engine thrust during takeoff and go around
* Rudder servo enganges and deflects the rudder toward operative engine
""")
    
with st.expander("What conditions are required for the RB to be armed?"):
    st.write("""
* N1 data valid from both engines
* Aircraft below 2,500 AGL
* Thrust levers in T/O position
* Yaw damper is OFF
""")
    
with st.expander("Until when will it remain activated?"):
    st.write("""
* The AP Quick Disconnect is pressed
* YD is enganged
* Thrus assymetry condition is eliminated
""")
    
with st.expander("When is the tactile feedback available?"):
    st.write("Anytime autopilot is not engaged")