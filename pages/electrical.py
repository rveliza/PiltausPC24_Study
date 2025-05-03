import streamlit as st

col_settings = [20, 80]
col_settings_wide = [35, 65]

st.title("Electrical")
st.write("#### Batteries")
nicad_lion = st.radio("Batt type", ("NiCad", "Li-ion"), index=0, horizontal=True, label_visibility="collapsed")

batt_volt, batt_amps = ("24V", "44A") if nicad_lion == "NiCad" else ("26.4V", "40A")

st.markdown(f"""
{batt_volt}DC/{batt_amps} {nicad_lion} batteries provide power to the aircraft for a minimum of 60 minutes

* BAT 1:
    * Left Nose Bay
    * Left and Essential Buses
* BAT 2:
    * Rear right wing fairing
    * Right Bus for engine starts
""")

st.write("#### Data Concentration and Processing Units")
st.markdown("""
* Primary Distribution System:
    * DCPU1, DCPU3: Power ditribution monitoring for left bus
        * DCPU 1 is also connected to the essential bus and its power is backed up by the batteries to ensure continued safe flight and landing.
    * DCPU2, DCPU4: Power distribution monitoring for right bus
* Secondary Distribution System:
    * Electronic circtuit breakers
        * Each EPDU contains 41 ECB's
    * Thermal circuit breakers
    * DCPU1 and DCUP2 are connected to all four Electronic Power Distribution Units (EPDU's)
""")



st.write("## Lights and Switches")

col1, col2 = st.columns(col_settings)
with col1:
    st.image("images/bat_1_sw.png")
with col2:
    with st.expander("BAT 1 Switch"):
        st.markdown("""
* BAT 1: Energizes Battery Contactor BC1 to closed
* OFF: De-energizes Battery Contactor BC1 to open 
                    
Bat 1 is in the left nose bay and provides power to the left and essential busses""")
        
col1, col2 = st.columns(col_settings)
with col1:
    st.image("images/bat_2_sw.png")
with col2:
    with st.expander("BAT 2 Switch"):
        st.markdown("""
* BAT 2: Energizes Battery Contactor BC2 to closed
* OFF: De-energizes Battery Contactor BC2 to open
                    
Bat 2 is in the rear right-wing fairing and provides power to the right bus for engine starts
                    
###### Notte: Bat 2 should not be turned on until ready to start the engine, or rapid depletion of the batteries will occur""")
        
col1, col2 = st.columns(col_settings)
with col1:
    st.image("images/gen_1_sw.png")
with col2:
    with st.expander("GEN 1 Switch"):
        st.markdown("""
* GEN 1: Arms associated PCU to operate in START mode or GENERATE mode as subsequently requested
* OFF: Disarms associated PCU - next selection to ON restarts the PCU
                    """)
        
col1, col2 = st.columns(col_settings)
with col1:

    st.image("images/gen_2_sw.png")
with col2:
    with st.expander("GEN 2 Switch"):
        st.markdown("""
* GEN 2: Arms associated PCU to operate in START mode or GENERATE mode as subsequently requested
* OFF: Disarms associated PCU - next selection to ON restarts the PCU
                    """)


off_avail_on = st.radio("off_avail_on", ("OFF", "AVAIL", "ON"), index=0, horizontal=True, label_visibility="collapsed")

gpu_data = {
    "OFF": {"image": "images/gpu_off_btn.png", "title": "GPU OFF", "desc": """GPU is not requested and no expternal power source is available"""},
    "AVAIL": {"image": "images/gpu_avail_btn.png", "title": "GPU AVAIL", "desc": """
    GPU is not requested but an external power source is connected and available.
    * If pressed: Closes GPC and GPU supplies power"""},
    "ON": {"image": "images/gpu_on_btn.png", "title": "GPU ON", "desc": """
    GPU is connected and supplying power to the aircraft\n
    * Pushing the button for 2 seconds opens the GPC and GPU stops supplying power"""},
}

