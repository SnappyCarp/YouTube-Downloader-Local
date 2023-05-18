from yt_dlp import YoutubeDL
import requests, time
from tkinter import Tk, Label, Button, Text



ydl_opts = {}
def download(url):
    try:
      with YoutubeDL(ydl_opts) as ydl: ydl.download([url])
    except: print('Download Error')
    else:
      raise SystemExit('Download Complete')

def button_start():
  value = txt.get(1.0, "end-1c")
  try: r = requests.get(value)
  except: pass
  else:
    if "Video unavailable" in r.text: print('Invalid Url')
    else: download(value)

def main():
  global txt
  root = Tk()
  root.title("YouTube Downloader")
  root.geometry('700x700')
  lab = Label(root, text='Enter Video Url Here')
  btn = Button(root, command=button_start, text='Download')
  txt = Text(root, height = 5, width = 30)
  lab.pack()
  txt.pack()
  btn.pack()
  root.mainloop()


main()
