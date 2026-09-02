from flask import Flask, jsonify
import os
from dotenv import load_dotenv
import awsgi

load_dotenv()

app = Flask(__name__)

APP_NAME = os.getenv("APP_NAME", "Python Lambda API")


@app.route("/")
def home():
    return jsonify({
        "status": "success",
        "messagee": f"{APP_NAME} is running!",
        "technologye": "Python Flask",
        "servere": "AWS Lambda"
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

    user = next(
        (user for user in users_data if user["id"] == user_id),
        None
    )

    if user is None:
        return jsonify({
            "status": "error",
            "message": "User not found"
        }), 404

    return jsonify({
        "status": "success",
        "user": user
    })


# AWS Lambda entry point
def lambda_handler(event, context):
    return awsgi.response(app, event, context)


# Local development
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", 5000)))
