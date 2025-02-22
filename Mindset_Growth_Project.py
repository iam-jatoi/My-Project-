# streamlit
import streamlit as st

st.set_page_config(page_title="Growth Mindset Project By Jabbar Jatoi")
st.title("🌱 Growth Mindset AI Project By Jabbar Jatoi")

st.header("🚀 Welcome to Your Growth Journey!")
st.write("Embrace Challenges, Learn From Mistakes, And Unlock Your Full Potential. This Is AI-Powered App Helps You Build a Growth Mindset With Reflection, Challenges And Achievments! 🌟")


# Quote Section
st.header("💡Today's Growth Mindset Quote")
st.write("Strive For The Moon. Even If You Fail, You Will Land Among The Stars 🌙✨🚀.""- By Jabbar Jatoi")

st.header("🛠️ What's Your Challenge Today?")
user_input = st.text_input("Describe a Challenge You're Facing: ")

# Condition
if user_input:
    st.success(f"😩 You're Facing: {user_input}. Keep Pushing Forward Towards Your Goal! 🎯")
else:
    st.warning("Tell Us About Your Challenge to Get Started!")

# Reflexing# 
st.header("🧠 Reflect In Your Learning!")
reflection = st.text_area("Write Your Reflections Here: ")

if reflection:
    st.success(f"✨ Great Insight! Your Reflection {reflection}")
else:
    st.info("Reflecting On Past Experience Help You Grow! Share Your Difficulties.")

# Achievement
st.header("🏆 Celebrate Your Wins!")
acheivment = st.text_input("Share Something You've Recently Accomplished: ")

if acheivment:
    st.success(f"🎉 Amazing! You Acheived: {acheivment}")
else:
    st.info("Big or Small, Every Acheivment Counts! Share One Now! 🤩")


# Footer
st.write("- - -")
st.write("🚀 Keep Believing In Yourself. Growth Is a Journey, Not a Destination! 🌟")
st.write("**⛔ Created By Jabbar Jatoi**") 










