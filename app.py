import pickle

with open("fake_news_model.pkl", "rb") as f:
    model = pickle.load(f)

with open("tfidf_vectorizer.pkl", "rb") as f:
    tfidf = pickle.load(f)

def predict_news(text):
    text = text.lower()
    text_tfidf = tfidf.transform([text])
    pred = model.predict(text_tfidf)[0]
    return "Fake News" if pred == 1 else "Real News"

if __name__ == "__main__":
    print("Fake News Detection App")
    text = input("Enter news text: ")
    print("Prediction:", predict_news(text))
