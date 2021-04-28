from flask import Flask
from flask import render_template
from fetch_videos import fetch_video_metadata
app = Flask(__name__)


@app.route('/')
def index():
    metadata = fetch_video_metadata()
    return render_template('index.html', metadata_list=metadata)


@app.route('/play')
def play():
    return render_template('play.html', video_id=video_id)
