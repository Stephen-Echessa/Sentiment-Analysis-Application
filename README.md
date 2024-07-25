# IMDB Sentiment Analysis App

## Project Overview
The IMDB Sentiment Analysis App is a web-based application designed to classify the sentiment of movie reviews. It was developed using two distinct models: a traditional Naive Bayes model and a state-of-the-art Transformer model. The app is deployed via Streamlit Sharing, providing a user-friendly interface for real-time sentiment analysis. Click the following link and give it a go: https://stevechesa-movie-review-sentiment-analyzer.streamlit.app/

## Dataset
The models were trained on the IMDB dataset, which contains 50,000 movie reviews labeled with positive or negative sentiment.

## Models
1. **Naive Bayes Model**: A classical machine learning model known for its simplicity and effectiveness in text classification tasks.
2. **Transformer Model**: A fine-tuned Transformer-based model, offering superior performance on sentiment analysis tasks. This model was pushed to Hugging Face for deployment.

## Deployment
The application was built and deployed using Streamlit, a powerful framework for building interactive web applications with Python. The Transformer model is hosted on Hugging Face at `chescore/finetuned-sentiment-model-45000-training-examples`, ensuring efficient and scalable inference.

## How to Use
1. Clone the repository.
2. Install the required dependencies using `pip install -r requirements.txt`.
3. Run the Streamlit app with `streamlit run streamlit_app.py`.
4. Enter a movie review in the text area and submit to get the sentiment analysis result.

## Files in the Repository
- `sentiment_analysis.ipynb`: Jupyter notebook containing the data preprocessing, model training, and evaluation code.
- `streamlit_app.py`: Streamlit application code for deploying the sentiment analysis app.
- `IMDB Dataset.csv`: Document containing movie reviews and their sentiments
- `preprocessed_imdb_dataset.csv`: Preprocessed IMDB csv file
- `requirement_txt.csv`: Doc containing libraries to be installed 

## Future Work
- Implement additional models for comparison.
- Improve the user interface for better user experience.
- Add more functionalities like bulk analysis and detailed sentiment scores.

## Conclusion
This project demonstrates the effective use of both traditional and modern NLP techniques in building a sentiment analysis application. By leveraging Streamlit and Hugging Face, it offers a robust and scalable solution for real-time sentiment analysis.

