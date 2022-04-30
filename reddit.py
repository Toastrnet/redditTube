# Pull current hottest post from r/askreddit
# Grab the top 5 comments from said post

import praw
from praw.models import MoreComments
import pandas as pd
from gtts import gTTS
import csv
from moviepy.editor import *
from mutagen.mp3 import MP3
import shutil


language = "en"


def listToStr(s):
    strinit = ""

    for ele in s:
        strinit += ele

    return strinit


# Login into reddit application
reddit_read_only = praw.Reddit(client_id="CLIENT-ID",
                               client_secret="CLIENT-SECRET",
                               user_agent="USER-AGENT")

# Set the subreddit as r/askreddit
subreddit = reddit_read_only.subreddit("askreddit")

# Display the name of the Subreddit
print("SubReddit Name:", subreddit.display_name)

# Grab the current hottest post
post = subreddit.hot(limit=1)

for post in post:
    url = post.url
    submission = reddit_read_only.submission(url=url)

    print("Post Title: ", post.title)
    title_ = post.title
    title = post.title + "..."

    post_comments = []

    for comment in submission.comments:
        if type(comment) == MoreComments:
            continue

        post_comments.append(comment.body + "... ... ...")

    # creating a dataframe
    del post_comments[5:]
    comments_df = pd.DataFrame(post_comments)
    comments_df.to_csv("comments.csv", index=False, header=False)

# Converts the Title of post to audio
print("Title: ", title)
voiceTitle = gTTS(text=title, lang=language, slow=False)
voiceTitle.save("title.mp3")

# Read the comments.csv file
rowCount = 1
with open("comments.csv", encoding="Latin1") as f:
    reader = csv.reader(f)
    for row in reader:
        print(rowCount, ":")
        print(" ".join(row))
        print("------------------------------------------------")
        rowCount += 1

# Converts top five comments to audio
print(post_comments)
voiceComments = gTTS(text=listToStr(post_comments), lang=language, slow=False)
voiceComments.save("comments.mp3")

# Combine title + comments into one audio file
combined = title + listToStr(post_comments)
voiceCombined = gTTS(text=combined, lang=language, slow=False)
voiceCombined.save("combined.mp3")

# Find the length of the audio file
audio = MP3("combined.mp3")
audioInfo = audio.info
audioLength = int(audioInfo.length)
print(audioLength)

# Add the audio to a base video file
shutil.copyfile("basevideo.mp4", "baseclip.mp4")  # Make a copy of the base video
videoClip = VideoFileClip("baseclip.mp4")
videoClip = videoClip.subclip(0, audioLength)  # Cut video to same length as audio
audioClip = AudioFileClip("combined.mp3")
newVideoClip = videoClip.set_audio(audioClip)  # Combine the video and audio
newVideoClip.write_videofile("final.mp4")  # Export new video
