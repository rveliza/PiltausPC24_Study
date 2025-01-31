import streamlit as st

highlight = ":orange-background"
note = ":blue-background[**NOTE**]"
warning = ":red-background[**WARNING**]"

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

with st.expander(f"{note}", expanded=True, icon="📝"):
    st.write("A wet runway is defined as a runway from which the surface is covered with a layer of water less than 1/8 in. (3 mm) in depth or the equivalent amount of a related substance or by a sufficient level of moisture to give a reflective appearance, but without any significant area of standing water.")

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
st.write("---------------")
st.write("## Advanced Cockpit Environment (ACE)")

with st.expander(f"{note}", expanded=True, icon="📝"):
    st.write("The use of 'PITCH ATTITUDE HOLD' mode is recommended during operation in severe turbulence.")

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
st.write("---------------")
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
st.write("---------------")
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
    key="baggage_cargo",
    horizontal=True
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
    label_visibility="collapsed",
    horizontal=True
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
st.write("---------------")
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
st.write("---------------")
st.write("## Cabin Pressurization")

off_on = st.toggle("off/on", key="cab_press")

max_pos_dif = ""
max_neg_dif = ""
max_press_dif = ""

if off_on:
    max_pos_dif = "9.27"
    max_neg_dif = "-0.3"
    max_press_dif = "0.7"

st.write(f"""
| Description | psid |
| :--------:  | :------: |
| Maximum cabin positive pressure differential | {max_pos_dif} |
| Maximum cabin negative pressure differential | {max_neg_dif} |
| Maximum pressure differential for takeoff and landing | {max_press_dif} |

""")


################## Door and Emergency Exit
st.write("---------------")
st.write("## Door and Emergency Exit")
st.write("#### Forward Airstar Limitation")
with st.expander("Do not allow more than ____ person on the forward airstair at any given time"):
    st.write("one")

st.write("#### Emergency Exit Security Pins")
with st.expander("Each internal emergency exit overnight security pin, if installed, must be _______ and _______ before flight"):
    st.write("removed / stowed")


#### Electrical System
st.write("---------------")
st.write("## Electrical System")
st.write("#### Generator Limitations")
off_on = st.toggle("off/on", key="gen_limits")

qpm_amps = ""
gnd_flight_amps = ""
max_voltage = ""

if off_on:
    qpm_amps = "250 A"
    gnd_flight_amps = "400 A"
    max_voltage = "29.5 Vdc"



st.write(f"""
| Description | Limitation |
| :-: | :-: |
| Quiet Power Mode  | {qpm_amps}  |
| Ground idle and above  | {gnd_flight_amps}   |
| Flight  | {gnd_flight_amps}  |
| Maximum Voltage  | {max_voltage} |
""")

st.write("#### Battery Limitations")

with st.expander("The voltage for charging the batteries must not exceed: "):
    st.write("32 V")

batt_type = st.radio("Batteries", ["Ni-Cd", "Li-Ion"], key="battery_type", horizontal=True)

min_bat_temp_flt = ""
min_bat_start = ""
min_bat_temp = ""

off_on = st.toggle("off/on", key="bat_limits")


if batt_type == "Ni-Cd" and off_on:
    min_bat_start = "22.0 V Bat 1 / 23.5 V Bat 2"
    min_bat_temp = "-20$\degree$C"
    min_bat_temp_flt = "0$\degree$"

elif batt_type == "Li-Ion" and off_on:
    min_bat_start = "State Of Charge (SOC) indicators of both batteries are green"
    min_bat_temp = "-5$\degree$C"
    min_bat_temp_flt = "0$\degree$"


battery_table_on = f"""
| Description | Limitation |
| :-: | :-: |
| Minimum battery temperature for flight | {min_bat_temp_flt} |
| Minimum battery volts for start | {min_bat_start} |
| Minimum {batt_type} battery temperature for battery engine starts | {min_bat_temp}  |
"""
st.write(battery_table_on)

st.write("#### Ground Power Unit Limitations")

off_on = st.toggle("off/on", key="gpu_limits")
voltage = ""
load_capacity = ""
min_v_start = ""
min_v_charge = ""
max_volt_charge = ""
min_oat_gpu_start = ""

if off_on:
    voltage = "25.0 - 29.5 Vdc"
    load_capacity = "1,200 A Initial State Surge, 450 A Continuous"
    min_v_start = "24.0 Vdc"
    min_v_charge = "20.9 Vdc"
    max_volt_charge = "29.5 Vdc"
    min_oat_gpu_start = "-54$\degree$C"

st.write(f"""
| Description | Limitation |
| :-: | :-: |
| Voltage | {voltage} |
| Load Capacity | {load_capacity } |
| Minimum volts for start | {min_v_start} |
| Minimum voltage to charge batteries | {min_v_charge} |
| Maximum voltage to charge batteries | {max_volt_charge} |
| Minimum OAT for GPU start | {min_oat_gpu_start} |
""")

#################### Flight Crew
st.write("---------------")
st.write("## Flight Crew")
with st.expander("The minimum required flight crew is _____ pilot in the _____ hand seat"):
    st.write("one / left")


