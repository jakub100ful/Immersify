import webvtt
import text2emotion as te
import operator


def decideEmotion(text):
    emotion_list = te.get_emotion(text)
    selected_emotion = max(emotion_list.items(),
                           key=operator.itemgetter(1))[0]
    if(selected_emotion):
        return selected_emotion


def classifySubtitle(video_id):
    subtitle_path = "static/videos/{0}/{1}_subtitles.vtt".format(
        video_id, video_id)

    vtt = webvtt.read(subtitle_path)

    for caption in vtt:
        print(caption.text)
        emotion = decideEmotion(caption.text)
        caption.text = '<{0}>{1}</{2}>'.format(
            emotion.lower(), caption.text, emotion.lower())

    vtt.save(
        './static/videos/{}/{}_emotive_subtitles.vtt'.format(video_id, video_id))
