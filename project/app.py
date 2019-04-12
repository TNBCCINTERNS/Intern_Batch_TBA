from flask import Flask, jsonify, render_template, request
import time
from fl import getquestions
app = Flask(__name__)
@app.route("/")
def main():
    return render_template('d.html')

@app.route("/get")
def add():
    a = request.args.get('a',0)
    ques = getquestions(a)
    print (ques)
    return render_template("d.html", ques = ques)

app.run()
