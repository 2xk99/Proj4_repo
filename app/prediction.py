import os
import joblib

from crud import save_prediction


# Find project root directory
BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)


# Paths to saved Day 2 models
MODEL_PATH = os.path.join(
    BASE_DIR,
    "sentiment_model.pkl"
)

EMBEDDING_PATH = os.path.join(
    BASE_DIR,
    "embedding_model.pkl"
)


# Load models
model = joblib.load(
    MODEL_PATH
)

embedding_model = joblib.load(
    EMBEDDING_PATH
)



def predict_and_save(text):

    # Convert text into embedding
    embedding = embedding_model.encode(
        [text]
    )


    # Predict sentiment
    sentiment = model.predict(
        embedding
    )[0]


    # Get prediction confidence
    score = max(
        model.predict_proba(
            embedding
        )[0]
    )


    # Store result in database
    save_prediction(
        text,
        sentiment,
        float(score)
    )


    return {
        "input_text": text,
        "predicted_sentiment": sentiment,
        "prediction_score": float(score)
    }