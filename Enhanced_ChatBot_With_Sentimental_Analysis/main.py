import random
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()

# Define a dictionary with intents and responses
intents = {
    "greeting": ["hello", "hi", "hey"],
    "goodbye": ["bye", "see you later", "goodbye"],
    "thanks": ["thank you", "thanks"],
    "help": ["help", "assistance"],
}

responses = {
    "greeting": ["Hi, how are you?", "Hello! How can I assist you?"],
    "goodbye": ["See you later!", "Goodbye!"],
    "thanks": ["You're welcome!", "No problem!"],
    "help": ["How can I assist you today?", "What do you need help with?"],
    "default": ["I didn't understand that.", "Can you please rephrase?"],
    "positive": ["Glad you're feeling good!", "That's awesome!"],
    "negative": ["Sorry to hear that.", "Hope things get better!"],
    "neutral": ["Interesting!", "Okay!"],
}

# Initialize sentiment analyzer
sia = SentimentIntensityAnalyzer()

def preprocess_message(message):
    tokens = nltk.word_tokenize(message)
    tokens = [lemmatizer.lemmatize(token) for token in tokens]
    return ' '.join(tokens).lower()

def analyze_sentiment(message):
    sentiment_scores = sia.polarity_scores(message)
    compound_score = sentiment_scores['compound']
    
    if compound_score >= 0.05:
        return "positive"
    elif compound_score <= -0.05:
        return "negative"
    else:
        return "neutral"

def chatbot(message):
    message = preprocess_message(message)
    sentiment = analyze_sentiment(message)
    
    # Check for matching intents
    for intent, keywords in intents.items():
        for keyword in keywords:
            if keyword in message:
                return random.choice(responses[intent])
    
    # Respond based on sentiment
    if sentiment == "positive" or sentiment == "negative" or sentiment == "neutral":
        return random.choice(responses[sentiment])
    
    # Return default response
    return random.choice(responses["default"])

def main():
    print("Welcome to the chatbot! Type 'quit' to exit.")
    
    while True:
        message = input("You: ")
        
        if message.lower() == "quit":
            break
        
        response = chatbot(message)
        print("Chatbot:", response)

if __name__ == "__main__":
    main()