col1, col2 = st.columns(col_settings)
with col1:
    st.image(gpu_data[off_avail_on]["image"])
with col2:
    with st.expander(gpu_data[off_avail_on]["title"], expanded=True):
        st.markdown(gpu_data[off_avail_on].get("desc", ""))


elec_dict = {"2 Generators": {"img": "images/elec_2gen_diag.png", "img2": "images/elec_2gen_diag2.png","title": "Normal Operating Mode - 2 Generators", "desc": "Both generator are operating and supplying their respective busses, and both generators are charging their respective batteries"},
             
             "Pre-Departure": {"img": "images/elec_predeparture_diag.png", "img2": "images/elec_predeparture_diag2.png", "title": "Pre-departure mode", "desc": """
1. Selected by placing BAT 1 to on.
    * Essential Bus is powered
        * BC1 and EC1 close and illuminate green
        * ESS Bus illuminates green and displays volts 
        * "PDC Loads" in left buss annunciator
    * BAT 1 can hold the load for 1 hour,
    """},

             "QPM": {"img": "images/elec_qpm_diag.png", "img2": "images/elec_qpm_diag2.png", "title": "Quiet Power Mode", "desc": """
* Engine operates at a slower than idle rpm
* Electrical loads of up to 250A
* All the services available in pre-departure mode + heating and cooling
* EPDU's shed certain outputs to prevent 250 A exceedance"""},

             "Ground Power": {"img": "images/elec_groundpower_diag.png", "img2": "images/elec_groundpower_diag2.png", "title": "Ground Power Mode", "desc": """
* If connected and any SGC is closed and the parking brake is released an amber GPU CONNECTED is displayed
* If connected batt 1 and batt 2 current shall not be negative (indication of discharging)
* EPDU's provide all emergency, pre-departure and start mode services"""},

             "Pre-Start": {"img": "images/elec_prestart_diag.png", "img2": "images/elec_prestart_diag2.png", "title": "Pre-Start Phase","desc": """
* Setting BAT 2 to ON enters pre-start mode.  Bat 2 has a continuity pathway to both starter/generator contactors."""},

             "Engine Start - Batt Only": {"img": "images/elec_engstart_diag.png", "title": "#2 Engine Start - Battery Only", "desc": """
"""},

             "Second Engine Pre-Start": {"img": "images/elec_second_eng_ps_diag.png", "title": "Single Generator - Second Engine Pre-Start", "desc": """
"""},
            "Cross Generator Start": {"img": "images/elec_crossgen_diag.png", "title": "Cross Generator Start", "desc": """
* PCU shifts the SGU on the operative engine into GEnerate mode after first engine has started.  Electrical system enters single generator configuration.
* Second engine start is a cross-generator start.
* After second engine start, PCHU shifts the second SGU into Generator mode and electrical system switches to the normal operation configuration"""},

            "GPU Start": {"img": "images/elec_gpustart_diag.png", "title": "GPU Start", "desc": """
* GPU current is used during the first engine start only.
* After start, PCU shifts the operating SGU to Generate mode and the electrical system switches into a single generator configuration.  
    * If GPU remains connected, it is held out of the system to avoid multiple power sources to the buses"""},

            "Single Gen, after GPU Start": {"img": "images/elec_aftergpu_diag.png", "img2": "images/elec_aftergpu_diag2.png", "title": "Single Generator after GPU start", "desc": """
* GPU remains held out of the elctrical system by the operating generator
* The electrical configuration for the start is a cross-generator start."""},

            "Single Gen, Left OFF / Fail": {"img": "images/elec_left_fail_diag.png", "img2": "images/elec_left_fail_diag2.png", "title": "Single Generator Mode - Flight", "desc": """
* When only a single generator is availabe the logic closes XC ! to connect the operative side to the inoperative side of the system
* Automatic shedding occurs."""},

            "Single Gen, Right OFF / Fail": {"img": "images/elec_right_fail_diag.png", "img2": "images/elec_right_fail_diag2.png", "title": "Single Generator - Right OFF / Fail", "desc": ""},

            "Dual Generator Failure": {"img": "images/elec_dual_gen_fail.png", "img2": "images/elec_dual_gen_fail2.png", "title": "Dual Generator Failure", "desc": """
* Automatic shedding occurs
* XC 1 is directed to close any time at least one generator is off line
    * Ensures that an electrical pathway exists between BAT 2 and SGU 1 so that a starter-assisted in-flight relight amy be attempeted.
* BTC 1 and BTC 2 are both opened
    * isolates the essential bus from the left bus and simultaneously opens BC 1 to disconenct BAT 1 from the left bus.  BAT 1 and BAT 2 supply only essential services via the essential bus"""},

            "Emergency Flap Mode": {"img": "images/elec_emerg_flap_diag.png", "title": "FLAPS PWR pushbutton switch", "desc": """
* When both generators fail only the essential bus is powered for landing, so the flaps (operated by the right bus) are not available.
* Allows selection of battery power to the right bus to enable the flaps by closing BTC 2, via EPDU 2 and EPDU 4
* Flaps Emer PWR pushbotton should only be operated prior to landing to prevent draining of the BAT 2.  """},

            "Right Bus Isolated / Feeder Fault": {"img": "images/elec_right_bus_isol_diag.png", "title": "Right Bus Isolated - Feeder Fault", "desc": """
* When right bus becomes isolated from all sources of electrical power, electrical loads supplied by EPDU 2 and EPDU 4 are unpowered.
    * Automatically if feeder fault protection for the right bus is activated
    * Procedural step in AFM when the Fire, Smoke or Fumes in Cockpit / Cabin procedure is performed."""},

            "Right Bus Isolation Procedure": {"img": "images/elec_right_bus_isol2_diag.png", "title": "Right Bus Isolation Procedure", "desc": """
1. Pilot selects GEN 2 OFF on the overhead panel to cause single generator mode -> Shedding of high amperage electrical systems and services
    * Causes XC 1 to close, connecting GEN 1 to the right bus
2. Pilot pushes Bus tie switch to open XC 1
    * Disables automatic bus tie operation creating a full electrical isolation"""},
               "Left and Essential Bus Isolation": {"img": "images/elec_left_essential_isol_diag.png", "title": "Left and Essential Bus Isolation", "desc": """
1. When left bus is isolated due to a procedural step in the AFM, the pilot first re-energizes the right bus by selecting GEN 2 back
2. After equipment re-initialization (aprox 1 minute), GEN 1 is selected OFF to isolate the left bus.  
3. BAT 1 is switched to OFF to isolate the essential bus which was powered by BAT 1"""},
            "Left Bus Fail Mode or Left Feeder Fault": {"img": "images/elec_left_feeder_diag.png", "title": "Left Bus Fail Mode or Left Feeder Fault", "desc": """
* Because the left and essential bus remain powered by BAT 1 only, BAT 1 will discharge quickly if not protected by accomplishing the **** L Bus Fail **** procedure to ensure isolation of BAT 1"""}
}

