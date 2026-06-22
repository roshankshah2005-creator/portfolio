import streamlit as st
import os

st.set_page_config(page_title="My Portfolio", layout="wide")

# ----------BACKGROUND SETUP ----------
bg_image = "https://images.unsplash.com/photo-1542051841857-5f90071e7989?q=80&w=1920&auto=format&fit=crop"

st.markdown(f"""
<style>
.stApp {{
    background: linear-gradient(rgba(0, 0, 0, 0.5), rgba(0, 0, 0, 0.5)), url("{bg_image}");
    background-size: cover;
    background-position: center;
    background-attachment: fixed;
    color: #f5f5f7 !important;
}}
h1, h2, h3, h4 {{
    color: #50fa7b !important;
    font-weight: 600 !important;
}}
p, span, li, div {{
    color: #f5f5f7 !important;
}}
a {{
    color: #50fa7b !important;
    text-decoration: none !important;
    font-weight: 600;
}}
a:hover {{
    text-decoration: underline !important;
}}
</style>
""", unsafe_allow_html=True)

# ---------- TITLE & HERO SECTION ----------
st.title("Roshan's Portfolio")
st.subheader("Chemical Engineering Student | Data Science Enthusiast")

st.markdown("---")

# ---------- ABOUT ME SECTION ----------
col1, col2 = st.columns([1, 2.5])

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

# ---------- SKILLS SECTION ----------
st.header("Skills")
st.success("⚡ Python  |  SQL  |  Pandas  |  NumPy  |  Matplotlib | Seaborn")

st.markdown("---")

# ---------- PROJECTS SECTION ----------
st.header("Projects")
with st.container():
    st.subheader("Project no. 1: Video Game Market Analysis")
    st.write("An end-to-end data processing and analysis project exploring historical video game industry sales trends.")
    st.write("🔗 GitHub Link: https://github.com/roshankshah2005-creator/Video-Game-Market-Analysis/tree/main")

st.markdown("---")

# ---------- CONTACT SECTION ----------
st.header("Contact Me")
st.markdown("📧 **Email:** roshank.shah2005@gmail.com")
st.markdown("💼 **LinkedIn:** https://www.linkedin.com/in/roshan-kumar-sah-5158653a5")
st.markdown("🐙 **GitHub:** https://github.com/roshankshah2005-creator")
