import streamlit as st

st.title("Environmental Control")   

st.write("## Question Bank")

with st.expander("What are the main components of the environmental control system?"):
    st.write("""
* Shutoff Valves - Spring loaded closed
* Diverter Valves
    - Open - hor air to system
    - Closed - air to precooler
* Croos-Bleed Valve - Spring loaded closed, connects the normally independent left and right systems
* Preecoler - Cool HP bleed air from the diverter valve using exhaust air
             """)
    
with st.expander("How are the bleed SOV's manually controlled?"):
    st.write("""
* With the Bleed Rotary Knob 
    - L: Left SOV available for UMS control, Right SOV closed
    - R: Right SOV available for UMS control, Left SOV closed
    - Both: Both SOV's available for UMS control
    - Off: Both SOV's closed""")



with st.expander("How many electrical heaters are there?"):
    st.write("""
* 4 in cabin
* 1 in cockpit""")
    
with st.expander("What happens when we select QPM mode?"):
    st.write("""
* Both bleed SOV are closed and displayed in white
* The cross-bleed valve is closed and displayed in white""")
    
with st.expander("In QPM mode, how can you warm the cabin?"):
    st.write("""
* By setting a warm temperature on the environmental summary window""")
    
with st.expander("What is the limit between the cockpit and the cabin temperature selection?"):
    st.write("""
* 5$\degree$C""")

with st.expander("By what percent will the fan speed be reduced when selected in silent mode?"):
    st.write("""
* 40%""")
    
with st.expander("Under what condition will the ram air scoop only open?"):
    st.write("""
* When the cabin is depressurized and the handle is pulled
    - The aircraft must descend to 15,000 ft or less to equalize the pressure and allow the scoop to extend""") 

with st.expander("What are the main components of the cabin pressure control system?"):
    st.write("""
* Outflow Valve - Opens to allow air to exit the pressurized cabin
* ECMU - Dual-channel controller thad modulates the position of the outflow valve
* PRV - Spring loaded closed, opens to prevent threshold exceedance
* 2 NPRV's - Spring loaded closed, opens to prevent threshold exceedance """)
    
with st.expander("What are the main controls of the cabin pressure control system?"):
    st.write("""
* Mode Rotary Knob
    - Auto: full automated control by the ECMU
    - Man: Enables the CABIN ALT knob
* CABIN ALT Knob - Spring loaded in center position 
    - DESCEND: Closes the outflow valve
    - CLIMB: Opens the outflow valve
* DUMP: Opens the outflow valve to dump cabin pressure
    - Pressed - Activates the dump function, illuminates ON in amber
    - Unpressed - Deactivates the dump function, extinguishes ON in amber""")


with st.expander("What indication will we see in the environmental summary window when the MODE rotary knob is in AUTO?"):
    st.write("""
* CAB LO: softkey is enabled to limit max differential pressure to 8.33 psi
* DEST ELEV: softkey is enabled to set the destination elevation manually
    * If destination set manually:
        * City code displays PILOT in green instead of the airport code
        * The active mode changes from FMS ELEV to ELEV
""")
    
with st.expander("What indication will we see in the environmental summary window when the MODE rotary knob is set to the MAN position?"):
    st.write("""
* City code, mode and LFE will be replaced by an amber CPS MANUAL
* DEST ELEV: greyed out and disabled
* CAB LO: greyed out and disabled""")
    
with st.expander("What are the trigger for FIELD HI??"):
    st.write("""
* Displays when a takeoff or landing at a high-altitude airport is detected.
* 8,3000 ft.""")
    
with st.expander("What control the oxygen masks deployment?"):
    st.write("""
* EMCU: 12,850 +/- 500
    - If ECMU fails, the ACE sets the system at 14,800 +/- 500""")

with st.expander("To what altitude is the altitude limiting mode set to?"):
    st.write("14,500 ft")



