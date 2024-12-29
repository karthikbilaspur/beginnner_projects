import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

def analyze_sentiment(text):
    """
    Analyze sentiment using VADER.

    Args:
        text (str): Input text.

    Returns:
        dict: Sentiment scores.
    """
    sia = SentimentIntensityAnalyzer()
    scores = sia.polarity_scores(text)
    return scores