import streamlit as st
import base64
import os

st.set_page_config(page_title="My Portfolio", layout="wide")

# ---------- FUNCTION TO ENCODE IMAGE ----------
def get_base64(filename):
    # 1. Check the portfolio folder dynamically
    current_dir = os.path.dirname(os.path.abspath(__file__))
    path_in_subfolder = os.path.join(current_dir, filename)
    
    # 2. Check the main root folder as a backup
    path_in_root = os.path.abspath(filename)
    
    # Decide which file exists
    if os.path.exists(path_in_subfolder):
        final_path = path_in_subfolder
    elif os.path.exists(path_in_root):
        final_path = path_in_root
    else:
        # If the file is completely missing from both places, don't crash!
        # Return a clean placeholder background color instead
        return "background: linear-gradient(135deg, #1e1e2f, #252545);"

    with open(final_path, "rb") as f:
        data = f.read()
    encoded = base64.b64encode(data).decode()
    return f'background-image: url("data:image/jpg;base64,{encoded}");'

# This function now safely returns the entire background CSS rule or a gradient fallback
background_style = get_base64("oip.jpg")

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
    # Applying the same dual-folder safety logic to your profile image
    current_dir = os.path.dirname(os.path.abspath(__file__))
    path_sub = os.path.join(current_dir, "image.jpg")
    path_root = os.path.abspath("image.jpg")
    
    if os.path.exists(path_sub):
        st.image(path_sub, width=200)
    elif os.path.exists(path_root):
        st.image(path_root, width=200)
    else:
        st.warning("👤 Profile image (image.jpg) not found in any folder.")

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
