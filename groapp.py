import streamlit as st
import random

# Growth mindset quotes
quotes = [
    "Mistakes are proof that you are trying.",
    "Your abilities can grow with effort and practice.",
    "Challenges are opportunities to learn and improve.",
    "The only limit to your learning is your willingness to grow.",
    "Believe in your ability to develop and succeed."
]

# Daily challenges
challenges = [
    "Reflect on a recent challenge and write down what you learned from it.",
    "Give yourself credit for the effort you put into something today.",
    "Ask for feedback from someone and use it to improve.",
    "Try learning something new that you previously found difficult.",
    "Encourage a friend or colleague to embrace a challenge."
]

st.title("🌱 Growth Mindset Challenge")

st.header("What is a Growth Mindset?")
st.write(
    "A growth mindset is the belief that abilities can be developed through dedication, learning, and effort. "
    "It helps you embrace challenges, learn from mistakes, and persist through difficulties."
)

st.subheader("💡 Growth Mindset Quote of the Day")
st.success(random.choice(quotes))

st.subheader("🎯 Daily Challenge")
st.info(random.choice(challenges))

st.subheader("📝 Reflect on Your Learning")
reflection = st.text_area("What did you learn today?")
if st.button("Submit Reflection"):
    if reflection:
        st.success("Great! Reflecting on your learning helps reinforce a growth mindset.")
    else:
        st.warning("Take a moment to write something before submitting.")

st.subheader("💬 Share Your Thoughts")
st.text_input("What does a growth mindset mean to you?")

st.write("---")
st.write("Keep pushing yourself to grow every day! 🚀")
