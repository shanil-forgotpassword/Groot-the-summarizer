import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from collections import Counter

from pypdf import PdfReader
from docx import Document


# Download required NLTK data
nltk.download("punkt")
nltk.download("punkt_tab")
nltk.download("stopwords")


def summarize_text(text, sentence_count=3):

    if not text or not text.strip():
        return "Please provide some text."

    sentences = sent_tokenize(text)

    if len(sentences) <= sentence_count:
        return text

    stop_words = set(stopwords.words("english"))

    words = word_tokenize(text.lower())

    word_frequency = Counter(
        word
        for word in words
        if word.isalpha() and word not in stop_words
    )

    sentence_scores = {}

    for sentence in sentences:

        sentence_words = word_tokenize(sentence.lower())

        score = sum(
            word_frequency[word]
            for word in sentence_words
            if word.isalpha() and word in word_frequency
        )

        sentence_scores[sentence] = score

    best_sentences = sorted(
        sentence_scores,
        key=sentence_scores.get,
        reverse=True
    )[:sentence_count]

    summary = [
        sentence
        for sentence in sentences
        if sentence in best_sentences
    ]

    return " ".join(summary)


def read_txt(file_path):

    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()


def read_pdf(file_path):

    reader = PdfReader(file_path)

    text = ""

    for page in reader.pages:
        page_text = page.extract_text()

        if page_text:
            text += page_text + "\n"

    return text


def read_docx(file_path):

    document = Document(file_path)

    text = ""

    for paragraph in document.paragraphs:
        text += paragraph.text + "\n"

    return text


def summarize_file(file_path, sentence_count=3):

    try:

        file_path_lower = file_path.lower()

        # TXT
        if file_path_lower.endswith(".txt"):
            text = read_txt(file_path)

        # PDF
        elif file_path_lower.endswith(".pdf"):
            text = read_pdf(file_path)

        # DOCX
        elif file_path_lower.endswith(".docx"):
            text = read_docx(file_path)

        else:
            return "Unsupported file type. Please use TXT, PDF, or DOCX."

        if not text.strip():
            return "The file does not contain readable text."

        return summarize_text(text, sentence_count)

    except FileNotFoundError:

        return "File not found."

    except Exception as e:

        return f"Error reading file: {e}"


# Test program
if __name__ == "__main__":

    print("================================")
    print("       TEXT SUMMARIZER")
    print("================================")

    print("\n1. Enter text")
    print("2. Summarize a file")

    choice = input("\nEnter your choice (1/2): ")

    if choice == "1":

        text = input("\nEnter your text:\n\n")

        summary = summarize_text(text)

        print("\n========== SUMMARY ==========\n")
        print(summary)

    elif choice == "2":

        file_path = input("\nEnter file path:\n\n")

        summary = summarize_file(file_path)

        print("\n========== SUMMARY ==========\n")
        print(summary)

    else:

        print("\nInvalid choice.")