import streamlit as st

st.title("Memory Items")

with st.expander(":red-background[EMERGENCY DESCENT]"):
    st.markdown("""
1. Crew oxygen Maskes - DON / 100% / Establish COMM
2. PASSENGER OXYGEN - ON, instruct passengers to don drop down masks
3. SEAT BELTS - ON
4. THRUST Levers - IDLE
5. AIRBRAKE lever - OUT
""")
    
with st.expander(":red-background[ENGINE FIRE ON-GROUND / TAIL PIPE FIRE]"):
    st.markdown("""
1. THRUST LEVER - IDENTYFY / IDLE
2. ENG SWITCH - OFF
3. ENG ISOL pushbutton - Push / check after 5 sec amber ':orange-background[**ENG ISOL**]'
4. FIRE XTING pushbutton - Push to activate
""")
    
with st.expander(":red-background[ENGINE FIRE OR FAILURE DURING TAKEOFF]"):
    st.markdown("""
*Airspeed below V1*
1. Rejected Takeoff 3-NAE-19 - Accomplish

*Airspeed at or above V1*
1. THRUST levers - Fully forward, ATR
2. VR - Rotate to 9 deg ANU initially
3. Airspeed - Maintain at or above V2
4. L/G - When positive rate of climb - UP
""")
    
with st.expander(":red-background[REJECTED TAKEOFF]"):
    st.markdown("""
1. THRUST LEVERS - IDLE
2. BRAKES - Max Braking / As Required
""")
    
with st.expander(":red-background[FIRE, SMOKE OR FUMES IN COCKPIT / CABIN]"):
    st.markdown("""
1. CREW OXYGEN MASK - DON / select EMGCY / Vent valve open
2. Smoke goggles - DON
3. Passenger OXYGEN - ON, Instruct PAX to don drop down masks
                
**LAND ASAP / INITIATE DIVERSION**    
4. Aircraft - Land as soon as possible
""")
    
    
with st.expander(":red-background[EMERGENCY EVACUATION]"):
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