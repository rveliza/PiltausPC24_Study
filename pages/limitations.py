import streamlit as st

highlight = ":orange-background"


st.title("Limitataions")

#################### AIRPLANE DOCUMENTATION
st.write("## Airplane Documentation")

with st.expander("Documents On Board"):
    st.markdown(f"""
*Hard Copy:*
- AFM Volumes 1 and 2

*Digital or Paper:*
- QRH
- ACE powered by Honewell {highlight}[applicable to the software and hardware configuration of the specific aircraft serial number.]
- FCOM
""")
    
################ AIRPORT LIMITATIONS
st.write("## Airport Limitations")
    
st.write(":blue-background[**Note:**] A wet runway is defined as a runway from which the surface is covered with a layer of water less than 1/8 in. (3 mm) in depth or the equivalent amount of a related substance or by a sufficient level of moisture to give a reflective appearance, but without any significant area of standing water.")

with st.expander("Approved takeoff and landing surface"):
    has_gravel_kit = st.checkbox("Gravel Kit Factiory option installed")

    surface_text = f"""
    - Dry and wet paved runways
    - Contaminated paved runways {highlight}[in accordance with AFM Supplement 02442 'Contaminated Runway Operation']
    """

    if has_gravel_kit:
        surface_text += f"""
    - Dry and wet prepared dirt-sand-gravel runways (or any combination of it) {highlight}[in accordance with AFM Supplement 02444 'Dirt-Sand-Gravel Runway Operation']
    - Dry and wet prepared grass runways {highlight}[in accordance with AFM Supplement 02472 'Grass Runway Operation']
    """
    st.markdown(surface_text)

with st.expander("Minimum Pressure Altitude"):
    st.write("-1,000 ft MSL")

with st.expander("Maximum Pressure Altitude Landing Field Elevation"):
    st.write("10,000 ft MSL")

with st.expander("Maximum runway slope"):
    st.write("+/- 2%")

with st.expander("Maximum tailwind component for takeoff and landing"):
    st.write("10 kt")



################ ACE

st.write("## Advanced Cockpit Environment (ACE)")

st.write(":blue-background[**Note:**] The us of 'PITCH ATTITUDE HOLD' mode recommended during operation in severe turbulence.")

st.write("## Automatic Flight Control System")
st.write("#### General")

with st.expander("During autopilot operation, an approprately qualified pilot must be seated in a pilot position with ______ ______ _______."):
    st.write("seat belt fastened")

with st.expander("Do not override the ________ or ___ _______"):
    st.write("autopilot / yaw damper")

with st.expander("Do not engange the autopilot while the ________ _________ _______ is active"):
    st.write("tactile feedback system")

with st.expander("The pilot side quick disconnect button must be ______ before departure"):
    st.write("operable")

with st.expander("Flight operation above 30,000 ft MSL with the yaw damper disengaged is:"):
    st.write("prohibited")
    
st.write("#### Take Off")
with st.expander("Minimum engagement height of the autopilot after take-off is:"):
    st.write("400 feet AGL")