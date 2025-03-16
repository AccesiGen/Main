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
        /* New Navigation Styles */
        .nav-link {
            padding: 0.75rem 1rem;
            margin: 0.5rem 0;
            border-radius: 8px;
            background-color: rgba(174, 214, 241, 0.1);
            transition: all 0.3s ease;
            text-decoration: none !important;
            display: block;
        }
        .nav-link:hover {
            background-color: rgba(174, 214, 241, 0.2);
            transform: translateX(5px);
        }
        .nav-divider {
            height: 1px;
            background: linear-gradient(to right, transparent, rgba(174, 214, 241, 0.3), transparent);
            margin: 1rem 0;
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
st.markdown("""
    <div style="background-color: rgba(52, 152, 219, 0.1); padding: 1.5rem; border-radius: 10px; margin-bottom: 2rem;">
        <h4>🌟 Welcome to AccessiGen</h4>
        <p>A collection of Chrome extensions designed to make the web more accessible for everyone. 
        Our tools help users with different abilities navigate and interact with websites more effectively.</p>
        <ul>
            <li>💡 <strong>Easy to Install:</strong> Simple one-click installation process</li>
            <li>🔒 <strong>Privacy Focused:</strong> All processing happens locally in your browser</li>
            <li>🆓 <strong>Free & Open Source:</strong> All extensions are free to use and modify</li>
        </ul>
    </div>
""", unsafe_allow_html=True)

# Updated Sidebar with improved navigation and proper section IDs
with st.sidebar:
    st.image("logo_wo_bg.png", width=150, caption=None, use_container_width=True)
    st.markdown('<div class="nav-divider"></div>', unsafe_allow_html=True)
    
    # Navigation header
    st.markdown("#### 🧭 Quick Access")
    
    # Group extensions by featured/regular
    featured_exts = [ext for ext in extensions if ext.get("featured")]
    regular_exts = [ext for ext in extensions if not ext.get("featured")]
    
    # Featured extensions first
    if featured_exts:
        for ext in featured_exts:
            section_id = ext['name'].lower().replace(' ', '-')
            st.markdown(
                f"""<a href="#{section_id}" class="nav-link">
                    ⭐ {ext['name']}
                </a>""",
                unsafe_allow_html=True
            )
    
    st.markdown('<div class="nav-divider"></div>', unsafe_allow_html=True)
    
    # Regular extensions
    for ext in regular_exts:
        section_id = ext['name'].lower().replace(' ', '-')
        st.markdown(
            f"""<a href="#{section_id}" class="nav-link">
                📌 {ext['name']}
            </a>""",
            unsafe_allow_html=True
        )

# Main content
for ext in extensions:
    st.markdown(f"<div id='{ext['name'].lower().replace(' ', '-')}' class='extension-card'>", unsafe_allow_html=True)
    if ext.get("featured"):
        st.markdown("⭐ **FEATURED**")
    st.subheader(f"🚀 {ext['name']}")
    st.markdown(f"*{ext['description']}*")
    st.video(ext["video"])
    
    # Download section
    st.markdown("### Installation")
    col1, col2 = st.columns([2, 2])
    with col1:
        st.markdown("""
        1. Download the ZIP file
        2. Extract the contents
        3. Open Chrome Extensions (chrome://extensions/)
        4. Enable Developer Mode
        5. Click 'Load unpacked'
        6. Select the extracted folder
        """)
    with col2:
        with open(ext["zip"], "rb") as zip_file:
            zip_data = zip_file.read()
            download_stats = f"Size: {len(zip_data)/1024:.1f}KB"
            st.download_button(
                label=f"⬇️ Download {ext['name']}",
                data=zip_data,
                file_name=ext["zip"],
                mime="application/zip",
                help=f"Click to download {ext['name']} extension\n{download_stats}",
                use_container_width=True
            )
        st.markdown(f"*{download_stats}*")
        st.markdown("*Compatible with Chrome v80+*")
    st.markdown("</div>", unsafe_allow_html=True)

# Add smooth scrolling
st.markdown("""
    <style>
        html {
            scroll-behavior: smooth;
        }
    </style>
""", unsafe_allow_html=True)
