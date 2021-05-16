import webvtt
import text2emotion as te
import operator
import os.path


def decideEmotion(text):
    # TODO: Filter
    emotion_list = te.get_emotion(text)
    print(emotion_list)
    selected_emotion = max(emotion_list.items(),
                           key=operator.itemgetter(1))[0]
    if(selected_emotion):
        return selected_emotion


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
            emotion = decideEmotion(caption.text)
            caption.text = "<p id='{0}'>{1}</p>".format(
                emotion.lower(), caption.text)

        vtt.save(emotive_subtitle_path)
