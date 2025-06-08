import streamlit as st
import base64
from typing import Optional

def inject_custom_css(
    bg_image_path: str,
    css_path: str = "style.css"
):
    """
    Inject custom CSS with background image
    
    Parameters:
    - bg_image_path: Path to background image file
    - css_path: Path to CSS file (default: "style.css")
    """
    # Read and encode background image
    try:
        with open(bg_image_path, "rb") as bg_file:
            bg_base64 = base64.b64encode(bg_file.read()).decode()
    except FileNotFoundError:
        st.error(f"Background image not found: {bg_image_path}")
        return

    # Read CSS file
    try:
        with open(css_path, "r", encoding="utf-8") as css_file:
            css_content = css_file.read()
    except FileNotFoundError:
        st.error(f"CSS file not found: {css_path}")
        return

    # Inject the CSS with image
    st.markdown(
        f"<style>{css_content.replace('{{BACKGROUND_IMAGE}}', bg_base64)}</style>",
        unsafe_allow_html=True
    )