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

st.write("#### Automatic Flight Control System")
st.write("###### General")

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
    
st.write("###### Take Off")
with st.expander("Minimum engagement height of the autopilot after take-off is:"):
    st.write("400 feet AGL")


st.write("###### Approach / Landing Minumum Usage Height")

with st.expander("Except during an approach, the autopilot, yaw damper and autothrottle must be disenganged below: "):
    st.write("1,000 ft AGL")

with st.expander("Approach with Vertical Guidance in VGP"):
    st.write("The autopilot, yaw damper and autothrottle must be disengaged below 200 ft AGL")

with st.expander("Coupled ILS Approach"):
    st.write("""
- The autopilot, yaw damper and autothrottle must be disengaged below 200 ft AGL
- Glide slope must be less than 4.5 $\degree$""")
    
with st.expander("Non-Precision Approach, Circling Approach and Visual Approach"):
    st.markdown("""
- Airspeed must be < 150 KIAS
- Vertical speed must be < 1,5000 ft/min
- The autopilot, yaw damper and autothrottle must be disengaged below 400 gt AGL
""")
    
st.write("#### TCAS II")

with st.expander("With one engine inoperative, select ____ only as the TCAS operating mode"):
    st.write("TA")

st.write("#### Weather Radar")
with st.expander("Do not operate the Weather Radar if:"):
    st.markdown("""
- The aircraft is located within a hangar or other enclosure
- The aircraft is being refueled or defueled
- Personell are positioned within the acceptable safe distance and +/- 60 $\degree$ from the aircraft nose
""")
    
st.write("#### INAV Map")
with st.expander("Do not use the INAV map for flight operations if:"):
    st.markdown("""
- The INAV topographical map is the primary source of davigation reference, or
- The display of airspace areas is the sole airspace reference
""")
    
st.write("#### Smart View")
with st.expander("Do not use Smart View for flight operations if:"):
    st.markdown("""
- It is the primary source of navigation reference, or
- It is the primary reference for obstacle clearance
""")
    
st.write("#### Vertical Situation Display")
with st.expander("Do not use the Vertical display as:"):
    st.write("Primary source of navigation")



#################### Airspeed Limitations
st.write("## Airspeed Limitations")
st.write("#### Maximum Operating Speed")
off_on = st.toggle(label="off/on", key="mos")

mos_table_off = """
| Airspeed | KIAS |
| :------: | :--: |
| $V_{mo}$ |      |
| $M_{mo}$ |      |
"""

mos_table_on = """
| Airspeed | KIAS   |
| :------: | :---:   |
| $V_{mo}$ | 290    |
| $M_{mo}$ | .74 M  |
"""

if off_on:
    st.write(mos_table_on)
else:
    st.write(mos_table_off)


st.write("#### Maximum Flap Extended Speed")
st.write("Do not exceed the following speed with the respective flap setting")

off_on = st.toggle("off/on", key="mfes")
flaps_speeds_on_ft = """
| Airspeed | Flap Setting | KIAS |
| :------: | :---------: | :---: | 
| $V_{FE}$ | 8$\degree$ | 200 |
| $V_{FE}$ | 15$\degree$ | 200 |
| $V_{FE}$ | 33$\degree$ | 175 |
"""

flaps_speeds_on_off = """
| Airspeed | Flap Setting | KIAS |
| :------: | :---------: | :---: | 
| $V_{FE}$ | 8$\degree$ |  |
| $V_{FE}$ | 15$\degree$ |  |
| $V_{FE}$ | 33$\degree$ |  |
"""

if off_on:
    st.write(flaps_speeds_on_ft)
else:
    st.write(flaps_speeds_on_off)


st.write("#### Maximum Landing Gear Speed")


off_on = st.toggle("off/on", key="mlges")

mlges_on = """
| Airspeed | KIAS | SIGNIFICANCE |
| :----:  | :----:| :------: |
| $V_{LE}$ | The lower of: 250 or 0.74 M| Do not exceed this speed with the landing gear extended |
| $V_{LO}$ (EXTEND) | The lower of: 250 or 0.74 M| Do not extend the landing gear above this speed. |
| $V_{LO}$ (RETRACT) | 200| Do not retract the landing gear above this speed |
| $V_{LO}$ (EXTEND-EGES)| 180 | Do not extend the emergency landing gear above this |
"""

