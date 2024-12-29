import spacy

def recognize_entities(text):
    """
    Recognize entities using spaCy.

    Args:
        text (str): Input text.

    Returns:
        list: Entities (text, label).
    """
    nlp = spacy.load('en_core_web_sm')
    doc = nlp(text)
    entities = [(entity.text, entity.label_) for entity in doc.ents]
    return entities