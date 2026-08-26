import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from collections import Counter


# Download required NLTK data
nltk.download("punkt")
nltk.download("punkt_tab")
nltk.download("stopwords")


def summarize_text(text, sentence_count=3):

    # Check if text is empty
    if not text or not text.strip():
        return "Please enter some text."

    # Split text into sentences
    sentences = sent_tokenize(text)

    # If the text already has fewer sentences than requested
    if len(sentences) <= sentence_count:
        return text

    # English stopwords
    stop_words = set(stopwords.words("english"))

    # Tokenize words
    words = word_tokenize(text.lower())

    # Calculate word frequency
    word_frequency = Counter(
        word
        for word in words
        if word.isalpha() and word not in stop_words
    )

    # Calculate score for every sentence
    sentence_scores = {}

    for sentence in sentences:

        sentence_words = word_tokenize(sentence.lower())

        score = 0

        for word in sentence_words:

            if word.isalpha() and word in word_frequency:
                score += word_frequency[word]

        sentence_scores[sentence] = score

    # Select highest-scoring sentences
    best_sentences = sorted(
        sentence_scores,
        key=sentence_scores.get,
        reverse=True
    )[:sentence_count]

    # Keep sentences in their original order
    summary = [
        sentence
        for sentence in sentences
        if sentence in best_sentences
    ]

    return " ".join(summary)


# Test the summarizer
if __name__ == "__main__":

    text = input("\nEnter the text you want to summarize:\n\n")

    summary = summarize_text(text)

    print("\n==============================")
    print("          SUMMARY")
    print("==============================\n")

    print(summary)