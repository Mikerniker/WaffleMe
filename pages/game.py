import streamlit as st
from PIL import Image
import time
from functions import local_css, remote_css, check_score, \
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

if 'attempts' not in st.session_state:
    st.session_state.attempts = 0

if 'game_state' not in st.session_state:
    st.session_state.game_state = 'start'  # Initial game state

if 'user_guess' not in st.session_state:
    st.session_state.user_guess = ''

instructions = st.empty()
waffle_score = st.empty()
total_guesses = st.empty()
countdown_placeholder = st.empty()
final_message = st.empty()
game_placeholder = st.empty()

player_choices = []
display = show_image()
button_counter = 0
hacker_image = Image.open(hacker_image())


def waffle_game():
    global button_counter
    while st.session_state.game_state == 'playing':
        play_game = True
        if play_game:
            instructions.write('## Choose a button, quickly!')
            # Replace the placeholder with some text:
            with game_placeholder.container():
                col1, col2 = st.columns(2)
                with col1:
                    if st.button('Waffle', key=f'waffle_button_{button_counter}'):
                        st.session_state.user_guess = "waffle"
                        player_choices.append("waffle")

                with col2:
                    if st.button('Hacker', key=f'hacker_button_{button_counter}'):
                        st.session_state.user_guess = "hacker"
                        player_choices.append("hacker")

                for col in st.columns(1):
                    with col:
                        user_choice = st.empty()
                        user_choice.write(f'## You chose {st.session_state.user_guess}')
                image_placeholder = st.empty()
                quiz_image = Image.open('images/questionmark.png')
                image_placeholder.image(quiz_image, width=600)

                countdown_on = True
                if countdown_on:
                    for i in range(4, -1, -1):
                        countdown(i, countdown_placeholder)
                        time.sleep(0.5)
                    countdown_on = False

                # Update the image placeholder with the final image
                final_image = Image.open(display[1])
                image_placeholder.image(final_image, width=600)

                if st.session_state.user_guess == "":
                    user_choice.write(f'### No choice was made.')
                    message = "Shenanihacks happen when " \
                              "choices aren't made..." \
                              "your waffles have been stolen!"
                    time.sleep(3)
                    image_placeholder.image(hacker_image, width=600)
                    st.session_state.game_state = 'end'
                    instructions.write('## Game Over!')
                    play_game = False

                else:
                    if check_score(st.session_state.user_guess, display[0]):
                        st.session_state.score += 1
                        message = "You're right, you get waffle points!!"
                        time.sleep(4)
                    else:
                        message = "Wrong choice...you've been shenanihacked and " \
                                  "your waffles have been stolen!"
                        instructions.write('## Game Over!')
                        time.sleep(3)
                        image_placeholder.image(hacker_image, width=600)
                        st.session_state.game_state = 'end'

                        play_game = False

                st.session_state.attempts += 1

                waffle_score.write(f"### Waffle Score 🧇: {st.session_state.score}")
                final_message.write(f"### {message}")
                total_guesses.write(f'### Total Tries: {st.session_state.attempts}')
                st.session_state.user_guess = ""

                if st.session_state.game_state == 'playing':
                    button_counter += 1
                else:
                    time.sleep(4)
                    break

waffle_game()

if st.session_state.game_state == 'end':
    # Reset the game state and user guess for the next round
    st.session_state.game_state = 'start'
    st.session_state.score = 0
    st.session_state.attempts = 0
    st.session_state.user_guess = ""

    # game_placeholder.empty()
    game_placeholder.markdown("")
    time.sleep(2)

for col in st.columns(1):
    with col:
        if st.button('Restart'):
            switch_page("main")
