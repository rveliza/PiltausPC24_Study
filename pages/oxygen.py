import streamlit as st

st.title("OXYGEN")

st.write("## Question Bank")

with st.expander("Where is the oxygen cylinder lcoated?"):
    st.write("""
* Right nosewheel compartment""")


with st.expander("What is the oxygen cylinder capacity?"):
    st.write("""
- Standard: 77 cu feet
- Optional: 115 cu feet""")
    
with st.expander("What is the only page where the oxygen indicator is displayed?"):
    st.write("""
* ECS synnoptic page
""")
    
with st.expander("What is the minimum oxygen qty?"):
    st.write("""
* 680 lt
""")
