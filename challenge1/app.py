import socket
from datetime import datetime

from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return f"""
<h1>Hello !</h1>
<p>Créé par Siffrein SIGY</p>
<p>Projet Kubernetes v1</p>
<p>Hostname: {socket.gethostname()}</p>
<p>Date: {datetime.now()}</p>
"""

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
