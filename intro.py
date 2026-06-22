import streamlit as st
import base64
import os

st.set_page_config(page_title="My Portfolio", layout="wide")

# ---------- FUNCTION TO ENCODE IMAGE ----------
def get_base64(file):
    # Safely check if the file actually exists before trying to open it
    if os.path.exists(file):
        with open(file, "rb") as f:
            data = f.read()
        return base64.b64encode(data).decode()
    return None  # Return None if the file is missing

# Dynamically locate the directory where intro.py is stored
current_dir = os.path.dirname(os.path.abspath(__file__))
image_path = os.path.join(current_dir, "rbg.jpg")

# Pass the path to your safe function
img_base64 = get_base64(image_path)

# Determine background style based on whether the image was successfully loaded
if img_base64:
    background_style = f'background-image: url("data:image/jpg;base64,{img_base64}");'
else:
    # Fallback to a sleek dark gradient if rbg.jpg cannot be found
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
    photo_path = os.path.join(current_dir, "photoopo.jpg")
    if os.path.exists(photo_path):
        st.image(photo_path, width=200)
    else:
        # Fallback placeholder if your profile photo is missing too
        st.warning("👤 Profile image not found on GitHub folder.")

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
