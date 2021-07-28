from flask import Flask
from flask import render_template
import gunicorn

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template("index.html")

@app.route("/portfolio")
def portfolio():
    return render_template("portfolio.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

if __name__ == "__main__":
    app.run()
