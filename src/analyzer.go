package main

import (
    "fmt"
    "io/ioutil"
    "os"
    "strings"
    "unicode"
)

func main() {
    if len(os.Args) != 2 {
        fmt.Println("Usage: go run main.go <textfile>")
        return
    }
    filepath := os.Args[1]
    result := analyzeText(filepath)
    fmt.Printf("Word count: %d\n", result.WordCount)
    fmt.Printf("Sentence count: %d\n", result.SentenceCount)
    fmt.Printf("Character count: %d\n", result.CharCount)
}

type AnalysisResult struct {
    WordCount    int
    SentenceCount int
    CharCount     int
}

func analyzeText(filepath string) AnalysisResult {
    content, err := ioutil.ReadFile(filepath)
    if err != nil {
        fmt.Println("Error reading file:", err)
        return AnalysisResult{}
    }
    text := string(content)
    wordCount := countWords(text)
    sentenceCount := countSentences(text)
    charCount := len(text)
    return AnalysisResult{
        WordCount:    wordCount,
        SentenceCount: sentenceCount,
        CharCount:     charCount,
    }
}

func countWords(text string) int {
    words := strings.FieldsFunc(text, func(r rune) bool {
        return unicode.IsSpace(r) || unicode.IsPunct(r)
    })
    return len(words)
}

func countSentences(text string) int {
    delimiters := []rune{'.', '!', '?'}
    sentenceCount := 0
    inSentence := false
    for _, r := range text {
        if contains(delimiters, r) {
            if inSentence {
                sentenceCount++
                inSentence = false
            }
        } else if !unicode.IsSpace(r) {
            inSentence = true
        }
    }
    if inSentence { // Handle case where text ends without a delimiter
        sentenceCount++
    }
    return sentenceCount
}

func contains(slice []rune, r rune) bool {
    for _, item := range slice {
        if item == r {
            return true
        }
    }
    return false
}
