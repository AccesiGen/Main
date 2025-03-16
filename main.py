import streamlit as st

# Custom CSS
st.markdown("""
    <style>
        .main {
            padding: 2rem;
        }
        .stTitle {
            color: #2E4053;
            text-align: center;
            padding-bottom: 2rem;
        }
        .extension-card {
            background-color: #f8f9fa;
            padding: 2rem;
            border-radius: 10px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            margin-bottom: 2rem;
        }
        .sidebar .sidebar-content {
            background-color: #2E4053;
            color: white;
        }
        .sidebar .sidebar-content a {
            color: #AED6F1;
        }
        .download-btn {
            background-color: #3498DB;
            color: white;
            padding: 0.5rem 1rem;
            border-radius: 5px;
            text-decoration: none;
        }
    </style>
""", unsafe_allow_html=True)

# Add CSS for logo
st.markdown("""
    <style>
        .sidebar-logo {
            margin-bottom: 20px;
            text-align: center;
        }
        .sidebar-logo img {
            max-width: 150px;
            border-radius: 10px;
        }
    </style>
""", unsafe_allow_html=True)

# List of extensions with descriptions
extensions = [
    {
        "name": "Cognitive UI",
        "video": "CognitiveUI.mp4",
        "zip": "CognitiveUI-main.zip",
        "description": "Adaptive interface that responds to user's cognitive load",
        "featured": True
    },
    {
        "name": "AirMouse",
        "video": "AirMousee.mp4",
        "zip": "AirMouse-main.zip",
        "description": "Control your cursor with hand gestures using your webcam",
        "featured": False
    },
    {
        "name": "Video to Sign Language",
        "video": "Vid2SL.mp4",
        "zip": "Vid2SL-main.zip",
        "description": "Convert video content to sign language in real-time",
        "featured": False
    },
    {
        "name": "Voice Navigation",
        "video": "VC.mp4",
        "zip": "VoiceCommand-main.zip",
        "description": "Navigate websites using voice commands",
        "featured": False
    }
]

# Page title
st.title("AccessiGen - Generating Accessibility For All")

# Sidebar with logo
with st.sidebar:
    st.image("logo.jpg", width=150, caption=None, use_container_width=True)
    st.markdown("---")
    for ext in extensions:
        st.markdown(f"[📌 {ext['name']}](#{ext['name'].lower().replace(' ', '-')})")

# Main content
for ext in extensions:
    st.markdown(f"<div id='{ext['name'].lower().replace(' ', '-')}' class='extension-card'>", unsafe_allow_html=True)
    if ext.get("featured"):
        st.markdown("⭐ **FEATURED**")
    st.subheader(f"🚀 {ext['name']}")
    st.markdown(f"*{ext['description']}*")
    st.video(ext["video"])
    
    col1, col2 = st.columns([4, 1])
    with col2:
        with open(ext["zip"], "rb") as zip_file:
            st.download_button(
                label=f"⬇️ Download",
                data=zip_file.read(),
                file_name=ext["zip"],
                mime="application/zip",
                use_container_width=True
            )
    st.markdown("</div>", unsafe_allow_html=True)

# Add smooth scrolling
st.markdown("""
    <style>
        html {
            scroll-behavior: smooth;
        }
    </style>
""", unsafe_allow_html=True)
