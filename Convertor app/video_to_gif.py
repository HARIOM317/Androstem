from tkinter import filedialog, messagebox
from moviepy.editor import *
import datetime

try:
    if not os.path.exists("A:\\My Projects\\Android Subsystem for Windows (Python)\\Convertor app\\Video to GIF"):
        os.mkdir("A:\\My Projects\\Android Subsystem for Windows (Python)\\Convertor app\\Video to GIF")
    vid = filedialog.askopenfilename(title="Select a Video")
    clip = (VideoFileClip(vid).subclip(0.3))
    current_time = datetime.datetime.now().strftime("%d%m%y%H%M%S")
    clip.write_gif \
        (f"A:\\My Projects\\Android Subsystem for Windows (Python)\\Convertor app\\Video to GIF\\GIF_{current_time}.gif", fps=10)
    messagebox.showinfo("Video to GIF", "File saved successfully in (A:\\My Projects\\Android Subsystem for Windows (Python)\\Convertor app\\Video to GIF) location")
except OSError:
    messagebox.showerror("Video to GIF", "Something went wrong or Please check your internet connection")
