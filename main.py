import streamlit as st
# import pandas as pd
from PIL import Image
import random
from streamlit_extras.switch_page_button import switch_page
from streamlit_extras.let_it_rain import rain



st.set_page_config(
    page_title="WaffleMe",
    page_icon="🧇",
    layout="wide",
)


# Add CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

def remote_css(url):
    st.markdown(f'<link href="{url}" rel="stylesheet">', unsafe_allow_html=True)

local_css("style.css")
remote_css('https://fonts.googleapis.com/css2?family=Afacad:wght@700&display=swap')
# Banner Section
banner_image = Image.open('images/waffle2.png')

st.image(banner_image, width=900)

rain(
    emoji="🧇",
    font_size=54,
    falling_speed=5,
    animation_length="infinite",
)

if st.button('Start Game'):
    switch_page("game")


# st.markdown("<br><br>", unsafe_allow_html=True)

