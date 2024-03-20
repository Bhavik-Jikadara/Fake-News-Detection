import streamlit as st
import pickle
import re
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

model = pickle.load(open('model/fake_news_detection_model.pkl', 'rb'))
tfidvect = pickle.load(open('model/tfidfvect.pkl', 'rb'))


st.set_page_config(
    page_title="Fake News Detection",
    page_icon="assets/logo.jpg"
)


st.write("# Fake News Detection")
st.markdown(
    """
        A fake news prediction web application using Machine Learning algorithms deployed using streamlit community cloud.
""")
st.markdown("## Input:")

text = st.text_area(
    label="Enter your text to try it.",
    placeholder="Enter your text to predict whether this is fake or not.",
    height=200
)
st.write(f'You wrote {len(text.split())} words.')


# Load model and vectorizer to predict the output
def predict(text):
    val_tfidvect = tfidvect.transform([text]).toarray()
    prediction = 'FAKE' if model.predict(val_tfidvect) == 0 else 'REAL'
    return prediction


if st.button("Predict"):
    st.markdown("## Output:")
    if predict(text) == "REAL":
        st.markdown("#### Looking Real News📰")
    else:
        st.markdown("#### Looking Spam⚠️News📰")
