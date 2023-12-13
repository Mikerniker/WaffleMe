import streamlit as st
import random

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

def remote_css(url):
    st.markdown(f'<link href="{url}" rel="stylesheet">', unsafe_allow_html=True)


def start_game_btn():
    st.session_state.game_btn = True


def check_score(guess, computer):
    if guess == computer:
        return True


def show_image():
    all_images = [("waffle", "images/waffle.png"), ("hacker", "images/hacker.png")]
    display_img = random.choice(all_images)
    image_path = display_img[1]
    image_choice = display_img[0]
    return image_choice, image_path


def countdown(time_sec, countdown_placeholder):
    if time_sec >= 0:
        mins, secs = divmod(time_sec, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        countdown_placeholder.write(f"#### Time remaining: {timeformat}")
        # time.sleep(1)


def hacker_image():
    hacker_image_paths = ["images/hackerwaffle.png", "images/hackerwaffle3.png"]
    display_img = random.choice(hacker_image_paths)

    return display_img
