import streamlit as st
# import pandas as pd
from PIL import Image
import random
from streamlit_extras.switch_page_button import switch_page
from streamlit_extras.let_it_rain import rain
from functions import local_css, remote_css


st.set_page_config(
    page_title="WaffleMe",
    page_icon="🧇",
    layout="wide",
)


# Add CSS
local_css("style.css")
remote_css('https://fonts.googleapis.com/css2?family=Afacad:wght@700&display=swap')

# Banner Section
banner_image = Image.open('images/waffle2.png')

st.image(banner_image, width=900)

# rain(
#     emoji="🧇",
#     font_size=54,
#     falling_speed=5,
#     animation_length="infinite",
# )
# st.write('# Is it a waffle or a hacker?')
st.write('## Take your best guess at whats behind the question mark '
         'and select a button before the time runs out, '
         'or risk losing your delicious waffles to a mischievous hacker!')

# st.write('## Make your best guess at whats behind the question'
#          ' mark. Choose a button before the time runs out '
#          'or a hacker will steal your waffles! ')

if st.button('Start Game'):
    st.session_state.game_state = 'playing'
    switch_page("game")
# if st.button('Start Game'):
#     switch_page("start_game")


# st.markdown("<br><br>", unsafe_allow_html=True)

