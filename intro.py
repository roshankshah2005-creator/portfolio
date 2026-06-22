import streamlit as st
import base64
import os

st.set_page_config(page_title="My Portfolio", layout="wide")

# ---------- GLOBAL CSS CUSTOMIZATION ----------
st.markdown("""
<style>
    .stApp {
        background-color: #0f0f1a;
        color: #e2e8f0;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    h1, h2, h3, h4 {
        color: #6366f1 !important;
        font-weight: 600 !important;
        letter-spacing: 0.5px;
    }
    p, span, li {
        color: #cbd5e1 !important;
        font-size: 16px;
    }
    a {
        color: #38bdf8 !important;
        text-decoration: none !important;
        font-weight: 500;
    }
    a:hover {
        color: #6366f1 !important;
        text-decoration: underline !important;
    }
</style>
""", unsafe_allow_html=True)

# ---------- PERMANENTLY SAFE ENCODING FUNCTION ----------
def get_base64_safely(file_path):
    try:
        if os.path.exists(file_path):
            with open(file_path, "rb") as f:
                data = f.read()
            return base64.b64encode(data).decode()
    except Exception:
        pass
    return None

images_dir = "./images"
background_path = os.path.join(images_dir, "OIP.jpg") 
photo_path = os.path.join(images_dir, "image.jpeg")

img_base64 = get_base64_safely(background_path)

if img_base64:
    background_style = f'background-image: linear-gradient(rgba(15, 15, 26, 0.6), rgba(15, 15, 26, 0.8)), url("data:image/jpeg;base64,{img_base64}");'
else:
    background_style = 'background: linear-gradient(135deg, #1e1b4b, #311042);'

# ---------- HERO SECTION (REWRITTEN TO AVOID PASTE ERRORS) ----------
html_hero = f"""
<style>
.hero {{
    {background_style}
    background-size: cover;
    background-position: center;
    padding: 140px 40px;
    border-radius: 20px;
    text-align: center;
    color: white;
    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.5);
    border: 1px solid rgba(255, 255, 255, 0.05);
}}
.hero h1 {{
    font-size: 55px !important;
    margin-bottom: 12px;
    color: #ffffff !important;
    font-weight: 800 !important;
    text-shadow: 2px 2px 10px rgba(0,0,0,0.6);
}}
.hero h3 {{
    font-size: 24px !important;
    font-weight: 300 !important;
    color: #cbd5e1 !important;
    text-shadow: 1px 1px 5px rgba(0,0,0,0.5);
}}
</style>
<div class="hero">
    <h1>Roshan</h1>
    <h3>Chemical Engineering Student | Data Science Enthusiast</h3>
</div>
"""

st.markdown(html_hero, unsafe_allow_html=True)
st.write("\n\n")

# ---------- ABOUT ----------
col1, col2 = st.columns([1, 2.5])

with col1:
    if os.path.exists(photo_path):
        st.image(photo_path, width=200)
    else:
        st.markdown("""
        <div style="width:200px; height:200px; border-radius:20px; background:#1e1e30; 
                    display:flex; align-items:center; justify-content:center; color:#6366f1; 
                    font-size:50px; border: 2px dashed rgba(99, 102, 241, 0.3);">
            👤
        </div>
        """, unsafe_allow_html=True)

with col2:
    st.header("About Me")
    st.write("""
    I am a Chemical Engineering student with strong interest in Data Science, Machine Learning, and Analytics.
    I enjoy building projects that combine engineering and programming.
    """)

st.markdown("---")

# ---------- SKILLS ----------
st.header("Skills")

skills = ["Python", "SQL", "Pandas", "NumPy", "Matplotlib"]
skill_cols = st.
