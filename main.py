import streamlit as st

memory_items_page = st.Page("pages/memory_items.py", title="Limitations", icon="🧠")

pg = st.navigation({
    "Must Know": [memory_items_page]
})

st.set_page_config(
    initial_sidebar_state="expanded"
)

pg.run()