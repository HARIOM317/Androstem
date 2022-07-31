# Importing useful packages
from tkinter import *
from pytube import YouTube
from tkinter import messagebox
import pyautogui        # for batter graphics
from threading import Thread
import os
import webbrowser


# threading in search function
def threading_search():
    t1 = Thread(target=search)
    t1.start()


# function for searching available resolution for given link
def search():
    try:
        download_button.config(state=NORMAL)

        link = entry_box.get()
        youtube = YouTube(link)

        title_label.config(text="Title : ")
        video_title.config(text=youtube.title)

        # deleting old items from listbox
        listbox1.delete(0, END)
        listbox2.delete(0, END)
        listbox3.delete(0, END)

        # for audio file
        global audio_resolution
        audio_resolution = youtube.streams.filter(only_audio=True)
        available_audio_resolutions = list(enumerate(audio_resolution))
        for i in available_audio_resolutions:
            listbox1.insert(END, str(i))

        # for video file
        global video_resolution
        video_resolution = youtube.streams.filter(only_video=True)
        available_video_resolutions = list(enumerate(video_resolution))
        for i in available_video_resolutions:
            listbox2.insert(END, str(i))

        # for video with audio file
        global audio_video_resolution
        audio_video_resolution = youtube.streams.filter(progressive=True).all()
        available_audio_video_resolutions = list(enumerate(audio_video_resolution))
        for i in available_audio_video_resolutions:
            listbox3.insert(END, str(i))

    except:
        messagebox.showinfo("Youtube video downloader", "Something went wrong!")


# threading in download function
def threading_download():
    t1 = Thread(target=download)
    t1.start()


# function for download selected file from listbox
def download():
    try:
        if not os.path.exists("A:\\My Projects\\Android Subsystem for Windows (Python)\\Youtube videos downloader\\YouTube Videos"):
            os.mkdir("A:\\My Projects\\Android Subsystem for Windows (Python)\\Youtube videos downloader\\YouTube Videos")

        download_button.config(fg="#28d1ff")
        download_label.config(text="Downloading...")
        message_label.config(text="Downloading may take some time. Please don't close the app for continuing.")

        # for audio file
        for i in listbox1.curselection():
            if i == listbox1.curselection()[0]:
                audio_resolution[i].download("A:\\My Projects\\Android Subsystem for Windows (Python)\\Youtube videos downloader\\YouTube Videos")
                messagebox.showinfo("Youtube video downloader", "Download successfully in (A:\\My Projects\\Android Subsystem for Windows (Python)\\Youtube videos downloader\\YouTube Videos) directory")
            else:
                messagebox.showinfo("Youtube video downloader", "Something went wrong!")

        # for video file
        for j in listbox2.curselection():
            if j == listbox2.curselection()[0]:
                video_resolution[j].download("A:\\My Projects\\Android Subsystem for Windows (Python)\\Youtube videos downloader\\YouTube Videos")
                messagebox.showinfo("Youtube video downloader", "Download successfully in (A:\\My Projects\\Android Subsystem for Windows (Python)\\Youtube videos downloader\\YouTube Videos) directory")
            else:
                messagebox.showinfo("Youtube video downloader", "Something went wrong!")

        # for video with audio file
        for k in listbox3.curselection():
            if k == listbox3.curselection()[0]:
                audio_video_resolution[k].download("A:\\My Projects\\Android Subsystem for Windows (Python)\\Youtube videos downloader\\YouTube Videos")
                messagebox.showinfo("Youtube video downloader", "Download successfully in (A:\\My Projects\\Android Subsystem for Windows (Python)\\Youtube videos downloader\\YouTube Videos) directory")
            else:
                messagebox.showinfo("Youtube video downloader", "Something went wrong!")

        download_button.config(fg="white")
        download_label.config(text="")
        message_label.config(text="")

    except:
        download_button.config(fg="white")
        download_label.config(text="")
        message_label.config(text="")
        messagebox.showerror("Youtube video downloader", "The video could not be downloaded")


