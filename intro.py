import streamlit as st
import os

st.set_page_config(page_title="My Portfolio", layout="wide")

# ---------- GLOBAL PREMIUM LUXURY CSS CUSTOMIZATION ----------
st.markdown("""
<style>
.stApp { 
    background-color: #1a102f !important; 
    color: #f5f5f7 !important; 
} 
/* Main Page Title */
h1 {
    color: #dfba73 !important; /* Premium Champagne Gold */
    font-weight: 800 !important;
    letter-spacing: 0.5px;
}
/* Section Headers */
h2 { 
    color: #e5c78d !important; /* Soft Satin Gold */
    font-weight: 700 !important; 
} 
/* Subheaders and Project Titles */
h3, h4 { 
    color: #f1dfbb !important; /* Warm Metallic Cream */
    font-weight: 600 !important; 
} 
/* Standard Body Text */
p, span, li, div { 
    color: #f5f5f7 !important; 
    font-size: 16px;
} 
/* Active Interactive Links */
a { 
    color: #dfba73 !important; 
    text-decoration: none !important; 
    font-weight: 600; 
} 
a:hover { 
    text-decoration: underline !important; 
    color: #f1dfbb !important;
}
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
    st.markdown("🔗 **GitHub Link:** [Video Game Market Analysis](https://github.com/roshankshah2005-creator/Video-Game-Market-Analysis/tree/main)")

st.markdown("---")

# ---------- CONTACT SECTION ----------
st.header("Contact Me")
st.markdown("📧 **Email:** roshank.shah2005@gmail.com")
st.markdown("💼 **LinkedIn:** [roshan-kumar-sah-5158653a5](https://www.linkedin.com/in/roshan-kumar-sah-5158653a5)")
st.markdown("🐙 **GitHub:** [roshankshah2005-creator](https://github.com/roshankshah2005-creator)")
