from flask import Flask

app = Flask(__name__)


@app.route("/index")
def index():
    return "index"


@app.route("/hello")
def hello():
    return str(1 + 2)


if __name__ == '__main__':
    app.run(debug=1)
