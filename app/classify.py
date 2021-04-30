import webvtt
import text2emotion as te


def decideEmotion(text):
    emotion_list = te.get_emotion(text)
    print(emotion_list)


def classifySubtitle(video_id):
    subtitle_path = "static/videos/{0}/{1}_subtitles.vtt".format(
        video_id, video_id)

    for caption in webvtt.read(subtitle_path):
        print(caption.text)
        decideEmotion(caption.text)