################ Normal Operatiing Mode #######################      
st.write("## Normal Operation")

elec_op_mode = st.radio("Operating Mode", ["2 Generators", "Pre-Departure"], horizontal=True, label_visibility="collapsed")

alt_img_avail = True
alternate_image = False

if alt_img_avail:
    alternate_image = st.toggle("Synoptic", key="normal_mode")

col1, col2 = st.columns(col_settings_wide)
with col1:
    alt_img_avail = elec_dict[elec_op_mode].get(f"img{2}", False)
    # st.write(alt_img_avail)
    if alt_img_avail and alternate_image:
        st.image(alt_img_avail)
    else:
        st.image(elec_dict[elec_op_mode]["img"])

with col2:
    with st.expander(elec_dict[elec_op_mode]["title"], expanded=True):
        st.write(elec_dict[elec_op_mode]["desc"])   


################# Alternate Normal Operation #######################
st.write("## Alternate Normal Operation")

elec_op_mode = st.radio("Operating Mode", ["QPM", "Ground Power"], horizontal=True, label_visibility="collapsed")

alt_img_avail = True
alternate_image = False

if alt_img_avail:
    alternate_image = st.toggle("Synoptic", key="alternate_mode")


col1, col2 = st.columns(col_settings_wide)
with col1:
    alt_img_avail = elec_dict[elec_op_mode].get(f"img{2}", False)
    if alt_img_avail and alternate_image:
        st.image(alt_img_avail)
    else:
        st.image(elec_dict[elec_op_mode]["img"])
