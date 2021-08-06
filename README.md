# Immersify

Immersify is a video player that aims to improve the viewing experience by delivering emotive subtitles that can be customised. It uses machine learning to analyse any scripted video and the subtitle visualisation style can be fully customised.

## Prerequisities

You need to ensure that [Python 3.6](https://www.python.org/downloads/) or later is installed.

# Installation

1. Download a copy of the project and extract it into a preferred folder.
2. Open a command prompt or terminal in the project root folder (Immersify by default).
3. Type the following command to create a virtual environment: `python3 -m venv env`
4. Depending on your operating system, enter one of the following commands to activate the virtual environment.

**On Windows:**  
`env\Scripts\activate`

**On Unix or MacOS:**  
`source env/bin/activate`

5. Install the required packages using pip by entering this command: `pip install -r requirements.txt`.
6. Install the [example videos](https://github.com/jakub100ful/Immersify/releases/tag/1.0) by extracting the `videos` folder into the `static` folder.
7. Start the application through this command `flask run`.

**If you are using MacOS and are having issues with SSL certificates**  
Ensure that you have installed the neccessary SSL bundle. You can do this either by running the native _Certificates.command_ file in the Python directory found in your Applications folder, or by installing the _certifi_ package through pip.

For more information view this article: https://stackoverflow.com/questions/40684543/how-to-make-python-use-ca-certificates-from-mac-os-truststore

# Usage

1. Depending on your operating system, enter one of the following commands to activate the virtual environment.

**On Windows:**
`env\Scripts\activate`

**On Unix or MacOS:**  
`source env/bin/activate`

2. Start the application using `flask run`

3. Paste `127.0.0.1:5000` in your preferred browser's address bar.

**NOTE: Immersify has only been tested on Google Chrome 91.0.4472.77**

You will be shown a library of available videos. Click on the image of a desired video to display the video player. During the first playback, emotional subtitles will be generated as `vidID_emotive_subtitles.vtt` and stored in `static/videos/vidID`. You can edit this file to change the classified emotions. Make sure that the **id** of the HTML tag is either `happy`, `sad`,`fear`,`anger` or `surprise`.

## Adding Videos

When adding new videos to the video player, a folder must be created within the videos directory. This folder must be named after the video id (vidID for future reference). The vidID name pattern is `vid_n` where `n` is equal to total number of video folders+1. For example, “vid1” is a valid name for the folder, and subsequent folders would be named “vid2”, “vid3”, etc. Inside of this folder, there are several files that need to be provided for the system to recognise the video.

| File Name       | Description                                                                                 | Required |
| --------------- | ------------------------------------------------------------------------------------------- | -------- |
| vidID_video     | The video file to be supplied to the video player.                                          | Yes      |
| vidID_subtitles | The subtitle file to be supplied to the video player.                                       | Yes      |
| vidID_metadata  | The metadata that contains information about the video to be presented by the video player. | Yes      |
| vidID_image     | The image file to be supplied as a preview on the home page.                                | No       |

### Metadata File

The metadata file is a JSON file used to give the system information about the video. The video player uses this information for better user experience. The list of keys recognised by the video player can be found in tablex.

| Key         | File Name | Description                                                                         | Required |
| ----------- | --------- | ----------------------------------------------------------------------------------- | -------- |
| id          | String    | The **vidID** for this video. Must correspond to the parent folder name.            | Yes      |
| title       | String    | The title for this video. It could be the name of a movie, or the title of a video. | Yes      |
| description | String    | A short description for the video.                                                  | Yes      |
| language    | String    | The language of the video. Must adhere to the **ISO 639-1:2002** standard.          | Yes      |
| image       | Boolean   | Should be `true` if an image is provided. Default value is `false`.                 | No       |
