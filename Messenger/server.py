from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World! 1234567"

@app.route("/status")
def status():
    return "I'm Ok"
app.run()