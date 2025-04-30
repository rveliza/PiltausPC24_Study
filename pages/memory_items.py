import streamlit as st

st.title("Memory Items")

with st.expander(":red-background[EMERGENCY DESCENT] * Non Annunciated"):
    st.markdown("""
1. Crew oxygen Masks - DON / 100% / Establish COMM
2. PASSENGER OXYGEN - ON, instruct passengers to don drop down masks
3. SEAT BELTS - ON
4. THRUST Levers - IDLE
5. AIRBRAKE lever - OUT
""")
    
with st.expander(":red-background[ENGINE FIRE ON-GROUND / TAIL PIPE FIRE] * Non Annunciated"):
    st.markdown("""
*If during start, engine fire detector senses a temperature below 510$\degree$C or else engine fire is indicated by ground personnel.*    
1. THRUST LEVER - IDENTYFY / IDLE
2. ENG SWITCH - OFF
3. ENG ISOL pushbutton - Push / check after 5 sec amber ':orange-background[**ENG ISOL**]'
4. FIRE XTING pushbutton - Push to activate
""")
    
with st.expander(":red-background[ENGINE FIRE OR FAILURE DURING TAKEOFF] * Non Annunciated"):
    st.markdown("""
*Airspeed below $V_{1}$*
1. Rejected Takeoff 3-NAE-19 - Accomplish

*Airspeed at or above $V_{1}$*
1. THRUST levers - Fully forward, ATR
2. VR - Rotate to 9 deg ANU initially
3. Airspeed - Maintain at or above $V_{2}$
4. L/G - When positive rate of climb - UP
""")
    
with st.expander(":red-background[REJECTED TAKEOFF] * Non Annunciated"):
    st.markdown("""
1. THRUST LEVERS - IDLE
2. BRAKES - Max Braking / As Required
""")
    
with st.expander(":red-background[FIRE, SMOKE OR FUMES IN COCKPIT / CABIN] * SMOKE Tab"):
    st.markdown("""
1. CREW OXYGEN MASK - DON / select EMGCY / Vent valve open
2. Smoke goggles - DON
3. Passenger OXYGEN - ON, Instruct PAX to don drop down masks
                
**LAND ASAP / INITIATE DIVERSION**    
4. Aircraft - Land as soon as possible
""")
    
    
with st.expander(":red-background[EMERGENCY EVACUATION] * EMERG EVAC Tab"):
    st.markdown("""
1. PARK BRAKE - Set
2. ATC / distress message - Notify
3. ENG L + R switches - Both OFF
""")
    

with st.expander(":red-background[ALL BRAKES FAIL]"):
    st.markdown("""
*On-ground during taxi:*
1. Wheel brakes / EMER brake - Use if available to stop aircraft
""")
    

with st.expander(":red-background[CABIN ALTITUDE]"):
    st.markdown("""
*Cabin altitude above warning threshold and voice callout 'CABIN ALTITUDE'*
1. Crew oxygen masks - Don / 100% / Establish COMM
2. Passenger oxygen - ON. Instruct passengers to don dropdown masks    
*IF rapid or explisve decompression:*    
3. Emergency Descent - 3-NAE-02 - Accomplish
""")
    

with st.expander(":red-background[CABIN PRESSURE]"):
    st.markdown("""
*In Flight with excessive negative differential pressure:*
1. Aircraft - Reduce descent rate    
                -- END --
""")
    
with st.expander(":red-background[L/R ENG FAIL]"):
    st.markdown("""
*The N1 has dropped 15% within 0.5 sec.  This will activate ATR during takeoff*
1. Engine instruments - Monitor / Confirm
""")
    
