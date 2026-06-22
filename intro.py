import streamlit as st
import os

st.set_page_config(page_title="My Portfolio", layout="wide")

# ----------BACKGROUND SETUP ----------
bg_image = "https://images.unsplash.com/photo-1542051841857-5f90071e7989?q=80&w=1920&auto=format&fit=crop"

st.markdown(f"""
<style>
.stApp {{
    background: linear-gradient(rgba(0, 0, 0, 0.4), rgba(0, 0, 0, 0.4)), url("{bg_image}");
    background-size: cover;
    background-position: center;
    background-attachment: fixed;
}}
/* High-visibility container boxes for text sections */
.glass-panel {{
    background-color: rgba(15, 15, 26, 0.75);
    padding: 25px;
    border-radius: 15px;
    border: 1px solid rgba(255, 255, 255, 0.08);
    margin-bottom: 20px;
    box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.37);
}}
h1, h2, h3, h4 {{
    color: #50fa7b !important;
    font-weight: 700 !important;
    margin-top: 0px !important;
}}
p, span, li, div {{
    color: #ffffff !important;
    font-size: 16px;
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
st.markdown('<div class="glass-panel"><h1>Roshan\'s Portfolio</h1><h3>Chemical Engineering Student | Data Science Enthusiast</h3></div>', unsafe_allow_html=True)

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
    st.markdown('''
    <div class="glass-panel">
        <h2>About Me</h2>
        <p>I am a Chemical Engineering student with strong interest in Data Science, Machine Learning, and Analytics. I enjoy building projects that combine engineering and programming.</p>
    </div>
    ''', unsafe_allow_html=True)

# ---------- SKILLS SECTION ----------
st.markdown('''
<div class="glass-panel">
    <h2>Skills</h2>
    <p style="color: #50fa7b !important; font-weight: 600; font-size: 18px;">
        ⚡ Python  |  SQL  |  Pandas  |  NumPy  |  Matplotlib | Seaborn
    </p>
</div>
''', unsafe_allow_html=True)

# ---------- PROJECTS SECTION ----------
st.markdown('''
<div class="glass-panel">
    <h2>Projects</h2>
    <h4 style="color: #ffffff !important;">Project no. 1: Video Game Market Analysis</h4>
    <p>An end-to-end data processing and analysis project exploring historical video game industry sales trends.</p>
    <a href="https://github.com/roshankshah2005-creator/Video-Game-Market-Analysis/tree/main" target="_blank">🔗 GitHub Link: Video Game Market Analysis</a>
</div>
''', unsafe_allow_html=True)

# ---------- CONTACT SECTION ----------
st.markdown('''
<div class="glass-panel">
    <h2>Contact Me</h2>
    <p>📧 <b>Email:</b> roshank.shah2005@gmail.com</p>
    <p>💼 <b>LinkedIn:</b> <a href="https://www.linkedin.com/in/roshan-kumar-sah-5158653a5" target="_blank">roshan-kumar-sah-5158653a5</a></p>
    <p>🐙 <b>GitHub:</b> <a href="https://github.com/roshankshah2005-creator" target="_blank">roshankshah2005-creator</a></p>
</div>
''', unsafe_allow_html=True)
