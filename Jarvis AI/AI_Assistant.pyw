# Import useful packages
import pyttsx3
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import datetime
import time
import random
import pyjokes
from tkinter import *
from threading import *
from PIL import Image, ImageTk
from tkinter.ttk import Combobox
import requests
from bs4 import BeautifulSoup
from tkinter import colorchooser, messagebox
from pywikihow import search_wikihow

from gui_automation import GuiAuto
# Make instance of class GuiAuto
Gcurser = GuiAuto()     # for more pixels in GUI

# Initialize engine of pyttsx3
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[2].id)

# create speake function
def speak(audio):
    # Get value of gender and speed combo boxes
    gender = gender_combo_box.get()
    speed = speed_combo_box.get()
    voices = engine.getProperty('voices')

    # define setvoice function to set the gender voice using gender combo box
    def setvoice():
        if gender == 'Male':
            engine.setProperty('voice', voices[0].id)
            engine.say(audio)
            engine.runAndWait()
        elif gender == 'Female1':
            engine.setProperty('voice', voices[1].id)
            engine.say(audio)
            engine.runAndWait()
        else:
            engine.setProperty('voice', voices[2].id)
            engine.say(audio)
            engine.runAndWait()

    # Define the Conditions for voice rate (Slow, Normal, Fast) using speed combo box
    if audio:
        if speed == 'Fast':
            engine.setProperty('rate', 200)
            setvoice()
        elif speed == 'Normal':
            engine.setProperty('rate', 150)
            setvoice()
        else:
            engine.setProperty('rate', 100)
            setvoice()

# create a function to wish user according the time
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good Morning sir!")
    elif 12 <= hour < 18:
        speak("Good Afternoon sir!")
    else:
        speak("Good Evening sir!")

# create the function TakeCommand() for taking any command which will give the user.
def TakeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        time.sleep(1)
        compText.set("Listening...")
        r.adjust_for_ambient_noise(source)  # Remove source noise
        r.pause_threshold = 1
        audio = r.listen(source)    # Listen user query

    try:
        compText.set("Recognizing...")
        query = r.recognize_google(audio, language='en-in')

    except:
        compText.set("Sorry sir i didn't understand what you said. \n\nSomething went wrong or please check your internet connection is ok")
        return "None"
    return query

# Handle threading of activate function
def Threading_activate():
    t1 = Thread(target=activate)
    t1.start()

