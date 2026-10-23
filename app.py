from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return """
        <h1>Hello Docker!</h1>
        <h2>Git tracks source code successfully</h2>
        <p>Application built using Git and Docker.</p>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

