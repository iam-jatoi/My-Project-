# streamlit
import streamlit as st

st.set_page_config(page_title="Growth Mindset Project By Jabbar Jatoi", project_icon="🌟")
st.title("Growth Mindset AI Project By Jabbar Jatoi")

st.header("🚀 Welcome to Your Growth Journey!")
st.write("Embrace challenges, learn from mistakes, and unlock your full potential. This is AI-Powered app helps you build a growth mindset with reflection, challenges and achievments! 🌟")


# Quote Section
st.header("💡Today's Growth Mindset Quote")
st.write("Strive for the Moon. Even if you fail, you will land among the Stars 🌙✨🚀.""- By Jabbar Jatoi")

st.header("🛠️ What's Your Challenge Today?")
user_input = st.text_input("Describe a challenge you're facing: ")

# Condition
if user_input:
    st.success(f"😩 You're facing: {user_input}. Keep pushing forward towards your goal! 🎯")
else:
    st.warning("Tell us about your challenge to get started!")

# Reflexing# 
st.header("🧠 Reflect In Your Learning")
reflection = st.text_area("Write your reflections here: ")

if reflection:
    st.success(f"✨ great Insight! Your reflection {reflection}")
else:
    st.info("Reflecting on past experience help you grow! share your difficulties")

# Achievement
st.header("🏆 Celebrate Your Wins!")
acheivment = st.text_input("Share something you've recently accompalished: ")

if acheivment:
    st.success(f"🎉 Amazing! You acheived: {acheivment}")
else:
    st.info("Big or Small, every acheivment counts! share one now 🤩")


# Footer
st.write("- - -")
st.write("🚀 Keep believing in yourself. Growth is a journey, not a destination! 🌟")
st.write("**⛔ Created By Jabbar Jatoi**") 










