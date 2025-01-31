.PHONY: test build run clean

# Run unit tests for both Python and Go
test:
    python -m unittest discover tests/
    go test ./tests/test_analyzer.go

# Build project (if any build steps are required)
build:
    # Add any build steps here if necessary
    @echo "Build complete"

# Run the main Python script with a sample input
run:
    python src/main.py examples/sample_input.txt
    go run src/analyzer.go examples/sample_input.txt

# Clean up generated files
clean:
    rm -rf __pycache__ output/*.png