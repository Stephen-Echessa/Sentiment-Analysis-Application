import streamlit as st
from transformers import pipeline

# Call the model I pushed to hugging face
sentiment_model = pipeline(model='chescore/finetuned-sentiment-model-45000-training-examples')

# Develop the UI
st.title('IMDB Sentiment Analysis App')
st.write('Welcome to my sentiment analysis application!')
form = st.form(key='sentiment-form')
user_input = form.text_area('Enter your text')
submit = form.form_submit_button('Submit')

# Predict the sentiment on sumbit
if submit:
    result = sentiment_model(user_input)[0]
    label = result['label']
    score = result['score']
    
    if label == 'LABEL_1':
        st.success(f'Positive sentiment (score: {score})')
    else:
        st.warning(f'Negative sentiment (score: {score})')