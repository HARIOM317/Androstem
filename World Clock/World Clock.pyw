# Import useful packages
from tkinter import *
from tkinter import messagebox, font
from datetime import datetime
import pytz
import time
from pygame import mixer
from threading import *

# Initialize mixer
mixer.init()

# Create a cancel variable and initialize it to False
cancel = False

# todo: ____________________________ Create Alarm App (Part-1) _____________________________

# Use the Threading in alarm function
def Threading():
    t1 = Thread(target=alarm)
    t1.start()

# Create alarm function to set an alarm
def alarm():
    try:
        # Infinite Loop
        while True:
            # Set Alarm
            set_alarm_time = f"{hour.get()}:{minute.get()}:{second.get()}"
            # Wait for one seconds
            time.sleep(1)
            # Get current time
            current_time = datetime.now().strftime("%H:%M:%S")
            # Check whether set alarm is equal to current time or not
            if current_time == set_alarm_time:
                # Play the sound
                mixer.music.load("A:\\My Projects\\Android Subsystem for Windows (Python)\\World Clock\\Mechanical Clock Ring.mp3")
                mixer.music.play()
                message = messagebox.showinfo("Alarm", "Wake up")
                # Stop sound using messagebox
                if message == 'ok':
                    mixer.music.stop()
    # Exception handling
    except:
        messagebox.showinfo("Alarm", "Something went wrong!")

# Create alarm_menu function to make GUI of alarm application
def alarm_menu():
    Alarm_button.config(fg="orange", activeforeground="orange", font="Papyrus 15 bold underline")
    Clock_button.config(fg="white", activeforeground="white", font="Papyrus 15 bold")
    Stopwatch_button.config(fg="white", activeforeground="white", font="Papyrus 15 bold")
    Timer_button.config(fg="white", activeforeground="white", font="Papyrus 15 bold")

    main_frame4 = Frame(root, width=1100, height=580, bg='#232734')
    main_frame4.place(x=0, y=50)
    # Create myfont variable to set a font style for OptionMenu
    myfont = font.Font(main_frame4, family='Aparajita', size=50)
    # Create menu_font variable to set a font style for list of option menu
    menu_font = font.Font(main_frame4, family='Aparajita', size=25)
    # Set some labels
    Label(main_frame4, text="Alarm", font=("Pristina 80"), fg="#ea3548", bg="#232734").place(x=430, y=10)
    Label(main_frame4, text="Set Time", font=("Bahnschrift Light Condensed", 20), bg="#232734", fg='white').place(x=300, y=150)
    # Creating frame
    frame = Frame(main_frame4, width=500, height=100, bg="#232734")
    frame.place(x=300, y=200)

    # Crating option menu to set hour
    global hour
    Label(main_frame4, text="Hour", font=("Gabriola", 25), bg="#232734", fg='gold').place(x=320, y=295)
    hour = StringVar()
    hours = ('01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24')
    hour.set(hours[0])
    hrs_alarm = OptionMenu(frame, hour, *hours)
    hrs_alarm.config(font=myfont, bg='#232734', fg='white', bd=0, relief=FLAT, activeforeground='white', activebackground="#232734", width=2)
    hrs_alarm['menu'].config(font=menu_font, bg='white', fg='black', bd=0, relief=FLAT, activeforeground='black')
    hrs_alarm.place(x=0, y=2)

    # Crating option menu to set minute
    global minute
    Label(main_frame4, text="Minute", font=("Gabriola", 25), bg="#232734", fg='gold').place(x=505, y=295)
    minute = StringVar()
    minutes = ('00', '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49', '50', '51', '52', '53', '54', '55', '56', '57', '58', '59')
    minute.set(minutes[0])
    min_alarm = OptionMenu(frame, minute, *minutes)
    min_alarm.config(font=myfont, bg='#232734', fg='white', bd=0, relief=FLAT, activeforeground='white', activebackground="#232734", width=2)
    min_alarm['menu'].config(font=menu_font, bg='white', fg='black', bd=0, relief=FLAT, activeforeground='black')
    min_alarm.place(x=195, y=2)

    # Crating option menu to set second
    global second
    Label(main_frame4, text="Second", font=("Gabriola", 25), bg="#232734", fg='gold').place(x=700, y=295)
    second = StringVar()
    seconds = ('00', '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49', '50', '51', '52', '53', '54', '55', '56', '57', '58', '59')
    second.set(seconds[0])
    secs_alarm = OptionMenu(frame, second, *seconds)
    secs_alarm.config(font=myfont, bg='#232734', fg='white', bd=0, relief=FLAT, activeforeground='white', activebackground="#232734", width=2)
    secs_alarm['menu'].config(font=menu_font, bg='white', fg='black', bd=0, relief=FLAT, activeforeground='black')
    secs_alarm.place(x=390, y=2)

    # Creating a button to save the alarm
    Button(main_frame4, text="SAVE", font=("Bahnschrift Light Condensed", 25), command=Threading, padx=10, pady=0, bd=1, relief=GROOVE, bg='#232734', activebackground='#232734', fg='#0AFF12', activeforeground='#18CD36', cursor='hand2').place(x=500, y=400)

