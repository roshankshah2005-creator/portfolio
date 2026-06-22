import streamlit as st
import base64
import os

st.set_page_config(page_title="My Portfolio", layout="wide")

# ---------- SAFE IMAGE LOADER ----------
def get_base64_safely(file_path):
    try:
        if os.path.exists(file_path):
            with open(file_path, "rb") as f:
                return base64.b64encode(f.read()).decode()
    except Exception:
        pass
    return None

images_dir = "./images"
bg_encoded = get_base64_safely(os.path.join(images_dir, "OIP.jpg"))
photo_path = os.path.join(images_dir, "image.jpeg")

# ---------- TITLE & HERO SECTION ----------
st.title("Roshan's Portfolio")
st.subheader("Chemical Engineering Student | Data Science Enthusiast")

if bg_encoded:
    st.info("🌌 Background Image Loaded Successfully from /images/OIP.jpg")
else:
    st.info("🎨 Clean Default Gradient Theme Active")

st.markdown("---")

# ---------- ABOUT ME SECTION ----------
col1, col2 = st.columns([1, 2.5])

with col1:
    if os.path.exists(photo_path):
        st.image(photo_path, width=200)
    else:
        st.write("👤 [Profile Image Ready]")

with col2:
    st.header("About Me")
    st.write("I am a Chemical Engineering student with strong interest in Data Science, Machine Learning, and Analytics. I enjoy building projects that combine engineering and programming.")

st.markdown("---")

# ---------- SKILLS SECTION ----------
st.header("Skills")
st.write("👉 Python  |  SQL  |  Pandas  |  NumPy  |  Matplotlib")

st.markdown("---")

# ---------- PROJECTS SECTION ----------
st.header("Projects")
st.subheader("Project no. 1: Video Game Market Analysis")
st.write("An end-to-end data processing and analysis project exploring historical video game industry sales trends.")
st.write("🔗 GitHub Link: https://github.com/roshankshah2005-creator/Video-Game-Market-Analysis/tree/main")

st.markdown("---")

# ---------- CONTACT SECTION ----------
st.header("Contact Me")
st.write("📧 Email: roshank.shah2005@gmail.com")
st.write("💼 LinkedIn: https://www.linkedin.com/in/roshan-kumar-sah-5158653a5")
st.write("🐙 GitHub: https://github.com/roshankshah2005-creator")
