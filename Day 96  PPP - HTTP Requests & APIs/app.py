# Professional Portfolio Project - HTTP Requests & APIs
# Custom API Based Website
# Author : Abraham

from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    suggestions = []
    text = ""
    
    if request.method == "POST":
        text = request.form["text"]
        response = requests.post(
            "https://api.languagetoolplus.com/v2/check",
            data={
                "text": text,
                "language": "en-US"
            }
        )
        results = response.json()
        for match in results.get("matches", []):
            suggestions.append({
                "message": match["message"],
                "offset": match["offset"],
                "length": match["length"],
                "suggestions": [s["value"] for s in match.get("replacements", [])],
                "context": match["context"]["text"]
            })

    return render_template("index.html", text=text, suggestions=suggestions)

if __name__ == "__main__":
    app.run(debug=True, port=5050)
