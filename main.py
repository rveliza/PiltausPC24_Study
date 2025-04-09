import streamlit as st

memory_items_page = st.Page("pages/memory_items.py", title="Memory Items", icon="🧠")
limitations_page = st.Page("pages/limitations.py", title="Limitations", icon="🚫")
ac_general_page = st.Page("pages/ac_general.py", title="AC General", icon="🛩️")

pg = st.navigation({
    "Must Know": [memory_items_page, limitations_page],
    "Aircraft Systems": [ac_general_page],
})

st.set_page_config(
    initial_sidebar_state="expanded",
    menu_items={
        'About': 'Reach me at reyner@reynerveliz.com for doubts, suggestions, error, etc.'
    }
)

pg.run()