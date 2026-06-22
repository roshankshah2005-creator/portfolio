import streamlit as st
import os

st.set_page_config(page_title="My Portfolio", layout="wide")

# ---------- FORCED LUXURY SYSTEM CSS CUSTOMIZATION ----------
st.markdown("""
<style>
.stApp { 
    background-color: #1a102f !important; 
    color: #f5f5f7 !important; 
} 

/* CUSTOM GLOBAL BYPASS FOR MASSSIVE PORTFOLIO HEADER */
.master-header {
    color: #dfba73 !important; /* Premium Champagne Gold */
    font-weight: 900 !important; 
    font-size: 80px !important; 
    line-height: 1.1 !important;
    letter-spacing: -2px !important;
    margin-top: 20px !important;
    margin-bottom: 5px !important;
    font-family: sans-serif !important;
}

/* SHIFTED TOWARD THE CENTER UNDER THE MAIN HEADER */
.heavy-subheader {
    color: #f1dfbb !important; /* Warm Metallic Cream */
    font-weight: 800 !important; 
    font-size: 26px !important; 
    margin-top: 0px !important;
    margin-bottom: 35px !important;
    letter-spacing: 0.3px;
    padding-left: 20px !important;
}

/* Section Headers scaled slightly to match the larger body text */
h2 { 
    color: #e5c78d !important; /* Soft Satin Gold */
    font-weight: 800 !important; 
    font-size: 34px !important;
} 

/* Project Titles scaled slightly */
h3, h4 { 
    color: #f1dfbb !important; /* Warm Metallic Cream */
    font-weight: 700 !important; 
    font-size: 24px !important;
} 

/* ENHANCED BODY TEXT SIZE (LOCKED TO 20px WITH OPTIMIZED LINE HEIGHT) */
p, span, li, div { 
    color: #f5f5f7 !important; 
    font-size: 20px !important; 
    line-height: 1.6 !important; 
} 

/* Active Interactive Links */
a { 
    color: #dfba73 !important; 
    text-decoration: none !important; 
    font-weight: 700 !important; 
} 
a:hover { 
    text-decoration: underline !important; 
    color: #f1dfbb !important;
}
</style>
""", unsafe_allow_html=True)

# ---------- TITLE & HERO SECTION ----------
st.markdown('<div class="master-header">Roshan\'s Portfolio</div>', unsafe_allow_html=True)
st.markdown('<div class="heavy-subheader">Chemical Engineering Student | Data Science Enthusiast</div>', unsafe_allow_html=True)

st.markdown("---")

# ---------- ABOUT ME SECTION ----------
col1, col2 = st.columns([1, 2.5])

images_dir = "./images"
photo_path = os.path.join(images_dir, "image.
