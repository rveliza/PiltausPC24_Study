import streamlit as st

st.title("Important Altitudes")

altitude_params = {"FL450": "8,000 ft Cabin @8.83 psi.  9.07 psi OFV starts to open.  9.27 Max", 
                   "FL300": "Yaw damper max / EDM is armed", 
                   "24,800": "FIELD HI mode from on to off", 
                   "15,000": "EDM descent altitude, Ram Air Max for opening", 
                   "14,800": ":red-background[CAB ALT] - Backup Avionics oxygen Deploy Set-Point", 
                   "14,500": "Outflow valve limit -ECMU controlled", 
                   "14,200": ":red-background[CAB ALT] for Field HI operation", 
                   "12,850": "Oxygen mask deployment - Commanded by ECMU", 
                   "9,500": ":red-background[CAB ALT] Normal operation - EDM @ 5 seconds",
                   "8,300": "Field HI", "0": "Select an altitude"}

altitude = st.radio("Select an altitude", ["FL450", "FL300", "24,800", "15,000", "14,800", "14,500", "14,200", "12,850", "9,500", "8,300", "0"], index=10)

st.subheader(altitude_params.get(altitude, "None yet"))