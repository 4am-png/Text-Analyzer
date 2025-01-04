import string
from collections import Counter

def analyze_text(filepath):
    with open(filepath, 'r') as file:
        text = file.read()

    word_count = count_words(text)
    sentence_count = count_sentences(text)
    char_count = len(text)

    # Remove punctuation for word frequency analysis
    cleaned_text = text.translate(str.maketrans('', '', string.punctuation))
    word_freq = get_word_frequency(cleaned_text)

    return {
        'word_count': word_count,
        'sentence_count': sentence_count,
        'char_count': char_count,
        'word_freq': word_freq
    }

def count_words(text):
    words = text.split()
    return len(words)

def count_sentences(text):
    # Simple sentence split by period, exclamation mark, and question mark
    sentences = text.split('.')
    sentences = [s for s in sentences if s.strip() != '']
    return len(sentences)

def get_word_frequency(text):
    words = text.lower().split()
    return dict(Counter(words))
