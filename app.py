import socket

from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    hostname = socket.gethostname()
    return "<html><body><h1>Hello, This is a server, {}</h1></body></html>".format(hostname)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, debug=True)

