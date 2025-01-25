import streamlit as st

ABOUT_ME = """

I am Atef Attia, a passionate and solution-driven Machine Learning Engineer with a strong academic foundation
in Computer Science (M.Sc., KIT, Germany). Over the years, I have honed my skills in ML engineering, data pipelines,
and cloud computing, contributing to impactful projects like chatbot development, TV attribution models, and cookieless
advertising solutions ✨.


With expertise in tools like Python, SQL, AWS, and MLOps frameworks, I thrive on solving complex problems
and enabling data-driven decision-making. Beyond work, I enjoy exploring the outdoors 🚞, diving into a good book 📚,
and playing soccer ⚽️ or padel tennis 🎾.


I value knowledge-sharing and collaboration and aim to create scalable, innovative, and practical solutions that make a difference. 🚀

"""


def render():
    st.header("About Me 💡")
    st.write(ABOUT_ME)
