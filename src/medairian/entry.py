from streamlit_option_menu import option_menu
import streamlit as st

# 1. as sidebar menu
with st.sidebar:
    selected = option_menu(
        "Hey there! 👋",
        ["About", "Resume"],
        icons=["house", "gear"],
        menu_icon="---",
        default_index=1,
    )

if selected == "About":
    st.write("Welcome to my portfolio. ✨")

elif selected == "Resume":
    st.write("This is my Resume. 🔥")
