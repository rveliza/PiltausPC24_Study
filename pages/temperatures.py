import streamlit as st

st.title("Important Temperatures")
temp_params = {"FL450": "8,000 ft Cabin @8.83 psi.  9.07 psi OFV starts to open.  9.27 Max", 
                   "135": "Max Oil temp", 
                   "80": "Max fuel temperature",
                   "50": "Max OAT (Sea Level)", 
                   "15": "WAI inhibited above this temp / Auto unlatchment of ICE mode 1 after 10 minutes", 
                   "10": "MAX TAT for WAI / Max for Windshield Emergency Heat / MIN Oil Temp for N2 > 80% / Max temp for NAI",
                   "2": "Min temp to operate water waste system", 
                   "0": "Min battery temp for flight",
                   "-5": "Min Lion battery for battery engine start",
                   "-12": "Min temp for OXY MASK TEST",
                   "-20": "Min NiCd battery for battery engine start", 
                   "-29": "Min temp for PBE", 
                   "-40": "Min fuel temperature / Min inflation of boots / Min Oil for starting ", 
                   "-54": "Min OAT for GPU start / MIN OAT (Sea Level)", 
                   "-65": "Landing Gear minimum temp", 
                   "": "Choose a temperature in $\degree$C"
                   }

temperature = st.radio("Select a temperature", ["135","80", "50", "15", "10", "2", "0", "-5", "-12", "-20", "-29", "-40", "-54", "-65", ""], index=14, label_visibility="collapsed")

st.subheader(temp_params.get(temperature, "None yet"))