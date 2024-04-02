from __future__ import annotations

from flask import Flask
from flask import jsonify
from flask import render_template
from flask import request

app = Flask(__name__)

# Sample data to simulate database entries
users = {
    "user@example.com": {"name": "John Doe", "points": 120},
    "test@example.com": {"name": "Jane Smith", "points": 150},
}


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/get_user_info", methods=["POST"])
def get_user_info():
    data = request.json
    email = data.get("email")
    user_info = users.get(email)

    if user_info:
        return jsonify(user_info), 200
    else:
        return jsonify({"error": "User not found"}), 404


if __name__ == "__main__":
    app.run(debug=True)
