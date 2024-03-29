import socket

from datetime import datetime
from flask import Flask

app = Flask(__name__)


@app.route("/")
@app.route("/training")
def index():
    hostname = socket.gethostname()
    isotime = datetime.now().isoformat()
    return "<html><body><h1>Hello, This is a server, {} ({})</h1></body></html>".format(hostname, isotime)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, debug=True)

