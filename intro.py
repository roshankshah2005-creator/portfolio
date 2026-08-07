import streamlit as st
import os

# ---------- PAGE CONFIGURATION ----------
st.set_page_config(
    page_title="Roshan Kumar Sah | Portfolio",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ---------- DESIGN & STYLING (CSS) ----------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700&display=swap');

header {visibility: hidden;}
[data-testid="stHeader"] {display: none;}
footer {visibility: hidden;}

.stApp {
    background-color: #1a102f !important;
    font-family: 'Plus Jakarta Sans', sans-serif;
    color: #f5f5f7 !important;
}

.block-container {
    max-width: 1000px;
    padding-top: 2rem !important;
}

.hero-title {
    color: #dfba73 !important;
    font-weight: 800 !important;
    font-size: 50px !important;
    margin-bottom: 0px !important;
}

.hero-subtitle {
    color: #f1dfbb !important;
    font-weight: 700 !important;
    font-size: 22px !important;
    margin-bottom: 30px !important;
}

h2 {
    color: #e5c78d !important;
    font-weight: 700 !important;
    font-size: 28px !important;
    margin-top: 30px !important;
}

p, span, li, div {
    color: #f5f5f7 !important;
    font-size: 18px !important;
    line-height: 1.6 !important;
}

.project-box {
    background: rgba(255, 255, 255, 0.04);
    border: 1px solid rgba(255, 255, 255, 0.1);
    border-radius: 12px;
    padding: 20px;
    margin-bottom: 20px;
}

a {
    color: #dfba73 !important;
    text-decoration: none !important;
    font-weight: 600 !important;
}
a:hover {
    text-decoration: underline !important;
    color: #f1dfbb !important;
}
</style>
""", unsafe_allow_html=True)

# ---------- HEADER SECTION ----------
st.markdown('<div class="hero-title">Roshan Kumar Sah</div>', unsafe_allow_html=True)
st.markdown('<div class="hero-subtitle">Chemical Engineering Undergraduate | Data Science Enthusiast</div>', unsafe_allow_html=True)
st.markdown("---")

# ---------- ABOUT ME SECTION ----------
col1, col2 = st.columns([1, 2.5], gap="large")
photo_path = os.path.join("./images", "image.jpeg")

with col1:
    if os.path.exists(photo_path):
        st.image(photo_path, width=200)
    else:
        st.write("👤 [Profile Image]")

with col2:
    st.markdown("<h2>About Me</h2>", unsafe_allow_html=True)
    st.write("I am an engineering student bridging the gap between physical systems and data science.")
    st.write("My academic core is in Chemical Engineering at NIT Durgapur, where I study complex process mechanics.")
    st.write("Alongside my coursework, I build machine learning models and data pipelines in Python to optimize systems.")

st.markdown("---")

# ---------- EDUCATION & SKILLS ----------
col3, col4 = st.columns(2, gap="large")

with col3:
    st.markdown("<h2>Education</h2>", unsafe_allow_html=True)
    st.write("• **Degree:** B.Tech in Chemical Engineering")
    st.write("• **Institution:** NIT Durgapur (2025–2029)")
    st.write("• **Focus:** Process Simulation & Data Modeling")

with col4:
    st.markdown("<h2>Skills</h2>", unsafe_allow_html=True)
    st.write("⚡ **Languages & Libraries:** Python, SQL, Pandas, NumPy, Scikit-Learn, Streamlit, Matplotlib, Seaborn")

st.markdown("---")

# ---------- PROJECTS SECTION (Simplified) ----------
st.markdown("<h2>Projects</h2>", unsafe_allow_html=True)

# Project 1
st.markdown("""
<div class="project-box">
    <h3>🎓 AI Student Score Predictor</h3>
    <p>Machine learning pipeline and interactive intelligence dashboard exploring academic success drivers and student performance trends.</p>
    <a href="https://github.com/roshankshah2005-creator/mlprojects" target="_blank">🔗 GitHub</a> &nbsp;|&nbsp; 
    <a href="https://3ioccprssrwschfmlonehi.streamlit.app/" target="_blank">🌐 Live App</a>
</div>
""", unsafe_allow_html=True)

# Project 2
st.markdown("""
<div class="project-box">
    <h3>📊 Netflix Analytics Dashboard</h3>
    <p>Interactive Netflix analytics platform for exploring content distribution, country-wise trends, ratings, genres, and release history.</p>
    <a href="https://github.com/roshankshah2005-creator/NETFLIX_ANALYTICS_DASHBOARD" target="_blank">🔗 GitHub</a> &nbsp;|&nbsp; 
    <a href="https://netflixinsights.streamlit.app/" target="_blank">🌐 Live App</a>
</div>
""", unsafe_allow_html=True)

# Project 3
st.markdown("""
<div class="project-box">
    <h3>🎯 Video Game Market Analysis</h3>
    <p>Advanced exploratory data analysis and SQL pipeline investigating global video game industry sales trends and regional preferences.</p>
    <a href="https://github.com/roshankshah2005-creator/Video-Game-Market-Analysis" target="_blank">🔗 GitHub</a> &nbsp;|&nbsp; 
    <a href="https://uwkdhet8w3cmbcp3ijboit.streamlit.app/" target="_blank">🌐 Live App</a>
</div>
""", unsafe_allow_html=True)

# Project 4
st.markdown("""
<div class="project-box">
    <h3>📚 Student Performance Predictor</h3>
    <p>A predictive web app for forecasting exam scores and analyzing the impact of study habits, attendance, and sleep on academic performance.</p>
    <a href="https://github.com/roshankshah2005-creator/Student-Performance-Prediction" target="_blank">🔗 GitHub</a> &nbsp;|&nbsp; 
    <a href="https://soft-treacle-87a14a.netlify.app/" target="_blank">🌐 Live App</a>
</div>
""", unsafe_allow_html=True)

st.markdown("---")

# ---------- CONTACT SECTION ----------
st.markdown("<h2>Contact Me</h2>", unsafe_allow_html=True)
st.markdown("📧 **Email:** roshank.shah2005@gmail.com")
st.markdown("💼 **LinkedIn:** [Profile Link](https://www.linkedin.com/in/roshan-kumar-sah-5158653a5)")
st.markdown("🐙 **GitHub:** [Profile Link](https://github.com/roshankshah2005-creator)")