# todo: ____________________________ Create Stopwatch App (Part-2) _____________________________

# make a create_labels function to create label for lapping
def create_labels(text, _x, _y):
    label = Label(lap_frame, text=text, fg='#37dee4', bg='#232734', font=("Aparajita", 15))
    label.place(x=_x, y=_y, width=100, height=45)

# Create start function to start and resume time
def start():
    start_button.place_forget()
    resume_button.place_forget()
    pause_button.place(x=380, y=200)
    global time_elapsed1, time_elapsed2, time_elapsed3, time1, time2, self_job
    time2 = int(time.time())
    if time2 != time1:
        time1 = time2
        if time_elapsed1 < 59:
            time_elapsed1 += 1
            clock_frame.config(text=(str(time_elapsed3).zfill(2)+":"+str(time_elapsed2).zfill(2)+":"+str(time_elapsed1).zfill(2)))
        else:
            time_elapsed1 = 0
            time_elapsed2 += 1
            if time_elapsed2 < 59:
                time_elapsed2 += 1
                clock_frame.config(text=(str(time_elapsed3).zfill(2)+":"+str(time_elapsed2).zfill(2)+":"+str(time_elapsed1).zfill(2)))
            else:
                time_elapsed1 = 0
                time_elapsed3 += 1
                if time_elapsed3 >= 24:
                    time_elapsed1 = 0
                    time_elapsed2 = 0
                    time_elapsed3 = 0
                else:
                    time_elapsed3 += 1
                    clock_frame.config(text=(str(time_elapsed3).zfill(2)+":"+str(time_elapsed2).zfill(2)+":"+str(time_elapsed1).zfill(2)))
    self_job = root.after(1000, start)

# create stop_time function to stop time
def stop_time():
    global self_job
    if self_job is not None:
        root.after_cancel(self_job)
        self_job = None
    pause_button.place_forget()
    resume_button.place(x=380, y=200)

# Create reset function to reset the stopwatch time and all lapping of time
def reset_time():
    global time_elapsed1, time_elapsed2, time_elapsed3, time1, self_job, time2, label, i, j
    try:
        stop_time()
        resume_button.place_forget()
        start_button.place(x=380, y=200)
    except:
        start()
        stop_time()
    clock_frame.config(text="00:00:00")
    time_elapsed1 = 0
    time_elapsed2 = 0
    time_elapsed3 = 0
    time1 = 0
    time2 = 0
    i = 0
    j = 0
    global main_frame3
    wig = main_frame3.winfo_children()
    for b in wig:
        b.place_forget()
        resume_button.place_forget()
    start_button.place(x=380, y=200)
    lap_button.place(x=515, y=200)
    reset_button.place(x=620, y=200)
    clock_frame.place(x=405, y=50)
    lap_frame.place(x=0, y=290)
    wig = lap_frame.winfo_children()
    for b in wig:
        b.place_forget()

# Create lap function for lapping
def lap():
    global time_elapsed1, time_elapsed2, time_elapsed3, time1, time2, self_job, i, j
    if i < 10:
        create_labels((str(time_elapsed3).zfill(2)+":"+str(time_elapsed2).zfill(2)+":"+str(time_elapsed1).zfill(2)), 5+(110*i), 10+(j*50))
    elif j > 3:
        i = 0
        j = 0
        global lap_frame
        wig = lap_frame.winfo_children()
        for b in wig:
            b.place_forget()
        create_labels((str(time_elapsed3).zfill(2)+":"+str(time_elapsed2).zfill(2)+":"+str(time_elapsed1).zfill(2)), 5+(110*i), 10+(j*50))
    else:
        j += 1
        i = 0
        create_labels((str(time_elapsed3).zfill(2)+":"+str(time_elapsed2).zfill(2)+":"+str(time_elapsed1).zfill(2)), 5+(110*i), 10+(j*50))
    i += 1

