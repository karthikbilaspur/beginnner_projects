from flask import Flask, render_template, request
from src.text_analyzer import analyze_text

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        text = request.form["text"]
        results = analyze_text(text)
        return render_template("results.html", results=results)
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)