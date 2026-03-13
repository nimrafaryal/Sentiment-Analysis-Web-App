import streamlit as st
from transformers import pipeline

# Load sentiment-analysis pipeline
@st.cache_resource
def load_model():
    return pipeline("sentiment-analysis")

analyzer = load_model()

# Streamlit app UI
st.title("🧠 Sentiment Analysis App")
st.write("Enter text to analyze the sentiment (Positive/Negative)")

user_input = st.text_area("Your text:")

if st.button("Analyze"):
    if user_input.strip() == "":
        st.warning("Please enter some text.")
    else:
        with st.spinner("Analyzing..."):
            result = analyzer(user_input)
            label = result[0]['label']
            score = result[0]['score']
            st.success(f"**Sentiment:** {label}  \n**Confidence:** {score:.2f}")
