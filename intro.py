import streamlit as st
import base64
import os

st.set_page_config(page_title="My Portfolio", layout="wide")

# ---------- PERMANENTLY SAFE ENCODING FUNCTION ----------
def get_base64_safely(file_path):
    """
    Attempts to read a file in binary mode. If it fails for any reason
    (missing file, wrong extension, capitalization change), it returns None
    instead of crashing the entire Streamlit application.
    """
    try:
        if os.path.exists(file_path):
            with open(file_path, "rb") as f:
                data = f.read()
            return base64.b64encode(data).decode()
    except Exception:
        pass
    return None

# Point directly to your images directory
images_dir = "./images"
background_path = os.path.join(images_dir, "OIP.jpg")
photo_path = os.path.join(images_dir, "image.jpeg")

# Safely attempt to encode the background image
img_base64 = get_base64_safely(background_path)

# Determine background style based on whether the image loaded successfully
if img_base64:
    background_style = f'background-image: url("data:image/jpeg;base64,{img_base64}");'
else:
    # Safe permanent fallback: A sleek modern gradient if OIP.jpg fails
    background_style = 'background: linear-gradient(135deg, #1e1e2f, #252545);'

# ---------- HERO SECTION ----------
st.markdown(f"""
<style>
.hero {{
    {background_style}
    background-size: cover;
    background-position: center;
    padding: 120px 40px;
    border-radius: 15px;
    text-align: center;
    color: white;
}}
.hero h1 {{
    font-size: 50px;
    margin-bottom: 10px;
    color: #f5f5f5;
}}
.hero h3 {{
    font-size: 22px;
    font-weight: 300;
}}
</style>

<div class="hero">
    <h1>Roshan</h1>
    <h3>Chemical Engineering Student | Data Science Enthusiast</h3>
</div>
""", unsafe_allow_html=True)

st.write("\n")

# ---------- ABOUT ----------
col1, col2 = st.columns([1, 2])

with col1:
    # Safely display the profile photo if it exists
    if os.path.exists(photo_path):
        st.image(photo_path, width=200)
    else:
        # Safe fallback layout if image.jpeg is missing or renamed
        st.markdown("""
        <div style="width:200px; height:200px; border-radius:10px; background:#2b2b40; 
                    display:flex; align-items:center; justify-content:center; color:gray; font-size:40px;">
            👤
        </div>
        """, unsafe_allow_html=True)

with col2:
    st.header("About Me")
    st.write("""
    I am a Chemical Engineering student with strong interest in Data Science, Machine Learning, and Analytics.
    I enjoy building projects that combine engineering and programming.
    """)

# ---------- SKILLS ----------
st.header("Skills")

skills = ["Python", "SQL", "Pandas", "NumPy", "Matplotlib"]
for skill in skills:
    st.write("•", skill)

# ---------- PROJECTS ----------
st.header("Projects")
st.subheader("Project no. 1")
st.write("https://github.com/roshankshah2005-creator/Video-Game-Market-Analysis/tree/main")

# ---------- CONTACT ----------
st.header("Contact")

st.write("Email: roshank.shah2005@gmail.com")
st.write("LinkedIn: https://www.linkedin.com/in/roshan-kumar-sah-5158653a5")
st.write("GitHub: https://github.com/roshankshah2005-creator")
