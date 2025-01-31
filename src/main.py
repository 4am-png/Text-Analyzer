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
    generate_word_frequency_graph(result['word_freq'])
