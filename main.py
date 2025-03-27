from pytube import YouTube

YouTube('https://www.youtu.be/ME6kweCwSP4').streams.first().download()
yt = YouTube('http://youtube.com/watch?v=ME6kweCwSP4')
yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download()