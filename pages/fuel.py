import streamlit as st

col_settings = [20, 80]

st.title("Fuel")







###################### Question Bank
st.write("## Question Bank")

with st.expander("What are the fuel tanks in each wing?"):
    st.markdown("""
    * Vent tank
    * Main tank
    * Collector tank""")

with st.expander("How many drain valves are there?"):
    st.markdown("""
    * 4 drain valves, each on an its own acces cover""")

with st.expander("What selections are available from the Fuel Synoptic Page?"):
    st.markdown("""
    * XFER
    * Left Pump
    * Right Pump
    * X Feed""")

with st.expander("When do we get a Fuel level Low?"):
    st.markdown("""
    * 250 lbs""")

with st.expander("Where are the boost pumps located?"):
    st.markdown("""
    * Forward section of the collector tank""")

with st.expander("When do the booster pumps provide fuel?"):
    st.markdown("""
    * Engine starts
    * Motive flow failure
    * Fuel balancing (crossfeed operation)
    * Fuel transfer
    * Defueling""")

with st.expander("From where does the left booster pump receive power?"):
    st.markdown("""
    * essential bus""")

with st.expander("From where does the right booster pump receive power?"):
    st.markdown("""
    * right bus""")

with st.expander("Where are the ejector pumps located?"):
    st.markdown("""
    * In the aft portion collector tank""")

with st.expander("What is the purpose of the ejector pumps?"):
    st.markdown("""
    * Provide fuel to the engines for normal operation when the booster pumps are off""")

with st.expander("What are the functions of the fuel/defuel valves?"):
    st.markdown("""
    * Pressure refueling
    * Fuel transfer
    * Defueling""")

with st.expander("Where are the fuel/defuel valves located?"):
    st.markdown("""
    * Forward portion of each inboard main tank""")

with st.expander("What is the normal position of the fuel xfeed valve?"):
    st.markdown("""
    * Closed""")    

with st.expander("When is the xfeed valve typically used?"):
    st.markdown("""
    * Fuel transfer inoperative and fuel balancing is required""")

with st.expander("What is the normal position of the Shutoff valves?"):
    st.markdown("""
    * Open""")

with st.expander("What powers the Shutoff valves?"):
    st.markdown("""
    * Essential bus""")

with st.expander("What closes the Shutoff valves?"):
    st.markdown("""
    * Engine Rotary Knob OFF
    * Engine Rotary Knob Dry Motor
    * Engine Isolation Pushbutton""")

with st.expander("What opens the Shutoff valves?"):
    st.markdown("""
    * Engine Rotary Knob RUN
    * Engine Rotary Knob IGN
    * Note: Both of this positions activate the boost pump untile engine N2 is above 40%""")

with st.expander("When do the endurance dashes disappear?"):
    st.markdown("""
    * During start, when N@ reaches 40%""")

with st.expander("When does the UMS control the fuel transfer between tanks?"):
    st.markdown("""
    * Difference of 220 lbs""")

with st.expander("When does the transfer stop?"):
    st.markdown("""
    * When the tanks are within 4.5 lb""")

with st.expander("When does the UMS deactivate the automatic fuel balancing funciton?"):
    st.markdown("""
    * If imbalance reaches 440 lbs""")

with st.expander("When is the xfeed valve typically used?"):
    st.markdown("""
    * During emergency or abnormal conditions such as:
        - Normal balancing not available
        - Right engine started after a dual generator failure""")
    
with st.expander("What must you NOT do if the REFUEL/DEFUEL switch is powered?"):
    st.markdown("""
    * Do not switch BAT2 on - may trigger a R BLEED Off/Fail message when engine is started.  If so, shut down engine and cycle power to reset""")
    
with st.expander("What must be done after a defuel procedure?"):
    st.markdown("""
    * Run the Dry Motor procedure 2 times before an engine start to remove air""")