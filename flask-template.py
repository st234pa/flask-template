from flask import Flask

app = Flask(__name__)

@app.route("/")
def default():
    return "This is the homepage."

@app.route("/page1")
def page1():
    return "This is page 1."

@app.route("/page2")
def page2():
    return "This is page 3."

if __name__ == "__main__":
    app.run();
