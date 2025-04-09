import streamlit as st

highlight = ":orange-background"
note = ":blue-background[**NOTE**]"
warning = ":red-background[**WARNING**]"
caution = ":orange-background[**CAUTION**]"

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

if off_on:
    st.write(mlges_on)
else:
    st.write(mlges_off)



############### Baggage Cargo
st.write("---------------")
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

msn = st.radio("MSN", ['101 - 500', '501 - UP'], index=1, horizontal=True)


with st.expander("Maximum Freight Load is: "):
    lbs_kgs = st.radio("Units", ["lb", "kg"], horizontal=True, label_visibility="collapsed")

    if msn == '101 - 500' and lbs_kgs == 'lb':
        weight = "2,500"

    elif msn == '101 - 500' and lbs_kgs == 'kg':
        weight = "1,134"

    elif msn == '501 - UP' and lbs_kgs == 'lb':
        weight = "2,940"

    else:
        weight = "1,334"

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

with st.expander("The inflation of the de-icing boots is not recommended when TAT < ______, unless it is required due to the presence of icing conditions."):
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


############ Kinds of Operation
st.write("## Kinds of Operation")

with st.expander("The PC-24 is certified in the Commuter Category and is approved for the following types of operation when the required equipment is installed and operational:"):
    st.write("""
- VFR Day
- VFR Night
- IFR Day including automatic approaches to CAT 1 weather minimums, single pilot
- IFR Night including automatic approaches to CAT 1 weather minimums, single pilot
- Flight Into Known Icing conditions
""")
    
with st.expander ("An approprately authorized and approved ______ may be used to operate the aircraft with inoperative equipment"):
    st.write("MMEL")


############# Landing Gear
st.write("## Landing Gear")

gear_temp = ""
with st.expander("Do not operate the landing gear if the temperature is less than _______"):
    temp_units = st.radio("Units", ['Fahrenheit', 'Celsius'], horizontal=True, label_visibility="collapsed", key="gear_temp", index=1)
    if temp_units == 'Fahrenheit':
        gear_temp = "-85$\degree$F"

    else:
        gear_temp = "-65$\degree$C"

    st.write(f"{gear_temp}")

st.write("#### Towing Limitations")
towing_max_w = ""

with st.expander("The weight of a towbar-less tug must not exceed____"):
    tow_weight = st.radio("Units", ['Pounds', 'Kilograms'], horizontal=True,        key="tow_limits", label_visibility="collapsed")
    if tow_weight == 'Pounds':
        towing_max_w = "5,379 lb"
    else:
        towing_max_w = "2,440 kg"
    st.write(f"{towing_max_w}")


############## Loading Limitations
st.write("## Loading Limitations")
st.write("#### Weight Limitations")

max_ramp_w = ""
max_takoff_w = ""
max_land_w = ""
max_zf_w = ""
max_cargo_w = ""
large_net = ""
small_net = ""
max_floor_load_seat_rails = ""
max_floor_load_panels = ""

col1, col2 = st.columns(2)

with col1:
    msn = st.radio("MSN", ["101 - 500", "501 - UP"], horizontal=True, key="weight_limits", index = 1)
with col2:
    units = st.radio("Units", ["Pounds", "Kilograms"], horizontal=True, key="weight_limits_units", label_visibility="collapsed")

off_on = st.toggle("off/on", key="weight_limits_table")

if msn == "101 - 500" and units == 'Kilograms' and off_on:
    max_ramp_w = "8,345"
    max_takoff_w = "8,300"
    max_land_w = "7,665"
    max_zf_w = "6,450"
    max_cargo_w = "1,134"

if msn == "501 - UP" and units == "Kilograms" and off_on:
    max_ramp_w = "8,545"
    max_takoff_w = "8,500"
    max_land_w = "7,865"
    max_zf_w = "6,650"
    max_cargo_w = "1,334"