with col2:
    with st.expander(elec_dict[elec_op_mode]["title"], expanded=True):
        st.write(elec_dict[elec_op_mode]["desc"])   

st.write("#### Refueling/Defueling Mode")
st.markdown("""
* Airplane may be refueled without energizing the entire electrical system
* Refueling panel.  When selected to ON, BAT 1 and BAT 2 are connected to supply terminals for all refueling/defueling required equipment.
""")

 
########################### Engine Starting Modes #########################
st.write("## Engine Starting")

st.markdown("""
* Turning BAT 2 ON enters Pre-Start Mode
    * Bat 1 depetes rapidly if GPU not connected (less than 30 minutes)
* During start
    * BAT 1 supplies all pre-departure mode services  additional required for engine start.
    * Bat 2 provides power for engine start.
    * Bat 2 and any other available power source (GPU, SGU) are connected to the SGU to operate the starter
* Three categories for engine start (electrical point of view")
    * Battery only start - On ground and in flight
    * Cross-generator start - On ground and in flight
    * GPU start - Ground only
* Each engine start consist of 3 phaeses:
    * Pre-start phase
    * Starting (SGU enganged) phase
    * Post-start phase.
"""
)

elec_op_mode = st.radio("Operating Mode", ["Pre-Start", "Engine Start - Batt Only", "Second Engine Pre-Start", "Cross Generator Start", "GPU Start", "Single Gen, after GPU Start"], horizontal=True, label_visibility="collapsed")

alt_img_avail = True
alternate_image = False

if alt_img_avail:
    alternate_image = st.toggle("Synoptic", key="starting_mode")

col1, col2 = st.columns(col_settings_wide)
with col1:
    alt_img_avail = elec_dict[elec_op_mode].get(f"img{2}", False)
    if alt_img_avail and alternate_image:
        st.image(alt_img_avail)
    else:
        st.image(elec_dict[elec_op_mode]["img"])

with col2:
    with st.expander(elec_dict[elec_op_mode]["title"], expanded=True):
        st.write(elec_dict[elec_op_mode]["desc"])   



########################### Abnormal / Emergency Operating Modes #########################
st.write("## Abnormal")


elec_op_mode = st.radio("Operating Mode", ["Single Gen, Left OFF / Fail", "Single Gen, Right OFF / Fail", "Dual Generator Failure", "Emergency Flap Mode", "Right Bus Isolated / Feeder Fault", "Right Bus Isolation Procedure", "Left and Essential Bus Isolation", "Left Bus Fail Mode or Left Feeder Fault"], horizontal=True)


alt_img_avail = True
alternate_image = False

if alt_img_avail:
    alternate_image = st.toggle("Synoptic", key="abnormal_mode")

col1, col2 = st.columns(col_settings_wide)
with col1:
    alt_img_avail = elec_dict[elec_op_mode].get(f"img{2}", False)
    if alt_img_avail and alternate_image:
        st.image(alt_img_avail)
    else:
        st.image(elec_dict[elec_op_mode]["img"])

with col2:
    with st.expander(elec_dict[elec_op_mode]["title"], expanded=True):
        st.write(elec_dict[elec_op_mode]["desc"])   


