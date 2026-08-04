from prediction import predict_and_save
from crud import get_predictions


def main():

    print("=== Sentiment Analysis System ===")

    text = input("\nEnter your text: ")


    # Run AI prediction and save to database
    result = predict_and_save(text)


    print("\nPrediction Result:")
    print("------------------")

    print(
        "Text:",
        result["input_text"]
    )

    print(
        "Sentiment:",
        result["predicted_sentiment"]
    )

    print(
        "Score:",
        result["prediction_score"]
    )


    print("\nPrediction History:")
    print("------------------")


    history = get_predictions()


    for row in history:
        print(row)



if __name__ == "__main__":
    main()