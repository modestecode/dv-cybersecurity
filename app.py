from flask import Flask, jsonify, request, render_template


app = Flask(__name__, template_folder='template')

@app.route('/')
def hello():
    return render_template("index.html")