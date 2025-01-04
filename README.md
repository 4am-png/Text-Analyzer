```markdown
# Text Analyzer

A simple text analysis tool written in **Python** and **Go** that counts words, sentences, and characters in a text file. It also identifies the most frequent words and generates a word frequency graph using **matplotlib** in Python.

## Features
- Count words, sentences, and characters in a text file.
- Identify the most common words.
- Generate a word frequency graph (using `matplotlib` in Python).
- Option to run the analysis in both Python and Go.

## Prerequisites
- Python 3.x (for Python version)
- Go (for Go version)
- **matplotlib** (for Python) for generating the word frequency graph.

## Installation

### Python Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/text-analyzer.git
    cd text-analyzer
    ```

2. Install Python dependencies:
    ```bash
    pip install -r src/requirements.txt
    ```

### Go Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/text-analyzer.git
    cd text-analyzer
    ```

2. Make sure you have **Go** installed.

## Usage

### Python

To run the text analyzer in Python:

1. Navigate to the `src/` directory:
    ```bash
    cd src
    ```

2. Run the Python script:
    ```bash
    python main.py path/to/your/textfile.txt
    ```

This will analyze the text in `textfile.txt` and print out the word count, sentence count, and character count. It will also generate a word frequency graph saved as `word_frequency.png`.

### Go

To run the text analyzer in Go:

1. Navigate to the `src/` directory:
    ```bash
    cd src
    ```

2. Run the Go script:
    ```bash
    go run main.go path/to/your/textfile.txt
    ```

This will perform the same analysis in Go as in Python, providing the word count, sentence count, and character count.

## Example

### Input

`example.txt`:
```
Hello world! This is a simple text analysis example. This is just an example.
```

### Output

```
Word count: 10
Sentence count: 2
Character count: 66
Most common words: ['This', 'is', 'example']
```

A word frequency graph will be saved as `word_frequency.png` (Python only).

## File Structure

```bash
text-analyzer/
├── src/                    # Source files
│   ├── main.py             # Entry point of the Python script
│   ├── analyzer.py         # Python file that performs text analysis
│   ├── analyzer.go         # Go file that performs text analysis
│   ├── utils.py            # Helper functions
│   └── requirements.txt    # Python dependencies
├── examples/               # Example files
│   ├── sample_input.txt    # Sample text file for testing
│   └── output.txt          # Expected output
├── output/                 # Directory for generated output
│   ├── word_frequency.png  # Generated plot of word frequencies
├── tests/                  # Unit tests
│   ├── test_analyzer.py    # Unit tests for Python text analyzer
│   └── test_analyzer.go    # Unit tests for Go text analyzer
├── .gitignore              # Git ignore file
├── README.md               # This file
├── LICENSE                 # License file
└── Makefile                # Build automation
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

1. Fork the repository.
2. Create your branch (`git checkout -b feature/your-feature`).
3. Commit your changes (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature/your-feature`).
5. Create a new Pull Request.

## Acknowledgements
- `matplotlib` for generating visualizations.
- Python's built-in libraries for text processing.
- Go for high-performance implementation.

```
