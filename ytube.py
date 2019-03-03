from pytube import YouTube
import sys
if len(sys.argv) !=2:
	print("Usage : python <filename.py> <video_url>")
	sys.exit(1)
videoUrl = sys.argv[1]
yt = YouTube(videoUrl)
print("Downloading",yt.title)
download = yt.streams.first()
download.download()
print("Video Downloaded in current directory")

