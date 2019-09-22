import subprocess
import tkinter
r=tkinter.Tk()
r.withdraw()
print(r.clipboard_get())
subprocess.call('youtube-dl -o "D:\\Torrent\\%(title)s.%(ext)s" -f "mp4"  "'+r.clipboard_get()+'"')

#youtube-dl -o "D:\Torrent\%(title)s.%(ext)s" -x --audio-format "mp3"  "$(Get-Clipboard)" #for powershell only