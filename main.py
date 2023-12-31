import streamlit as st
from PIL import Image
from streamlit_extras.switch_page_button import switch_page
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

st.write('#### Take your best guess at whats behind the question mark '
         'and select a button before the time runs out, '
         'or risk losing your delicious waffles to a mischievous hacker!')

for col in st.columns(1):
    with col:
        if st.button('Start'):
            st.session_state.game_state = 'playing'
            switch_page("game")


# st.markdown("<br><br>", unsafe_allow_html=True)

