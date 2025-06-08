from flask import Flask, render_template, request
from generate import generate_recap
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    recap = ""
    if request.method == "POST":
        notes = request.form["notes"]
        recap = generate_recap(notes)
    return render_template("index.html", recap=recap)

if __name__ == "__main__":
    app.run(debug=True)
