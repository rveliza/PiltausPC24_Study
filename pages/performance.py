import streamlit as st

st.title("Performance")

st.write("#### Takeoff Information (FCOM page 1646)")

with st.expander("Takeoff Data", expanded=True):
    st.write("""
**The minimum required is the longest of the following:**
- All engines operating accelerate stop distance
- The accelerate-stop distance after engine failure
- The (continued) takeoff distance with one engine inoperative
- 115% of the all engines operating takeoff distance""")