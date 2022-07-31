# Importing required modules
import os
from tkinter import *
import pickle
from tkinter import filedialog
from tkinter import PhotoImage
from pygame import mixer
from PIL import Image, ImageTk, ImageSequence
import time

# creating Player class
class Player(Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.config(bg='#35363b')
        self.pack()

        mixer.init()

        # Open pickle file for loading all songs
        if os.path.exists('A:\\My Projects\\Android Subsystem for Windows (Python)\\Music Player\\songs.pickle'):
            with open('A:\\My Projects\\Android Subsystem for Windows (Python)\\Music Player\\songs.pickle', 'rb') as f:
                self.playlist = pickle.load(f)
        else:
            self.playlist = []

        self.current = 0
        self.paused = True
        self.played = False

        self.create_frames()
        self.track_widgets()
        self.control_widgets()
        self.tracklist_widgets()

    def create_frames(self):
        # Create frame for current playing song and GIF window
        self.track = Frame(self, bg='black', bd=0, relief=FLAT, highlightthickness=1, highlightbackground='#00fbff')
        self.track.config(width=410, height=300)
        self.track.grid(row=0, column=0, padx=10, pady=10)

        # Create frame for song list
        self.tracklist = LabelFrame(self, text=f'Playlist songs - {str(len(self.playlist))}', font=('Aparajita', 15), bg='#35363b', fg='dark gray', bd=0, relief=FLAT)
        self.tracklist.config(width=190, height=400)
        self.tracklist.grid(row=0, column=1, rowspan=3, pady=5)

        # Create frame for buttons
        self.control = LabelFrame(self, font=('times new roman', 15, 'bold'), bg='#35363b', fg='white', bd=0)
        self.control.config(width=410, height=80)
        self.control.grid(row=2, column=0, pady=5, padx=10)

    # Function For Updating First Frame
    def track_widgets(self):
        self.canvas = Label(self.track, image=img)
        self.canvas.config(width=400, height=290, bg='black')
        self.canvas.grid(row=0, column=0)

        self.songtrack = Label(self.track, font=("Comic Sans MS", 12), bg='black', fg='#ffbd00')
        self.songtrack['text'] = "Mp3 Music Player"
        self.songtrack.config(width=32, height=1)
        self.songtrack.grid(row=1, column=0)

    # Function For Updating Button Frame
    def control_widgets(self):
        self.loadSongs = Button(self.control, bg='#21b3de', fg='black', font=("Bahnschrift Light Condensed", 18), cursor='hand2', activebackground='#21b3de', bd=1, relief=RIDGE, overrelief=GROOVE)
        self.loadSongs['text'] = 'Load Songs'
        self.loadSongs['command'] = self.retrieve_songs
        self.loadSongs.grid(row=0, column=0, padx=10)

        self.prev = Button(self.control, image=prev, bd=0, bg='#35363b', cursor='hand2', activebackground='#35363b', relief=FLAT)
        self.prev['command'] = self.prev_song
        self.prev.grid(row=0, column=1)

        self.pause = Button(self.control, image=pause, bd=0, bg='#35363b', cursor='hand2', activebackground='#35363b', relief=FLAT)
        self.pause['command'] = self.pause_song
        self.pause.grid(row=0, column=2)

        self.next = Button(self.control, image=next, bd=0, bg='#35363b', cursor='hand2', activebackground='#35363b', relief=FLAT)
        self.next['command'] = self.next_song
        self.next.grid(row=0, column=3)

        # Create a slider in music list frame for volume up - down
        self.volume = DoubleVar()
        self.slider = Scale(self.tracklist, from_=100, to=0, orient=VERTICAL, cursor='hand2', bg='#35363b', fg='#08E8DE', activebackground='orange', relief=FLAT, bd=0, length=500, width=7, troughcolor='#21b3de', label='Volume', font='Georgia 10', highlightbackground='#32343a', sliderrelief=RIDGE)
        self.slider['variable'] = self.volume
        self.slider.set(50)     # Set default volume value
        mixer.music.set_volume(0.5)     # Set default volume according the volume value
        self.slider['command'] = self.change_volume
        self.slider.grid(row=0, column=4, pady=10)

    # Updating the songs list frame
    def tracklist_widgets(self):
        # Create a scollbar in songs list
        self.scrollbar = Scrollbar(self.tracklist, orient=VERTICAL, cursor='hand2', width=15, bd=0, relief=FLAT, highlightcolor='yellow', activerelief=FLAT)
        self.scrollbar.grid(row=0, column=1, rowspan=5, sticky=NS)

        # creating a listbox for displaying all songs
        self.list = Listbox(self.tracklist, selectmode=SINGLE, yscrollcommand=self.scrollbar.set, selectbackground='#7FFFD4', width=52, height=12, bg='#141516', fg='#ffffff', font=("Gabriola", 15), selectborderwidth=3, selectforeground='black', cursor='hand2', bd=2, relief=RIDGE, highlightbackground='light blue', highlightcolor='#00b3ea', highlightthickness=2)
        self.enumerate_songs()
        self.list.bind('<Double-1>', self.play_songs)   # Bind listbox to double-click for play the song
        self.list.bind('<space>', lambda e: self.pause_song())   # Bind listbox to space bar for play and pause the song
        self.list.bind('<Left>', lambda e: self.prev_song())   # Bind listbox to left arrow key for next song
        self.list.bind('<Right>', lambda e: self.next_song())   # Bind listbox to right arrow key for previews song
        self.scrollbar.config(command=self.list.yview)
        self.list.grid(row=0, column=0, rowspan=5)

    # create a function for enumerate all songs of a directory
    def enumerate_songs(self):
        for index, song in enumerate(self.playlist):
            self.list.insert(index, os.path.basename(song))

    # creting a function for retrieve all songs in list
    def retrieve_songs(self):
        self.songlist = []
        directory = filedialog.askdirectory()
        for root_, dirs, files in os.walk(directory):
            for file in files:
                if os.path.splitext(file)[1] == '.mp3':
                    path = (root_ + '/' + file).replace('\\', '/')
                    self.songlist.append(path)

        # Crete a pickle file for writing all songs of recentaly open directory
        with open('songs.pickle', 'wb') as f:
            pickle.dump(self.songlist, f)

        self.playlist = self.songlist
        self.tracklist['text'] = f'PlayList - {str(len(self.playlist))}'    # Display No. of songs available in directory
        self.list.delete(0, END)
        self.enumerate_songs()

    # Creating function for play the song
    def play_songs(self, event=None):
        if event is not None:
            self.current = self.list.curselection()[0]
            for i in range(len(self.playlist)):
                self.list.itemconfigure(i, fg='white')

        mixer.music.load(self.playlist[self.current])
        self.pause['image'] = play
        self.paused = False
        self.played = True
        self.songtrack['anchor'] = W
        self.songtrack['text'] = os.path.basename(self.playlist[self.current])
        self.list.activate(self.current)
        self.list.itemconfigure(self.current, fg='#00FFFF')
        mixer.music.play()

    # Creating function for pause the song
    def pause_song(self):
        if not self.paused:
            self.paused = True
            mixer.music.pause()
            self.pause['image'] = pause     # Change Image from play to pause
        else:
            if self.played == False:
                self.play_songs()
            self.paused = False
            mixer.music.unpause()
            self.pause['image'] = play      # Change Image from pause to play

    # Creating function for going on previese song
    def prev_song(self):
        if self.current > 0:
            self.current -= 1
        else:
            self.current = 0
        self.list.itemconfigure(self.current+1, fg='white')
        self.play_songs()

    # Creating function for going on next song
    def next_song(self):
        if self.current < len(self.playlist) - 1:
            self.current += 1
        else:
            self.current = 0
            self.play_songs()

        self.list.itemconfigure(self.current-1, fg='white')
        self.play_songs()

    # create a function for change the music volume
    def change_volume(self, event=None):
        self.v = self.volume.get()
        mixer.music.set_volume(self.v / 100)

# Start program execution from here
if __name__ == '__main__':
    # Create instance of Tk class
    root = Tk()
    root.geometry('970x570+180+20')
    root.wm_attributes('-alpha', 0.98)
    root.resizable(False, False)
    root.wm_title("Music Player")
    root.config(bg="#011627")
    root.wm_iconbitmap("A:\\My Projects\\Android Subsystem for Windows (Python)\\Music Player\\Music_Logo.ico")

    # Set images on buttons and frames
    img = PhotoImage(file="A:\\My Projects\\Android Subsystem for Windows (Python)\\Music Player\\mymusic.png")
    next = PhotoImage(file="A:\\My Projects\\Android Subsystem for Windows (Python)\\Music Player\\next_music.png")
    prev = PhotoImage(file="A:\\My Projects\\Android Subsystem for Windows (Python)\\Music Player\\previese_music.png")
    play = PhotoImage(file="A:\\My Projects\\Android Subsystem for Windows (Python)\\Music Player\\play_music.png")
    pause = PhotoImage(file="A:\\My Projects\\Android Subsystem for Windows (Python)\\Music Player\\pause_music.png")

    # Create instance of Player class
    app = Player(master=root)

    # Play GIF
    try:
        while True:
            global gif
            gif = Image.open("A:\\My Projects\\Android Subsystem for Windows (Python)\\Music Player\\music_player.gif")

            label = Label(app.canvas, bd=0, activebackground='black', activeforeground='black')
            label.place(x=55, y=5)

            for gif in ImageSequence.Iterator(gif):
                gif = gif.resize((300, 175))
                gif = ImageTk.PhotoImage(gif)

                label.config(image=gif, activebackground='black')
                root.update()
                time.sleep(0.01)
    except:
        pass

    root.mainloop()