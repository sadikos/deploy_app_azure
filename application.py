from flask import Flask
app = Flask(__name__)

@app.route("/")
def index():
    return "<h1>Hello from  Azure cloud </h1>"
@app.route("/isem")
def isem():
    return "<h1>Hello ISEM</h1>"

