from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello World! I am a dockerised Flask web app.'

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
