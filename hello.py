from flask import Flask
from flask import render_template
import gunicorn

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template("home.html")

@app.route("/portfolio")
def portfolio():
    return render_template("portfolio.html")

@app.route("/resume")
def resume():
    return render_template("resume.html")

if __name__ == "__main__":
    app.run()
