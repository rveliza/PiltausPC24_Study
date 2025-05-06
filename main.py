import streamlit as st

memory_items_page = st.Page("pages/memory_items.py", title="Memory Items", icon="🧠")
limitations_page = st.Page("pages/limitations.py", title="Limitations", icon="🚫")
ac_general_page = st.Page("pages/ac_general.py", title="AC General", icon="🛩️")
indicating_recording_page = st.Page("pages/indicating_recording.py", title="Indicating & Recording", icon="📊")
electrical_page = st.Page("pages/electrical.py", title="Electrical", icon="⚡")
communications_page = st.Page("pages/communications.py", title="Communications", icon="📱")
lighting_page = st.Page("pages/lighting.py", title="Lighting", icon="💡")
flight_controls_page = st.Page("pages/flight_controls.py", title="Flight Controls", icon="🕹️")
fuel_page = st.Page("pages/fuel.py", title="Fuel", icon="⛽")
performance_page = st.Page("pages/performance.py", title="Performance", icon="📈")
powerplant_page = st.Page("pages/powerplant.py", title="Powerplant", icon="🛞")
fire_protection_page = st.Page("pages/fire_protection.py", title="Fire Protection", icon="🔥",)
landing_gear_page = st.Page("pages/landing_gear.py", title="Landing Gear", icon="🚦")
environmental_control_page = st.Page("pages/environmental_control.py", title="Environmental Control", icon="🌡️")
oxygen_control_page = st.Page("pages/oxygen.py", title="Oxygen", icon="👃")
altitudes_page = st.Page("pages/altitudes.py", title="Altitudes", icon="⛰️")
ice_protection_page = st.Page("pages/ice_protection.py", title="Ice Protection", icon="⛄")

pg = st.navigation({
    "Must Know": [memory_items_page, limitations_page],
    "Nice to Know": [altitudes_page],
    "Aircraft Systems": [ac_general_page, indicating_recording_page, electrical_page, communications_page, environmental_control_page, ice_protection_page, landing_gear_page ,lighting_page, fire_protection_page, flight_controls_page, fuel_page, oxygen_control_page, powerplant_page],
    "Performance": [performance_page],
})

st.set_page_config(
    initial_sidebar_state="expanded", layout="wide",
    menu_items={
        'About': 'Reach me at reyner@reynerveliz.com for doubts, suggestions, error, etc.'
    }
)

pg.run()