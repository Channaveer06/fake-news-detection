# Fake News Detection using Machine Learning

This project classifies news articles as Fake or Real using
Natural Language Processing and Machine Learning.

## Approach
- Text preprocessing and cleaning
- Feature extraction using TF-IDF
- Classification using Logistic Regression

## Model Details
- Vectorizer: TF-IDF (5000 features)
- Classifier: Logistic Regression

## How to Run
1. Install dependencies:
   pip install -r requirements.txt
2. Run the app:
   python app.py

## Example
Enter news text when prompted and the model will predict:
- Fake News
- Real News

## Note
The model predicts based on learned text patterns and does not verify real-world facts.