################### Fuel System
st.write("---------------")
st.write("## Fuel System")
st.write("#### General")

with st.expander("The electric fuel booster pumps must be:"):
    st.write("operative")

with st.expander("The fuel crossfeed valve must be:"):
    st.write("operative")

with st.expander("The maximum permissible fuel temperature is:"):
    st.write("80$\degree$C")

with st.expander("The minimum permissible fuel temperature is:"):
    st.write("-40$\degree$C")

st.write("#### Fuel Quantity")

fuel_units = st.radio("Units", ["Gallons", "Liters", "Pounds", "Kilograms"], index=2, horizontal=True, label_visibility="collapsed")

total_qty = ""
usable_qty = ""
max_imb = ""
unusable = ""

off_on = st.toggle("off/on", key="fuel_qyt")

if fuel_units == "Gallons" and off_on:
    total_qty = "895"
    usable_qty = "890"
    max_imb = "49"
    unusable = "5.3"

elif fuel_units == "Liters" and off_on:
    total_qty = "3,389"
    usable_qty = "3,369"
    max_imb = "189"
    unusable = "20"

elif fuel_units == "Pounds" and off_on:
    total_qty = "5,999.8"
    usable_qty = "5,964"
    max_imb = "330"
    unusable = "35"

elif fuel_units == "Kilograms" and off_on:
    total_qty = "2,721"
    usable_qty = "2,705"
    max_imb = "150"
    unusable = "16"


st.write(f"""
| Quantity Description | Quantity |
| :-: | :-: |
| Total quantity | {total_qty} |
| Usuable quantity | {usable_qty} |
| Maximum permissible imbalance | {max_imb} |
| Unusuable fuel quantity | {unusable} |
""")

st.write("#### Pressure Refueling Limitations")

with st.expander("The maximum refueling pressure is:"):
    st.write("60 psi")

with st.expander("The maximum defueling suction pressure is:"):
    st.write("10 psi")

with st.expander("Prior to departure the pwer switch (PWR - REFUEL /DEFUEL) must be:"):
    st.write("off")

st.write("---------------")
############## Ice Protection
st.write("## Ice Protection System")
st.write("#### Pneumatic Deice Boots")

with st.expander("The inflation of the de-icing boots is note recommended when TAT < ______, unless it is required due to the presence of icing conditions."):
    st.write("""

-40$\degree$C

:blue-background[Note:] If operated below -40$\degree$C, a visual isnpection of the pneumatic boots must be performed and a system functional test carried out before takeoff.
""")
    
st.write("#### Wing Anti-Ice System")
with st.expander("The WAI is inhibited in these conditions:"):
    st.write("""
* TAT > 15$\degree$C
* Aircraft on ground
""")
    
with st.expander("Do not operate the WAI system with a TAT of more than __  ___, unless required by the presence of icing conditions."):
    st.write("10$\degree$C")

st.write("#### Windshield Heating System")
with st.expander("Do not operate the Windshield Emergency heating on ground or when TAT is > _______"):
    st.write("10$\degree$C")

st.write("#### Wing inspection Light")
with st.expander(f"The wing inspection light must be _________ if flying into known icing conditions at {highlight}[night] or if known acing conditions are forecasted at {highlight}[night]"):
    st.write("operational")

############## ICING Limitations
st.write("___________")
st.write("## Icing Limitations")

with st.expander(f"{warning}", expanded=True, icon="🚨"):
    st.write("**THE PILOT SHALL PERIODICALLY CHECK THE LEFT WING UPPER SURFACE ON A REGULAR BASIS WHILE FLYING IN ICING CONDITIONS TO ENSURE THERE IS NO UNUSUAL ICE ACCUMULATION**")

with st.expander("Do not _________ if there are signs of ice, snow or frost on the lifting surfaces."):
    st.write("takeoff")

with st.expander("If the airplane encounters conditions that are ddetermined to contain _____________ or ___________, the pilot must immediately exit the conditions by changing altitude or course"):
    st.write("freezing rain / freezing drizzle")

with  st.expander("Do not operate into airports reporting __________ or _________"):
    st.write("freezing rain / freezing drizzle")

st.write("#### Extended Holding")
with st.expander ("Extended holding in icing conditions in single bleed source is ____________"):
    st.write("not allowed")

st.write("#### Use of flaps in Icing Conditions")
with st.expander("Do not extend the flaps beyond ______ if in icing conditions"):
    st.write("15$\degree$")

with st.expander("Do not use Flaps ______ for landing in current, active icing conditions"):
    st.write("33")

with st.expander("Do not retract the flaps below _____, if signs of ice are present on the lifting surfaces"):
    st.write("8")

with st.expander("The minimum airspeed with flaps retracted in icing conditions is _________ :"):
    st.write("150 KIAS")

st.write("#### Severe Icing Conditions")

with st.expander("Do not ________ the ________ in severe icing conditions"):
    st.write("engange / autopilot")


st.write("#### Use of SWPS Ice Mode Override")
with st.expander(" Do not opearte thw ________________ push botton / _______________ rotary selector if there are signs of ice on the wings"):
    st.write(" SWPS ICE OVRD / SWPS ICE MODE")