# create activate function to activate the AI Assistant
def activate():
    try:
        import pywhatkit
        # Calling wishMe function to wish the user
        wishMe()
        while True:
            random_song = random.randint(1, 243)
            query = TakeCommand().lower()

            # Logic for executing tasks based on query
            if 'wikipedia' in query:
                try:
                    speak('searching wikipedia...')
                    results = wikipedia.summary(query, sentences=1)
                    userText.set(f"{query}")
                    compText.set(results)
                    speak("According to wikipedia")
                    speak(results)
                except:
                    speak("No such wikipedia found!")

            elif 'what is' in query or "what are" in query or 'who is' in query or 'search' in query:
                pywhatkit.search(query)
                query = query.replace("search", "")
                url = "https://www.google.com/search?q=" + query
                r = requests.get(url)
                data = BeautifulSoup(r.text, "html.parser")
                ans_ = data.find("div", class_="BNeawe").text
                userText.set(f"User asked - {query}")
                compText.set(f"Answer - {ans_}")
                speak(f"{ans_}")

            elif 'how to' in query:
                pywhatkit.search(query)
                userText.set(query)
                compText.set("Getting things ready...")
                max_result = 1
                result = search_wikihow(query, max_result)
                assert len(result) == 1
                compText.set(result[0])
                speak(result[0].summary)

            elif 'temperature' in query:
                url = "https://www.google.com/search?q=temperature"
                r = requests.get(url)
                data = BeautifulSoup(r.text, "html.parser")
                ans_ = data.find("div", class_="BNeawe").text
                userText.set(f"User asked - {query}")
                compText.set(f"Anandipura, MP \n{ans_}")
                speak(f"{ans_}")

            elif 'play music' in query or 'play songs' in query or 'play a song' in query or 'open music' in query:
                userText.set(query)
                compText.set("Enjoy the music")
                music_dir = 'C:\\Users\\hariom mewada\\Music'
                songs = os.listdir(music_dir)
                os.startfile(os.path.join(music_dir, songs[random_song]))

            elif 'close browser' in query or 'close the browser' in query or 'close my browser' in query:
                try:
                    userText.set("Close the browser.")
                    compText.set("Closed Browser Successfully!")
                    speak("Closing the browser...")
                    os.system("taskkill /im msedge.exe /f")     # it will close the browser
                except Exception as e:
                    speak("The edge Browser is not found in progress...")
                    compText.set(str(e))

            elif 'your name' in query or 'tell me about your self' in query or 'who are you' in query:
                userText.set(query)
                compText.set("I am an AI Assistant and i can help you to automate your daily tasks. please tell me How may i help you?")
                speak("I am an AI Assistant. How may i help you?")

            elif 'how old are you' in query or 'your age' in query:
                userText.set(query)
                compText.set("There is no age define for me but i created at 15 March 2022.")
                speak("There is no age define for me but i created at 15 March 2022.")

            elif 'joke' in query:
                say_joke()

            elif 'open youtube' in query or 'open the youtube' in query or 'open my youtube' in query:
                openYoutube()

            elif 'open google' in query or 'open the google' in query or 'open my google' in query:
                openGoogle()

            elif 'open gmail' in query or 'open the gmail' in query or 'open my gmail' in query:
                Gmail()

            elif 'open outlook' in query or 'open the outlook' in query or 'open my outlook' in query:
                open_outlook()

            elif 'open code' in query or 'vs code' in query or 'visual studio code' in query:
                userText.set(query)
                compText.set("VS Code has been opened")
                code_path = "C:\\Users\\hariom mewada\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
                os.startfile(code_path)

            elif 'time' in query or 'the time' in query:
                current_time = datetime.datetime.now().strftime("%I:%M:%S %p")
                userText.set(query)
                compText.set(current_time)
                speak(f"The current time is: {current_time}")

            elif 'empty recycle bin' in query or 'empty my recycle bin' in query or 'clear recycle bin' in query:
                userText.set(query)
                compText.set("Are you sure to clear the recycle bin?")
                Empty_recycle_bin()

            elif 'quit' in query or 'exit' in query:
                speak("Thanks sir! Have a nice day.")
                root.destroy()
                exit()

            else:
                userText.set(query)

            time.sleep(3)

    except:
        messagebox.showinfo("AI Assistant", "Please check your internet connection")

# create function to automatically send the email
def sendEmail():
    webbrowser.open("Enter your send gmail url here")

def Empty_recycle_bin():
    try:
        import winshell
        winshell.recycle_bin().empty(confirm=True, show_progress=True, sound=True)
        speak("done sir")
    except:
        messagebox.showinfo("Recycle bin", "Already clear the recycle bin")

# create function for opening the YouTube
def openYoutube():
    try:
        userText.set("Request for opening YouTube")
        compText.set("YouTube has been opened Successfully")
        webbrowser.open("youtube.com")
    except:
        compText.set("Something went wrong!")

# create function for opening the Google
def openGoogle():
    try:
        userText.set("Request for opening Google")
        compText.set("Google has been opened successfully")
        webbrowser.open("google.com")
    except Exception as e:
        compText.set("Something went wrong!")

# create function for opening the Chrome
def openChrome():
    try:
        userText.set("Request for opening Google Chrome")
        compText.set("Google Chrome has been opened successfully")
        os.startfile("C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Google Chrome")
    except Exception as e:
        compText.set("Something went wrong!")

# create function for opening the gmail
def Gmail():
    try:
        userText.set("Request for opening Gmail")
        compText.set("Gmail has been opened successfully")
        webbrowser.open("mail.google.com")
    except Exception as e:
        compText.set("Something went wrong!")

# create function for opening the Google Photos
def open_Photos():
    try:
        userText.set("Request for opening Google Photos")
        compText.set("Google Photos has been opened successfully")
        webbrowser.open("photos.google.com")
    except Exception as e:
        compText.set("Something went wrong!")

# create function for opening the Outlook
def open_outlook():
    try:
        userText.set("Request for opening Microsoft Outlook")
        compText.set("Microsoft Outlook has been opened successfully")
        webbrowser.open("outlook.live.com")
    except Exception as e:
        compText.set("Something went wrong!")

