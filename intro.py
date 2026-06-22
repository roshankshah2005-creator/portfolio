import streamlit as st
import os

st.set_page_config(page_title="My Portfolio", layout="wide")

# ---------- FORCED LUXURY SYSTEM CSS CUSTOMIZATION ----------
st.markdown("""
<style>
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

# ---------- TITLE & HERO SECTION ----------
st.markdown('<div class="master-header">Roshan\'s Portfolio</div>', unsafe_allow_html=True)
st.markdown('<div class="heavy-subheader">Chemical Engineering Student | Data Science Enthusiast</div>', unsafe_allow_html=True)

st.markdown("---")

# ---------- ABOUT ME SECTION ----------
col1, col2 = st.columns([1, 2.5])

# Flattened paths onto single lines to permanently stop copy-paste breaking
images_dir = "./images"
photo_path = os.path.join(images_dir, "image.jpeg")

with col1:
    if os.path.exists(photo_path):
        st.image(photo_path, width=200)
    else:
        st.write("👤 [Profile Image Container Ready]")

with col2:
    st.header("About Me")
    st.write("I am a Chemical Engineering student with strong interest in Data Science, Machine Learning, and Analytics. I enjoy building projects that combine engineering and programming.")

st.markdown("---")

# ---------- ACADEMIC PROFILE & 3RD SEMESTER FOCUS ----------
st.header("Education & Core Focus")
col3, col4 = st.columns(2)

with col3:
    st.subheader("🎓 Academic Background")
    st.write("• **Degree:** B.Tech in Chemical Engineering")
    st.write("• **Institution:** National Institute of Technology (NIT)")
    st.write("• **Interests:** Process Simulation, Optimization, and Data-Driven Modeling")

with col4:
    st.subheader("🧪 3rd Semester Core Engineering Modules")
    st.write("• **Chemical Process Calculations:** Material and energy balances.")
    st.write("• **Fluid Mechanics:** Fluid behavior, piping networks, and transport.")
    st.write("• **Chemical Engineering Thermodynamics:** Phase equilibrium and energy laws.")
    st.write("• **Advanced Mathematics:** Numerical methods, linear algebra, and calculus.")

st.markdown("---")

# ---------- SKILLS SECTION ----------
st.header("Skills")
st.success("⚡ Python  |  SQL  |  Pandas  |  NumPy  |  Matplotlib | Seaborn")

st.markdown("---")

# ---------- PROJECTS SECTION ----------
st.header("Projects")
with st.container():
    st.subheader("Project no. 1: Video Game Market Analysis")
    st.write("An end-to-end data processing and analysis project exploring historical video game industry sales trends.")
    st.markdown("🔗 **GitHub Link:** [Video Game Market Analysis](
