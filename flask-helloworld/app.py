from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

#runs the app when this file is ran
if __name__ == '__main__':
    app.run()