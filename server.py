from flask import Flask, request
from datetime import datetime
from database import *




app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
db = getfromdb()
unique_users = []


@app.route("/")
def hello():
    return "Hello, World! <a href = '/status'>Статус</a>"


@app.route("/status")
def status():
    """Some information about count of users and messages"""
    for message in db:
        if message[1] not in unique_users:
            unique_users.append(message[1])

    return {'status':True, 'name': 'JustAnotherMessenger',
            'time': datetime.now().strftime('%d.%m.%Y %H:%M:%S'),
            'Messages count: ' : len(db),
            'Unique users count' : (len(unique_users), unique_users)}


@app.route("/send", methods = ['POST'])
def send():
    data = request.json
    saving_message = {'name': data['name'], 'text': data['text'], 'time': datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
    savetodb(saving_message)
    return {'ok': True}


@app.route("/messages")
def messages():
    """Getting args and send messages back"""
    if 'after_id' in request.args:
        after_id = int(request.args['after_id'])
    else:
        after_id = 0
    return {'messages': getfromdb(after_id)}

app.run()