if msn == "101 - 500" and units == "Pounds" and off_on:
    max_ramp_w = "18,400"
    max_takoff_w = "18,300"
    max_land_w = "16,900"
    max_zf_w = "14,220"
    max_cargo_w = "2,500"

if msn == "501 - UP" and units == "Pounds" and off_on:
    max_ramp_w = "18,840"
    max_takoff_w = "18,740"
    max_land_w = "17,340"
    max_zf_w = "14,660"
    max_cargo_w = "2,940"

if units == 'Kilograms' and off_on:
    large_net = "240"
    small_net = "180"
    max_floor_load_seat_rails = "1,000 kg/m"
    max_floor_load_panels = "500 $kg/m^2$"

if units == 'Pounds' and off_on:
    large_net = "530"
    small_net = "400"
    max_floor_load_seat_rails = "670 lb/ft"
    max_floor_load_panels = "100 $lb/ft^2$"

st.write(f"""
| Description | Weight in {units}|
| :-: | :-: |
| Maximum Ramp Weight | {max_ramp_w} |
| Maximum Takeoff Weight | {max_takoff_w} |
| Maximum Landing Weight | {max_land_w} |
| Maximum Zero Fuel Weight | {max_zf_w} |
| Maximum Cargo Weight | {max_cargo_w} |
| Maximum Baggage Weight (large restraint net) | {large_net} |
| Maximum Baggage Weight (small restraint net) | {small_net} |
| Maximum Floor Loading (on seat rails) | {max_floor_load_seat_rails} |
| Maximum Floor Loading (over floor panels) | {max_floor_load_panels} |
         
""")

st.write("#### Center of Gravity Limitations")

max_r_w_cg_fwd = ""
max_r_w_cg_aft = ""
max_takeoff_w_cg_fwd = ""
max_takeoff_w_cg_aft = ""



units = st.radio("Units", ["Pounds", "Kilograms"], horizontal=True, key="cg_limits_units", label_visibility="collapsed")

off_on = st.toggle("off/on", key="cg_limits_table")
max_r_w_cg_fwd = ""
max_r_w_cg_aft = ""
max_takoff_w_cg_fwd = ""
max_takoff_w_cg_aft = ""
weight_1 = ""
weight_1_cg = ""
weight_2 = ""
weight_2_cg =""
weight_3 = ""
weight_3_cg = ""
weight_4 = ""
weight_4_cg = ""

if units == "Kilograms":
    weight_1 = "6,150"
    weight_2 = "5,850"
    weight_3 = "5,221"
    weight_4 = "4,988"
else:
    weight_1 = "13,560"
    weight_2 = "12,895"
    weight_3 = "11,510"
    weight_4 = "10,995"

if off_on:
    max_r_w_cg_fwd = "25.0"
    max_r_w_cg_aft = "40.0"
    max_takeoff_w_cg_fwd = "25.0"
    max_takeoff_w_cg_aft = "39.8"
    weight_1_cg = "47.6"
    weight_2_cg = "25.0"
    weight_3_cg = "37.0"
    weight_4_cg = "47.6"



st.write(f"""
| Weight in {units} | Forward Limit AOD: % MAC | Aft Limit AOD: % MAC |
| :-: | :-: | :-: |
| Maximum Ramp Weight | {max_r_w_cg_fwd} | {max_r_w_cg_aft} |
| Maximum Takeoff Weight | {max_takeoff_w_cg_fwd} | {max_takeoff_w_cg_aft} |
| {weight_1} | | {weight_1_cg} |
| {weight_2} | {weight_2_cg} | |
| {weight_3} | {weight_3_cg} | |
| {weight_4} | | {weight_4_cg} |
         
""")

st.write("#### Flight Maneuver Load Factor Limits")
with st.expander("Operation is limited to any manouvre incident to normal flying, stalls (except whip stalls) and steep turns in which the angle of bank is not more than:"):
    st.write("60$\degree$")

up_limits = ""
down_limits = ""

