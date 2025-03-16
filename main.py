import streamlit as st

# Page title
st.title("My Chrome Extensions")

# List of extensions with video previews and downloads
extensions = [
    {"name": "Extension 1", "video": "AirMouse.mp4", "zip": "extension1.zip"},
    {"name": "Extension 2", "video": "video2.mp4", "zip": "extension2.zip"},
    {"name": "Extension 3", "video": "video3.mp4", "zip": "extension3.zip"},
    {"name": "Extension 4", "video": "video4.mp4", "zip": "extension4.zip"}
]

# Loop through extensions and display content
for ext in extensions:
    st.subheader(ext["name"])
    st.video(ext["video"])
    
    # Load ZIP file
    with open(ext["zip"], "rb") as zip_file:
        zip_bytes = zip_file.read()
    
    # Download button
    st.download_button(
        label=f"Download {ext['name']}",
        data=zip_bytes,
        file_name=ext["zip"],
        mime="application/zip"
    )
    st.markdown("---")