######################## ELECTRICAL BUSES #######################
st.write("## Electrical Buses")
with st.expander("Essential Bus"):
    st.markdown("""
* Pilot PFD - DU 1
* Upper MFD - DU 2 
* Captain side PFD controller
* Cockpit Voice / Flight Data Recorder
* KMA 29 audio panel 1
* XPDR 1
* GPS 1
* External Lights:
    * Left inboard landing light
    * Left inboard taxi light
    * Wing inspection light
* Rudder Travel Limiter
* Flaps - via FLAPS EMER PWR btn
* Pitch Trim - Channe1 1""")
    

with st.expander("EPDU 2"):
    st.markdown("""
* Lower MFD - DU 3
* Copilot PFD - DU 4 
* Copilot side PFD controller
* Cursor Control Device - CCD
* Electronic Stanby Instrument System EPDU2""")
    
with st.expander("Left Bus"):
    st.markdown("""
* SATCOM
* DME1
* Spoliers
""")
    
with st.expander("Right Bus"):
    st.markdown("""
* KMA 29 audio panel 2
* DME2 if installed
* XPDR 2
* GPS 2
* Flaps - via EPDU 4
* Spoilers
""")
    
with st.expander("Battery 1 direct bus"):
    st.write("""
* Welcome lights
* Ground equipment compartment""")
    
with st.expander("Battery 2 direct bus"):
    st.write("""
* Baggage Lights
* refuel / defuel compartment""")

###################### QUESTION BANK
st.write("## Question Bank")

with st.expander("Battery 2 is used for PDC mode.  True of False?: "):
    st.write("False")

with st.expander("What is the minimum Li-Ion battery voltage for engine starting?"):
    st.write("BAT1 and BAT2 SOC indicators are green")

with st.expander("If a dual generator failure occurs, the aircraft is only powered via the _______ bus"):
    st.write("Essential")

with st.expander("When ground power is available to power the electrical system, the GPU displays ______"):
    st.write("AVAIL")

with st.expander("What is the main difference between the Nicad and the Li-Ion batteries?"):
    st.write("""  Li-Ion batteries monitor, optimize and protect the battery from failure.""")

with st.expander("What busses are powered by Batt 1?"):
    st.write("""
* Left Bus
* Essential Bus""")
    
with st.expander("What busses are powered by Batt 2?"):
    st.write("""
* Right Bus (for engine starts)""")
    

with st.expander("Volts and amps of Batt 1?"):
    st.write("""
* 24V / 44A""")
    
with st.expander("Volts and amps of Batt 2?"):
    st.write("""
* 26.4V / 40A""")
    
with st.expander("What converts power from DC to AC and from AC to DC?"):
    st.write("""
* PCU's - Power Conversion Unit""")
    
with st.expander("What type of 'modes' may we see on the ELEC syn page during different phases?"):
    st.write("""
* PDC Loads - Pre-departure cleareance Mode - Batt 1 ON
* START Loads - Prestart Mode - Bat 2 ON
* QPM Loads 
* S/GEN Loads - Single Generator after GPU start / Genrator Failure
* DASHES - Dual generator failure
""")
    
with st.expander("What does XC1 enable?"):
    st.write("""
* A generator to power all busses""")
    
with st.expander("What does XC2 connect?"):
    st.write("""
* Left Bus and Right Bus""")
    
with st.expander("When might you see XC2 closed?"):
    st.write("""
* During Left engine start
* GPU on
* GPU right engine start
""")
    
with st.expander("When might you see XC1 closed?"):
    st.write("""
* QPM mode
* GPU on
* During starts / Batt or GPU
* Single generator running""")
    
with st.expander("In normal conditions, what is being powered by GEN 1?"):
    st.write("""
* Left Bus
* Essential Bus""")
    
with st.expander("In normal conditions, what is being powered by GEN 2?"):
    st.write("""
* Right Bus""")
    
with st.expander("What performs power distribution monitoring functions for the left bus?"):
    st.write("""
* DCPU 1 and DCPU 3""") 

with st.expander("What performs power distribution monitoring functions for the right bus?"):
    st.write("""""
* DCPU 2 and DCPU 4""") 
    
with st.expander("How many SB's per EPDU?"):
    st.write("""
* 41""")
    

