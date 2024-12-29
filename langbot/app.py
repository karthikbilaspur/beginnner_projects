from flask import Flask, request, jsonify
import nltk
from nltk.stem import WordNetLemmatizer
from transformers import AutoModelForSequenceClassification, AutoTokenizer
import langdetect
from google.cloud import translate

app = Flask(__name__)

# Pre-trained language model
model_name = "distilbert-base-uncased-finetuned-sst-2-english"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)

# Language detection and translation
translate_client = translate.Client()

# NLP preprocessing
nltk.download('wordnet')
lemmatizer = WordNetLemmatizer()

def preprocess_text(text):
    tokens = nltk.word_tokenize(text)
    tokens = [lemmatizer.lemmatize(token) for token in tokens]
    return ' '.join(tokens)

def detect_language(text):
    return langdetect.detect(text)

def translate_text(text, target_language):
    result = translate_client.translate(text, target_language=target_language)
    return result['translatedText']

# Contextual understanding
context = {}

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    user_message = data['message']
    user_language = data['language']

    detected_language = detect_language(user_message)

    if detected_language != 'en':
        translated_message = translate_text(user_message, 'en')
        user_message = translated_message

    # Conversational logic
    context[user_message] = nltk.sentiment.vader.SentimentIntensityAnalyzer().polarity_scores(user_message)['compound']

    # Response generation
    response = ''
    if context[user_message] > 0.05:
        response = 'Positive sentiment detected!'
    elif context[user_message] < -0.05:
        response = 'Negative sentiment detected!'
    else:
        response = 'Neutral sentiment detected!'

    # Translate response back to user's language
    if detected_language != 'en':
        response = translate_text(response, detected_language)

    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True)