#!/usr/bin/env python3
import flask
import socket
import time
import random

h_name = socket.gethostname()
IP_address = socket.gethostbyname(h_name)
app = flask.Flask(__name__)

@app.route('/')
def index():
    host = IP_address
    client_ip = flask.request.remote_addr
    client_port = str(flask.request.environ.get('REMOTE_PORT'))
    Time = time.strftime("%H:%M:%S")
    rand = str(random.randint(0,100))
    return f"{Time} {client_ip}:{client_port} -- {host} ({h_name}) {rand}\n"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
