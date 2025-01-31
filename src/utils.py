import string


def clean_text(text):
    """
    Cleans the text by removing punctuation and converting to lowercase.
    """
    return text.translate(str.maketrans("", "", string.punctuation)).lower()
