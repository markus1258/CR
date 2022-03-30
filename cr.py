from flask import Flask

app = Flask(__name__)


@app.route("/")
def blank():
    return "Yody!!"


@app.route("/_health")
def health():
    return "201"


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
