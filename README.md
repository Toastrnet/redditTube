# autoTube
autoTube is a program to automatically make Reddit TTS YouTube Shorts. 

# Requirements
1) praw
2) pandas
3) gTTS
4) moviepy
5) mutagen
6) reddit app

# How to setup the reddit app
1) Go to https://www.reddit.com/prefs/apps
2) Click on "are you a developer? create an app…"
3) Enter the name and description of your choice. In the redirect uri box, enter http://localhost:8080
4) After entering the details, click on “create app”
The Reddit app has been created. Note down the client_id, secret, and user_agent values. These values will be used to connect to Reddit using praw

# Running the script
After you've setup your reddit app and put in you client_id, secret, and user_agent. Make sure you have a video saved in the working directory saved as "basevideo.mp4". You can then run the script like any other python script.
> $ python autotube.py

From there your final video will be saved as "final.mp4" along with several other mp3 files for debugging.
