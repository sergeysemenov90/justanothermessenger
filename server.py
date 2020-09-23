from flask import Flask
import time


app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World! <a href = '/status'>Статус</a>"

@app.route("/status")
def status():
    return {'status':'True', 'name': 'JustAnotherMessenger', 'time': time.asctime()}


app.run()