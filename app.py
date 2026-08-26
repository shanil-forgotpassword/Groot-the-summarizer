from flask import Flask, render_template, request, session
from summarizer import summarize_text, summarize_file
import os


app = Flask(__name__)

app.secret_key = os.environ.get("SECRET_KEY", "i-am-ironman-snap")

UPLOAD_FOLDER = "uploads"

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@app.route("/")
def home():

    conversations = session.get("conversations", [])

    return render_template(
        "index.html",
        conversations=conversations
    )


@app.route("/summarize", methods=["POST"])
def summarize():

    text = request.form.get("text", "").strip()

    uploaded_file = request.files.get("file")

    original_text = ""
    filename = ""

    # -----------------------------
    # TEXT INPUT
    # -----------------------------

    if text:

        original_text = text

        filename = ""

    # -----------------------------
    # FILE INPUT
    # -----------------------------

    elif uploaded_file and uploaded_file.filename:

        filename = uploaded_file.filename

        allowed_extensions = [
            ".txt",
            ".pdf",
            ".docx"
        ]

        extension = os.path.splitext(
            filename
        )[1].lower()

        if extension not in allowed_extensions:

            return "Unsupported file type. Please use TXT, PDF or DOCX."

        file_path = os.path.join(
            app.config["UPLOAD_FOLDER"],
            filename
        )

        uploaded_file.save(file_path)

        # Read the file through the summarizer
        from summarizer import (
            read_txt,
            read_pdf,
            read_docx
        )

        if extension == ".txt":

            original_text = read_txt(file_path)

        elif extension == ".pdf":

            original_text = read_pdf(file_path)

        elif extension == ".docx":

            original_text = read_docx(file_path)

        # Remove temporary file
        os.remove(file_path)

    else:

        return "Please enter text or upload a file."


    # -----------------------------
    # AUTOMATIC SUMMARY LENGTH
    # -----------------------------

    sentence_count = len(
        original_text.split(".")
    )

    if sentence_count <= 5:

        summary_length = 2

    elif sentence_count <= 15:

        summary_length = 3

    elif sentence_count <= 30:

        summary_length = 5

    elif sentence_count <= 50:

        summary_length = 8

    else:

        summary_length = 10


    # -----------------------------
    # SUMMARIZE
    # -----------------------------

    summary = summarize_text(
        original_text,
        summary_length
    )


    # -----------------------------
    # SAVE CONVERSATION
    # -----------------------------

    conversations = session.get(
        "conversations",
        []
    )

    conversations.append({

        "text": original_text,

        "summary": summary,

        "filename": filename

    })

    session["conversations"] = conversations

    session.modified = True


    return render_template(
        "index.html",
        conversations=conversations
    )


@app.route("/clear")
def clear():

    session.pop(
        "conversations",
        None
    )

    return render_template(
        "index.html",
        conversations=[]
    )


if __name__ == "__main__":

    app.run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 5000)),
        debug=False
    )