with st.expander(":red-background[L/R ENGINE FIRE]"):
    st.markdown("""
*The indicated Engine Fire detector senses a temperature above 510$\degree$C*    
*Audio 'Left/Right Engine Fire' callout*    
*:red['FIRE'] light on the associated Engine Isolation Push button*    
1. ENGINE FIRE - CONFIRM L or R    
*IF fire confirmed:*    
2. THRUST LEVER - IDLE
3. ENGINE SWITCH - OFF / STOP
4. ENGINE ISOLATION push button - Check associated CAS 'ENGINE ISOLATED' after five sec. CONFIRM ASSOCIATED :green-background['**1**'] illuminated    
*If CAS Message remains, affected side:*    
5. EXTINGUISHER push button - PUSH
""")
    
    
with st.expander(":orange-background[AFCS ABNORMAL DISCONNECT] * Non Annunciated"):
    st.markdown("""
*Indication: Flashing :red['AP'] on PFD and continuous 'Cavalry Charge' aural warning*
1. Airplane control wheel - Grasp firmly and regain aircraft control
2. Autopilot Disengage switch - Press to cancel aural warning (pilot or copilot wheel)
3. Aircraft - Retrim manually as necessary    
*If no AFCS associated CAS messages:*    
4. Aircraft - Attempt to re-engange autopilot once
""")
    

with st.expander(":orange-background[ENGINE HOT START ON GROUND] * Non Annunciated"):
    st.markdown("""
*Indications for hot start: Rapidly rising ITT approaching engine limits of 1,000$\degree$C or ITT hanging between 900$\degree$C and 1,000$\degree$C for 15 sec.*
1. Engine Switch - OFF
""")
    
with st.expander(":orange-background[ENGINE HUNG START ON GROUND] * Non Annunciated"):
    st.markdown("""
*Indications: engine fails to accelerate for > 30 sec*
1. Engine Switch - OFF
""")
    
with st.expander(":orange-background[SWPS INADVERTENT PUSHER OPERATION] * Non Annunciated"):
    st.markdown("""
*Non-commanded pusher operation, rapid nose-down motion*    
:red-background[**WARNING: NATURAL STALLS ARE NOT PREVENTED WITH THE STICK PUSHER INOPERATIVE. STALLS MUST BE AVOIDED WHEN THE STICK PUSHER IS INOPERATIVE**]
1. Control Wheel - Hold against pusher action
2. AP disconnect button - Press and hold continuously
""")
    
with st.expander(":red-background[TCAS RESOLUTION ADVISORY * FAS Message List]"):
    st.markdown("""
*Accompanied by audio commands for climb, descend, level off or maintain vertical speed.*    
1. Autopilot - Use yoke quick disconnect if AP enganged
2. Aircraft attitude - Immediately comply with RA commands indicated on the PFD
3. ATC Inform of TCAS RA    
*When clear of conflict*     
4. Aircraft - Return to previously assigned altitude and advice ATC    
                      -- END --
""")
    
with st.expander("RH ENG START"):
    st.markdown("""
To start the RH Engine:
1. R engine switch rotate to RUN
2. Confirm R Booster pump running and no FUEL PRESSURE CAS messages appear
3. R START PRESS
Monitor start sequence as follows:
1. When pressing start button "START" will appear "ON" on the PFD
2. At about 10%, N$_{2}$ "START" and "IGN" is illuminated in inverse video.  Check N$_{1}$ is increasing
3. Observe light-up and engine parameters until "IDL" is reached
4. Depending on ambient conditions "START" and "IGN" extinguish at approximately 45% - 50% of N$_{2}$""")
    
with st.expander("LH ENG START"):
    st.markdown("""
1. LH Engine Start
    * Start LH engine accordingly
    
##### Note: The right engine must exit QPM and set to Ground Idle before Left Engine start""")
    
with st.expander("ENGINE APPROXIMATE GND IDLE VALUES"):
    st.markdown("""   
* N$_{1}$: 25%
* ITT: 400 $\degree$C    
* N$_{2}$: 53.4%
* FF: 160 - 180 lbs
                
#### Confirm GEN 2 takes over and is supplying the aircraft body 
                
##### Note: If TAT or reported OAT is < 10$_\degree$C and visible signs of moisure are present then set the IPS rotary switch to AUTO/NAI""")
    

with st.expander("CLIMB"):
    st.markdown("""
1. Gear - UP    
    * Confirm Lever Up and Lights Out on System Summary Page"    
2. Yaw Damper - ON    
    * Confirm on FMA
3. Flaps - UP    
    * Confirm lever at 0 and indication on System Summary Page
4. Thrust - MCT
    * Thrust Levers back at MCT gate within five min after setting T/O
    * Verify MCT indication on both engine PDF indications""")