# Create stopwatch_menu function to make GUI of stopwatch application
def stopwatch_menu():
    Alarm_button.config(fg="white", activeforeground="white", font="Papyrus 15 bold")
    Clock_button.config(fg="white", activeforeground="white", font="Papyrus 15 bold")
    Stopwatch_button.config(fg="orange", activeforeground="orange", font="Papyrus 15 bold underline")
    Timer_button.config(fg="white", activeforeground="white", font="Papyrus 15 bold")

    global main_frame3
    main_frame3 = Frame(root, width=1100, height=580, bg='#232734')
    main_frame3.place(x=0, y=50)
    global lap_frame
    lap_frame = Frame(main_frame3, width=1100, height=260, bg='#232734')
    lap_frame.place(x=0, y=290)
    global time_elapsed1, time_elapsed2, time_elapsed3
    time_elapsed1 = 0
    time_elapsed2 = 0
    time_elapsed3 = 0
    global clock_frame, start_button, pause_button, resume_button, lap_button, reset_button, time1, time2, i, j
    time1 = 0
    time2 = 0
    i = 0
    j = 0
    # Creating labels and buttons
    clock_frame = Label(main_frame3, text="00:00:00", bg='#232734', fg='white', font=("Bahnschrift SemiBold Condensed", 75))
    start_button = Button(main_frame3, text="Start", bg='#232734', bd=0, relief=FLAT, activebackground="#232734", activeforeground="#0AFF12", fg='#0AFF12', font=("Cambria", 25), command=start, cursor='hand2')
    pause_button = Button(main_frame3, text="Pause", bg='#232734', bd=0, relief=FLAT, activebackground="#232734", activeforeground="red", fg='red', font=("Cambria", 25), command=stop_time, cursor='hand2')
    resume_button = Button(main_frame3, text="Resume", bg='#232734', bd=0, relief=FLAT, activebackground="#232734", activeforeground="#74FF33", fg='#74FF33', font=("Cambria", 25), command=start, cursor='hand2')
    lap_button = Button(main_frame3, text="Lap", bg='#232734', bd=0, relief=FLAT, activebackground="#232734", activeforeground="gold", fg='gold', font=("Cambria", 25), command=lap, cursor='hand2')
    reset_button = Button(main_frame3, text="Reset", bg='#232734', bd=0, relief=FLAT, activebackground="#232734", activeforeground="orange", fg='orange', font=("Cambria", 25), command=reset_time, cursor='hand2')
    # set labels and buttons
    start_button.place(x=380, y=200)
    lap_button.place(x=515, y=200)
    reset_button.place(x=620, y=200)
    clock_frame.place(x=405, y=50)

# todo: ____________________________ Create Timer App (Part-3) _____________________________