off_on = st.toggle("off/on", key="man_limits")

if off_on:
    up_limits = "+3.0 g, -1.2 g"
    down_limits = "+2.0 g, 0.0 g"

st.write(f"""
| Flap Position | Load Limitations |
| :-: | :-: |
| Up | {up_limits} |
| Down | {down_limits} |
""")


st.write("#### Passenger Seating")
with st.expander ("Maximum number of occupants"):
    st.write("""
- **Executive Interior**    
    - 8 passenger (one per seat) in the cabin    
    - An optional fit allows two additional infants to be carried at the ferst seating row on the left and right sides
- **Commuter interior**    
    - 10 passenger (one per seat) in the cabin
""")
    

st.write("## Oil")
st.write("#### Oil Quatity Limitations")

off_on = st.toggle("off/on", key="oil_limits")
oil_tank_total_volume = ""
oil_tank_fill_volume = ""
oil_tank_useable = ""

if off_on:
    oil_tank_total_volume = "5.85"
    oil_tank_fill_volume = "5.65"
    oil_tank_useable = "4.32"

st.write(f"""
| Quantity Description | Quantity (qt) |
| :-: | :-: |
| Oil Tank Total Volume | {oil_tank_total_volume} |
| Oil Tank Fill Volume | {oil_tank_fill_volume} |
| Oil Tank Usable Volume | {oil_tank_useable} |
""")

with st.expander("Oil level must not be below the _____ indicator mark on the oil tank sight glass prior to flight"):
    st.write("ADD")

with st.expander("The maximum permissible oil consumption rate is: "):
    oil_qty = ""
    oil_level_ind = st.radio("Units", ["Gallons", "Quarts"], label_visibility="collapsed", horizontal=True, index=1)
    if oil_level_ind == "Gallons":
        oil_qty = "0.032 gal/hr"
    else:
        oil_qty = "0.128 qt/hr"

    st.write(f"{oil_qty}")


##################### Operating Altitude
st.write("## Operating Altitude")
with st.expander("The maximum operating altitude is: "):
    altitude = ""
    altitude_units = st.radio("Units", ['Feet', 'Meters'], label_visibility="collapsed", horizontal=True, key="altitude_oper")
    if altitude_units == "Feet":
        altitude = "45,000 ft"
    else:
        altitude = "14,716 m"
    st.write(f"{altitude}")


################# Outside Air Temperature
st.write("## Outside Air Temperature")

oat = ""

oat_temp_units = st.radio("Units", ["Celsius", "Fahrenheit"], horizontal=True, label_visibility="collapsed")
off_on = st.toggle("off/on", key="oat_temps")

min_oat = ""
max_oat = ""


if oat_temp_units == "Celsius" and off_on:
    min_oat = "-54$\degree$C"    
    max_oat = "+50$\degree$C"

if oat_temp_units == "Fahrenheit" and off_on:
    min_oat = "-65$\degree$F"
    max_oat = "122$\degree$F"

oat_text = f"""
    | Description | Limit |
    | :-: | :-: |
    | Minimum OAT (Sea Level) | {min_oat} |
    | Maximum OAT (Sea Level) | {max_oat} |
"""

st.write(oat_text)

###################### Oxygen System
st.write("## Oxygen System")
st.write("#### General")

with st.expander("Minimum oxygen for dispatch is: "):
    st.write("680 liters")

with st.expander("Do not use the oxygen saver function below: "):
    st.write("25,000 feet")

with st.expander("Passenger oxygen masks are limited to a maximum cabin altitude of:"):
    st.write("40,000 feet")

with st.expander("If installed, do not operate the PBE when the cockipt tempertaure is $\le$:"):
    pbe_temp_radio = st.radio("PBE Temp", ["Celsius", "Fahrenheit"], key="pbe_temp", horizontal=True, label_visibility="collapsed")

    pbe_temp = "-29$\degree$C"

    if pbe_temp_radio == "Fahrenheit":
        pbe_temp = "-20$\degree$F"

    st.write(pbe_temp)

