import streamlit as st
import pyttsx3
import speech_recognition as sr
import webbrowser
import requests

# Initialize text-to-speech engine
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # 0 = Male, 1 = Female

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        st.info("🎙️ Listening for your command...")
        audio = recognizer.listen(source)
        try:
            command = recognizer.recognize_google(audio)
            st.success(f"✅ You said: {command}")
            return command.lower()
        except sr.UnknownValueError:
            st.error("😕 Sorry, I could not understand.")
        except sr.RequestError:
            st.error("⚠️ Could not request results from speech service.")
    return ""

def get_weather():
    city = "your_city_here"  # e.g., "Karachi"
    api_key = "your_openweather_api_key"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url).json()
    if response["cod"] == 200:
        temp = response["main"]["temp"]
        description = response["weather"][0]["description"]
        result = f"Current temperature in {city} is {temp}°C with {description}."
        st.info(result)
        speak(result)
    else:
        st.error("Couldn't fetch weather data.")

# Streamlit UI
st.title("🔊 Nexa - Your Voice Assistant (Beta)")
st.write("Press the button and speak a command like 'open google' or 'tell me the weather'.")

if st.button("🎤 Activate Nexa"):
    command = listen()

    if "open google" in command:
        speak("Opening Google")
        webbrowser.open("https://www.google.com")

    elif "weather" in command:
        speak("Fetching the weather")
        get_weather()

    else:
        speak("Sorry, I can't do that yet.")
