import streamlit as st
from PIL import Image

from pathlib import Path

PROJECT_ROOT: Path = Path(__file__).parent.parent.parent.parent

# --- GENERAL SETTINGS ---
PAGE_TITLE = "Med.AI.rian"
PAGE_ICON = "🌊"
NAME = "Atef Attia"
DESCRIPTION = """
Senior ML Engineer, assisting enterprises by supporting data-driven decision-making.
"""
EMAIL = "attia.atef92@gmail.com"
SOCIAL_MEDIA = {
    "LinkedIn": "https://www.linkedin.com/in/atef-attia-b03307194/",
    "GitHub": "https://github.com/atefattia",
}
PROJECTS = {
    "🏆 Medialytics - tool that measure the performance of TV Ads based on user website traffic": "https://youtu.be/Sb0A9i6d320",
    "🏆 Income and Expense Tracker - Web app with NoSQL database": "https://youtu.be/Sb0A9i6d320",
    "🏆 Desktop Application - Excel2CSV converter with user settings & menubar": "https://youtu.be/Sb0A9i6d320",
    "🏆 MyToolBelt - Custom MS Excel add-in to combine Python & Excel": "https://youtu.be/Sb0A9i6d320",
}


def show_hero_section(resume_file: Path, profile_pic: Path):
    with open(resume_file, "rb") as pdf_file:
        PDFbyte = pdf_file.read()
    profile_pic = Image.open(profile_pic)  # type: ignore

    # --- HERO SECTION ---
    col1, col2 = st.columns(2, gap="small")
    with col1:
        st.image(profile_pic, width=230)

    with col2:
        st.title(NAME)
        st.write(DESCRIPTION)
        st.download_button(
            label=" 📄 Download Resume",
            data=PDFbyte,
            file_name=resume_file.name,
            mime="application/octet-stream",
        )
        st.write("📫", EMAIL)

    # --- SOCIAL LINKS ---
    st.write("\n")
    cols = st.columns(len(SOCIAL_MEDIA))
    for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
        cols[index].write(f"[{platform}]({link})")


def show_experience_qualifications():
    # --- EXPERIENCE & QUALIFICATIONS ---
    st.write("\n")
    st.subheader("Experience & Qulifications")
    st.write(
        """
    - ✔️ 7 Years expereince extracting actionable insights from data
    - ✔️ Strong hands on experience and knowledge in Python and Excel
    - ✔️ Good understanding of statistical principles and their respective applications
    - ✔️ Excellent team-player and displaying strong sense of initiative on tasks
    """
    )


def show_skills():
    # --- SKILLS ---
    st.write("\n")
    st.subheader("Hard Skills")
    st.write(
        """
    - 👩‍💻 Programming: Python (Scikit-learn, Pandas), SQL, VBA
    - 📊 Data Visulization: PowerBi, MS Excel, Plotly
    - 📚 Modeling: Logistic regression, linear regression, decition trees
    - 🗄️ Databases: Postgres, MongoDB, MySQL
    """
    )


def show_work_history():
    # --- WORK HISTORY ---
    st.write("\n")
    st.subheader("Work History")
    st.write("---")

    # --- JOB 1
    st.write("🚧", "**Senior Data Analyst | Ross Industries**")
    st.write("02/2020 - Present")
    st.write(
        """
    - ► Used PowerBI and SQL to redeﬁne and track KPIs surrounding marketing initiatives, and supplied recommendations to boost landing page conversion rate by 38%
    - ► Led a team of 4 analysts to brainstorm potential marketing and sales improvements, and implemented A/B tests to generate 15% more client leads
    - ► Redesigned data model through iterations that improved predictions by 12%
    """
    )

    # --- JOB 2
    st.write("\n")
    st.write("🚧", "**Data Analyst | Liberty Mutual Insurance**")
    st.write("01/2018 - 02/2022")
    st.write(
        """
    - ► Built data models and maps to generate meaningful insights from customer data, boosting successful sales eﬀorts by 12%
    - ► Modeled targets likely to renew, and presented analysis to leadership, which led to a YoY revenue increase of $300K
    - ► Compiled, studied, and inferred large amounts of data, modeling information to drive auto policy pricing
    """
    )

    # --- JOB 3
    st.write("\n")
    st.write("🚧", "**Data Analyst | Chegg**")
    st.write("04/2015 - 01/2018")
    st.write(
        """
    - ► Devised KPIs using SQL across company website in collaboration with cross-functional teams to achieve a 120% jump in organic traﬃc
    - ► Analyzed, documented, and reported user survey results to improve customer communication processes by 18%
    - ► Collaborated with analyst team to oversee end-to-end process surrounding customers' return data
    """
    )


def show_project_accomplishments():
    # --- Projects & Accomplishments ---
    st.write("\n")
    st.subheader("Projects & Accomplishments")
    st.write("---")
    for project, link in PROJECTS.items():
        st.write(f"[{project}]({link})")


def render():
    # style(css_file=css_file)

    resume_file: Path = PROJECT_ROOT / "assets" / "AtefAttiaCV.pdf"
    profile_pic: Path = PROJECT_ROOT / "assets" / "profile-pic.jpg"
    show_hero_section(resume_file=resume_file, profile_pic=profile_pic)

    show_experience_qualifications()
    show_skills()
    show_work_history()
    show_project_accomplishments()
