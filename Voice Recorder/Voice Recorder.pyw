# Importing Useful Libraries
from tkinter import *
from tkinter import messagebox
import sounddevice as sound
import soundfile as sf
import threading
import queue
import datetime
import time
import os

# Create and initialize variable to current date and time for a separate audio file
address = datetime.datetime.now().strftime("%d%H%M%S")
name = f"Recording-{address}"


def Threading_start():
    t1 = threading.Thread(target=start)
    t1.start()


# Create start function to start recording
def start():
    t1 = threading.Thread(target=recording)     # Use threading so that buttons work properly and program didn't make un-responsible
    t1.start()
    # Crete a Timer
    time_var = 0
    while duration:
        root.update()
        time.sleep(1)
        time_var += 1
        if duration == False:
            time_var = ""
        # Set and update timer in a label
        Label(text=f"{str(time_var)}", font="Georgia 20", width=4, bg="#131c2a", fg='orange').place(x=100, y=350)


# create stop function to stop the recording
def stop():
    global duration
    duration = False
    messagebox.showinfo(message="Recording Finished and Saved Successfully!")


# create play function to play the recently made recording audio file
def play():
    if file_existing:
        # Reading the recently recording audio file if it exists and play it
        data, fs = sf.read(f"A:\\My Projects\\Android Subsystem for Windows (Python)\\Voice Recorder\\Recording\\{name}.wav", dtype='float32')
        sound.play(data, fs)
        sound.wait()
    else:
        # Display and error if file is not found
        messagebox.showerror(message="Please Record Something to Play")


def Threadin_play():
    t1 = threading.Thread(target=play)
    t1.start()


# creating a callback function with 4 arguments so that we can easily use this function in callback variable of InputStream method
def callback(data, frames, time, status):
   q.put(data.copy())


# Create recording function to activate the recording throw mic
def recording():
    if not os.path.exists("A:\\My Projects\\Android Subsystem for Windows (Python)\\Voice Recorder\\Recording"):
        os.mkdir("A:\\My Projects\\Android Subsystem for Windows (Python)\\Voice Recorder\\Recording")

    global duration
    duration = True
    global file_existing
    # Write audio file
    with sf.SoundFile(f"A:\\My Projects\\Android Subsystem for Windows (Python)\\Voice Recorder\\Recording\\{name}.wav", mode='w', samplerate=44100, channels=2) as f:
        with sound.InputStream(samplerate=44100, channels=2, callback=callback):
            while duration == True:
                file_existing = True
                f.write(q.get())


# Start execution of this program from here
if __name__ == '__main__':
    # Create instance of Tk() class and make the window
    root = Tk()
    root.geometry("265x400+400+30")
    root.resizable(False, False)
    root.attributes('-alpha', 0.98)  # Transparent 2% or 0.02%
    root.title("Voice Recorder")
    root.config(bg="#131c2a")
    root.wm_iconbitmap("A:\\My Projects\\Android Subsystem for Windows (Python)\\Voice Recorder\\voice_recorder_icon.ico")

    # set Logo
    logo = PhotoImage(file='A:\\My Projects\\Android Subsystem for Windows (Python)\\Voice Recorder\\voice_recorder.png')
    logoLabel = Label(root, image=logo, bg='#131c2a')
    logoLabel.pack()

    # Creating a queue for containing the audio date
    q = queue.Queue()

    # Creating some variables and initialize them to False
    duration = False
    file_existing = False

    # Create a label to set Voice Recorder on screen
    Label(text="Voice Recorder", font=("Pristina", 25), background="#131c2a", fg='gold').pack(pady=10)

    # __________ Creating Record, Stop and Play Button __________
    record_button = Button(root, font=("Monotype Corsiva", 15), text="Record", bg="#101723", fg='light green', bd=0.5, activeforeground='#08E8DE', activebackground="#101723", relief=GROOVE, width=7, command=Threading_start, cursor='hand2').pack(pady=2)

    stop_button = Button(root, font=("Monotype Corsiva", 15), text="Stop", bg="#101723", fg='red', bd=0.5, activeforeground='#08E8DE', activebackground="#101723", relief=GROOVE, width=7, command=stop, cursor='hand2').pack(pady=2)

    play_button = Button(root, font=("Monotype Corsiva", 15), text="Play", bg="#101723", fg='sky blue', bd=0.5, activeforeground='#08E8DE', activebackground="#101723", relief=GROOVE, width=7, command=Threadin_play, cursor='hand2').pack(pady=2)

    root.mainloop()
