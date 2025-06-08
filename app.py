from flask import Flask, render_template, request
from generate import generate_recap
import os
from dotenv import load_dotenv
from werkzeug.utils import secure_filename

load_dotenv()

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = "static/uploads"
app.config["ALLOWED_EXTENSIONS"] = {"png", "jpg", "jpeg", "gif", "mp4", "mov"}

def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in app.config["ALLOWED_EXTENSIONS"]

@app.route("/", methods=["GET", "POST"])
def index():
    recap = ""
    media_url = ""
    if request.method == "POST":
        notes = request.form.get("notes", "")
        file = request.files.get("media")
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file_path = os.path.join(app.config["UPLOAD_FOLDER"], filename)
            file.save(file_path)
            media_url = file_path
        recap = generate_recap(notes, media_url)
    return render_template("index.html", recap=recap, media_url=media_url)

if __name__ == "__main__":
    app.run(debug=True)
