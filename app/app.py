from flask import Flask, jsonify, render_template
from datetime import datetime

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/health")
def health():
    return jsonify({
        "status": "healthy",
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "application": "DevOps Assignment",
        "version": "1.0"
    })


@app.route("/about")
def about():
    return jsonify({
        "application": "DevOps Assignment",
        "developer": "Aryen Garg",
        "framework": "Flask",
        "environment": "Production"
    })


@app.route("/users")
def users():
    return jsonify([
        {
            "id": 1,
            "name": "Alice",
            "role": "Developer"
        },
        {
            "id": 2,
            "name": "Bob",
            "role": "DevOps Engineer"
        },
        {
            "id": 3,
            "name": "Charlie",
            "role": "Cloud Engineer"
        }
    ])


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)