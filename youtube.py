import yt_dlp

class Youtube(object):
    def debug(self, msg):
        pass

    def warning(self, msg):
        pass

    def error(self, msg):
        print(msg)

def my_hook(d):
    if d['status'] == 'finished':
        print('Done downloading, now converting...')

link = input('Please enter a url link... MAKE SURE TO USE https://youtube.com/watch?[id]\n')
word = 'playlist'

if word in link.lower():
    ydl_opts = {
        'outtmpl': 'downloaded_music/%(title)s.%(ext)s',
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'noplaylist': False,
        'logger': Youtube(),
        'progress_hooks': [my_hook],
        'verbose': True,
    }
else:
    ydl_opts = {
        'outtmpl': 'downloaded_music/%(title)s.%(ext)s',
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'logger': Youtube(),
        'progress_hooks': [my_hook],
        'verbose': True,
    }

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([link])
print("Done.")