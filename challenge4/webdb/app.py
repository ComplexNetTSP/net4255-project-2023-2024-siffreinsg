import os
import socket
from datetime import datetime

import pymongo
from flask import Flask

application = Flask(__name__)

client = pymongo.MongoClient(host=os.environ['MONGODB_HOSTNAME'],
                        port=int(os.environ['MONGODB_PORT']),
                        username=os.environ['MONGODB_USERNAME'],
                        password=os.environ['MONGODB_PASSWORD'],
                        authSource="admin")

db = client[os.environ["MONGODB_DATABASE"]]


@application.route("/")
def hello_world():
    # Log the request IP and current date in MongoDB
    db.requests.insert_one({
        "ip": socket.gethostbyname(socket.gethostname()),
        "date": datetime.now()
    })

    html = f"""
<h1>Hello !</h1>
<p>Créé par Siffrein SIGY</p>
<p>Projet Kubernetes v4</p>
<p>Hostname: {socket.gethostname()}</p>
<p>Date: {datetime.now()}</p>
"""

    # Append last 10 requests from MongoDB to the HTML output
    html += "<h2>Last 10 requests:</h2>"

    for request in db.requests.find().sort("date", -1).limit(10):
        html += f"<p>{request['date']} - {request['ip']}</p>"

    return html

if __name__ == "__main__":
    ENVIRONMENT_DEBUG = bool(os.environ.get("APP_DEBUG", True))
    ENVIRONMENT_PORT = int(os.environ.get("APP_PORT", 5000))
    application.run(host='0.0.0.0', port=ENVIRONMENT_PORT, debug=ENVIRONMENT_DEBUG)
