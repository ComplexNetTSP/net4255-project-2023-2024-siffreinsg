import os
import socket
from datetime import datetime

from flask import Flask

application = Flask(__name__)

@application.route("/")
def hello_world():
    html = f"""
<h1>Hello !</h1>
<p>Créé par Siffrein SIGY</p>
<p>Projet Kubernetes v4</p>
<p>Hostname: {socket.gethostname()}</p>
<p>Date: {datetime.now()}</p>
"""

    return html

if __name__ == "__main__":
    ENVIRONMENT_DEBUG = bool(os.environ.get("APP_DEBUG", True))
    ENVIRONMENT_PORT = int(os.environ.get("APP_PORT", 5000))
    application.run(host='0.0.0.0', port=ENVIRONMENT_PORT, debug=ENVIRONMENT_DEBUG)
