#!/usr/bin/python3
"""Flask API example with user management and JSON responses."""

from flask import Flask, jsonify, request

app = Flask(__name__)

users = {}


@app.route("/")
def home():
    """Return a welcome message for the API root endpoint."""
    return "Welcome to the Flask API!"


@app.route("/status")
def status():
    """Return the API status as OK."""
    return "OK"


@app.route("/data")
def get_data():
    """Return a JSON list of all usernames in the API."""
    return jsonify(list(users.keys()))


@app.route("/users/<username>")
def get_user(username):
    """
    Return the user object corresponding to the given username.

    If the user does not exist, return a 404 error with a JSON message.
    """
    if username not in users:
        return jsonify({"error": "User not found"}), 404
    return jsonify(users[username])


@app.route("/add_user", methods=["POST"])
def add_user():
    """
    Add a new user to the API via a JSON POST request.

    Expected JSON body:
    {
        "username": "alice",
        "name": "Alice",
        "age": 25,
        "city": "San Francisco"
    }

    Returns:
        201: Confirmation message with added user data.
        400: If JSON is invalid or username is missing.
        409: If username already exists.
    """
    if not request.is_json:
        return jsonify({"error": "Invalid JSON"}), 400

    data = request.get_json()
    username = data.get("username")

    if not username:
        return jsonify({"error": "Username is required"}), 400

    if username in users:
        return jsonify({"error": "Username already exists"}), 409

    users[username] = data
    return jsonify({"message": "User added", "user": data}), 201


if __name__ == "__main__":
    app.run()
