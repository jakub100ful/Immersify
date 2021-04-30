from flask import Flask
from flask import render_template
from flask import request
from fetch_videos import fetch_metadata_list
app = Flask(__name__)


@app.route('/')
def index():
    metadata = fetch_metadata_list()
    return render_template('index.html', metadata_list=metadata)


@app.route('/play')
def play():
    video_id = request.args.get('id')
    return render_template('play.html', video_id=video_id)