# create function for opening the Google Drive
def open_drive():
    try:
        userText.set("Request for opening Google Drive")
        compText.set("Google Drive has been opened successfully")
        webbrowser.open("drive.google.com")
    except Exception as e:
        compText.set("Something went wrong!")

# Creating theme 1
def theme1():
    root.config(bg="#2b2b2b")
    Panel.config(bg="#2b2b2b")
    activate_button.config(bg="#2b2b2b")
    close_button.config(bg="#2b2b2b")
    Iconbar_Left.config(bg="#2b2b2b")
    Iconbar_Right.config(bg="#2b2b2b")
    youtube_button.config(bg="#2b2b2b")
    chrome_button.config(bg="#2b2b2b")
    drive_button.config(bg="#2b2b2b")
    photos_button.config(bg="#2b2b2b")
    gmail_button.config(bg="#2b2b2b")
    outlook_button.config(bg="#2b2b2b")
    recycle_bin_button.config(bg="#2b2b2b")
    send_mail_button.config(bg="#2b2b2b")
    user_image.config(bg="#2b2b2b")
    assistant_image.config(bg="#2b2b2b")
    userFrame.config(bg="#2b2b2b")
    compFrame.config(bg="#2b2b2b")
    open_side_menu.config(bg="#2b2b2b")
    time_label.config(bg="#2b2b2b")
    date_label.config(bg="#2b2b2b")
    label1.config(bg="#202020")
    label2.config(bg="#202020")
    userText.set("Request for changing the current theme.")
    compText.set("The Theme has been updated.")

# Creating theme 2
def theme2():
    root.config(bg="#2c3942")
    Panel.config(bg="#2c3942")
    activate_button.config(bg="#2c3942")
    close_button.config(bg="#2c3942")
    Iconbar_Left.config(bg="#2c3942")
    Iconbar_Right.config(bg="#2c3942")
    youtube_button.config(bg="#2c3942")
    chrome_button.config(bg="#2c3942")
    drive_button.config(bg="#2c3942")
    photos_button.config(bg="#2c3942")
    gmail_button.config(bg="#2c3942")
    outlook_button.config(bg="#2c3942")
    recycle_bin_button.config(bg="#2c3942")
    send_mail_button.config(bg="#2c3942")
    user_image.config(bg="#2c3942")
    assistant_image.config(bg="#2c3942")
    userFrame.config(bg="#2c3942")
    compFrame.config(bg="#2c3942")
    open_side_menu.config(bg="#2c3942")
    time_label.config(bg="#2c3942")
    date_label.config(bg="#2c3942")
    label1.config(bg="#314859")
    label2.config(bg="#314859")
    userText.set("Request for changing the current theme.")
    compText.set("The Theme has been updated.")

# Creating theme 3
def theme3():
    root.config(bg="#051a2a")
    Panel.config(bg="#051a2a")
    activate_button.config(bg="#051a2a")
    close_button.config(bg="#051a2a")
    Iconbar_Left.config(bg="#051a2a")
    Iconbar_Right.config(bg="#051a2a")
    youtube_button.config(bg="#051a2a")
    chrome_button.config(bg="#051a2a")
    drive_button.config(bg="#051a2a")
    photos_button.config(bg="#051a2a")
    gmail_button.config(bg="#051a2a")
    outlook_button.config(bg="#051a2a")
    recycle_bin_button.config(bg="#051a2a")
    send_mail_button.config(bg="#051a2a")
    user_image.config(bg="#051a2a")
    assistant_image.config(bg="#051a2a")
    userFrame.config(bg="#051a2a")
    compFrame.config(bg="#051a2a")
    open_side_menu.config(bg="#051a2a")
    time_label.config(bg="#051a2a")
    date_label.config(bg="#051a2a")
    label1.config(bg="#011627")
    label2.config(bg="#011627")
    userText.set("Request for changing the current theme.")
    compText.set("The Theme has been updated.")

