import os
from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/medications')
def medications():
    return render_template('medications.html')


@app.route('/diet')
def diet():
    return render_template('diet.html')


@app.route('/followups')
def followups():
    return render_template('followups.html')


@app.route('/symptoms')
def symptoms():
    return render_template('symptoms.html')


@app.route('/share')
def share():
    return render_template('share.html')


@app.route('/resources')
def resources():
    return render_template('resources.html')


@app.route('/register')
def register():
    return render_template('register.html')


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/notes')
def notes():
    return render_template('notes.html')


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 0))
    if port:
        app.debug = False
        app.run(host='0.0.0.0', port=port)
    else:
        app.debug = True
        app.run()
