import streamlit as st
from PIL import Image
import random
import time
from functions import local_css, remote_css, start_game_btn, check_score, \
    show_image, countdown, hacker_image
from streamlit_extras.switch_page_button import switch_page

st.set_page_config(
    page_title="WaffleMe",
    page_icon="🧇",
    layout="wide",
)

# ADD CSS
local_css("style.css")
remote_css('https://fonts.googleapis.com/css2?family=Afacad:wght@700&display=swap')


# Create session state variables
if 'score' not in st.session_state:
    st.session_state.score = 0

if 'game_state' not in st.session_state:
    st.session_state.game_state = 'start'  # Initial game state

if 'game_btn' not in st.session_state:
    st.session_state.game_btn = False


st.write('# Choose a button, quickly!')

user_guess = ""
player_choices = []
display = show_image()
button_counter = 0
hacker_image = Image.open(hacker_image())
game_placeholder = None


while st.session_state.game_state == 'playing':
    # button_counter = 0
    play_game = True
    if play_game:
        # game_placeholder = st.empty()

    # Replace the placeholder with some text:
        with game_placeholder.container():
            col1, col2 = st.columns(2)
            with col1:
                if st.button('Waffle', key=f'waffle_button_{button_counter}'):
                    user_guess = "waffle"
                    player_choices.append("waffle")

            with col2:
                if st.button('Hacker', key=f'hacker_button_{button_counter}'):
                    user_guess = "hacker"
                    player_choices.append("hacker")

            waffle_score = st.empty()
            user_choice = st.empty()
            user_choice.write(f'### You chose {user_guess}')
            total_guesses = st.empty()
            final_message = st.empty()
            countdown_placeholder = st.empty()
            image_placeholder = st.empty()
            quiz_image = Image.open('images/questionmark.png')
            image_placeholder.image(quiz_image, width=600)

            countdown_on = True
            if countdown_on:
                for i in range(10, -1, -1):
                    countdown(i, countdown_placeholder)
                    time.sleep(0.5)
                countdown_on = False

            # Update the image placeholder with the final image
            final_image = Image.open(display[1])
            image_placeholder.image(final_image, width=600)

            if user_guess == "":
                # User did not choose any button
                user_choice.write(f'### No choice was made.')
                message = "Shenanihacks can't happen when " \
                          "choices aren't made..." \
                          "your waffles have been stolen!"
                time.sleep(3)
                image_placeholder.image(hacker_image, width=600)
                st.session_state.game_state = 'end'
                play_game = False


            else:
                if check_score(user_guess, display[0]):
                    st.session_state.score += 1
                    message = "You're right, you get waffle points!!"
                else:
                    message = "Wrong choice...you've been shenanihacked and " \
                              "your waffles have been stolen!"
                    time.sleep(3)
                    image_placeholder.image(hacker_image, width=600)
                    st.session_state.game_state = 'end'
                    play_game = False

            waffle_score.write(f"## Waffle Score 🧇: {st.session_state.score}")
            final_message.write(f"### {message}")
            total_guesses.write(f'Total Tries: {len(player_choices)}')
            user_guess = ""

            if st.session_state.game_state == 'playing':
                button_counter += 1
            else:
                time.sleep(4)
                break

if st.session_state.game_state == 'end':
    # Reset the game state and user guess for the next round
    st.session_state.game_state = 'start'
    st.session_state.score = 0
    user_guess = ""
            # REVIEW

if st.button('Restart'):
    st.write("Restart button clicked!")
    game_placeholder.empty()
    switch_page("main")


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