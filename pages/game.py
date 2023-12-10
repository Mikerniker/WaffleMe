import streamlit as st
from PIL import Image
import random
import time

st.set_page_config(
    page_title="WaffleMe",
    page_icon="🧇",
    layout="wide",
)

# Create a session state variable
if 'score' not in st.session_state:
    st.session_state.score = 0


st.header('Is it a waffle or a hacker?')
st.subheader(f'Waffle Score: {st.session_state.score}')
st.subheader('Total: 0')

st.markdown("<br>", unsafe_allow_html=True)

col1, col2 = st.columns(2)

user_guess = ""
player_choices = []
# score = 0


def check_score(guess, computer):
    if guess == computer:
        return True


def show_image():
    all_images = [("waffle", "images/waffle.png"), ("hacker", "images/hacker.png")]
    display_img = random.choice(all_images)
    image_path = display_img[1]
    image_choice = display_img[0]
    # quiz_image = Image.open(image_path)
    return image_choice, image_path

# def countdown(time_sec):
#     if time_sec >= 0:
#         mins, secs = divmod(time_sec, 60)
#         timeformat = '{:02d}:{:02d}'.format(mins, secs)
#         print(f'\r{timeformat}', end='')  #pycharm
#         time.sleep(1)
#         time_sec -= 1


def countdown(time_sec):
    if time_sec >= 0:
        mins, secs = divmod(time_sec, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        return timeformat




display = show_image()

with col1:
    if st.button('Waffle'):
        # display_img = random.choice(all_images)

        user_guess = "waffle"
        # st.write('You chose Waffle')
        player_choices.append("waffle")
        st.write(f'You chose {user_guess}')
        # if check_score(user_guess, display[0]):
        #     st.session_state.score += 1

with col2:
    if st.button('Hacker'):
        user_guess = "hacker"
        # st.write('You chose Hacker')
        player_choices.append("hacker")
        st.write(f'You chose {user_guess}')
        # if check_score(user_guess, display[0]):
        #     st.session_state.score += 1


if check_score(user_guess, display[0]):
    st.session_state.score += 1

        # if check_score(display[0], player_choices):
        #     score += 1

countdown_placeholder = st.empty()

for i in range(10, -1, -1):
    time_str = countdown(i)
    countdown_placeholder.write(f"Time remaining: {time_str}")
    time.sleep(1)

game_on = True

if game_on:
    quiz_image = Image.open(display[1])
    st.image(quiz_image, width=600)
else:
    quiz_image = Image.open('images/questionmark.png')
    st.image(quiz_image, width=600)
st.write(f"Score is: {st.session_state.score} ")
# player_choices = []

# ORIGINAL

# img, pth = show_image()
# quiz_image = Image.open(pth)
# st.image(quiz_image, width=600)
# display.append(img)
# print(display)
#
# #player_choices = []
# score = 0

# check_score(display, player_choices)



# # Create a session state variable
# if 'test' not in st.session_state:
#     st.session_state.test = 5
#
# if st.button('Click me'):
#     st.write(f"Test is: {st.session_state.test}")
#     st.session_state.test -= 1
# test = 5
# if st.button('Click me'):
#     st.write(f"Test is: {test} ")
#     test -= 0


# quiz_image = Image.open('images/questionmark.png')
# st.image(quiz_image, width=600)