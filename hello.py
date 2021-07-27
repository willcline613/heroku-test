from flask import Flask
from waitress import serve

app = Flask(__name__)

@app.route("/", methods=['GET','POST'])
def hello():
    return "Hello World!"

# if __name__ == "__main__":
#     app.run()

if __name__ == "__main__":
    serve(app, host='0.0.0.0', port=5000)
