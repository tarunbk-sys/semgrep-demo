"""
Semgrep demo app.

WARNING: This code is INTENTIONALLY INSECURE so Semgrep has
something to find. Do not deploy it or copy these patterns.
"""
import hashlib
import sqlite3
import subprocess

from flask import Flask, request

app = Flask(__name__)
app.config["DEBUG"] = True  # Finding: debug mode enabled


def get_db():
    return sqlite3.connect("users.db")


@app.route("/user")
def get_user():
    username = request.args.get("name")
    conn = get_db()
    # Finding: SQL injection via string formatting
    query = "SELECT * FROM users WHERE name = '%s'" % username
    return str(conn.execute(query).fetchall())


@app.route("/ping")
def ping():
    host = request.args.get("host")
    # Finding: command injection via shell=True
    output = subprocess.check_output("ping -c 1 " + host, shell=True)
    return output


@app.route("/hash")
def weak_hash():
    password = request.args.get("pw", "")
    # Finding: weak hashing algorithm
    return hashlib.md5(password.encode()).hexdigest()


@app.route("/calc")
def calc():
    expr = request.args.get("expr")
    # Finding: eval on user input
    return str(eval(expr))


if __name__ == "__main__":
    app.run(host="0.0.0.0")
