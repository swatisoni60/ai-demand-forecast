from flask import Blueprint, request, jsonify
import sqlite3

auth_bp = Blueprint("auth", __name__)

DB = "database.db"


# Register
@auth_bp.route("/register", methods=["POST"])
def register():
    data = request.get_json()

    username = data["username"]
    password = data["password"]

    conn = sqlite3.connect(DB)
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS users(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE,
            password TEXT
        )
    """)

    try:
        cur.execute(
            "INSERT INTO users(username,password) VALUES(?,?)",
            (username, password)
        )
        conn.commit()
        return jsonify({"message": "Registered successfully"})
    except:
        return jsonify({"message": "Username already exists"})



# Login
@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.get_json()

    username = data["username"]
    password = data["password"]

    conn = sqlite3.connect(DB)
    cur = conn.cursor()

    cur.execute(
        "SELECT * FROM users WHERE username=? AND password=?",
        (username, password)
    )

    user = cur.fetchone()

    if user:
        return jsonify({
            "success": True,
            "username": username
        })
    else:
        return jsonify({
            "success": False,
            "message": "Invalid login"
        })