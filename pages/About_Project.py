import streamlit as st
import time
import numpy as np

st.set_page_config(page_title="About project", page_icon="")

st.markdown("# About project")
st.write(
    """
    ### Project Description
    The spread of fake news has become a major concern in today’s society, and it is important to be able to identify news articles that are not based on facts or are intentionally misleading. In this project, we will use machine learning to classify news articles as either real or fake based on their content. By identifying fake news articles, we can prevent the spread of misinformation and help people make more informed decisions.

    This project is relevant to the media industry, news outlets, and social media platforms that are responsible for sharing news articles. Classifying news articles as real or fake can help these organizations improve their content moderation and reduce the spread of fake news.

    ### Problem Statement
    This project aims to classify news articles as real or fake based on their content. Specifically, we will use machine learning to build a model to predict whether a given news article is real or fake based on its text.

    ### Learning objectives:
    * Understand the basics of natural language processing (NLP) and how it can be used to preprocess textual data for machine learning models.
    * Learn how to use the CountVectorizer class from the scikit-learn library to convert text data into numerical feature vectors.
    * Build a fake news detection system using machine learning algorithms such as logistic regression and evaluate its performance.

    ### Prerequisites
    To complete this project, you should understand Python programming, data manipulation, visualization libraries such as Pandas and Matplotlib, and machine learning libraries such as Scikit-Learn. Additionally, some background knowledge of natural language processing (NLP) techniques and text classification methods would be helpful.

    ### Resources
    - Check out  [Dataset](https://www.kaggle.com/datasets/bhavikjikadara/fake-news-detection)
    - Jump into our [GitHub](https://github.com/Bhavik-Jikadara/Fake-News-Detection)
    """
)