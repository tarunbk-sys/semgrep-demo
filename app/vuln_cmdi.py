import subprocess

from flask import Flask, request

app = Flask(__name__)


# INTENTIONALLY VULNERABLE: command injection for Semgrep demo purposes only.
@app.route("/ping")
def ping():
    host = request.args.get("host", "127.0.0.1")
    output = subprocess.check_output("ping -c 1 " + host, shell=True)
    return output
