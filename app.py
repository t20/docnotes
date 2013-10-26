from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route('/')
def index():
    return "Index Page!"

@app.route('/hello')
def hello_world():
    return "Hello World!"

if __name__ == '__main__':
    app.debug = True
    app.run()