mlges_off = """
| Airspeed | KIAS | SIGNIFICANCE |
| :----:  | :----:| :------: |
| $V_{LE}$ | | Do not exceed this speed with the landing gear extended |
| $V_{LO}$ (EXTEND) |  | Do not extend the landing gear above this speed. |
| $V_{LO}$ (RETRACT) | | Do not retract the landing gear above this speed |
| $V_{LO}$ (EXTEND-EGES)|  | Do not extend the emergency landing gear above this |
"""

############### Baggage Cargo

if off_on:
    st.write(mlges_on)
else:
    st.write(mlges_off)

st.write("## Baggage / Cargo Area")
lbs_kgs = st.radio(
    "Units",
    ["lb", "kg"],
    index=0,
    label_visibility="collapsed",
    key="baggage_cargo"
)

weight = 0

if lbs_kgs == "lb":
    weight = 66
else:
    weight = 30

with st.expander(f"Baggage is any item that has a mass $\leq$ ___ {lbs_kgs}.  All baggage must be stowed in the restraing system (baggage net)"):
    st.write(weight)

with st.expander(f"Cargo is any item that has a mass > ____ {lbs_kgs}.  All cargo must be tied down to the seat rails and must be secured individually with an approved cargo tie down"):
    st.write(weight)

with st.expander("Do not open / close the cargo door, or perform cargo loading operations in crosswinds exceeding ____ kt"):
    st.write("60")

st.write("#### Baggage Limitations")

in_or_mm = st.radio(
    "Units",
    ["in", "mm"],
    key="baggage_limitation",
    index=1,
    label_visibility="collapsed"
)

off_on = st.toggle("off/on", key="baggs_limits")

larg_bag_fwd = ""
small_bag_fwd = ""
cargo_fwd = ""

if in_or_mm == 'in' and off_on:
    larg_bag_fwd = 9.1
    small_bag_fwd = 7.5
    cargo_fwd = 4
elif in_or_mm == 'mm' and off_on:
    larg_bag_fwd = 250
    small_bag_fwd = 190
    cargo_fwd = 100

baggage_limitations_table_on = f"""
| Location | Distance ({in_or_mm}) |
| :------: | :------: |
| Forward of the large baggage restraint system | {larg_bag_fwd} |
| Forward of the small baggage restraint system | {small_bag_fwd} |
| In front of the cargo in the cabin | {cargo_fwd} |
"""

st.write(baggage_limitations_table_on)


st.write("#### Cargo Limitations")
weight = ""

col1, col2 = st.columns(2)
weight = ""


with col1:
    msn = st.radio("MSN", ['101 - 500', '501 - UP'], index=1)
with col2:
    lbs_kgs = st.radio("Units", ["lb", "kg"])

if msn == '101 - 500' and lbs_kgs == 'lb':
    weight = "2,500"

elif msn == '101 - 500' and lbs_kgs == 'kg':
    weight = "1,134"

elif msn == '501 - UP' and lbs_kgs == 'lb':
    weight = "2,940"

else:
    weight = "1,334"


with st.expander("Maximum Freight Load is: "):
    st.write(f"{weight} {lbs_kgs}")


################## Brakes and Tires
st.write("## Brakes and Tires")

st.write("#### Brakes")
with st.expander("To allow adequate cooling of the wheels and brakes the aircraft must remain on the ground for at leat 120 min following these two events"):
    st.markdown("""
* Rejected takeoff with brake on speed greater than $V_R$ -20 kt and heavy brake usage
* 0$\degree$ flap full stop landing and heavy brake usage
""")
    
st.write("#### Tires")
with st.expander("The maximum permissible tire speed is:"):
    st.write("165 kt")

with st.expander("The nose tire must be a _______ _________ tire"):
    st.write("Dual Chine")


############# Cabin Pressurization
st.write("## Cabin Pressurization")

st.write("""
| Description | psid |
| :--------:  | :------: |
| Maximum cabin positive pressure differential | 9.29 |
| Maximum cabin negative pressure differential | -0.3 |
| Maximum pressure differential for takeoff and landing | 0.7 |

""")