# Creating default theme
def default_theme():
    root.config(bg="#222634")
    Panel.config(bg="#222634")
    activate_button.config(bg="#222634")
    close_button.config(bg="#222634")
    Iconbar_Left.config(bg="#222634")
    Iconbar_Right.config(bg="#222634")
    youtube_button.config(bg="#222634")
    chrome_button.config(bg="#222634")
    drive_button.config(bg="#222634")
    photos_button.config(bg="#222634")
    gmail_button.config(bg="#222634")
    outlook_button.config(bg="#222634")
    recycle_bin_button.config(bg="#222634")
    send_mail_button.config(bg="#222634")
    user_image.config(bg="#222634")
    assistant_image.config(bg="#222634")
    userFrame.config(bg="#222634")
    compFrame.config(bg="#222634")
    open_side_menu.config(bg="#222634")
    time_label.config(bg="#222634")
    date_label.config(bg="#222634")
    label1.config(bg="#1b1e29")
    label2.config(bg="#1b1e29")
    userText.set("Request for changing the current theme.")
    compText.set("The Theme has been updated.")

# Handle threading of change_theme function
def Threading_change_theme():
    t1 = Thread(target=change_theme)
    t1.start()

# Creating change_theme function to change the theme
def change_theme():
    new_window = Tk()
    new_window.geometry("150x250")
    new_window.config(bg="#1b1e29")
    new_window.resizable(False, False)
    default = Button(new_window, text="Default", font=("Monotype Corsiva", 15), padx=5, bd=0, relief=FLAT, bg="#1b1e29", fg="white", activebackground="#1b1e29", activeforeground="white", cursor='hand2', command=default_theme)
    default.pack(pady=(5, 0))
    button1 = Button(new_window, text="Theme1", font=("Monotype Corsiva", 15), padx=5, bd=0, relief=FLAT, bg="#1b1e29", fg="white", activebackground="#1b1e29", activeforeground="white", cursor='hand2', command=theme1)
    button1.pack()
    button2 = Button(new_window, text="Theme2", font=("Monotype Corsiva", 15), padx=5, bd=0, relief=FLAT, bg="#1b1e29", fg="white", activebackground="#1b1e29", activeforeground="white", cursor='hand2', command=theme2)
    button2.pack()
    button3 = Button(new_window, text="Theme3", font=("Monotype Corsiva", 15), padx=5, bd=0, relief=FLAT, bg="#1b1e29", fg="white", activebackground="#1b1e29", activeforeground="white", cursor='hand2', command=theme3)
    button3.pack()
    new_window.mainloop()

# Handle threading of change_font function
def Threading_change_font():
    t1 = Thread(target=change_font)
    t1.start()

# Creating change_font function to change the font color
def change_font():
    add_color = colorchooser.askcolor(title="Select Color")
    color = "white"
    color = add_color[1]
    label1.config(fg=color)
    label2.config(fg=color)

# Handle threading of say_joke function
def Threading_say_joke():
    t1 = Thread(target=say_joke)
    t1.start()

# Creating say_joke function to say a joke in english
def say_joke():
    try:
        userText.set("Request for Saying a Joke...")
        speak("Okay here i present a joke for you...")
        jokes = pyjokes.get_joke(language="en", category="all")  # Speak random jokes
        compText.set(jokes)
        speak(jokes)
    except Exception as e:
        speak("Something went wrong!")
        compText.set("Something went wrong!")

# Handle threading of about_my_self function
def Threading_about_my_self():
    t1 = Thread(target=about_myself)
    t1.start()

# Create the about_my_self function
def about_myself():
    userText.set("Tell me about your self.")
    compText.set("I am an AI Assistant and i can help you to automate your daily tasks and can make your life easy.")
    speak("I am an AI Assistant and i can help you to automate your daily tasks and can make your life easy.")

# Handle threading of close_program function
def Threading_close_program():
    t1 = Thread(target=close_program)
    t1.start()

# Create the close_program function to close the assistant
def close_program():
    speak("Thanks sir! Have a nice day. Exiting...")
    root.destroy()
    exit()


