import sqlite3

from flask import Flask, request

app = Flask(__name__)


# INTENTIONALLY VULNERABLE: SQL injection for Semgrep demo purposes only.
@app.route("/user")
def get_user():
    username = request.args.get("username", "")
    conn = sqlite3.connect("demo.db")
    query = "SELECT * FROM users WHERE username = '" + username + "'"
    rows = conn.execute(query).fetchall()
    return {"users": rows}
