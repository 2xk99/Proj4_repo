from datetime import datetime

from sqlalchemy import select

from database import engine
from models import sentiment_predictions


# Create a new prediction record
def save_prediction(
    text,
    sentiment,
    score
):

    query = sentiment_predictions.insert().values(

        input_text=text,

        predicted_sentiment=sentiment,

        prediction_score=score,

        created_at=datetime.utcnow()

    )


    with engine.connect() as conn:

        conn.execute(query)

        conn.commit()



# Retrieve all prediction history
def get_predictions():

    query = select(
        sentiment_predictions
    )


    with engine.connect() as conn:

        result = conn.execute(query)

        rows = result.fetchall()


    return rows