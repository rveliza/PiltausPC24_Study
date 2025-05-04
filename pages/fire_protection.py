import streamlit as st

st.title("Fire Protection")


st.write("## Question Bank")

with st.expander("What allows air to enter and ventilate the nacelle?"):
    st.write("""
* 2 NACA Ductos, one in the front-top and the other in the front-bottom of the cowlings, therefore they are an important part of the preflight inspection.""")
    
with st.expander("How many fire sensors elements are in the engine?"):
    st.write("""
* 1 fire sensor elements""")
    
with st.expander("At what temperature does the fire sensor element activate?"):
    st.write("""
* 510$\degree$C +/- 10$\degree$C
    - This temperature is only achivable in the event of a fire, eliminating the possibility of a false alarm.""")

with st.expander("How many fire extinguishing bottles are there?"):
    st.write("""
* 2 fire extinguishing bottles""")
    
with st.expander("Where are the fire extinguishing bottles located?"):
    st.write("""
* Upper rear fuselage under the vertical stabilizer""")
    
with st.expander("What are the indications of a fire?"):
    st.write("""
* FIRE on ENG ISOL pushbutton
* FIRE on ITT gauge
* L/R ENG FIRE CAS message
* Engine icon changes from gray to red
* Aural warning ("Left/Righet Engine Fire")""")
    
with st.expander("What happens when the ENG ISOL pushbutton is pressed?"):
    st.write("""
* Locks it in the present position
* Illuminates the ENG ISOL in the lower portion
* Closes the associated fuel shutoff valve
* Closes the associated bleed air valve
* After five seconds, the L/R Engine Isolated CAS message will display
* Arms the fire extinguisher bottle
* FIRE XTING 1 illuminates
* Bottle Icon becomes green
* Piping from the bottle to the engine becomes green
* Text box ARMED""")
    
with st.expander("At what temperature will the FIRE indications extinguish?"):
    st.write("""
* 405$\degree$C""")
    
with st.expander("How many seconds for the second bottle to be armed?"):
    st.write("""
* 30 seconds""")
    
with st.expander("What is the indication of the fire bottle when empty?"):
    st.write("""
* The bottle icon will turn yellow
* EMPTY will display in the text box
* XTING 1 or XTING 2 Empty""")
    

with st.expander("What indications are there when both fire bottles are empty?"):
    st.write("""
* Both bottle icons will turn yellow
* EMPTY will display in the text box in both extinguisher icons
* EMPTY will display in both FIRE XTING pushbuttons
* XTING 1 EMPTY cas message
* XTING 2 EMPTY cas message""")
    
with st.expander("Where is the cabin smoke detector located?"):
    st.write("""
* behind the aft right-hand headliner near the evaporator inlets""")
    
with st.expander("How many portable fire extinguishers are there?"):
    st.write("""
* 2 portable fire extinguishers""")
    
with st.expander("Where are the portable fire extinguishers located?"):
    st.write("""""
* Behind the copilot seat
* Cabin floor behind the last right-hand passenger seat or behind the aft divider wall in the baggage compartment""")