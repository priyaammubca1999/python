from flask import Flask, jsonify
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

APP_NAME = os.getenv("APP_NAME", "Python EC2 API")
PORT = int(os.getenv("PORT", 5000))


@app.route("/")
def home():
    return jsonify({
        "status": "success",
        "message": f"{APP_NAME} is running!",
        "technology": "Python Flask",
        "server": "AWS EC2"
    })


@app.route("/api/health")
def health():
    return jsonify({
        "status": "OK",
        "message": "Python API is healthy"
    })


@app.route("/api/users")
def users():
    users_data = [
        {"id": 1, "name": "Priya", "role": "DevOps Engineer"},
        {"id": 2, "name": "John", "role": "Developer"},
        {"id": 3, "name": "David", "role": "Cloud Engineer"}
    ]

    return jsonify({
        "status": "success",
        "users": users_data
    })


@app.route("/api/users/<int:user_id>")
def get_user(user_id):
    users_data = [
        {"id": 1, "name": "Priya", "role": "DevOps Engineer"},
        {"id": 2, "name": "John", "role": "Developer"},
        {"id": 3, "name": "David", "role": "Cloud Engineer"}
    ]

    user = next((user for user in users_data if user["id"] == user_id), None)

    if user is None:
        return jsonify({
            "status": "error",
            "message": "User not found"
        }), 404

    return jsonify({
        "status": "success",
        "user": user
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=PORT, debug=False)
