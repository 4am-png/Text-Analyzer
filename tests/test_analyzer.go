package main

import (
    "testing"
)

func TestWordCount(t *testing.T) {
    text := "This is a test."
    result := analyzeText(text)
    if result["word_count"] != 5 {
        t.Errorf("Expected 5, got %v", result["word_count"])
    }
}

func TestSentenceCount(t *testing.T) {
    text := "This is a test. Here's another sentence."
    result := analyzeText(text)
    if result["sentence_count"] != 2 {
        t.Errorf("Expected 2, got %v", result["sentence_count"])
    }
}

func TestCharacterCount(t *testing.T) {
    text := "Hello!"
    result := analyzeText(text)
    if result["character_count"] != 6 {
        t.Errorf("Expected 6, got %v", result["character_count"])
    }
}

func TestMostFrequentWord(t *testing.T) {
    text := "apple apple banana"
    result := analyzeText(text)
    if result["word_frequency"]["apple"] != 2 {
        t.Errorf("Expected 2 for 'apple', got %v", result["word_frequency"]["apple"])
    }
}
