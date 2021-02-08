from flask import Flas, render_template
import flask

app = flask(__name__)

@app.route('/')
@app.route('/jobs')
def jobs():
    return render_template('index.html')
