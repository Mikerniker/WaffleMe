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
# Links to other Pages

# st.header('Waffle Score: 0')
# st.subheader('Total: 0')
#
# st.markdown("<br>", unsafe_allow_html=True)
#
#
#
# all_images = ["images/waffle.png", "images/hacker.png"]
# display_img = random.choice(all_images)
# print(display_img)
# # quiz_image = Image.open('images/questionmark.png')
# quiz_image = Image.open(display_img)
# st.image(quiz_image, width=900)
#
# col1, col2 = st.columns(2)
#
# with col1:
#     if st.button('Waffle'):
#         st.write('Waffle')
#     else:
#         st.write('Hacker')
#
#
# with col2:
#     if st.button('Hacker'):
#         st.write('Hacker')
#     else:
#         st.write('Hacker')


# with col3:
#     image_login_path = "images/login_btn.png"
#     login_image_base64 = convert_image(image_login_path)
#
#     html = f"<a href='#'><img src='data:image/png;base64,{login_image_base64}'  style='border-radius: 30px;'></a>"
#     st.markdown(html, unsafe_allow_html=True)
#
#     st.write("Admin Login")


st.markdown("<br><br>", unsafe_allow_html=True)

