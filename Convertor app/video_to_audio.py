import moviepy.editor
from tkinter import filedialog, messagebox
import os
import datetime


# function for converting video to audio
def converting_video_to_audio():
    try:
        if not os.path.exists("A:\\My Projects\\Android Subsystem for Windows (Python)\\Convertor app\\Video to Audio"):
            os.mkdir("A:\\My Projects\\Android Subsystem for Windows (Python)\\Convertor app\\Video to Audio")

        vid = filedialog.askopenfilename(title="Select Video")
        video = moviepy.editor.VideoFileClip(vid)
        aud = video.audio
        current_time = datetime.datetime.now().strftime("%d%m%y%H%M%S")
        aud.write_audiofile(f"A:\\My Projects\\Android Subsystem for Windows (Python)\\Convertor app\\Video to Audio\\Audiofile_{current_time}.mp3")
        messagebox.showinfo("Video to audio", "File saved successfully in (A:\\My Projects\\Android Subsystem for Windows (Python)\\Convertor app\\Video to Audio) location")
    except OSError:
        messagebox.showerror("Video to audio", "Something went wrong")


converting_video_to_audio()
