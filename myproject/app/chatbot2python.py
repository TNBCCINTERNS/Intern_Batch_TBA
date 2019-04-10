#examples/flask/22/app.py
from flask import Flask, jsonify, render_template, request
import time
import moduledb
app = Flask(__name__)
@app.route("/")
def main():
    return render_template('chatbot2.html', reload = time.time())

@app.route("/api/calc")
def add():
    a = request.args.get('message', 0)
    res=moduledb.getvalue(a)
    print(res)
    return res
app.run()