# Starting the code....
if __name__ == '__main__':
    root = Tk()
    root.geometry("1800x900+50+20")
    root.title("AI Assistant")
    root.resizable(False, False)
    root.wm_iconbitmap("A:\\My Projects\\Android Subsystem for Windows (Python)\\Jarvis AI\\icon.ico")
    root.attributes('-alpha', 0.98)  # Transparent 2% or 0.02%
    root.config(background='#232734')

    img = ImageTk.PhotoImage(Image.open('A:\\My Projects\\Android Subsystem for Windows (Python)\\Jarvis AI\\AI.png'))
    Panel = Label(root, image=img, bg='#232734')
    Panel.pack(side=TOP, fill=BOTH, expand=NO)

    # create activate and close button
    activate_button = Button(root, text='Activate', command=Threading_activate, font=("Pristina", 25, 'italic'), bg="#232734", activebackground="#232734", fg="Orange", activeforeground="Red", bd=0, width=10, cursor='hand2')
    activate_button.pack()
    close_button = Button(root, text='Close', command=Threading_close_program, font=("Pristina", 25, 'italic'), bg="#232734", activebackground="#232734", fg="Orange", activeforeground="Red", bd=0, width=10, cursor='hand2')
    close_button.pack()

    Iconbar_Left = Frame(root, width=100, bg='#232734')
    Iconbar_Left.place(x=400, y=30)

    Iconbar_Right = Frame(root, width=100, bg='#232734')
    Iconbar_Right.place(x=1190, y=30)

    youtube = PhotoImage(file="A:\\My Projects\\Android Subsystem for Windows (Python)\\Jarvis AI\\youtube-icon.png")
    Google_Chrome = PhotoImage(file="A:\\My Projects\\Android Subsystem for Windows (Python)\\Jarvis AI\\Google-Chrome-icon.png")
    google_photos = PhotoImage(file="A:\\My Projects\\Android Subsystem for Windows (Python)\\Jarvis AI\\google-photos.png")
    drive = PhotoImage(file="A:\\My Projects\\Android Subsystem for Windows (Python)\\Jarvis AI\\Google-Drive-icon.png")
    gmail = PhotoImage(file="A:\\My Projects\\Android Subsystem for Windows (Python)\\Jarvis AI\\Gmail-icon.png")
    Outlook = PhotoImage(file="A:\\My Projects\\Android Subsystem for Windows (Python)\\Jarvis AI\\Microsoft-Outlook.png")

    youtube_button = Button(Iconbar_Left, image=youtube, bg="#232734", bd=0, activebackground="#232734", command=openYoutube, cursor='hand2')
    youtube_button.pack(side=LEFT, padx=10)
    chrome_button = Button(Iconbar_Left, image=Google_Chrome, bg="#232734", bd=0, activebackground="#232734", command=openChrome, cursor='hand2')
    chrome_button.pack(side=LEFT, padx=10)
    photos_button = Button(Iconbar_Left, image=google_photos, bg="#232734", bd=0, activebackground="#232734", command=open_Photos, cursor='hand2')
    photos_button.pack(side=LEFT, padx=10)

    drive_button = Button(Iconbar_Right, image=drive, bg="#232734", bd=0, activebackground="#232734", command=open_drive, cursor='hand2')
    drive_button.pack(side=LEFT, padx=10)
    gmail_button = Button(Iconbar_Right, image=gmail, bg="#232734", bd=0, activebackground="#232734", command=Gmail, cursor='hand2')
    gmail_button.pack(side=LEFT, padx=10)
    outlook_button = Button(Iconbar_Right, image=Outlook, bg="#232734", bd=0, activebackground="#232734", command=open_outlook, cursor='hand2')
    outlook_button.pack(side=LEFT, padx=10)

    empty_recycle_bin = PhotoImage(file="A:\\My Projects\\Android Subsystem for Windows (Python)\\Jarvis AI\\recycle-bin-icon.png")
    send_mail = PhotoImage(file="A:\\My Projects\\Android Subsystem for Windows (Python)\\Jarvis AI\\mail-icon.png")

    recycle_bin_button = Button(root, image=empty_recycle_bin, text="Empty Recycle Bin", bg="#232734", bd=0, activebackground="#3b415a", command=Empty_recycle_bin, cursor='hand2', font=("Aparajita", 10), fg='white', compound=TOP, activeforeground='gold')
    recycle_bin_button.place(x=600, y=175)

    send_mail_button = Button(root, image=send_mail, text="Send Email", bg="#232734", bd=0, activebackground="#3b415a", command=sendEmail, cursor='hand2', font=("Aparajita", 10), fg='white', compound=TOP, activeforeground='gold')
    send_mail_button.place(x=1130, y=175)

    compText = StringVar()
    userText = StringVar()

    userText.set("Click on Activate Button to Activate Assistant")
    compText.set("I am an AI Assistant! Please Activate and tell me How can i help you...")

    userFrame = LabelFrame(root, text='_____________User____________', font=("Tempus Sans ITC", 20), bg='#232734', fg='#F0F8FF')
    userFrame.pack(side=LEFT, fill=Y, expand=YES, padx=100, pady=20)

    compFrame = LabelFrame(root, text='___________Assistant__________', font=("Tempus Sans ITC", 20), bg="#232734", fg='#F0F8FF')
    compFrame.pack(side=RIGHT, fill=Y, expand=YES, padx=100, pady=20)

    User = PhotoImage(file="A:\\My Projects\\Android Subsystem for Windows (Python)\\Jarvis AI\\User.png")
    Assistant = PhotoImage(file="A:\\My Projects\\Android Subsystem for Windows (Python)\\Jarvis AI\\AI_Assistant.png")

    user_image = Label(root, image=User, bg="#232734")
    user_image.place(x=430, y=320)
    assistant_image = Label(root, image=Assistant, bg="#232734")
    assistant_image.place(x=1315, y=320)

    label1 = Message(userFrame, padx=20, pady=30, textvariable=userText, font=('Monotype Corsiva', 15, 'italic'), bg='#1c1f29', fg='White', justify=CENTER)
    label1.pack(fill=BOTH, expand=YES)

    label2 = Message(compFrame, padx=20, pady=30, textvariable=compText, font=('Monotype Corsiva', 15, 'italic'), bg='#1c1f29', fg='White', justify=CENTER)
    label2.pack(fill=BOTH, expand=YES)

    # create gender combo box
    gender_combo_box = Combobox(root, values=['Male', 'Female1', 'Female2'], font='Georgia 10', state='r', width=10)
    gender_combo_box.place(x=825, y=550)
    gender_combo_box.set('Female2')

    # create speed combo box
    speed_combo_box = Combobox(root, values=['Fast', 'Normal', 'Slow'], font='Georgia 10', state='r', width=10)
    speed_combo_box.place(x=825, y=640)
    speed_combo_box.set('Normal')

    # Creating side menu
    def toggle_menu():
        f1 = Frame(root, width=145, height=1000, bg='#36454F')
        f1.place(x=0, y=0)

        def button(x, y, text, activbcolor, bcolor, cmd):
            def on_press(e):
                myButton1['background'] = activbcolor
                myButton1['foreground'] = 'black'

            def on_leave(e):
                myButton1['background'] = bcolor
                myButton1['foreground'] = '#FFFFF0'

            myButton1 = Button(f1, text=text, width=12, justify=CENTER, fg='#FFFFF0', bd=0, bg=bcolor, activeforeground='black', activebackground=activbcolor, command=cmd, font='Georgia 9', pady=5, padx=10, anchor='w', cursor='hand2')

            myButton1.bind('<Enter>', on_press)
            myButton1.bind('<Leave>', on_leave)

            myButton1.place(x=x, y=y)

        button(0, 60, "About me", 'sky blue', '#36454F', Threading_about_my_self)
        button(0, 100, "Say joke", 'sky blue', '#36454F', Threading_say_joke)
        button(0, 140, "Change Theme", 'sky blue', '#36454F', Threading_change_theme)
        button(0, 180, "Font color", 'sky blue', '#36454F', Threading_change_font)
        button(0, 220, "Exit", 'sky blue', '#36454F', Threading_close_program)

        def delete():
            f1.destroy()

        Button(f1, image=bar_image, command=delete, activebackground='#36454F', bg='#36454F', fg='white', bd=0, activeforeground='white').place(x=10, y=10)

    bar_image = PhotoImage(file='A:\\My Projects\\Android Subsystem for Windows (Python)\\Jarvis AI\\three_lines.png')
    open_side_menu = Button(root, command=toggle_menu, image=bar_image, bd=0, fg='white', bg='#232734', activebackground='#232734')
    open_side_menu.place(x=10, y=10)

    time_label = Label(root, text="", font="Aparajita 20", fg='white', bg="#222634")
    time_label.place(x=1630, y=10)
    date_label = Label(root, text="", font="Aparajita 10", fg='white', bg="#222634")
    date_label.place(x=1630, y=50)

    def my_time():
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        current_date = datetime.datetime.now().strftime("%d-%b-%y")
        date_label.config(text=current_date)
        time_label.config(text=current_time)
        time_label.after(200, my_time)

    my_time()

    root.mainloop()
