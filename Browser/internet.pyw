# Importing useful packages
try:
    from googlesearch import search
    from tkinter import *
    from tkinter import messagebox
    from threading import Thread
    import webbrowser
    import pyautogui
    import requests
    from bs4 import BeautifulSoup
    import pywhatkit
    import speech_recognition as sr
except:
    pass


# handle threading of mic function
def threading_mic():
    t1 = Thread(target=mic)
    t1.start()


# Create mic function for using the mic
def mic():
    try:
        listbox.delete(0, END)
        r = sr.Recognizer()
        with sr.Microphone() as source:
            listening_label.config(text="Listening...")
            r.adjust_for_ambient_noise(source)  # Remove source noise
            r.pause_threshold = 1
            audio = r.listen(source)    # Listen user query
        try:
            listening_label.config(text="Recognizing...", fg='orange')
            query = r.recognize_google(audio, language='en')
        except Exception as e:
            messagebox.showinfo("Internet", "Something went wrong")
            return "None"
        command.set(query)
        pywhatkit.search(query)
        query = query.replace("search", "")
        url = "https://www.google.com/search?q=" + query
        r = requests.get(url)
        data = BeautifulSoup(r.text, "html.parser")
        ans_ = data.find("div", class_="BNeawe").text
        listening_label.config(text="", fg='gold')
        result = search(query, 25)
        # inserting all links in listbox
        for i in result:
            listbox.insert(END, i)
        listbox.select_set(0)  # default set first link
        return query
    except:
        listbox.delete(0, END)
        listbox.insert(END, "Opps....")
        listbox.insert(END, "No result found!")
        listbox.insert(END, "Please check your internet connection!")
        listbox.insert(END, "🙁🙁🙁")


# threading in search_entry function
def threading_search_entry():
    t1 = Thread(target=search_entry)
    t1.start()


# threading in search_top_entry function
def threading_search_top_entry():
    t1 = Thread(target=search_top_entry)
    t1.start()


# creating search_top_entry function to google search
def search_top_entry():
    try:
        listbox.delete(0, END)
        query = top_search.get()
        pywhatkit.search(query)
        query = query.replace("search", "")
        url = "https://www.google.com/search?q=" + query
        r = requests.get(url)
        data = BeautifulSoup(r.text, "html.parser")
        ans_ = data.find("div", class_="BNeawe").text

        result = search(query, 25)

        # inserting all links in listbox
        for i in result:
            listbox.insert(END, i)

        listbox.select_set(0)  # default set first link
    except:
        listbox.delete(0, END)
        listbox.insert(END, "Opps....")
        listbox.insert(END, "No result found!")
        listbox.insert(END, "Please check your internet connection!")
        listbox.insert(END, "🙁🙁🙁")


# creating search_entry function to google search
def search_entry():
    try:
        listbox.delete(0, END)
        query = google_search.get()
        result = search(query, 25)

        # inserting all links in listbox
        for i in result:
            listbox.insert(END, i)

        listbox.select_set(0)       # default set first link

        for i in listbox.curselection():
            if i == listbox.curselection()[0]:
                webbrowser.open(listbox.get(i))     # open first link of search result
            else:
                break
    except:
        listbox.delete(0, END)
        listbox.insert(END, "Opps....")
        listbox.insert(END, "No result found!")
        listbox.insert(END, "Please check your internet connection!")
        listbox.insert(END, "🙁🙁🙁")


# function for opening link on single click
def open_(event):
    url = ""
    for i in listbox.curselection():
        url = listbox.get(i)
    webbrowser.open(url)


