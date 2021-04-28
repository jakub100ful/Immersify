from flask import Flask
from flask import render_template
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/play')
def play():
    return render_template('play.html', video_id=video_id)
