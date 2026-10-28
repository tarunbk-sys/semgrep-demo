from flask import Flask, request

app = Flask(__name__)


# INTENTIONALLY VULNERABLE: code injection via eval for Semgrep demo purposes only.
@app.route("/eval")
def evaluate():
    expression = request.args.get("expr", "1+1")
    result = eval(expression)
    return {"result": result}
