import streamlit as st

st.title("Landing Gear")

st.write("## Question Bank")

with st.expander("How many degrees of steering does the nose wheel have?"):
    st.write("""
* 60$\degree$ left and right in free castoring mode accomplished with differential braking
* 17$\degree$ left
* 15.6$\degree$ right""")
    
with st.expander("What prevents the landing gear handle from being moved to the UP position while on ground?"):
    st.write("""
* Spring loaded solenoid""")
    
with st.expander("What keeps the landing gear in the up and down position?"):
    st.write("""
* Actuator contain internal brakes, therefore the aircraft does no require downlock or gear pins when on ground""")
    
with st.expander("What are the normal gear indications?"):
    st.write("""
* DOWN: 3 green DN semi round lights
* TRANSIT: 3 Square with dashes
* UP: 3 up squares in white
* Declutter: Greyed out when both flaps and gear are up""")
    
with st.expander("After how many seconds of a mismatch do we get warning?"):
    st.write("""
* 30 seconds""")
    
with st.expander("What are the indications of a mismatch when gear is selected down?"):
    st.write("""
* Not down/locked box illuminates with red and white lines
* Down/locked boxes remain green
* CAS Gear Mismatch illuminates""")
    
with st.expander("What CAS messages would lead to using the emergency extension?"):
    st.write("""
* Gear Mismatch
* Gear Actuator""")
    
with st.expander("What must be accomplished before pulling the emergency extension handle?"):
    st.write("""
* Gear lever must be in the down position""")
    
with st.expander("What is the normal pressure for the nose tire?"):
    st.write("""
* 58 psi""")
    
with st.expander("What is the normal pressore of the main tires?"):
    st.write("""
* 73 psi""")
    
with st.expander("What is the psi overinflation of all wheels?"):
    st.write("""
* Rupture disc set at 300 psi""")
    
with st.expander("How many fusible plgugs are in each wheel?"):
    st.write("""
* 3 fusible""")
    
with st.expander("At what temperature do the fusible plugs melt?"):
    st.write("""
* 182$\degree$C""")
    
with st.expander("What are the Hydraulic Power Generation System components?"):
    st.write("""
* Hydraulic Resorvoir - Holds pressure between 37-43 psi
* Motor Pump - Provides 2700 - 3000 psi to the system
* Main Brake Accumulator - Stores pressure from motor pump for high-demand situation.  2700-3000 psi
* Digital Antiskid Control Unit - Limits wheel speed on all four wheels and modulates the pressure to limit skidding
* Park/Emergency Accumulator - operates at 3000 psi, 24 hours for parking
* Brake Valve - Hydraulic pressure proportional to the PARK/EMER BRAKE lever""")
    
with st.expander("How many Brake Wear Indicators are there?"):
    st.write("""
* 2 brake wear indicators per wheel.  8 in total""")
    
with st.expander("What softkeys are available in the BRAKES SYN page?"):
    st.write("""
* Pump: (AUTO-ON-OFF)
* ANTISKID: (AUTO-OFF)
    
""")
    
with st.expander("To which direction may you turn the PARK/EMER Brake?"):
    st.write("""
* 90$\degree$ any direction""")
    
with st.expander("What is the nominal hydraulic pressure?"):
    st.write("""3100 +/- 50 psi""")


with st.expander("Describe the Park Brake System Check?"):
    st.write("""
* Set and release the PB until the pressure falls below 2800 psi
* Check that the pum starts 
* Check pressure recharged to above 2850 psi
* Check that the pump stops""")
    
with st.expander("What indications do you expect when gear is up?"):
    st.write("""
* UMS disabes the system, as it bleeds down:
    - Motor pump is off
    Main brake accumulator and readout turn amber""")

with st.expander("What indications do you expect when gear is down?"):
    st.write("""
* Either flaps or the gear are down, the system is active to charge in flight prior to landing:
    - Motor pump is on
    Main brake accumulator and readout turn green when pressure is above 2600 psi""")

with st.expander("What is braking Despin??"):
    st.write("""
* If UMS detects aircraft is on flight and landing gear begin to reetract, it commands the brakes to be applied in order to stop them prior to entenring the MLG bay.""")
    
with st.expander("How does the antiskid system work?"):
    st.write("""
Takeoff:
* Inactive - 0-10 knots
* Active - above 10 kts
* Inactive - six seconds after gear up (to allow for despin)

Landing:
* Antiskid is disable during touchdown protection.
* Active - 3 seconds after touchdown or wheel speed is > 60 knots
* Inactive - speed < 10 knots
             
Rejected Takeoff:
* Disabled < 10kt
* Enabled > 10kt
* Disabled < 10kt""")
    
with st.expander("What pressures does the parking brake handle give?"):
    st.write("""
* Starting turn: 700 psi
* 30$\degree$ turn: 1000 psi
* 300$\degree$ and upper limit: 1600 psi""")
    
with st.expander("How may the hydraulic power generation be overriden?"):
    st.write("""
* Selecting the Pump from auto to ON""")
    
with st.expander("When will the UMS inhibit the overriding of the hydraulic system?"):
    st.write("""
* Temperature > 125$\degree$C
* Pressure > 3200 psi
* Reservoir is empty""")
    

    
