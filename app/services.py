from app import app

@app.route("/")
def index():
	hostname = socket.gethostname()
	isotime = datetime.now().isoformat()
	return "<html><body>Hello, This is a server, {} ({})</body></html>".format(hostname, isotime)
