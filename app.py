import logging
import socket

from datetime import datetime
from flask import Flask, make_response
from flask_restx import Api, Resource, reqparse

app = Flask(__name__)
app.config["DEBUG"] = True
app.logger.setLevel(logging.DEBUG)
api = Api(app, version="1.0", title="API Documentation", description="Swagger UI", doc="/api-docs")
ns_test = api.namespace("test", description="Retrieve API")

@ns_test.route("/")
@ns_test.produces(["text/html"])
class Test(Resource):
    def get(self):
        hostname = socket.gethostname()
        isotime = datetime.now().isoformat()
        body = "<html><body><h1>Hello, This is a server, {} ({})</h1></body></html>".format(hostname, isotime)
        
        resp = make_response(body)
        return resp

@ns_test.route("/message")
class TestMessage(Resource):
    def get(self):
        body = "<h1>Returns a message</h1>"

        resp = make_response(body)
        return resp