# Starting point of program
if __name__ == '__main__':
    # Creating GUI
    root = Tk()
    root.config(bg="#353535")
    root.geometry("1300x850+300+50")
    root.wm_iconbitmap("A:\\My Projects\\Android Subsystem for Windows (Python)\\Browser\\browser_icon.ico")
    root.resizable(False, False)
    root.title("Internet")
    root.attributes('-alpha', 0.98)  # Transparent 2% or 0.02%

    # create top frame
    top_frame = Frame(root, width=1300, height=60, bg="#292a2d", bd=0.5, relief=SOLID).place(x=0, y=0)
    Label(top_frame, text="Search : ", bg="#292a2d", fg='white').place(x=10, y=10)
    # top search bar
    top_search = Entry(top_frame, width=118, bg='#181b23', fg='white', bd=2, relief=RIDGE)
    top_search.bind("<Return>", lambda e: threading_search_top_entry())    # binding with enter key
    top_search.place(x=100, y=10)

    # setting google image
    google_image = PhotoImage(file="A:\\My Projects\\Android Subsystem for Windows (Python)\\Browser\\Icons\\google_label.png")
    Label(root, image=google_image, bg="#353535").pack(pady=(65, 0))

    # creating main search bar
    search_bar_image = PhotoImage(file="A:\\My Projects\\Android Subsystem for Windows (Python)\\Browser\\google_search_bar.png")
    search_bar = Label(root, image=search_bar_image, bg="#353535").pack()
    command = StringVar()
    google_search = Entry(root, width=23, bg='white', font="Aparajita 20", bd=0, relief=FLAT, textvariable=command)
    google_search.bind("<Return>", lambda e: threading_search_entry())    # binding with enter key
    google_search.place(x=462, y=118)

    # set search and mic icon on main search bar
    search_icon = PhotoImage(file="A:\\My Projects\\Android Subsystem for Windows (Python)\\Browser\\Icons\\search.png")
    mic_icon = PhotoImage(file="A:\\My Projects\\Android Subsystem for Windows (Python)\\Browser\\Icons\\google_mic.png")

    # creating search and mic button
    search_button = Button(root, image=search_icon, bg='white', activebackground='white', bd=0, relief=FLAT, command=threading_search_entry)
    search_button.place(x=425, y=125)
    mic_button = Button(root, image=mic_icon, bg='white', activebackground='white', bd=0, relief=FLAT, command=threading_mic)
    mic_button.place(x=835, y=125)

    listening_label = Label(root, text="", font="Georgia 15", bg="#353535", fg='gold')
    listening_label.place(x=20, y=70)

    # Creating side menu for Google products
    def toggle_menu():
        f1 = Frame(root, width=300, height=575, bg='#16191f', bd=2, relief=GROOVE)
        f1.place(x=1000, y=65)

        header = Frame(f1, width=296, height=55, bg='#313745', bd=1, relief=SOLID)
        header.place(x=0, y=0)

        def button(x, y, text, image, activbcolor, bcolor, cmd):
            def on_press(e):
                myButton1['background'] = activbcolor
                myButton1['foreground'] = 'white'

            def on_leave(e):
                myButton1['background'] = bcolor
                myButton1['foreground'] = 'white'

            myButton1 = Button(f1, text=text, image=image, width=75, height=75, justify=CENTER, bd=0, bg=bcolor, activebackground=activbcolor, command=cmd, cursor='hand2', compound=TOP, fg='white', activeforeground='white')

            myButton1.bind('<Enter>', on_press)
            myButton1.bind('<Leave>', on_leave)

            myButton1.place(x=x, y=y)

        # Google products on buttons
        button(10, 70, "Google", google_icon, '#26282d', '#16191f', open_google)
        button(110, 70, "YouTube", youtube_icon, '#26282d', '#16191f', open_youtube)
        button(210, 70, "Gmail", gmail_icon, '#26282d', '#16191f', open_gmail)
        button(10, 170, "Photos", photos_icon, '#26282d', '#16191f', open_photos)
        button(110, 170, "Drive", drive_icon, '#26282d', '#16191f', open_drive)
        button(210, 170, "Calendar", calendar_icon, '#26282d', '#16191f', open_calendar)
        button(10, 270, "Meet", meet_icon, '#26282d', '#16191f', open_meet)
        button(110, 270, "Map", map_icon, '#26282d', '#16191f', open_map)
        button(210, 270, "Translator", translator_icon, '#26282d', '#16191f', open_translator)
        button(10, 370, "Play store", playstore_icon, '#26282d', '#16191f', open_playstore)
        button(110, 370, "Notes", notes_icon, '#26282d', '#16191f', open_notes)
        button(210, 370, "Books", books_icon, '#26282d', '#16191f', open_books)
        button(10, 470, "Docs", docs_icon, '#26282d', '#16191f', open_docs)
        button(110, 470, "Sheet", sheet_icon, '#26282d', '#16191f', open_sheet)
        button(210, 470, "Slide", slide_icon, '#26282d', '#16191f', open_slide)

        # function for closing side menu
        def delete():
            f1.destroy()

        Button(header, image=apps_image, command=delete, activebackground='#313745', bg='#313745', bd=0).place(x=240, y=0)

    # set google product icon on button
    apps_image = PhotoImage(file="A:\\My Projects\\Android Subsystem for Windows (Python)\\Browser\\Icons\\google_apps.png")
    open_side_menu = Button(root, command=toggle_menu, image=apps_image, bd=0, bg='#353535', activebackground='#353535')
    open_side_menu.place(x=1245, y=70)

    # load all google product icons
    google_icon = PhotoImage(file="A:\\My Projects\\Android Subsystem for Windows (Python)\\Browser\\Icons\\google.png")
    youtube_icon = PhotoImage(file="A:\\My Projects\\Android Subsystem for Windows (Python)\\Browser\\Icons\\youtube.png")
    gmail_icon = PhotoImage(file="A:\\My Projects\\Android Subsystem for Windows (Python)\\Browser\\Icons\\gmail.png")
    photos_icon = PhotoImage(file="A:\\My Projects\\Android Subsystem for Windows (Python)\\Browser\\Icons\\photos.png")
    drive_icon = PhotoImage(file="A:\\My Projects\\Android Subsystem for Windows (Python)\\Browser\\Icons\\drive.png")
    calendar_icon = PhotoImage(file="A:\\My Projects\\Android Subsystem for Windows (Python)\\Browser\\Icons\\calander.png")
    meet_icon = PhotoImage(file="A:\\My Projects\\Android Subsystem for Windows (Python)\\Browser\\Icons\\meet.png")
    map_icon = PhotoImage(file="A:\\My Projects\\Android Subsystem for Windows (Python)\\Browser\\Icons\\map.png")
    translator_icon = PhotoImage(file="A:\\My Projects\\Android Subsystem for Windows (Python)\\Browser\\Icons\\translator.png")
    playstore_icon = PhotoImage(file="A:\\My Projects\\Android Subsystem for Windows (Python)\\Browser\\Icons\\playstore.png")
    notes_icon = PhotoImage(file="A:\\My Projects\\Android Subsystem for Windows (Python)\\Browser\\Icons\\notes.png")
    books_icon = PhotoImage(file="A:\\My Projects\\Android Subsystem for Windows (Python)\\Browser\\Icons\\books.png")
    docs_icon = PhotoImage(file="A:\\My Projects\\Android Subsystem for Windows (Python)\\Browser\\Icons\\docs.png")
    sheet_icon = PhotoImage(file="A:\\My Projects\\Android Subsystem for Windows (Python)\\Browser\\Icons\\sheet.png")
    slide_icon = PhotoImage(file="A:\\My Projects\\Android Subsystem for Windows (Python)\\Browser\\Icons\\slide.png")

    # load default set application icons
    github_icon = PhotoImage(file="A:\\My Projects\\Android Subsystem for Windows (Python)\\Browser\\Icons\\github.png")
    hotstar_icon = PhotoImage(file="A:\\My Projects\\Android Subsystem for Windows (Python)\\Browser\\Icons\\hotstar.png")
    outlook_icon = PhotoImage(file="A:\\My Projects\\Android Subsystem for Windows (Python)\\Browser\\Icons\\outlook.png")
    whatsapp_icon = PhotoImage(file="A:\\My Projects\\Android Subsystem for Windows (Python)\\Browser\\Icons\\WhatsApp.png")
    stack_overflow_icon = PhotoImage(file="A:\\My Projects\\Android Subsystem for Windows (Python)\\Browser\\Icons\\stack_overflow.png")

    ''' ________________ creating functions for opening website to click on icon ________________'''

    # For opening google
    def open_google():
        webbrowser.open("https://www.google.co.in/webhp?tab=rw")

    # For opening YouTube
    def open_youtube():
        webbrowser.open("https://www.youtube.com/")

    # For opening gmail
    def open_gmail():
        webbrowser.open("https://mail.google.com/mail/u/0/#inbox")

    # For opening photos
    def open_photos():
        webbrowser.open("https://photos.google.com/?tab=rq&pageId=none&pli=1")

    # For opening drive
    def open_drive():
        webbrowser.open("https://drive.google.com/drive/my-drive")

    # For opening calendar
    def open_calendar():
        webbrowser.open("https://calendar.google.com/calendar/u/0/r?tab=oc&pli=1")

    # For opening meet
    def open_meet():
        webbrowser.open("https://meet.google.com/?hs=197&pli=1&authuser=0")

    # For opening map
    def open_map():
        webbrowser.open("https://www.google.co.in/maps/@18.6687859,94.455956,3.25z?hl=en")

    # For opening translator
    def open_translator():
        webbrowser.open("https://translate.google.co.in/?hl=en&tab=rT&sl=en&tl=hi&op=translate")

    # For opening playstore
    def open_playstore():
        webbrowser.open("https://play.google.com/store/games?hl=en&tab=T8")

    # For opening notes
    def open_notes():
        webbrowser.open("https://keep.google.com/")

    # For opening books
    def open_books():
        webbrowser.open("https://books.google.co.in/books?uid=108456653472613128042")

    # For opening docs
    def open_docs():
        webbrowser.open("https://docs.google.com/document/u/0/")

    # For opening sheet
    def open_sheet():
        webbrowser.open("https://docs.google.com/spreadsheets/u/0/")

    # For opening slide
    def open_slide():
        webbrowser.open("https://docs.google.com/presentation/u/0/")

    # For opening GitHub
    def open_github():
        webbrowser.open("https://github.com/HARIOM317")

    # For opening hot-star
    def open_hotstar():
        webbrowser.open("https://www.hotstar.com/in")

    # For opening outlook
    def open_outlook():
        webbrowser.open("https://outlook.live.com/mail/0/")

    # For opening whatsapp
    def open_whatsapp():
        webbrowser.open("https://web.whatsapp.com/")

    # For opening stack overflow
    def open_stack_overflow():
        webbrowser.open("https://stackoverflow.com/")

    # Creating default application buttons
    Button(root, text="YouTube", image=youtube_icon, compound=TOP, justify=CENTER, width=120, height=70, bg="#353535", activebackground="#353535", fg='white', activeforeground='white', bd=0, relief=FLAT, command=open_youtube).place(x=200, y=185)
    Button(root, text="GitHub", image=github_icon, compound=TOP, justify=CENTER, width=120, height=70, bg="#353535", activebackground="#353535", fg='white', activeforeground='white', bd=0, relief=FLAT, command=open_github).place(x=350, y=185)
    Button(root, text="Hot star", image=hotstar_icon, compound=TOP, justify=CENTER, width=120, height=70, bg="#353535", activebackground="#353535", fg='white', activeforeground='white', bd=0, relief=FLAT, command=open_hotstar).place(x=500, y=185)
    Button(root, text="Outlook", image=outlook_icon, compound=TOP, justify=CENTER, width=120, height=70, bg="#353535", activebackground="#353535", fg='white', activeforeground='white', bd=0, relief=FLAT, command=open_outlook).place(x=650, y=185)
    Button(root, text="WhatsApp", image=whatsapp_icon, compound=TOP, justify=CENTER, width=120, height=70, bg="#353535", activebackground="#353535", fg='white', activeforeground='white', bd=0, relief=FLAT, command=open_whatsapp).place(x=800, y=185)
    Button(root, text="Stack overflow", image=stack_overflow_icon, compound=TOP, justify=CENTER, width=120, height=70, bg="#353535", activebackground="#353535", fg='white', activeforeground='white', bd=0, relief=FLAT, command=open_stack_overflow).place(x=950, y=185)

    # Creating a new frame for listbox
    new_frame = Frame(root, width=1300, height=580, bg="#353535", bd=0, relief=FLAT)
    new_frame.pack(side=BOTTOM)

    # Create listbox to show output links
    listbox = Listbox(new_frame, selectbackground='#13c0ff', selectforeground='dark blue', selectborderwidth=3, font=("Bahnschrift Light Condensed", 12), bd=0, bg="#353535", justify=LEFT, fg='#f6ffa9', relief=FLAT, selectmode=SINGLE, cursor='hand2')
    listbox.bind("<Button-1>", open_)       # binding with left click event
    listbox.insert(END, "www.google.com")      # Inserting google link as default
    listbox.select_set(0)       # select google link as default
    listbox.place(relx=0, rely=0, relheight=1, relwidth=1)
    scrollbar = Scrollbar(listbox, orient=VERTICAL, command=listbox.yview)    # link scrollbar to listbox
    scrollbar.pack(side=RIGHT, fill=Y)
    listbox.config(yscrollcommand=scrollbar.set)

    root.mainloop()