with st.expander("For pressurized flight above ____________, a minimum oxygen supply of _______ duration for flight crew and passengers is required"):
    st.write("25,000 ft MSL / 10 min")


with st.expander("After ground cold soak, do not operate the Crew Oxygen Masks press to test / reset button when the cockpit temperature is $\le$:"):
    temp = st.radio("Temperature", ["Ceslius", "Fahrenheit"], key="soak_temp", horizontal=True, label_visibility="collapsed")
    soak_temp = "-12$\degree$C"
    if temp == "Fahrenheit":
        soak_temp = "-10$\degree$F"

    st.write(soak_temp)


st.write("#### High Field Mode")
with st.expander("For single pilot operations, the pilot is required to use oxygen when the ______________ is active"):
    st.write("High Field Mode")

with st.expander("For multi pilot operations, at least one pilot is required to use oxygen when the ______________ is active"):
    st.write("High Field Mode")



########################## Powerplant
st.write("## Powerplant")

st.write("#### Engine Operating Limitations")

with st.expander(f"{caution}", expanded=True, icon="⚠️"):
    st.write("When te tailwind component is greater than 10kt, do not exceed 60% N1 engine speed until the aircraft rolling speed is greater than the tailwind component.")


with st.expander("Except in an emergency, selection of engine thrust settings greater than NTO is: "):
    st.write("Prohibited")


engine_op_limits = """
| Operating Condition | Thrust (lb) | N1 (%) | n2 (%) | ITT ($\degree$C) | Oil PRESS (psi) | Oil TEMP ($\degree$C) |
| :-: | :-: | :-: | :-: | :-: | :-: | :-: |
| Normal Takeoff (1)  | 3,420 | 104.7 | 100.8 | 855 | 40 - 120 (4) | 10 - 135 |
| ATR (2) | 3,600 | 104.7 | 100.8 | 855 | 40 - 120 (4)| 10 - 135 |
| Maximum Cont / Climb (3) |  | 104.7 | 100.8 | 855 | 40 - 120 (4) | 10 - 135 |
| Ground or Flight Idle (Cont) |  |  |  |  | 30 Min (4), 120 Max (5)| -40 - 135 |
| QPM |  |  | 45.4 |  | 30 - 120 | 10 - 135 |
| Starting |  |  |  | See Fig.  2-1-4 |  | -40 - 135 |
| Transient High |  | 105.7 (2 Min) | 101.5 (2 Min) | 855 (0 sec) | 130 (6 and 7) | 149 (5) |
| Transient Low |  |  |  |  | 23  (5)|  |
"""

engine_op_limits_off = """
| Operating Condition | Thrust (lb) | N1 (%) | n2 (%) | ITT ($\degree$C) | Oil PRESS (psi) | Oil TEMP ($\degree$C) |
| :-: | :-: | :-: | :-: | :-: | :-: | :-: |
| Normal Takeoff |  |  |  |  |  |  |
| ATR |  |  |  |  |  |  |
| Maximum Cont / Climb |  |  |  |  |  |  |
| Ground or Flight Idle (Cont) |  |  |  |  |  |  |
| QPM |  |  |  |  |  |  |
| Starting |  |  |  |  |  |  |
| Transient High |  |  |  |  |  |  |
| Transient Low |  |  |  |  |  |  |

"""

off_on = st.toggle("off/on", key="eng_limits_toggle")

if off_on:
    st.markdown(engine_op_limits)
else:
    st.write(engine_op_limits_off)

