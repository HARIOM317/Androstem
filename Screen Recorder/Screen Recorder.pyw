from tkinter import *
from tkinter import messagebox
from threading import Thread
import pyscreenrec
import os


# create start_recording function to start recording
def start_recording():
    if not os.path.exists("A:\\My Projects\\Android Subsystem for Windows (Python)\\Screen Recorder\\Recording"):
        os.mkdir("A:\\My Projects\\Android Subsystem for Windows (Python)\\Screen Recorder\\Recording")

    try:
        file = Filename.get()
        my_label.config(text="Recording...")
        rec.start_recording(str(f"A:\\My Projects\\Android Subsystem for Windows (Python)\\Screen Recorder\\Recording\\{file}.mp4"), 5)
    except:
        messagebox.showinfo("Screen Recorder", "Something went wrong")


# Handle threading of start recording
def Threading_start():
    t = Thread(target=start_recording)
    t.start()


# create pause_recording function to pause recording
def pause_recording():
    try:
        my_label.config(text="Paused")
        rec.pause_recording()
    except Exception as e:
        messagebox.showinfo("Screen Recorder", f"Error- {e}")
# Handle threading of pause recording


def Threading_pause():
    t = Thread(target=pause_recording)
    t.start()


# create stop_recording function to stop recording
def stop_recording():
    try:
        my_label.config(text="File Saved Successfully...")
        rec.stop_recording()
    except Exception as e:
        messagebox.showinfo("Screen Recorder", f"Error- {e}")


# Handle threading of stop recording
def Threading_stop():
    t = Thread(target=stop_recording)
    t.start()


# create resume_recording function to resume recording
def resume_recording():
    try:
        my_label.config(text="Recording...")
        rec.resume_recording()
    except:
        messagebox.showinfo("Screen Recorder", "Please start recording first")


# Handle threading of pause recording
def Threading_resume():
    t = Thread(target=resume_recording)
    t.start()


# Creating main window
root = Tk()
root.title("Screen Recorder")
root.geometry("400x600+700+80")
root.config(bg="#232734")
root.resizable(False, False)
root.wm_iconbitmap("A:\\My Projects\\Android Subsystem for Windows (Python)\\Screen Recorder\\screen_recorder_icon.ico")
root.attributes('-alpha', 0.98)  # Transparent 2% or 0.02%

rec = pyscreenrec.ScreenRecorder()

# Set Heading
label = Label(root, text="Screen Recorder", bg="#232734", fg='gold', font=("Javanese Text", 20))
label.pack(padx=10, pady=20)

Label(root, text="File Name", font="Aparajita 15", bg="#232734", fg='orange').pack(pady=10)
# Set Entry box for getting file name
Filename = StringVar()
entry = Entry(root, textvariable=Filename, width=25, font="Aparajita 15", fg='white', bg="#1c1f29", justify=CENTER)
entry.pack()
Filename.set("New Recording 1")

# Make a start button
start = Button(root, text="Start", font=("Monotype Corsiva", 20), bd=2, bg="#232734", fg='light green', activebackground="#232734", activeforeground="light green", command=Threading_start, cursor='hand2', padx=5)
start.pack(pady=25)

my_label = Label(root, text="", font=("Pristina", 20), bg='#232734', fg='Yellow')
my_label.pack()

# Make a pause button
pause_button = Button(root, text="Pause", bd=2, bg="#232734", activebackground="#232734", command=Threading_pause, fg='orange', activeforeground='orange', font="Aparajita 15 bold", width=7, cursor='hand2')
pause_button.pack(side=LEFT, anchor='ne', pady=50, padx=13)

# Make a resume button
resume_button = Button(root, text="Resume", bd=2, bg="#232734", activebackground="#232734", command=Threading_resume, fg='green', activeforeground='green', font="Aparajita 15 bold", width=7, cursor='hand2')
resume_button.pack(side=LEFT, anchor='ne', pady=50, padx=13)

# Make a stop button
stop_button = Button(root, text="Stop", bd=2, bg="#232734", activebackground="#232734", command=Threading_stop, fg='red', activeforeground='red', font="Aparajita 15 bold", width=7, cursor='hand2')
stop_button.pack(side=LEFT, anchor='ne', pady=50, padx=13)

root.mainloop()
