# this script is for downloading youtube videos
# https://www.freecodecamp.org/news/python-automation-scripts/

import sys
import pytube

get_link = input("Enter the Youtube url: ")
if not get_link:
    print("Invalid url detected, exiting.... ")
    sys.exit()
if not get_link.startswith("https:") or not get_link.startswith("http:"):
    print("Input is not a valid url: ")
    sys.exit()
video_download = pytube.YouTube(get_link)
video_download.streams.first().download()
print(f"Video is downloaded: {get_link}")

# NOTE:
# this works but video format is video/3gpp! how to get HD or 1080p format?
# TODO:
# how to show progress bar?
# ask user in where location to put the download file?
