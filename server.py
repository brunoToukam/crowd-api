from flask import Flask

app = Flask(__name__)

@app.route('/')
def do_great():
    return '<h1>Great Flask API</h1>'
