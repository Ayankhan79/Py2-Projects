# Importing the yt_dlp library, which is an advanced version of youtube-dl.
# It allows you to download videos from a wide range of websites, not limited to YouTube.
import yt_dlp

# Prompting the user to input the URL of the video they want to download.
url = input("Enter url: \n")

# Creating a context (using 'with' statement) for the YoutubeDL class from the yt_dlp library.
# This context will handle the downloading process and close automatically when done.
with yt_dlp.YoutubeDL() as ydl:
    
    # Using the 'download' method of YoutubeDL to start downloading the video.
    # The 'download' method takes a list of URLs as an argument, even if only one URL is provided.
    ydl.download([url])
