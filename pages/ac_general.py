import streamlit as st

st.title("Aircraft General")

with st.expander("Engines"):
    st.write("Williams International FJ44-4A QPM turbofan engines")

with st.expander("Maximum continuous thrust"):
    st.write("3,420 lbs")

with st.expander("Maximum takeoff thrust"):
    st.write("3,600 lbs")



    ac_wheelbase = "3 m"

with st.expander("Aircraft Dimensions"):
    feet_cm = st.radio(
    "Units",
    ["ft", "mt"],
    index=0,
    label_visibility="collapsed",
    key="dimensions",
    horizontal=True
)
    ac_length = "16.8 m" if feet_cm == "mt" else "55 ft 2 in"
    ac_wingspan = "17 m" if feet_cm == "mt" else "55 ft 9 in"
    ac_height = "5.3 m" if feet_cm == "mt" else "17 ft 4 in"
    ac_wheelbase = "3.0 m" if feet_cm == "mt" else "9 ft 10 in"
    st.markdown(f"""
* Length: {ac_length}
* Wingspan: {ac_wingspan}
* Height: {ac_height}
* Wheelbase: {ac_wheelbase}
""")
    
with st.expander("Cabin Door"):
    st.markdown("""
* Only one person a time
* Six shoot bolt indicators
* Door is closed when all six indicators are green
    * When door is open or disenganges, indicors are red
    * PAX DOOR OPEN Cass message displays
""")
    

with st.expander("Cargo Door"):
    st.markdown("""
* Must not be operated in crosswinds exceeding 60 kt
* Four shoot bolt indicators
* Five hook latch indicators
    * When cargo door is open or improperly secured, indicators turn red and a CARGO DOOR OPEN CAS message displays.
* Tail support must be installed if personell in the cargo area during loading
* CAUTION: Operation of the left engine is prohibited with the cargo door open """)
    

with st.expander("Maximum towbarless tug weight"):
    lb_kg = st.radio(
        "Units",
        ["lb", "kg"],
        index=0,
        label_visibility="collapsed",
        key="towbarless",
        horizontal=True
    )
    tow_weight = "5379 lb" if lb_kg == "lb" else "2440 kg"
    st.markdown(f"""
* {tow_weight}""")
    
with st.expander("Minimum width to complete a minimum 180-degree turn with differential braking"):
    ft_m = st.radio(
        "Units",
        ["ft", "m"],
        index=1,
        label_visibility="collapsed",
        key="turning_radius",
        horizontal=True
    )
    turning_radius = "50 ft" if ft_m == "ft" else "15.2 m"
    st.markdown(f"""
* {turning_radius}""")
    
with st.expander("Standard Emergency Equipment"):
    st.markdown("""
* Smoke goggles - Behind pilot seat in stowage box"
* Fire extinguishers - 2
    * 1 in cockpit behind copilot seat in stowage box
    * 1 in cabin behind the last passenger seat on right
* Emergency lighting
* Overwing emergency exits - 2
* ELT - Rear fuselage """)
    

with st.expander("Emergency Exits"):
    st.markdown("""
* Overwing exits - 2
* Cabin door - 1 """)
    
with st.expander("Certification"):
    st.markdown("""
* Day, night, VFR, IFR including CAT I APR, and icing, single pilot operations""")
    
with st.expander("Maximum passengers (based on configuration)"):
    st.markdown("""
* 10 passengers""")
    
with st.expander("Aircraft manuals that must be onboard"):
    st.markdown("""
* Aircraft Flight Manual (AFM) Volume 1 - Printed
* Aircraft Flight Manual (AFM) Volume 2 - Printed
* QRH - Printed or electronic
* ACE$^{tm}$ Pilot Guide - Printed or electronic
* FCOM - Printed or electronic """)