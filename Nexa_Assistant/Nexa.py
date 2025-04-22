import streamlit as st
import pyttsx3
import speech_recognition as sr
import pywhatkit
import datetime
import time

# Set up Streamlit UI
st.set_page_config(page_title="Nexa - Voice Assistant", layout="centered")
st.title("🎙️ Nexa - Your Personal Assistant")

# Initialize text-to-speech engine
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # 0 for male, 1 for female

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        speak("Listening...")
        st.info("Listening... Speak now.")
        audio = recognizer.listen(source)
    try:
        command = recognizer.recognize_google(audio)
        st.success(f"You said: {command}")
        return command.lower()
    except sr.UnknownValueError:
        st.error("Sorry, I didn't understand that.")
        return ""
    except sr.RequestError:
        st.error("Speech service is not available.")
        return ""

def process_command(command):
    if "whatsapp" in command:
        speak("Who should I message?")
        person = listen()

        speak("What should I say?")
        message = listen()

        if person and message:
            # Default: send in 1 minute from current time
            now = datetime.datetime.now()
            hour = now.hour
            minute = now.minute + 1
            speak(f"Sending message to {person} saying {message}")
            pywhatkit.sendwhatmsg(f"+92xxxxxxxxxx", message, hour, minute)  # Replace with actual number
            st.success("Message sent!")
        else:
            speak("Couldn't get person or message.")
    
    elif "read message" in command:
        speak("This feature will be added soon.")  # Placeholder
    
    else:
        speak("I can only help with WhatsApp commands right now.")

# Streamlit UI
if st.button("Start Nexa"):
    speak("Hello, I'm Nexa. How can I help you?")
    command = listen()
    if command:
        process_command(command)
