import streamlit as st
import base64
import os

st.set_page_config(page_title="My Portfolio", layout="wide")

# ---------- AUTO-SEARCH IMAGE ENGINE ----------
def find_and_encode_image(filename):
    """
    Scans the entire repository directory tree to find the filename,
    preventing any crash and handling location shifts perfectly.
    """
    # Search recursively starting from the main execution folder
    for root, dirs, files in os.walk("."):
        if filename in files:
            full_path = os.path.join(root, filename)
            with open(full_path, "rb") as f:
                data = f.read()
            return base64.b64encode(data).decode(), None
            
    # If not found anywhere, return a list of folders we found to debug
    all_folders = [root for root, dirs, files in os.walk(".")]
    return None, all_folders

# Run the search for your files
bg_encoded, debug_folders_bg = find_and_encode_image("oip.jpg")
profile_encoded, debug_folders_prof = find_and_encode_image("image.jpg")

# Set up background style safely based on search results
if bg_encoded:
    background_style = f'background-image: url("data:image/jpg;base64,{bg_encoded}");'
else:
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

# ---------- DIAGNOSTIC BAR (Only shows if files are genuinely missing) ----------
if not bg_encoded or not profile_encoded:
    st.error("⚠️ File Search Diagnostic Engine Mode Active")
    st.write("The files could not be detected in any repository directory. Here is the current structure Streamlit sees:")
    if debug_folders_bg:
        st.json(debug_folders_bg)

# ---------- ABOUT ----------
col1, col2 = st.columns([1, 2])

with col1:
    if profile_encoded:
        st.markdown(f'<img src="data:image/jpg;base64,{profile_encoded}" width="200" style="border-radius:10px;">', unsafe_allow_html=True)
    else:
        st.warning("👤 Profile image ('image.jpg') missing.")

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