# starting point of program
if __name__ == '__main__':
    # creating window
    root = Tk()
    root.geometry("1650x900+130+20")
    root.resizable(False, False)
    root.title("V Downloader")
    root.wm_iconbitmap("A:\\My Projects\\Android Subsystem for Windows (Python)\\Youtube videos downloader\\video_downloader_icon.ico")

    # creating frames
    top_frame = Frame(root, width=1000, height=150, bg='#272727')
    top_frame.pack(side=TOP, fill=X)

    middle_frame1 = LabelFrame(root, width=550, height=700, bg='#272727', fg='#00eafd', font=("MV Boli", 13), bd=0, relief=FLAT, text="Available audio resolutions")
    middle_frame1.place(x=0, y=150)

    middle_frame2 = LabelFrame(root, width=550, height=700, bg='#272727', fg='#00eafd', font=("MV Boli", 13), bd=0, relief=FLAT, text="Available video resolutions")
    middle_frame2.place(x=550, y=150)

    middle_frame3 = LabelFrame(root, width=550, height=700, bg='#272727', fg='#00eafd', font=("MV Boli", 13), bd=0, relief=FLAT, text="Available audio & video resolutions")
    middle_frame3.place(x=1100, y=150)

    bottom_frame = Frame(root, width=1000, height=50, bg='#272727')
    bottom_frame.pack(side=BOTTOM, fill=X)

    Label(top_frame, text="Enter URL", font=("Pristina", 15), bg="#272727", fg="white").place(x=10, y=18)

    url_box = PhotoImage(file="A:\\My Projects\\Android Subsystem for Windows (Python)\\Youtube videos downloader\\url_box.png")
    Label(top_frame, image=url_box, bg="#272727").place(x=150, y=0)

    # entry box for enter url
    entry_box = Entry(root, width=28, font=("Pristina", 16), bg="#141414", fg='white', bd=0, relief=FLAT)
    entry_box.bind("<Return>", lambda e: threading_search())
    entry_box.place(x=180, y=17)

    search_icon = PhotoImage(file="A:\\My Projects\\Android Subsystem for Windows (Python)\\Youtube videos downloader\\search_icon.png")

    search_button = Button(top_frame, image=search_icon, command=threading_search, bg="#141414", activebackground="#141414", bd=0, relief=FLAT)
    search_button.place(x=550, y=17)

    # function for opening YouTube
    def open_youtube():
        webbrowser.open("https://www.youtube.com/")

    youtube_icon = PhotoImage(file="A:\\My Projects\\Android Subsystem for Windows (Python)\\Youtube videos downloader\\youtube.png")

    # YouTube button
    youtube_button = Button(top_frame, image=youtube_icon, text="Open YouTube", bg="#272727", activebackground="#272727", bd=0, relief=FLAT, compound=LEFT, fg='white', activeforeground='white', command=open_youtube)
    youtube_button.place(x=1470, y=17)

    title_label = Label(top_frame, text="", font=("Corbel", 15, 'italic'), bg="#272727", fg='light blue')
    title_label.place(x=10, y=85)
    video_title = Label(top_frame, text="", font=("Corbel", 15, 'italic'), bg="#272727", fg='light blue')
    video_title.place(x=100, y=85)

    # Creating listbox for different types of file
    listbox1 = Listbox(middle_frame1, selectbackground='#12fff0', selectforeground='black', selectborderwidth=2, font=("Gabriola", 15), bd=0.5, relief=RIDGE, bg="#202020", fg='white', justify=LEFT, highlightthickness=0)
    listbox1.place(relx=0, rely=0, relheight=1, relwidth=1)

    listbox2 = Listbox(middle_frame2, selectbackground='#12fff0', selectforeground='black', selectborderwidth=2, font=("Gabriola", 15), bd=0.5, relief=RIDGE, bg="#202020", fg='white', justify=LEFT, highlightthickness=0)
    listbox2.place(relx=0, rely=0, relheight=1, relwidth=1)

    listbox3 = Listbox(middle_frame3, selectbackground='#12fff0', selectforeground='black', selectborderwidth=2, font=("Gabriola", 15), bd=0.5, relief=RIDGE, bg="#202020", fg='white', justify=LEFT, highlightthickness=0)
    listbox3.place(relx=0, rely=0, relheight=1, relwidth=1)

    download_label = Label(bottom_frame, text="", font=("Comic Sans MS", 12), fg='orange', bg="#272727")
    download_label.place(x=200, y=5)

    message_label = Label(bottom_frame, text="", font=("Bahnschrift Light Condensed", 12), bg="#272727", fg='gold')
    message_label.place(x=1020, y=7)

    # download button
    download_button = Button(bottom_frame, text="Download", command=threading_download, bg="#272727", activebackground="#272727", bd=0, relief=FLAT, font=("Bahnschrift Light Condensed", 13), fg='white', activeforeground='white', cursor='hand2', state=DISABLED)
    download_button.place(x=10, y=0)

    root.mainloop()
