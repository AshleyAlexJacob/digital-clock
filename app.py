import streamlit as st
from datetime import datetime
import time

# Page config
st.set_page_config(page_title="Digital Clock", layout="centered")

# Title
st.title("🕒 Digital Clock 2.0")

# Hide Streamlit's default menu and footer
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

# Create a placeholder for the clock
clock_placeholder = st.empty()

# Run the clock
while True:
    now = datetime.now().strftime("%H:%M:%S")
    clock_placeholder.markdown(f"<h1 style='text-align: center; color: white;'>{now}</h1>", unsafe_allow_html=True)
    time.sleep(1)
