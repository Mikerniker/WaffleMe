import streamlit as st
from PIL import Image
import random

st.header('Waffle Score: 0')
st.subheader('Total: 0')

st.markdown("<br>", unsafe_allow_html=True)


all_images = ["images/waffle.png", "images/hacker.png"]
display_img = random.choice(all_images)
# quiz_image = Image.open('images/questionmark.png')
quiz_image = Image.open(display_img)
st.image(quiz_image, width=600)

col1, col2 = st.columns(2)

with col1:
    if st.button('Waffle'):
        display_img = random.choice(all_images)
        # quiz_image = Image.open('images/questionmark.png')
        quiz_image = Image.open(display_img)
    # else:
    #     st.write('Hacker')


with col2:
    if st.button('Hacker'):
        st.write('Hacker')
    else:
        st.write('Hacker')
