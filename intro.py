import streamlit as st
import base64
import os

st.set_page_config(page_title="My Portfolio", layout="wide")

# ---------- FUNCTION TO ENCODE IMAGE ----------
def get_base64(file):
    with open(file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

# Find the main root directory, then step into the 'images' folder
current_dir = os.path.dirname(os.path.abspath(__file__))  # portfolio folder
root_dir = os.path.dirname(current_dir)                    # main project folder
images_dir = os.path.join(root_dir, "images")              # images folder

# Safe paths directly inside your 'images' folder
background_path = os.path.join(images_dir, "oip.jpg")
photo_path = os.path.join(images_dir, "image.jpg")

# Encode the background image
img_base64 = get_base64(background_path)

# ---------- HERO SECTION ----------
st.markdown(f"""
<style>
.hero {{
    background-image: url("data:image/jpg;base64,{img_base64}");
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
    # Load your profile photo safely from the images folder
    st.image(photo_path, width=200)

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
