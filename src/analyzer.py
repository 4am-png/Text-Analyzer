def get_word_frequency(text):
    words = text.lower().split()
    return dict(Counter(words))
