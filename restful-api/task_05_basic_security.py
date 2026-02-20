#!/usr/bin/python3
"""
Flask API demonstrating Basic Authentication, JWT authentication,
and role-based access control.

Endpoints:
- /basic-protected: Protected with Basic Auth
- /login: Obtain a JWT token
- /jwt-protected: Protected with JWT token
- /admin-only: Protected with JWT token, admin role required
"""

from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import (
    JWTManager, create_access_token, jwt_required, get_jwt_identity
)
from werkzeug.security import generate_password_hash, check_password_hash

# ------------------ App Setup ------------------ #
app = Flask(__name__)
# Secret key for JWT token signing
app.config["JWT_SECRET_KEY"] = "secret-key"

# Auth objects
auth = HTTPBasicAuth()  # For Basic Authentication
jwt = JWTManager(app)   # For JWT token authentication

# ------------------ JWT Error Handlers ------------------ #

@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    """Handle missing JWT token."""
    return jsonify({"error": "Missing or invalid token"}), 401


@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    """Handle invalid JWT token."""
    return jsonify({"error": "Invalid token"}), 401


@jwt.expired_token_loader
def handle_expired_token_error(jwt_header, jwt_payload):
    """Handle expired JWT token."""
    return jsonify({"error": "Token has expired"}), 401


@jwt.revoked_token_loader
def handle_revoked_token_error(err):
    """Handle revoked JWT token."""
    return jsonify({"error": "Token has been revoked"}), 401


@jwt.needs_fresh_token_loader
def handle_needs_fresh_token_error(err):
    """Handle non-fresh JWT token."""
    return jsonify({"error": "Fresh token required"}), 401

# ------------------ In-memory User Storage ------------------ #
users = {
    "user1": {
        "username": "user1",
        "password": generate_password_hash("password"),
        "role": "user"
    },
    "admin1": {
        "username": "admin1",
        "password": generate_password_hash("password"),
        "role": "admin"
    }
}

# ------------------ Basic Auth ------------------ #
@auth.verify_password
def verify_password(username, password):
    """Verify username and password for Basic Auth."""
    user = users.get(username)
    if not user:
        return False
    return check_password_hash(user["password"], password)

@app.route("/basic-protected", methods=["GET"])
@auth.login_required
def basic_protected():
    """Return message if Basic Auth credentials are valid."""
    return "Basic Auth: Access Granted"

# ------------------ JWT Authentication ------------------ #
@app.route("/login", methods=["POST"])
def login():
    """
    Login endpoint: Accepts JSON payload with username and password.
    Returns a JWT token if credentials are valid.
    """
    data = request.get_json(silent=True)
    if data is None:
        return jsonify({"error": "Invalid credentials"}), 401
    else:
        username = data.get("username", None)
        password = data.get("password", None)

    if not username or not password:
        return jsonify({"error": "Invalid credentials"}), 401

    user = users.get(username)

    if not user or not check_password_hash(user["password"], password):
        return jsonify({"error": "Invalid credentials"}), 401

    # Include username and role in the JWT payload
    access_token = create_access_token(identity=username)
    return jsonify({"access_token": access_token})

@app.route("/jwt-protected", methods=["GET"])
@jwt_required()
def jwt_protected():
    """Return message if a valid JWT token is provided."""
    return "JWT Auth: Access Granted"

@app.route("/admin-only", methods=["GET"])
@jwt_required()
def admin_only():
    """
    Admin-only route:
    Requires JWT token with role = 'admin'.
    Returns 403 if role is not admin.
    """
    identity = get_jwt_identity()  # Get current JWT payload
    user_role = users[identity]["role"]

    if user_role != "admin":
        return jsonify({"error": "Admin access required"}), 403

    return "Admin Access Granted"

# ------------------ Run Server ------------------ #
if __name__ == "__main__":
    app.run()
