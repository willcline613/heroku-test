from flask import Flask
from waitress import serve

if __name__ == "__main__":
    serve(app, host='0.0.0.0', port=5000)

app = Flask(__name__)

@app.route("/")
    def hello():
        return "Hello World!"

# if __name__ == "__main__":
#     app.run()

if __name__ == "__main__":
    serve(app, host='0.0.0.0', port=5000)
