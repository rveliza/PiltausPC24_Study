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

pg = st.navigation({
    "Must Know": [memory_items_page, limitations_page],
    "Aircraft Systems": [ac_general_page, indicating_recording_page, electrical_page, communications_page, lighting_page, flight_controls_page, fuel_page],
})

st.set_page_config(
    initial_sidebar_state="expanded", layout="wide",
    menu_items={
        'About': 'Reach me at reyner@reynerveliz.com for doubts, suggestions, error, etc.'
    }
)

pg.run()