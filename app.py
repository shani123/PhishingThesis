import streamlit as st
import pickle
import string

# Load model and vectorizer
model = pickle.load(open("model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

# Text cleaning function
def preprocess_text(text):
    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))
    return text

# Streamlit App
st.title("📧 Spam Detector")
st.write("Paste a message below and check if it's SPAM or HAM.")

user_input = st.text_area("Enter your message here:")

if st.button("Check"):
    cleaned = preprocess_text(user_input)
    vectorized = vectorizer.transform([cleaned])
    prediction = model.predict(vectorized)[0]
    if prediction == 1:
        st.error("🚨 This is SPAM!")
    else:
        st.success("✅ This is HAM (not spam).")
