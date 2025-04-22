import streamlit as st
from streamlit_webrtc import webrtc_streamer, AudioProcessorBase
import speech_recognition as sr
from gtts import gTTS
import os
import tempfile
import webbrowser
import requests
import json

# Set up Streamlit page
st.set_page_config(page_title="Nexa - Voice Assistant", page_icon="🎤", layout="centered")
st.title("🎙️ Nexa - Your Female Voice Assistant")

# Replace with your OpenWeatherMap API Key
WEATHER_API_KEY = "YOUR_OPENWEATHER_API_KEY"
CITY_NAME = "Karachi"  # You can make this dynamic later

# Function to speak response using gTTS
def speak(text):
    tts = gTTS(text=text, lang='en')
    with tempfile.NamedTemporaryFile(delete=True, suffix=".mp3") as fp:
        tts.save(fp.name)
        st.audio(fp.name, format='audio/mp3', autoplay=True)

# Function to fetch weather
def get_weather():
    try:
        url = f"https://api.openweathermap.org/data/2.5/weather?q={CITY_NAME}&appid={WEATHER_API_KEY}&units=metric"
        response = requests.get(url)
        data = response.json()
        if data["cod"] == 200:
            temp = data["main"]["temp"]
            desc = data["weather"][0]["description"]
            return f"The current temperature in {CITY_NAME} is {temp}°C with {desc}."
        else:
            return "Sorry, I couldn't fetch the weather."
    except:
        return "There was an error retrieving the weather."

# Recognize command from mic input
def recognize_speech():
    recognizer = sr.Recognizer()
    mic = sr.Microphone()

    with mic as source:
        st.info("🎧 Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio)
        st.success(f"🗣️ You said: {command}")
        return command.lower()
    except sr.UnknownValueError:
        st.error("❌ Could not understand audio")
    except sr.RequestError:
        st.error("❌ Could not request results")
    return ""

# Handle command
def handle_command(command):
    if "open google" in command:
        speak("Opening Google")
        webbrowser.open("https://www.google.com")
    elif "weather" in command:
        weather = get_weather()
        st.write(weather)
        speak(weather)
    else:
        speak("Sorry, I didn't understand the command.")

# Streamlit interaction
if st.button("🎤 Talk to Nexa"):
    cmd = recognize_speech()
    if cmd:
        handle_command(cmd)

st.write("---")
st.markdown("Made with ❤️ by Jabbar Jatoi")
