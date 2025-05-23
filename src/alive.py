import os
import time
from flask import Flask
from ping3 import ping

app = Flask(__name__)
NODES_FILE = '/opt/nodes.txt'

@app.route('/')
def node_status():
    if not os.path.exists(NODES_FILE):
        return "nodes.txt not found", 500
    
    status = []
    with open(NODES_FILE) as f:
        nodes = [line.strip() for line in f if line.strip()]
    
    for node in nodes:
        response = ping(node, timeout=1, unit='ms')
        if response is not None:
            status.append(f"{node}:ALIVE")
        else:
            status.append(f"{node}:DOWN")
    
    return '\n'.join(status) + '\n'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)