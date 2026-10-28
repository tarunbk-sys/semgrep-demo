import ast
import operator
import sqlite3

from flask import Flask, abort, request

app = Flask(__name__)

OPS = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
}


def safe_eval(node):
    if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)):
        return node.value
    if isinstance(node, ast.BinOp) and type(node.op) in OPS:
        return OPS[type(node.op)](safe_eval(node.left), safe_eval(node.right))
    raise ValueError("unsupported expression")


@app.route("/user")
def get_user():
    username = request.args.get("username", "")
    conn = sqlite3.connect("demo.db")
    rows = conn.execute(
        "SELECT id, username FROM users WHERE username = ?", (username,)
    ).fetchall()
    return {"users": rows}


@app.route("/calc")
def calc():
    expression = request.args.get("expr", "1+1")
    try:
        result = safe_eval(ast.parse(expression, mode="eval").body)
    except (ValueError, SyntaxError, ZeroDivisionError):
        abort(400)
    return {"result": result}
