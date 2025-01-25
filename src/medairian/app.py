from streamlit_option_menu import option_menu
import streamlit as st
from medairian.pages import resume, about

from pathlib import Path

# PATH SETTINGS
PROJECT_ROOT: Path = Path(__file__).parent.parent.parent
css_file: Path = PROJECT_ROOT / "styles" / "main.css"

st.set_page_config(page_title="Med.AI.rian", page_icon="🌊")


def style(css_file: Path):
    # --- LOAD CSS, PDF & PROFIL PIC ---
    with open(css_file) as f:
        st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)


def main():
    # 1. as sidebar menu
    with st.sidebar:
        selected = option_menu(
            "Hey there! 👋",
            ["About", "Resume"],
            icons=["file-earmark-person-fill", "briefcase-fill"],
            menu_icon="---",
            default_index=0,
        )

    if selected == "About":
        about.render()

    elif selected == "Resume":
        resume.render()


if __name__ == "__main__":
    style(css_file=css_file)
    main()