# Create Timer function to start timer
def Timer():
    try:
        bottom_frame2 = Frame(main_frame2, height=70, width=300, bg="#232734")
        bottom_frame2.place(x=410, y=480)
        cancel_button = Button(bottom_frame2, text="Cancel", bg="#232734", fg='#FF3E29', cursor='hand2', font=("French Script MT", 25), bd=1, relief=GROOVE, command=cancel_time, activebackground='#232734', activeforeground='#FF3E29')
        cancel_button.place(x=110, y=0)

        global times
        times = int(hrs.get())*3600 + int(min.get())*60 + int(sec.get())

        while times >= 0:
            global cancel
            cancel = False
            minute, second = (times//60, times % 60)
            hour = 0
            if minute > 60:
                hour, minute = (minute//60, minute % 60)
            sec.set(second)
            min.set(minute)
            hrs.set(hour)
            root.update()
            time.sleep(1)
            if (times == 0):
                bottom_frame3 = Frame(main_frame2, height=70, width=300, bg="#232734")
                bottom_frame3.place(x=410, y=480)
                button = Button(bottom_frame3, text="Start", bg="#232734", fg='#1AFF2D', cursor='hand2', font=("French Script MT", 25), bd=1, relief=GROOVE, command=Timer, activebackground='#232734', activeforeground='#1AFF2D', padx=5)
                button.place(x=110, y=0)
                sec.set("00")
                min.set("00")
                hrs.set("00")
                mixer.music.load("A:\\My Projects\\Android Subsystem for Windows (Python)\\World Clock\\Mechanical Clock Ring.mp3")
                mixer.music.play()
                new_frame = Frame(main_frame2, width=200, height=100, bg='#232734')
                new_frame.place(x=480, y=380)
                Button(new_frame, text="Stop", command=stop, padx=30, pady=10, font=("Gabriola", 25, 'bold'), bg='#232734', fg='#0AFFBE', bd=0, relief=FLAT, activebackground='#232734', activeforeground='#0AFFBE', cursor='hand2').place(x=20, y=0)
            if cancel == True:
                times = 0
                bottom_frame4 = Frame(main_frame2, height=70, width=300, bg='#232734')
                bottom_frame4.place(x=410, y=480)
                button = Button(bottom_frame4, text="Start", bg="#232734", fg='#1AFF2D', cursor='hand2', font=("French Script MT", 25), bd=1, relief=GROOVE, command=Timer, activebackground='#232734', activeforeground='#1AFF2D', padx=5)
                button.place(x=110, y=0)
                break
            times -= 1
    except:
        messagebox.showinfo("Timer", "Invalid Time \nPlease restart your program")

# Create stop function to stop sound when timer is completed
def stop():
    mixer.music.stop()
    Frame(main_frame2, width=200, height=100, bg='#232734').place(x=480, y=380)

# Create cancel_time function to cancel timer
def cancel_time():
    global cancel
    cancel = True
    hrs.set("00")
    min.set("00")
    sec.set("00")

# Create timer_menu function to make GUI of Timer application
def timer_menu():
    Alarm_button.config(fg="white", activeforeground="white", font="Papyrus 15 bold")
    Clock_button.config(fg="white", activeforeground="white", font="Papyrus 15 bold")
    Stopwatch_button.config(fg="white", activeforeground="white", font="Papyrus 15 bold")
    Timer_button.config(fg="orange", activeforeground="orange", font="Papyrus 15 bold underline")

    global main_frame2
    main_frame2 = Frame(root, width=1100, height=580, bg='#232734')
    main_frame2.place(x=0, y=50)
    heading = Label(main_frame2, text="Timer ", font=("Monotype Corsiva", 80), bg='#232734', fg="#ea3548")
    heading.place(x=430, y=20)

    global hrs
    global min
    global sec

    hrs = StringVar()
    Entry(main_frame2, textvariable=hrs, width=2, font=("Cambria", 50), bg='#232734', fg='white', bd=0, relief=FLAT).place(x=400, y=155)
    hrs.set("00")

    min = StringVar()
    Entry(main_frame2, textvariable=min, width=2, font=("Cambria", 50), bg='#232734', fg='white', bd=0, relief=FLAT).place(x=520, y=155)
    min.set("00")

    sec = StringVar()
    Entry(main_frame2, textvariable=sec, width=2, font=("Cambria", 50), bg='#232734', fg='white', bd=0, relief=FLAT).place(x=640, y=155)
    sec.set("00")

    Label(main_frame2, text="Hours", font=("Gabriola", 20), bg='#232734', fg='orange').place(x=408, y=240)
    Label(main_frame2, text="Minutes", font=("Gabriola", 20), bg='#232734', fg='orange').place(x=520, y=240)
    Label(main_frame2, text="Seconds", font=("Gabriola", 20), bg='#232734', fg='orange').place(x=640, y=240)

    bottom_frame1 = Frame(main_frame2, height=70, width=300, bg="#232734")
    bottom_frame1.place(x=410, y=480)
    button = Button(bottom_frame1, text="Start", bg="#232734", fg='#1AFF2D', cursor='hand2', font=("French Script MT", 25), bd=1, relief=GROOVE, command=Timer, activebackground='#232734', activeforeground='#1AFF2D', padx=5)
    button.place(x=110, y=0)

    def brush():
        hrs.set("00")
        min.set("02")
        sec.set("00")
    def face():
        hrs.set("00")
        min.set("15")
        sec.set("00")
    def eggs():
        hrs.set("00")
        min.set("10")
        sec.set("00")
    def reset():
        hrs.set("00")
        min.set("00")
        sec.set("00")
    def breakfast():
        hrs.set("00")
        min.set("30")
        sec.set("00")
    def exercise():
        hrs.set("01")
        min.set("00")
        sec.set("00")

    frame1 = Frame(main_frame2, width=100, height=100, bg='#232734', bd=1, relief=GROOVE)
    frame1.place(x=20, y=20)
    Button(frame1, text="Brush Teeth\n00:02:00", font=("Georgia", 12), pady=25, padx=0, command=brush, bd=0, relief=FLAT, bg='#232734', fg='#33FFF1', activebackground='#232734', activeforeground='#06EFE3', cursor='hand2').place(x=2, y=2)

    frame2 = Frame(main_frame2, width=100, height=100, bg='#232734', bd=1, relief=GROOVE)
    frame2.place(x=20, y=150)
    Button(frame2, text="Face Mask\n00:15:00", font=("Georgia", 12), pady=25, padx=5, command=face, bd=0, relief=FLAT, bg='#232734', fg='#33FFF1', activebackground='#232734', activeforeground='#06EFE3', cursor='hand2').place(x=2, y=2)

    frame3 = Frame(main_frame2, width=100, height=100, bg='#232734', bd=1, relief=GROOVE)
    frame3.place(x=20, y=280)
    Button(frame3, text="Steam Eggs\n00:10:00", font=("Georgia", 12), pady=25, padx=2, command=eggs, bd=0, relief=FLAT, bg='#232734', fg='#33FFF1', activebackground='#232734', activeforeground='#06EFE3', cursor='hand2').place(x=2, y=2)

    frame4 = Frame(main_frame2, width=100, height=100, bg='#232734', bd=1, relief=GROOVE)
    frame4.place(x=980, y=20)
    Button(frame4, text="Reset\n00:00:00", font=("Georgia", 12), pady=25, padx=8, command=reset, bd=0, relief=FLAT, bg='#232734', fg='#33FFF1', activebackground='#232734', activeforeground='#06EFE3', cursor='hand2').place(x=2, y=2)

    frame5 = Frame(main_frame2, width=100, height=100, bg='#232734', bd=1, relief=GROOVE)
    frame5.place(x=980, y=150)
    Button(frame5, text="Breakfast\n00:30:00", font=("Georgia", 12), pady=25, padx=9, command=breakfast, bd=0, relief=FLAT, bg='#232734', fg='#33FFF1', activebackground='#232734', activeforeground='#06EFE3', cursor='hand2').place(x=2, y=2)

    frame6 = Frame(main_frame2, width=100, height=100, bg='#232734', bd=1, relief=GROOVE)
    frame6.place(x=980, y=280)
    Button(frame6, text="Exercise\n01:00:00", font=("Georgia", 12), pady=25, padx=9, command=exercise, bd=0, relief=FLAT, bg='#232734', fg='#33FFF1', activebackground='#232734', activeforeground='#06EFE3', cursor='hand2').place(x=2, y=2)

# todo: ____________________________ Create Word Clock App (Part-3) _____________________________

# Create some functions to set the default time zones
# Create function 1 to set default for india time zone
def India_time():
    home = pytz.timezone("Asia/kolkata")
    local_time = datetime.now(home)
    current_time = local_time.strftime("%a - %H:%M:%S")
    global clock1
    clock1.config(text=current_time, fg='white')
    name1.config(text="India", fg='gold')
    clock1.after(200, India_time)

# Create function 2 to set default for USA time zone
def USA_time():
    home2 = pytz.timezone("America/New_York")
    local_time2 = datetime.now(home2)
    current_time2 = local_time2.strftime("%a - %H:%M:%S")
    clock2.config(text=current_time2, fg='white')
    name2.config(text="New York", fg='gold')
    clock2.after(200, USA_time)

# Create function 3 to set default for europe time zone
def Europe_time():
    home3 = pytz.timezone("europe/london")
    local_time3 = datetime.now(home3)
    current_time3 = local_time3.strftime("%a - %H:%M:%S")
    clock3.config(text=current_time3, fg='white')
    name3.config(text="London", fg='gold')
    clock3.after(200, Europe_time)

# Create function 4 to set default for tokyo time zone
def Japan_time():
    home4 = pytz.timezone("Asia/Tokyo")
    local_time4 = datetime.now(home4)
    current_time4 = local_time4.strftime("%a - %H:%M:%S")
    clock4.config(text=current_time4, fg='white')
    name4.config(text="Tokyo", fg='gold')
    clock4.after(200, Japan_time)

# Create clock_menu function to make GUI of clock application
def clock_menu():
    Alarm_button.config(fg="white", activeforeground="white", font="Papyrus 15 bold")
    Clock_button.config(fg="orange", activeforeground="orange", font="Papyrus 15 bold underline")
    Stopwatch_button.config(fg="white", activeforeground="white", font="Papyrus 15 bold")
    Timer_button.config(fg="white", activeforeground="white", font="Papyrus 15 bold")

    global main_frame1
    main_frame1 = Frame(root, width=1100, height=630, bg='#232734')
    main_frame1.place(x=0, y=50)

    # Create Time_of_country function to show the clock of country which we choose from time zone list
    def Time_of_country(event):
        zone = ""
        for i in box.curselection():
            zone = box.get(i)
        new_home = pytz.timezone(zone)
        new_local_time = datetime.now(new_home)
        new_current_time = new_local_time.strftime("%A - %H:%M (%d %B %Y)")
        new_clock.config(text=new_current_time, fg='white')
        default_str.set(zone)

    # Create a Listbox to show all available time zones
    box = Listbox(main_frame1, font=("Microsoft Uighur", 22), fg='black', bg='#1a6b6e', height=14, bd=0, relief=FLAT, selectbackground='#1a6b6e', selectforeground='white', cursor='hand2', highlightcolor='#1a6b6e', highlightbackground='#1a6b6e', highlightthickness=10, selectborderwidth=0.5, selectmode=SINGLE)
    for timeZone in pytz.all_timezones:
        box.insert(END, timeZone)
    box.bind("<Double-1>", Time_of_country)
    box.place(x=0, y=0)

    # Create a toggle menu bar to set some buttons to add time zone of given countries
    def toggle_menu():
        # create a frame for toggle menu
        f1 = Frame(main_frame1, width=873, height=60, bg='#259498')
        f1.place(x=224, y=517)

        # create a template by using button function to create buttons for adding a time zone with name of there country
        def button(x, y, text, activbcolor, bcolor, cmd):
            def on_press(e):
                myButton1['background'] = activbcolor
                myButton1['foreground'] = 'white'
            def on_leave(e):
                myButton1['background'] = bcolor
                myButton1['foreground'] = 'black'

            myButton1 = Button(f1, text=text, height=2, justify=LEFT, fg='black', bd=0, relief=SUNKEN, bg=bcolor, activeforeground='white', activebackground=activbcolor, command=cmd, font='Georgia 10 bold', padx=5, cursor='hand2')
            # Binding buttons to mouse event
            myButton1.bind('<Enter>', on_press)
            myButton1.bind('<Leave>', on_leave)
            myButton1.place(x=x, y=y)

        # Create function to add time zone of India
        def Time_of_India():
            new_home = pytz.timezone("Asia/Kolkata")
            new_local_time = datetime.now(new_home)
            new_current_time = new_local_time.strftime("%A - %H:%M (%d %B %Y)")
            new_clock.config(text=new_current_time, fg='white')
            default_str.set("India (Kolkata)")

        # Create function to add time zone of Pakistan
        def Time_of_Pakistan():
            new_home = pytz.timezone("Asia/karachi")
            new_local_time = datetime.now(new_home)
            new_current_time = new_local_time.strftime("%A - %H:%M (%d %B %Y)")
            new_clock.config(text=new_current_time, fg='white')
            default_str.set("pakistan (Karachi)")

        # Create function to add time zone of USA
        def Time_of_USA():
            new_home = pytz.timezone("America/New_York")
            new_local_time = datetime.now(new_home)
            new_current_time = new_local_time.strftime("%A - %H:%M (%d %B %Y)")
            new_clock.config(text=new_current_time, fg='white')
            default_str.set("New York (USA)")

        # Create function to add time zone of Europe
        def Time_of_Europe():
            new_home = pytz.timezone("Europe/london")
            new_local_time = datetime.now(new_home)
            new_current_time = new_local_time.strftime("%A - %H:%M (%d %B %Y)")
            new_clock.config(text=new_current_time, fg='white')
            default_str.set("Europe (London)")

        # Create function to add time zone of Australia
        def Time_of_Australia():
            new_home = pytz.timezone("Australia/adelaide")
            new_local_time = datetime.now(new_home)
            new_current_time = new_local_time.strftime("%A - %H:%M (%d %B %Y)")
            new_clock.config(text=new_current_time, fg='white')
            default_str.set("Astralia (Adelaide)")

        # Create function to add time zone of France
        def Time_of_france():
            new_home = pytz.timezone("Europe/paris")
            new_local_time = datetime.now(new_home)
            new_current_time = new_local_time.strftime("%A - %H:%M (%d %B %Y)")
            new_clock.config(text=new_current_time, fg='white')
            default_str.set("France (Paris)")

        # Create function to add time zone of Singapore
        def Time_of_singapore():
            new_home = pytz.timezone("Asia/Singapore")
            new_local_time = datetime.now(new_home)
            new_current_time = new_local_time.strftime("%A - %H:%M (%d %B %Y)")
            new_clock.config(text=new_current_time, fg='white')
            default_str.set("Singapore (Singapore)")

        # Create function to add time zone of Norway
        def Time_of_norway():
            new_home = pytz.timezone("Europe/Oslo")
            new_local_time = datetime.now(new_home)
            new_current_time = new_local_time.strftime("%A - %H:%M (%d %B %Y)")
            new_clock.config(text=new_current_time, fg='white')
            default_str.set("Norway (Oslo)")

        # Create function to add time zone of Africa
        def Time_of_africa():
            new_home = pytz.timezone("Africa/luanda")
            new_local_time = datetime.now(new_home)
            new_current_time = new_local_time.strftime("%A - %H:%M (%d %B %Y)")
            new_clock.config(text=new_current_time, fg='white')
            default_str.set("Africa (Luanda)")

        # Create function to add time zone of Dubai
        def Time_of_dubai():
            new_home = pytz.timezone("Asia/dubai")
            new_local_time = datetime.now(new_home)
            new_current_time = new_local_time.strftime("%A - %H:%M (%d %B %Y)")
            new_clock.config(text=new_current_time, fg='white')
            default_str.set("Dubai (Asia)")

        # Create function to add time zone of Hong Kong
        def Time_of_hong_kong():
            new_home = pytz.timezone("Asia/Hong_kong")
            new_local_time = datetime.now(new_home)
            new_current_time = new_local_time.strftime("%A - %H:%M (%d %B %Y)")
            new_clock.config(text=new_current_time, fg='white')
            default_str.set("Hong Kong (Asia)")

        # Create function to add time zone of Canada
        def Time_of_canada():
            new_home = pytz.timezone("Canada/Mountain")
            new_local_time = datetime.now(new_home)
            new_current_time = new_local_time.strftime("%A - %H:%M (%d %B %Y)")
            new_clock.config(text=new_current_time, fg='white')
            default_str.set("Canada (Mountain)")

        # Create Buttons in toggle menu
        button(0, 9, "India", '#259498', '#259498', Time_of_India)
        button(50, 9, "Pakistan", '#259498', '#259498', Time_of_Pakistan)
        button(125, 9, "USA", '#259498', '#259498', Time_of_USA)
        button(170, 9, "Europe", '#259498', '#259498', Time_of_Europe)
        button(237, 9, "Australia", '#259498', '#259498', Time_of_Australia)
        button(320, 9, "France", '#259498', '#259498', Time_of_france)
        button(385, 9, "Singapore", '#259498', '#259498', Time_of_singapore)
        button(472, 9, "Dubai", '#259498', '#259498', Time_of_dubai)
        button(528, 9, "Canada", '#259498', '#259498', Time_of_canada)
        button(595, 9, "Norway", '#259498', '#259498', Time_of_norway)
        button(665, 9, "Africa", '#259498', '#259498', Time_of_africa)
        button(723, 9, "Hong Kong", '#259498', '#259498', Time_of_hong_kong)

        # Create delete function to close the toggle menu
        def delete():
            f1.destroy()

        # Create a Button to close the toggle menu
        Button(f1, text='⋙', font='arial 40 bold', fg='#F5F5DC', command=delete, activebackground='#259498', bg='#259498', bd=0, activeforeground='#F5F5DC', cursor='hand2').place(x=820, y=-20)

    # Create a Button to open the toggle menu
    Button(main_frame1, command=toggle_menu, text='⋘', font='arial 40 bold', fg='#F5F5DC', bd=0, bg='#232734', activebackground='#232734', activeforeground='#F5F5DC', cursor='hand2').place(x=1040, y=497)

    # First default Time zone
    f1 = Frame(main_frame1, bd=0, bg='#232734')
    f1.place(x=225, y=30, width=180, height=150)
    global name1
    name1 = Label(f1, font=("Georgia", 20, "bold"), bg='#232734')
    name1.place(x=50, y=10)
    global clock1
    clock1 = Label(f1, font=("Georgia", 15), bg='#232734')
    clock1.place(x=22, y=60)
    India_time()

    # Second default Time zone
    f2 = Frame(main_frame1, bd=0, bg='#232734')
    f2.place(x=455, y=30, width=180, height=150)
    global name2
    name2 = Label(f2, font=("Georgia", 20, "bold"), bg='#232734')
    name2.place(x=18, y=10)
    global clock2
    clock2 = Label(f2, font=("Georgia", 15), bg='#232734')
    clock2.place(x=21, y=60)
    USA_time()

    # Third default Time zone
    f3 = Frame(main_frame1, bd=0, bg='#232734')
    f3.place(x=685, y=30, width=180, height=150)
    global name3
    name3 = Label(f3, font=("Georgia", 20, "bold"), bg='#232734')
    name3.place(x=33, y=10)
    global clock3
    clock3 = Label(f3, font=("Georgia", 15), bg='#232734')
    clock3.place(x=25, y=60)
    Europe_time()

    # Forth default Time zone
    f4 = Frame(main_frame1, bd=0, bg='#232734')
    f4.place(x=915, y=30, width=180, height=150)
    global name4
    name4 = Label(f4, font=("Georgia", 20, "bold"), bg='#232734')
    name4.place(x=44, y=10)
    global clock4
    clock4 = Label(f4, font=("Georgia", 15), bg='#232734')
    clock4.place(x=23, y=60)
    Japan_time()

    # Add New Time zone for any country
    New = Frame(main_frame1, bd=5, bg='#232734')
    New.place(x=225, y=250, width=875, height=200)
    default_str = StringVar()
    new_name = Label(New, font=("Georgia", 34, "bold"), bg='#232734', textvariable=default_str, fg='#ea3548')
    default_str.set("                       Add Time Zone")
    new_name.place(x=0, y=10)
    new_clock = Label(New, font=("Georgia", 15), bg='#232734')
    new_clock.place(x=0, y=80)

# Start to program execution
if __name__ == '__main__':
    # Initialize object of class Tk and create main window (root)
    root = Tk()
    root.geometry('1100x630+100+5')
    root.config(bg='#232734')
    root.resizable(False, False)
    root.title("World Clock")
    root.attributes('-alpha', 0.99)  # Transparent 1% or 0.01%
    root.wm_iconbitmap("A:\\My Projects\\Android Subsystem for Windows (Python)\\World Clock\\clock.ico")

    # create menu_Frame to show all four app buttons
    menu_frame = Frame(root, width=1100, height=50, bg="#208488")
    menu_frame.place(x=0, y=0)

    # create and set app buttons on menu frame
    Alarm_button = Button(menu_frame, text="Alarm", font="Papyrus 15 bold underline", bg="#208488", fg='orange', activebackground='#208488', activeforeground='white', bd=0, relief=FLAT, command=alarm_menu)
    Alarm_button.place(x=10, y=0)

    Clock_button = Button(menu_frame, text="Clock", font="Papyrus 15 bold", bg="#208488", fg='white', activebackground='#208488', activeforeground='white', bd=0, relief=FLAT, command=clock_menu)
    Clock_button.place(x=90, y=0)

    Stopwatch_button = Button(menu_frame, text="Stopwatch", font="Papyrus 15 bold", bg="#208488", fg='white', activebackground='#208488', activeforeground='white', bd=0, relief=FLAT, command=stopwatch_menu)
    Stopwatch_button.place(x=170, y=0)

    Timer_button = Button(menu_frame, text="Timer", font="Papyrus 15 bold", bg="#208488", fg='white', activebackground='#208488', activeforeground='white', bd=0, relief=FLAT, command=timer_menu)
    Timer_button.place(x=300, y=0)

    # call alarm_menu function to set it as a default app
    alarm_menu()

    root.mainloop()
