from flask import Flask

app = Flask(__name__)

@app.route("/_health")
def health():
    return 2002
