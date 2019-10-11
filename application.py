from flask import Flask
from flask import request
from flask import jsonify


app = Flask(__name__)

@app.route("/", methods=["GET"])
def get_my_ip():
    return "hello from cloud  , you ip address is : "+str(request.remote_addr)


@app.route("/isem")
def isem():
    return "<h1>Hello ISEM</h1>"

