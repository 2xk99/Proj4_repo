# Airline Sentiment Analysis System

## Overview

This project is an end-to-end sentiment analysis system that classifies airline tweets into three categories:

- Positive
- Neutral
- Negative

The project covers:

- Data preparation
- Text preprocessing
- Feature extraction
- Machine learning model training
- Model evaluation
- Embedding-based improvement
- Model saving
- Database integration
- Prediction history storage

---

## Project Structure

```
Proj4_repo/

├── app/
│   ├── create_db.py
│   ├── crud.py
│   ├── database.py
│   ├── main.py
│   ├── models.py
│   ├── prediction.py
│   ├── test_db.py
│   └── test_prediction.py
│
├── data/
│   ├── Tweets.csv
│   └── database.sqlite
│
├── notebooks/
│   └── Day1.ipynb
│
├── embedding_model.pkl
├── sentiment_model.pkl
│
├── requirements.txt
├── README.md
├── LICENSE
└── .gitignore
```

---

# Technologies Used

- Python
- Pandas
- Scikit-learn
- Sentence Transformers
- Joblib
- SQLAlchemy Core
- SQLite
- Jupyter Notebook

---

# Day 1: Data Preparation and Classical Machine Learning

## Dataset

The project uses an airline tweets dataset.

Important columns:

- `text` : Tweet content
- `airline_sentiment` : Target sentiment label

The target classes are:

- negative
- neutral
- positive

---

## Text Preprocessing

The text data was cleaned using:

- Lowercase conversion
- Removing URLs
- Removing mentions
- Removing special characters
- Removing unnecessary words

---

## Feature Extraction

### TF-IDF

TF-IDF was used to convert text into numerical vectors.

The model learns from the importance of words inside tweets.

Pipeline:

```
Tweet Text
    |
    ↓
TF-IDF Vectorization
    |
    ↓
Machine Learning Model
```

---

# Machine Learning Models

## Naive Bayes

Results:

```
Accuracy: 72.23%
F1 Score: 67.10%
```

---

## Logistic Regression

Results:

```
Accuracy: 78.14%
F1 Score: 76.71%
```

Logistic Regression performed better than Naive Bayes.

---

# Day 2: Advanced Features and Model Deployment

## Sentence Embeddings

To improve performance, sentence embeddings were used.

Embeddings capture the meaning of sentences instead of only word frequency.

The embedding model converts text into numerical vectors that contain semantic information.

---

## Embedding Model Results

Logistic Regression using embeddings achieved:

```
Accuracy: 78.55%
F1 Score: 77.96%
```

The embedding approach improved the results compared with TF-IDF.

---

## Hyperparameter Tuning

Logistic Regression was tuned using GridSearchCV.

The tested parameter was:

```
C = [0.01, 0.1, 1, 10, 100]
```

Best parameter:

```
C = 1
```

---

## Saved Models

The trained models were saved using Joblib:

```
sentiment_model.pkl
embedding_model.pkl
```

These files are used later for predictions without retraining.

---

# Day 3: Database Integration

The sentiment analysis model was integrated with a database to store prediction history.

The project uses SQLite with SQLAlchemy Core.

---

## Database Table

Table name:

```
sentiment_predictions
```

Columns:

| Column | Description |
|---|---|
| id | Unique prediction ID |
| input_text | User text |
| predicted_sentiment | Model prediction |
| prediction_score | Confidence score |
| created_at | Prediction timestamp |

---

## Database Operations

The application supports:

### Creating Predictions

Stores:

- User input text
- Predicted sentiment
- Prediction confidence
- Creation time

### Retrieving History

Retrieves previous sentiment predictions from the database.

---

# Application Workflow

```
User Input

    ↓

main.py

    ↓

prediction.py

    ↓

Embedding Model

    ↓

Sentiment Model

    ↓

Prediction Result

    ↓

SQLAlchemy Core

    ↓

SQLite Database
```

---

# Running the Application

## Activate Virtual Environment

```bash
source venv/bin/activate
```

---

## Install Requirements

```bash
pip install -r requirements.txt
```

---

## Run Application

From the project root:

```bash
python app/main.py
```

---

# Example Predictions

## Positive Example

Input:

```
I love this product, it works perfectly!
```

Output:

```
Sentiment: positive
```

---

## Negative Example

Input:

```
This was a terrible experience. I'll never buy it again.
```

Output:

```
Sentiment: negative
```

---

## Neutral Example

Input:

```
It's okay, not bad but not great either.
```

Output:

```
Sentiment: neutral
```

---

# Testing

The project contains testing files:

```
app/test_db.py
app/test_prediction.py
```

They test:

- Database insertion
- Database retrieval
- Prediction pipeline

---

# Conclusion

This project demonstrates a complete machine learning application pipeline:

- Data preprocessing
- Feature extraction
- Model training
- Model evaluation
- Embedding-based improvement
- Model deployment
- Database integration

The final system can analyze new text inputs, predict sentiment, calculate confidence scores, and store prediction history.