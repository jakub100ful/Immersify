import os
import json


def fetch_video_metadata():
    """Crawls the videos folder and returns a list of metadata."""

    list_of_videos = []

    for root, dirs, files in os.walk("./static/videos", topdown=False):
        for name in files:
            if name.endswith('_metadata.json'):
                try:
                    with open(os.path.join(root, name)) as json_file:
                        metadata = json.load(json_file)
                        list_of_videos.append(metadata)
                except:
                    print("No metadata found.")

    return list_of_videos
