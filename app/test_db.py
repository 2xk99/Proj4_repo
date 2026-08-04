from crud import save_prediction, get_predictions


save_prediction(
    "I love this product, it works perfectly!",
    "positive",
    0.95
)


save_prediction(
    "This was a terrible experience.",
    "negative",
    0.90
)


history = get_predictions()


for item in history:
    print(item)