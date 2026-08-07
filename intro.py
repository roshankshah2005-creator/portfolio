import streamlit as st
import os

st.set_page_config(page_title="My Portfolio", layout="wide")

# ---------- BACKGROUND ----------
st.markdown("""
<style>
/* Hide the top header bar while preserving the 'Manage app' button */
header {visibility: hidden;}
[data-testid="stHeader"] {display: none;}
div[data-testid="stDecoration"] {display: none;}

/* Adjust top padding since the top bar is gone */
.block-container {padding-top: 2rem !important;}

.stApp { background-color: #1a102f !important; color: #f5f5f7 !important; } 
.master-header { color: #dfba73 !important; font-weight: 900 !important; font-size: 80px !important; line-height: 1.1 !important; letter-spacing: -2px !important; margin-top: 20px !important; margin-bottom: 5px !important; font-family: sans-serif !important; }
.heavy-subheader { color: #f1dfbb !important; font-weight: 800 !important; font-size: 26px !important; margin-top: 0px !important; margin-bottom: 35px !important; letter-spacing: 0.3px; padding-left: 20px !important; }
h2 { color: #e5c78d !important; font-weight: 800 !important; font-size: 34px !important; } 
h3, h4 { color: #f1dfbb !important; font-weight: 700 !important; font-size: 24px !important; } 
p, span, li, div { color: #f5f5f7 !important; font-size: 20px !important; line-height: 1.6 !important; } 
a { color: #dfba73 !important; text-decoration: none !important; font-weight: 700 !important; } 
a:hover { text-decoration: underline !important; color: #f1dfbb !important; }
</style>
""", unsafe_allow_html=True)

# ---------- HEADER SECTION ----------
st.markdown('<div class="master-header">Roshan\'s Portfolio</div>', unsafe_allow_html=True)
st.markdown('<div class="heavy-subheader">Chemical Engineering Student | Data Science Enthusiast</div>', unsafe_allow_html=True)
st.markdown("---")

# ---------- ABOUT ME SECTION ----------
col1, col2 = st.columns([1, 2.5])
photo_path = os.path.join("./images", "image.jpeg")

with col1:
    if os.path.exists(photo_path):
        st.image(photo_path, width=200)
    else:
        st.write("👤 [Profile Image Ready]")

with col2:
    st.header("About Me")
    st.write("I am an engineering student bridging the gap between physical systems and data science.")
    st.write("My academic core is in Chemical Engineering, where I study complex process mechanics.")
    st.write("Alongside my coursework, I build machine learning models and data pipelines in Python.")
    st.write("I aim to apply data-driven optimization to chemical processes and industrial systems.")

st.markdown("---")

# ---------- ACADEMIC & CURRICULUM FOCUS ----------
st.header("Education & Core Focus")
col3, col4 = st.columns(2)

with col3:
    st.subheader("🎓 Academic Background")
    st.write("• **Degree:** B.Tech in Chemical Engineering")
    st.write("• **Institution:** National Institute of Technology (NIT), Durgapur")
    st.write("• **Batch:** 2025-29")
    st.write("• **Interests:** Process Simulation and Data Modeling")

with col4:
    st.subheader("🧪 3rd Sem Engineering Modules")
    st.write("• **Process Calculations:** Material and energy balances.")
    st.write("• **Fluid Mechanics:** Flow behavior and piping networks.")
    st.write("• **Thermodynamics:** Phase equilibrium and energy laws.")
    st.write("• **Advanced Math:** Numerical methods and linear algebra.")

st.markdown("---")

# ---------- SKILLS SECTION ----------
st.header("Skills")
st.success("⚡ Python  |  SQL  |  Pandas  |  NumPy  |  Matplotlib | Seaborn")
st.markdown("---")

# ---------- PROJECTS SECTION ----------
st.header("Projects")
with st.container():
    st.subheader("Project no. 1: Video Game Market Analysis")
    st.write("Data processing and analysis project exploring video game industry sales trends.")
    st.markdown("[🔗 GitHub Repository Link](https://github.com/roshankshah2005-creator/Video-Game-Market-Analysis)")
    st.subheader("Project no. 2: AI Student Score Predictor")
    st.write("Machine learning pipeline and interactive intelligence dashboard exploring academic success drivers and student performance trends.")
    st.markdown("[🔗 GitHub Repository Link](https://github.com/roshankshah2005-creator/mlprojects)")
    st.markdown("[🌐Project Website Link](https://3ioccprssrwschfmlonehi.streamlit.app/)")
    st.subheader("Project no. 3: Netflix Analytics")
    st.write("Interactive Netflix analytics platform for exploring content distribution, country-wise trends, ratings, genres, and release history.")
    st.markdown("[🔗 GitHub Repository Link](https://github.com/roshankshah2005-creator/NETFLIX_ANALYTICS_DASHBOARD)")
    st.markdown("[🌐Project Website Link](https://netflixinsights.streamlit.app/)")
    st.subheader("Project no. 3: Student Performance Predictor")
    st.write("A predictive web app for forecasting exam scores and analyzing the impact of study habits, attendance, and sleep on academic performance.")
    st.markdown("[🔗 GitHub Repository Link](https://github.com/roshankshah2005-creator/Student-Performance-Prediction)")
    st.markdown("[🌐Project Website Link](https://soft-treacle-87a14a.netlify.app/)")
st.markdown("---")

# ---------- CONTACT SECTION ----------
st.header("Contact Me")
st.markdown("📧 **Email:** roshank.shah2005@gmail.com")
st.markdown("💼 **LinkedIn:** [Profile Link](https://www.linkedin.com/in/roshan-kumar-sah-5158653a5)")
st.markdown("🐙 **GitHub:** [Profile Link](https://github.com/roshankshah2005-creator)")
