# Hello there! Susan is a Chat Bot designed to assist deaf people (those who have trouble hearing) to collaborate with their friends, family, or co-workers.
# This project uses the SpeechRecognition and streamlit libraries to function. streamlit is used for the user interface and to display the converted speech to the deaf person.

import pyaudio
import speech_recognition as sp
import streamlit as st
import time

st.title(":blue[Beep Boop, hello there! I'm Susan the Chat Bot 🤖. I was designed to assist deaf people with communicating with others.]")
st.header("Please note that you can exit this program by pressing Ctrl+C at any time.")

run = True
recognize_speech = sp.Recognizer()
recognize_speech.energy_threshold = 5000
while run:
    with sp.Microphone() as source:
        try:
            st.subheader("Please start speaking within the next 20 seconds.")
            text = recognize_speech.listen(source, 10, 10)
            st.subheader("Processing speech.")
            time.sleep(1)
            st.markdown("Speech converted to text: '" +  recognize_speech.recognize_google(text) + "'")
        except:
            st.markdown("We were unable to process your speech. Please speak louder or clearer.")
        time.sleep(2)











