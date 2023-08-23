from flask import Flask

print(__name__)
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"
