import webvtt
import text2emotion as te
import operator
import os.path
import json


def decideEmotion(text):
    # Function for deciding the emotion from a string
    emotion_list = te.get_emotion(text)

    # Return the highest value from the dictionary as the selected emotion, as well as the original list
    emotion_dict = {
        "selected_emotion": (max(emotion_list.items(),
                                 key=operator.itemgetter(1))[0]),
        "emotion_list": emotion_list
    }

    return emotion_dict


def classifySubtitle(video_id):

    emotive_subtitle_path = './static/videos/{}/{}_emotive_subtitles.vtt'.format(
        video_id, video_id)

    if (os.path.exists(emotive_subtitle_path)):
        print("File already exists.")

    else:
        subtitle_path = "static/videos/{0}/{1}_subtitles.vtt".format(
            video_id, video_id)

        vtt = webvtt.read(subtitle_path)

        for caption in vtt:
            print(caption.text)
            emotion_dict = decideEmotion(caption.text)

            if (emotion_dict["selected_emotion"]):
                caption.text = "<p id='{0}'>{1}</p>".format(
                    emotion_dict["selected_emotion"].lower(), caption.text)
            else:
                caption.text = "<p>{1}</p>".format(caption.text)

            caption.identifier = "Emotions: " + \
                json.dumps(emotion_dict["emotion_list"])

        vtt.save(emotive_subtitle_path)
