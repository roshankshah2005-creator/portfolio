import streamlit as st
import base64
import os

st.set_page_config(page_title="My Portfolio", layout="wide")

# ---------- GLOBAL CSS CUSTOMIZATION ----------
st.markdown("""
<style>
    /* 1. Global Background & Font Styling */
    .stApp {
        background-color: #0f0f1a;
        color: #e2e8f0;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    
    /* 2. Styling Headings (About Me, Skills, Projects, Contact) */
    h1, h2, h3, h4 {
        color: #6366f1 !important; /* Beautiful Indigo Neon Color */
        font-weight: 600 !important;
        letter-spacing: 0.5px;
    }
    
    /* 3. Global Styling for Standard Text */
    p, span, li {
        color: #cbd5e1 !important; /* Soft white/gray for better readability */
        font-size: 16px;
    }
    
    /* 4. Link Button Customization */
    a {
        color: #38bdf8 !important; /* Electric Blue for Links */
        text-decoration: none !important;
        font-weight: 500;
        transition: color 0.2s ease-in-out;
    }
    a:hover {
        color: #6366f1 !important; /* Changes to Indigo on Hover */
        text-decoration: underline !important;
    }
</style>
""", unsafe_allow_html=True)


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
    background_style = f'background-image: linear-gradient(rgba(15, 15, 26, 0.6), rgba(15, 15, 26, 0.8)), url("data:image/jpeg;base64,{img_base64}");'
else:
    # Upgraded fallback: A premium neon purple/indigo space gradient
    background_style = 'background: linear-gradient(135deg, #1e1b4b, #311042);'


# ---------- HERO SECTION ----------
st.markdown(f"""
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
    font-size: 55px !
