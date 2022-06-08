from transformers import pipeline
import fire


def sentiment_analysis(text: str):
    try:
        model = pipeline("text-classification", model="./model")
    except: 
        model = pipeline("text-classification", model="distilbert-base-uncased-finetuned-sst-2-english")
    return model(text)


if __name__ == "__main__":
    fire.Fire(sentiment_analysis)