with st.expander("""Footnotes:""", expanded=True):
    st.write("""
(1) Maximum 5 min.    
(2) Maximum 10 min (with OEI, otherwise 5 min).    
(3) Maximum Continuous and maximum climb thrust is obtained when the Thrust Lever Angle
(TLA) is in the Max Continuous / Climb thrust position. Cruise thrust is obtained when the
TLA is in the MCT position. Continuous operation is acceptable provided engine limits are not
exceeded.    
(4) Minimum oil pressure is 40 psig when operating at or above 80% N2; 30 psig when
operating below 80% N2.    
(5) When operating below 80% N2 for up to 5 min.    
(6) When operating above 80% N2 for up to 5 min.    
(7) Maximum allowable oil pressure is 130 psig for 5 min maximum.    
(8) Elevated oil pressure values are typically observed when oil temperature is cold.   
    """)

st.write("#### Engine Starting Limitations")
st.write("###### Wind and Time Limitations")

with st.expander(f"{caution}", expanded=True, icon="⚠️"):
    st.write("For engint starting, point the nose of the aircraft into the wind.  If this is not possible, adhere to the engine start wind limits imntioned below...")

start_limits_table = """
| Condition | Limits | 
| :-: | :-: | 
| Maximum tailwind component for engine start | 20 kt (estimated steady wind conditions  |
| Maximum crosswind component for engine start | 25 kt tower wind |
| Maximum time to Light-Off for engine start (1) | 12 sec (2) |
| Minimum oil temperature for battery engine start | -40$\degree$C (3 and 4) |
| Before left engine start | Main passenger door and cargo door must be clsoed and secured |
"""

start_limits_table_off = """
| Condition | Limits | 
| :-: | :-: | 
| Maximum tailwind component for engine start |  |
| Maximum crosswind component for engine start |  |
| Maximum time to Light-Off for engine start (1) |  |
| Minimum oil temperature for battery engine start |  |
| Before left engine start |  |
"""

off_on = st.toggle("off/on", key="eng_limits_start_table")

if off_on:
    st.write(start_limits_table)
else:
    st.write(start_limits_table_off)

with st.expander("""Footnotes:""", expanded=True):
    st.write("""
(1) Higher minimum throttle up speeds up to 60% N1 may be required if tailwind component    
exceeds 10 kt.    
(2) Time to light-off is defined as the time after signal to the igniter is indicated and increase in ITT is seen.    
(3) For ground start only. For In Flight starter assisted and windmill starts, refer to AFM Section 3 Non-annunciated Procedures.    
(4) For limitations of “Minimum Ni-Cd / Li-Ion battery temperature for battery engine start”,
refer to Battery Limitations.
    """)

st.write("#### Quiet Power Mode")
with st.expander("Do not operate the _____ during QPM operation"):
    st.write("NAI")

st.write("QPM operation is permitted only if all the requirements listed below are fullfilled:")

visible_moisture = True
idle_time = st.checkbox("Aircraft at Ground idle N2 (stabilized operation) for at least 2 minutes")
brake_on = st.checkbox("Aircraft is stationary with Park Brake ON")
ground_ice = st.checkbox("Ground icing conditions are NOT present")
temp = st.radio("Temperature", ["Above 10$\degree$C", "Below 10$\degree$C"], horizontal=True, label_visibility="visible", key="temp_qpm")
if  temp == "Below 10$\degree$C":
    moisture = st.checkbox("Visible moisture not present")
    if moisture:
        visible_moisture = True
    else:
        visible_moisture = False

crew_seated = st.checkbox("A flight crew memeber is seated at the controls with a lap belt fastened")
xwind = st.checkbox("Crosswind / tailwind are less than 20 kt (Average)")
r_engine = st.checkbox("Only the right engine is to be operated in QPM")

st.write(f"Idle Time: {idle_time}, Brake On {brake_on}, Temperauter: {temp}, Visible Moisture: {visible_moisture}, Crew Seated: {crew_seated}, Xwind: {xwind}, R Engine: {r_engine}")
if idle_time and brake_on  and visible_moisture and crew_seated and xwind and r_engine:
    st.success("CLEAR TO ACTIVATE QPM")
else:
    st.warning("DO NOT ACTIVATE QPM")
