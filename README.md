# text-summarizer
A Python-based extractive text summarization tool using NLTK, supporting direct text input and TXT, PDF, and DOCX files.
# Text Summarizer

A Python-based text summarization project that generates concise summaries from user-provided text and documents.

## Version 1.0

This is the initial version of the Text Summarizer project. The current version focuses on building and testing the core summarization engine before integrating it into a web application.

## Features

- Summarize user-provided text
- Summarize `.txt` files
- Summarize `.pdf` files
- Summarize `.docx` files
- Extractive text summarization using NLTK
- Sentence scoring based on word frequency
- Selects the most important sentences while maintaining their original order

## Technologies Used

- Python
- NLTK
- PyPDF
- python-docx

## Project Structure

```text
text-summarizer/
│
├── summarizer.py
├── app.py
├── requirements.txt
│
├── templates/
│   └── index.html
│
└── static/
    └── style.css
