import sys
import os
from src.analyzer import analyze_text
import matplotlib.pyplot as plt


def main():
    if len(sys.argv) != 2:
        print("Usage: python main.py <textfile>")
        sys.exit(1)

    filepath = sys.argv[1]

    if not os.path.isfile(filepath):
        print(f"File {filepath} does not exist.")
        sys.exit(1)

    result = analyze_text(filepath)

    print(f"Word count: {result['word_count']}")
    print(f"Sentence count: {result['sentence_count']}")
    print(f"Character count: {result['char_count']}")

    # Generate the word frequency graph
    generate_word_frequency_graph(result["word_freq"])


def generate_word_frequency_graph(word_freq):
    words = list(word_freq.keys())
    frequencies = list(word_freq.values())

    plt.figure(figsize=(10, 6))
    plt.bar(words, frequencies)
    plt.title("Word Frequency")
    plt.xlabel("Words")
    plt.ylabel("Frequency")
    plt.xticks(rotation=90)
    plt.tight_layout()
    plt.savefig("output/word_frequency.png")
    print("Word frequency graph saved as 'output/word_frequency.png'")


if __name__ == "__main__":
    main()
