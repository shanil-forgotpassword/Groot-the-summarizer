# 🧠 Groot – AI Text & PDF Summarizer

Groot is a web-based text summarization application built using **Python, Flask, and NLTK**. It allows users to enter text or upload documents and automatically generates a concise summary.

## 🚀 Live Demo

👉 [**Try Groot – Groot - Text Summarizer](https://groot-summarizer.onrender.com/)

---

## ✨ Current Features

* 📝 Summarize manually entered text
* 📄 Upload PDF files
* 📘 Upload DOCX files
* 📃 Upload TXT files
* 🤖 Automatically generate summaries
* 📏 Automatically adjust summary length according to the input
* 💬 Chat-style interface
* 🗑️ Clear conversation
* 🌐 Online deployment using Render

---

# 📖 How to Use Groot

### 1. Enter Text

Type or paste the content you want summarized into the input area.

For example:

```text
Artificial Intelligence is transforming many industries...
```

Click **Send/Summarize** and Groot will generate a shorter version.

### 2. Upload a PDF

Click the **+ / Upload** button and select a PDF.

Groot will:

```text
PDF
 ↓
Extract Text
 ↓
Process Text
 ↓
Generate Summary
 ↓
Display Summary
```

### 3. Upload DOCX or TXT

Groot also supports:

* `.docx`
* `.txt`

Simply upload the file and Groot will process it automatically.

---

# 📏 Current Summary Behavior

At the moment, Groot automatically decides the approximate summary length based on the amount of input text.

| Input Size      | Approximate Summary |
| --------------- | ------------------: |
| Short text      |         2 sentences |
| 6–15 sentences  |         3 sentences |
| 16–30 sentences |         5 sentences |
| 31–50 sentences |         8 sentences |
| 50+ sentences   |        10 sentences |

This means the user **does not currently need to manually select the summary length**.

---

# ⚠️ Current Limitations

Groot is currently an early version of the project. Some features available in advanced AI assistants are **not implemented yet**.

### Currently NOT Available

* ❌ User-selected summary length such as `50 words`, `100 words`, or `200 words`
* ❌ "Summarize in exactly 100 words"
* ❌ Bullet-point summary mode
* ❌ Key-points extraction
* ❌ Custom instructions such as "Explain like I'm 10"
* ❌ Multiple summary styles
* ❌ Automatic language translation
* ❌ Question answering about uploaded documents
* ❌ Chatting with the uploaded document
* ❌ Conversation memory across different sessions
* ❌ User accounts/login
* ❌ Download summary as PDF
* ❌ Download summary as TXT/DOCX
* ❌ Advanced AI/LLM-based summarization
* ❌ Real-time streaming responses
* ❌ Voice input/output

---

# 🔮 Planned Improvements

These features are planned for future versions of Groot.

### 🎯 Custom Summary Length

Users will be able to request:

```text
Summarize this in 50 words.
```

```text
Summarize this in 100 words.
```

```text
Summarize this in 200 words.
```

Groot will attempt to follow the requested word limit.

### 📝 Summary Styles

Future versions may support:

```text
Short Summary
Detailed Summary
Bullet Points
Key Points
Executive Summary
Study Notes
```

### 💬 Chat With Your Document

Instead of only summarizing a document, users will eventually be able to ask:

```text
What is this document about?
```

```text
What are the main points?
```

```text
Explain the third section.
```

```text
What conclusion does the document give?
```

### 🧠 AI-Powered Summarization

The current version uses traditional NLP techniques.

Future versions may use modern **Transformer/LLM-based models** to improve:

* Context understanding
* Summary quality
* Long-document handling
* Important information selection
* Natural language generation

### 🌍 Multiple Languages

Future versions may support summarization of documents written in multiple languages.

### 📥 Export Summaries

Users may eventually be able to download generated summaries as:

* PDF
* TXT
* DOCX
* Markdown

---

# 🛠️ Technology

Current version:

```text
Python
Flask
NLTK
PyPDF
python-docx
HTML
CSS
```

Future versions may include:

```text
Transformers
LLMs
Vector Databases
Embeddings
RAG
Cloud AI APIs
```

---

# 🔄 Current Workflow

```text
             User
               │
       ┌───────┴────────┐
       │                │
    Enter Text       Upload File
       │                │
       │         ┌──────┴──────┐
       │         │             │
       │        PDF          DOCX/TXT
       │         │             │
       │         └──────┬──────┘
       │                │
       └────────┬───────┘
                ↓
          Text Extraction
                ↓
          NLP Processing
                ↓
       Sentence Analysis
                ↓
          Generate Summary
                ↓
             🧠 Groot
                ↓
          Display Result
```

---

# 🚧 Project Status

**Current Version: v1.0**

Groot is currently a working prototype with:

* ✅ Text summarization
* ✅ PDF summarization
* ✅ DOCX summarization
* ✅ TXT summarization
* ✅ Automatic summary length
* ✅ Chat-style interface
* ✅ Cloud deployment

More advanced AI features are planned for future versions.

> **Groot is continuously being improved. More features will be added in future updates.** 🚀

---

# 👨‍💻 Author

**L. Shanil Reddy**

BCA Student

**Project:** Groot – AI Text & PDF Summarizer

