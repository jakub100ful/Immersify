import webvtt

def classifySubtitle(subtitleFile){
    try:
        for caption in webvtt.read('captions.vtt'):
            print(caption.start)
            print(caption.end)
            print(caption.text)
    except:
        print("File could not be open.")
}
