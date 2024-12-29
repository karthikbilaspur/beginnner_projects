from sentiment_analysis import analyze_sentiment
from entity_recognition import recognize_entities

def analyze_text(text):
    sentiment_scores = analyze_sentiment(text)
    entities = recognize_entities(text)
    return {
        "sentiment": sentiment_scores,
        "entities": entities
    }