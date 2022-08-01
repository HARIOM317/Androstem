# Importing required libraries
from tkinter import *
from tkinter import messagebox, ttk, filedialog
from threading import Thread
import os
import subprocess
import winapps
import datetime
import webbrowser
import pyautogui
import keyboard
import time
import screen_brightness_control
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
import psutil
import requests
import json
import urllib.request
from bs4 import BeautifulSoup
from tkcalendar import *
import babel.numbers        # for backend process in .exe file


''' *****-----***** FUNCTIONS FOR OPENING ANY APPS *****-----*****'''


# for opening AI Assistant
def opening_ai_assistant():
    os.startfile("A:\\My Projects\\Android Subsystem for Windows (Python)\\Jarvis AI\\AI_Assistant.pyw")


# for opening browser
def opening_browser():
    os.startfile("A:\\My Projects\\Android Subsystem for Windows (Python)\\Browser\\internet.pyw")


# for opening camera
def opening_camera():
    subprocess.run('start microsoft.windows.camera:', shell=True)


# for opening calculator
def opening_calculator():
    os.startfile("A:\\My Projects\\Android Subsystem for Windows (Python)\\Calculator\\Calculator.pyw")


# for opening convertor
def opening_convertor():
    os.startfile("A:\\My Projects\\Android Subsystem for Windows (Python)\\Convertor app\\convertor.pyw")


# for opening currency convertor
def opening_currency_convertor():
    os.startfile("A:\\My Projects\\Android Subsystem for Windows (Python)\\Currency Convertor\\Currency converter.pyw")


# for opening google webpage
def opening_google():
    webbrowser.open("https://www.google.co.in/webhp?tab=rw")


# for opening Google Drive
def opening_drive():
    webbrowser.open("https://drive.google.com/drive/my-drive")


# for opening Google Calendar
def opening_calendar():
    webbrowser.open("https://calendar.google.com/calendar/u/0/r?tab=rc")


# for opening Gmail
def opening_gmail():
    webbrowser.open("https://mail.google.com/mail/u/0/?tab=rm#inbox")


# for opening Google map
def opening_map():
    webbrowser.open("https://www.google.co.in/maps?hl=en&tab=rl")


# for opening Google photos
def opening_photos():
    webbrowser.open("https://photos.google.com/?tab=rq&pageId=none")


# for opening playstore
def opening_playstore():
    webbrowser.open("https://play.google.com/store/games?hl=en&tab=r8")


# for opening YouTube
def opening_youtube():
    webbrowser.open("https://www.youtube.com/")


# for opening file manager
def opening_file_manager():
    os.startfile("A:\\My Projects\\Android Subsystem for Windows (Python)\\File Manager\\file_manager.pyw")


# for opening google translator
def opening_google_translator():
    os.startfile("A:\\My Projects\\Android Subsystem for Windows (Python)\\Google Translator\\Google Translator.pyw")


# for opening image viewer
def opening_image_viewer():
    os.startfile("A:\\My Projects\\Android Subsystem for Windows (Python)\\Image Viewer\\Image Viewer.pyw")


# for opening internet speed test tool
def opening_interet_speed_test():
    os.startfile("A:\\My Projects\\Android Subsystem for Windows (Python)\\Internet Speed Tester\\Internet Speed Tester.pyw")


# for opening messaging app
def opening_message():
    os.startfile("A:\\My Projects\\Android Subsystem for Windows (Python)\\Message app\\messaging.pyw")


# for opening mobile number tracker
def opening_mobile_number_tracker():
    os.startfile("A:\\My Projects\\Android Subsystem for Windows (Python)\\Mobile Number Tracker\\Get Phone Number Details.pyw")


# for opening music player
def opening_music_player():
    os.startfile("A:\\My Projects\\Android Subsystem for Windows (Python)\\Music Player\\Music Player.pyw")


# for opening pdf viewer
def opening_pdf_viewer():
    os.startfile("A:\\My Projects\\Android Subsystem for Windows (Python)\\PDF Reader\\PDF Viewer.pyw")


# for opening phone app
def opening_phonebook():
    os.startfile("A:\\My Projects\\Android Subsystem for Windows (Python)\\Phonebook App\\phone.pyw")


# for opening qr code generator
def opening_qr_code_generator():
    os.startfile("A:\\My Projects\\Android Subsystem for Windows (Python)\\QR Code\\QR Code Generator.pyw")


# for opening screen recorder
def opening_screen_recorder():
    os.startfile("A:\\My Projects\\Android Subsystem for Windows (Python)\\Screen Recorder\\Screen Recorder.pyw")


# for opening spelling checker
def opening_spelling_checker():
    os.startfile("A:\\My Projects\\Android Subsystem for Windows (Python)\\Mini apps\\Spelling checker\\Spelling checker.pyw")


# for opening system information app
def opening_sys_info():
    os.startfile("A:\\My Projects\\Android Subsystem for Windows (Python)\\System Information app\\system_info.pyw")


# for opening video player
def opening_video_player():
    os.startfile("A:\\My Projects\\Android Subsystem for Windows (Python)\\Video Player\\Video Player.pyw")


# for opening voice recorder
def opening_voice_recorder():
    os.startfile("A:\\My Projects\\Android Subsystem for Windows (Python)\\Voice Recorder\\Voice Recorder.pyw")


# for opening weather app
def opening_weather():
    os.startfile("A:\\My Projects\\Android Subsystem for Windows (Python)\\Weather App\\Weather.pyw")


# for opening white board
def opening_white_board():
    os.startfile("A:\\My Projects\\Android Subsystem for Windows (Python)\\White board\\whiteboard.pyw")


# for opening world clock
def opening_world_clock():
    os.startfile("A:\\My Projects\\Android Subsystem for Windows (Python)\\World Clock\\World Clock.pyw")


# for opening text to handwriting convertor
def opening_text_to_handwriting():
    os.startfile("A:\\My Projects\\Android Subsystem for Windows (Python)\\Mini apps\\Text to Handwriting\\Handwritting.pyw")


# for opening video and audio downloader
def opening_v_downloader():
    os.startfile("A:\\My Projects\\Android Subsystem for Windows (Python)\\Youtube videos downloader\\Youtube video downloader.pyw")


# for opening country information app
def opening_country_info():
    os.startfile("A:\\My Projects\\Android Subsystem for Windows (Python)\\Mini apps\\Explore world\\Country Info.pyw")


# for opening encryption decryption messaging app
def opening_encryption_decryption():
    os.startfile("A:\\My Projects\\Android Subsystem for Windows (Python)\\Steganography\\Encrypt-Decrypt.pyw")


# for opening text file sharing app
def opening_text_file_sharing():
    os.startfile("A:\\My Projects\\Android Subsystem for Windows (Python)\\Mini apps\\Text file transfer\\SendText.pyw")


# for opening covid app
def opening_covid_news():
    os.startfile("A:\\My Projects\\Android Subsystem for Windows (Python)\\Covid update\\covid-case.pyw")


# for opening text editor
def opening_text_editor():
    os.startfile("A:\\My Projects\\Android Subsystem for Windows (Python)\\Text Editor\\text_editor.pyw")


# for opening image editor
def opening_image_editor():
    os.startfile("A:\\My Projects\\Android Subsystem for Windows (Python)\\Image editor\\editor.pyw")


# for opening base convertor
def opening_base_convertor():
    os.startfile("A:\\My Projects\\Android Subsystem for Windows (Python)\\Mini apps\\Base convertor\\base_convertor.pyw")


# for opening screen rotator
def opening_screen_rotator():
    os.startfile("A:\\My Projects\\Android Subsystem for Windows (Python)\\Mini apps\\Screen rotater\\Screen Rotater.pyw")

# ---------------------------------------- X -----------------------------------------


# for showing current time in the status bar
def my_time():
    current_time = datetime.datetime.now().strftime("%I:%M %p")
    time_label.config(text=current_time)
    time_label.after(200, my_time)


# for showing current date and time in the home screen
def main_time():
    current_time = datetime.datetime.now().strftime("%I:%M %p")
    main_time_label.config(text=current_time)
    current_date = datetime.datetime.now().strftime("%a, %d %b")
    date_label.config(text=current_date)
    main_time_label.after(200, main_time)


# =============================================================================================
# Creating windows
root = Tk()
root.attributes('-fullscreen', True)
root.config(bg="#232733")
root.wm_attributes('-alpha', 0.995)

# loading background image
background = PhotoImage(file="A:\\My Projects\\Android Subsystem for Windows (Python)\\main\\App icons\\background.png")
background2 = PhotoImage(file="A:\\My Projects\\Android Subsystem for Windows (Python)\\main\\App icons\\background2.png")

# creating background image
bg_label = Label(root, image=background, bg="#232733")
bg_label.place(x=700, y=300)
bg_label2 = Label(root, image=background2, bg="#232733")
bg_label2.place(x=906, y=515)
Label(root, text="HSR", bg="#232733", font="Papyrus 15", fg="#c38ae2").place(x=914, y=615)


# Creating calendar
def my_calender():
    calendar_frame = Frame(root, width=463, height=454, highlightthickness=1, highlightbackground='#00d6ff', highlightcolor='#00a9ff', bg="#10161f")
    calendar_frame.place(x=1325, y=545)

    # Create the calendar
    my_Calender = Calendar(calendar_frame, setmode="day", get_pattern="dd/mm/yy", background="#10161f", foreground='white', font=("Bahnschrift Light Condensed", 17), headersbackground='#10161f', headersforeground='#FAF0BE', selectbackground='orange', selectforeground='white', normalbackground='#131823', normalforeground='Alice Blue', weekendbackground='#131823', weekendforeground='Alice Blue', othermonthbackground='#131823', othermonthwebackground='#131823', bordercolor='#222b32')
    my_Calender.place(x=0, y=0)

    week = datetime.datetime.now().strftime("Week - %W")
    Label(calendar_frame, text=week, fg='#ffffff', bg='#10161f', font=("Bahnschrift Light Condensed", 15)).place(x=180, y=400)

    def delete():
        calendar_frame.destroy()

    Button(calendar_frame, text="Close", command=delete, activebackground='#131823', bg='#131823', fg='white', bd=1, relief=RIDGE, activeforeground='white', font=("Bahnschrift Light Condensed", 13), width=9, overrelief=GROOVE).place(x=227, y=3)


# =========================== Top menu widgets and functions start =============================

# handle threading in enable_disable_wifi function
def threading_enable_disable_wifi():
    t1 = Thread(target=enable_disable_wifi)
    t1.start()


# for enable or disable wifi
def enable_disable_wifi():
    keyboard.press_and_release('windows+a')
    time.sleep(1)
    pyautogui.click(x=1424, y=184)
    time.sleep(5)
    threading_check_connection()


# for enable or disable bluetooth
def enable_disable_bluetooth():
    keyboard.press_and_release('windows+a')
    time.sleep(1)
    pyautogui.click(x=1613, y=177)


# for enable or disable airplane mode
def enable_disable_airplane_mode():
    keyboard.press_and_release('windows+a')
    time.sleep(1)
    pyautogui.click(x=1775, y=179)


# for enable or disable battery saver
def enable_disable_battery_saver():
    keyboard.press_and_release('windows+a')
    time.sleep(1)
    pyautogui.click(x=1460, y=324)


# for enable or disable focus assist
def enable_disable_focus_assist():
    keyboard.press_and_release('windows+a')
    time.sleep(1)
    pyautogui.click(x=1626, y=322)


# for enable or disable accessibility
def enable_disable_accessibility():
    keyboard.press_and_release('windows+a')
    time.sleep(1)
    pyautogui.click(x=1772, y=321)


# for enable or disable screencast
def enable_disable_cast():
    keyboard.press_and_release('windows+a')
    time.sleep(1)
    pyautogui.click(x=1459, y=468)


# for enable or disable hotspot
def enable_disable_hotspot():
    keyboard.press_and_release('windows+a')
    time.sleep(1)
    pyautogui.click(x=1622, y=470)


# for enable or disable keyboard layout
def enable_disable_keyboard_layout():
    keyboard.press_and_release('windows+a')
    time.sleep(1)
    pyautogui.click(x=1769, y=468)


# for enable or disable eye comfort
def enable_disable_eye_comfort():
    keyboard.press_and_release('windows+a')
    time.sleep(1)
    pyautogui.click(x=1466, y=613)


# for enable or disable projector
def enable_disable_project():
    keyboard.press_and_release('windows+a')
    time.sleep(1)
    pyautogui.click(x=1620, y=611)


# for enable or disable nearby sharing
def enable_disable_nearby_sharing():
    keyboard.press_and_release('windows+a')
    time.sleep(1)
    pyautogui.click(x=1784, y=611)


# Creating top menu for enable and disable Wi-Fi, bluetooth etc., and controlling brightness and speaker
def top_menu():
    f1 = Frame(root, width=1800, height=140, bg='#8c9cc9', bd=2, relief=RIDGE)
    f1.place(x=60, y=40)
    Frame(root, width=700, height=650, bg='#232733').place(x=610, y=335)
    Frame(root, width=720, height=685, bg='#232733').place(x=600, y=300)

    bg_label_ = Label(root, image=background, bg="#232733")
    bg_label_.place(x=700, y=300)
    bg_label2 = Label(root, image=background2, bg="#232733")
    bg_label2.place(x=906, y=515)
    Label(root, text="HSR", bg="#232733", font="Papyrus 15", fg="#c38ae2").place(x=914, y=615)

    # function for creating buttons for top menu
    def button(x, y, photo, text, activbcolor, bcolor, cmd):
        def on_press(e):
            myButton1['background'] = activbcolor

        def on_leave(e):
            myButton1['background'] = bcolor

        myButton1 = Button(f1, image=photo, text=text, bd=0, bg=bcolor, activebackground=activbcolor, command=cmd, cursor='hand2', compound=TOP, width=140, height=70)

        myButton1.bind('<Enter>', on_press)
        myButton1.bind('<Leave>', on_leave)

        myButton1.place(x=x, y=y)

    # Creating buttons for top menu
    button(0, 5, wifi, "Wi-Fi", '#a4b7ed', '#8c9cc9', threading_enable_disable_wifi)
    button(150, 5, bluetooth, "Bluetooth", '#a4b7ed', '#8c9cc9', enable_disable_bluetooth)
    button(300, 5, aeroplane, "Airplane mode", '#a4b7ed', '#8c9cc9', enable_disable_airplane_mode)
    button(450, 5, keyboard_layout, "Keyboard layout", '#a4b7ed', '#8c9cc9', enable_disable_keyboard_layout)
    button(600, 5, hotspot, "Mobile hotspot", '#a4b7ed', '#8c9cc9', enable_disable_hotspot)
    button(750, 5, battery, "Battery saver", '#a4b7ed', '#8c9cc9', enable_disable_battery_saver)
    button(900, 5, focus_assist, "Focus assist", '#a4b7ed', '#8c9cc9', enable_disable_focus_assist)
    button(1050, 5, accessibility, "Accessibility", '#a4b7ed', '#8c9cc9', enable_disable_accessibility)
    button(1200, 5, cast_screen, "Cast", '#a4b7ed', '#8c9cc9', enable_disable_cast)
    button(1350, 5, night_light, "Eye comfort", '#a4b7ed', '#8c9cc9', enable_disable_eye_comfort)
    button(1500, 5, project, "Project", '#a4b7ed', '#8c9cc9', enable_disable_project)
    button(1650, 5, nearby_sharing, "Nearby sharing", '#a4b7ed', '#8c9cc9', enable_disable_nearby_sharing)

    # _________________________ Controlling Brightness ________________________
    label_brightness = Label(f1, image=brightness_, bg="#8c9cc9")
    label_brightness.place(x=50, y=90)

    current_value = DoubleVar()

    # get current brightness
    def get_current_value():
        return "{: .2f}".format(current_value.get())

    # for changing the brightness
    def brightness_changed(event):
        screen_brightness_control.set_brightness(get_current_value())

    brightness = Scale(f1, from_=0, to=100, orient=HORIZONTAL, command=brightness_changed, variable=current_value, width=10, length=700, cursor='hand2', showvalue=False, activebackground='orange', relief=FLAT, bd=0, troughcolor='#719fbd', sliderrelief=SOLID, sliderlength=45, highlightbackground='dark blue', highlightthickness=1, bg='#586281')
    brightness.place(x=100, y=100)
    brightness.set(40)
    # _________________________________________________________________________

    # _____________________ Controlling Speaker __________________________
    label_speaker = Label(f1, image=volume_, bg="#8c9cc9")
    label_speaker.place(x=980, y=90)

    volume_value = DoubleVar()

    # for getting volume value
    def get_current_volume_value():
        return '{: .2f}'.format(volume_value.get())

    # for changing the volume
    def volume_changed(event):
        try:
            device = AudioUtilities.GetSpeakers()
            interface = device.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
            volume = cast(interface, POINTER(IAudioEndpointVolume))
            volume.SetMasterVolumeLevel(-float(get_current_volume_value()), None)
        except Exception as e:
            pass

    style = ttk.Style()
    style.configure("TScale", background="#f4f5f5")

    volume = Scale(f1, from_=60, to=0, orient=HORIZONTAL, command=volume_changed, variable=volume_value, showvalue=False, width=10, length=700, cursor='hand2', activebackground='orange', relief=FLAT, bd=0, troughcolor='#719fbd', sliderrelief=SOLID, sliderlength=45, highlightbackground='dark blue', highlightthickness=1, bg='#586281')
    volume.place(x=1030, y=100)

    volume.set(10)
    # _____________________________________________________________

    # for closing thr top menu
    def delete_f1():
        f1.destroy()

    Button(f1, image=top_menu_bar, command=delete_f1, activebackground='#8c9cc9', bg='#8c9cc9', bd=0, font=("Pristina", 30), cursor='hand2').place(x=873, y=120)


# top menu bar icon
top_menu_bar = PhotoImage(file="A:\\My Projects\\Android Subsystem for Windows (Python)\\main\\top_menu_bar.png")

# button for opening top menu bar
Button(root, command=top_menu, bd=0, bg='#232733', activebackground='#232733', image=top_menu_bar, font=("Pristina", 15), cursor='hand2').place(x=939, y=40)

# brightness icon
brightness_ = PhotoImage(file="A:\\My Projects\Android Subsystem for Windows (Python)\\main\\adapter_icons\\brightness.png")
# speaker icon
volume_ = PhotoImage(file="A:\\My Projects\Android Subsystem for Windows (Python)\\main\\adapter_icons\\volume.png")

# Loading all adaptor icons
wifi = PhotoImage(file="A:\\My Projects\\Android Subsystem for Windows (Python)\\main\\adapter_icons\\wifi.png")
bluetooth = PhotoImage(file="A:\\My Projects\\Android Subsystem for Windows (Python)\\main\\adapter_icons\\bluetooth_mode.png")
aeroplane = PhotoImage(file="A:\\My Projects\\Android Subsystem for Windows (Python)\\main\\adapter_icons\\aeroplane_mode.png")
keyboard_layout = PhotoImage(file="A:\\My Projects\\Android Subsystem for Windows (Python)\\main\\adapter_icons\\keyboard_layout.png")
hotspot = PhotoImage(file="A:\\My Projects\\Android Subsystem for Windows (Python)\\main\\adapter_icons\\hotspot.png")
battery = PhotoImage(file="A:\\My Projects\\Android Subsystem for Windows (Python)\\main\\adapter_icons\\battery_saver.png")
focus_assist = PhotoImage(file="A:\\My Projects\\Android Subsystem for Windows (Python)\\main\\adapter_icons\\focus_assist.png")
accessibility = PhotoImage(file="A:\\My Projects\\Android Subsystem for Windows (Python)\\main\\adapter_icons\\accessibility.png")
cast_screen = PhotoImage(file="A:\\My Projects\\Android Subsystem for Windows (Python)\\main\\adapter_icons\\cast.png")
night_light = PhotoImage(file="A:\\My Projects\\Android Subsystem for Windows (Python)\\main\\adapter_icons\\eye_comfort.png")
project = PhotoImage(file="A:\\My Projects\\Android Subsystem for Windows (Python)\\main\\adapter_icons\\project.png")
nearby_sharing = PhotoImage(file="A:\\My Projects\\Android Subsystem for Windows (Python)\\main\\adapter_icons\\nearby_sharing.png")

# =========================== Top menu widgets and functions end =============================
# ---------------------------------------- X -----------------------------------------


# =========================== Side menu widgets and functions start =============================
time_variable = True


# Creating side menu
def side_menu():
    f2 = Frame(root, width=585, height=1025, bg='#3d4459', bd=1, relief=SOLID)
    f2.place(x=11, y=45)
    Frame(root, width=700, height=650, bg='#232733').place(x=610, y=335)
    Frame(root, width=720, height=685, bg='#232733').place(x=600, y=300)

    bg_label_ = Label(root, image=background, bg="#232733")
    bg_label_.place(x=700, y=300)
    bg_label2 = Label(root, image=background2, bg="#232733")
    bg_label2.place(x=906, y=515)
    Label(root, text="HSR", bg="#232733", font="Papyrus 15", fg="#c38ae2").place(x=914, y=615)

    # label and frame 1 for quick functions
    Label(f2, text="Quick Functions", fg='#bababa', bg="#3d4459", font=("Bahnschrift Light Condensed", 10)).place(x=10, y=0)
    widget1 = Frame(f2, width=563, height=207, bg='#353b4e', bd=0.5, relief=RIDGE)
    widget1.place(x=10, y=30)

    # label and frame 2 for weather
    Label(f2, text="Weather", fg='#bababa', bg="#3d4459", font=("Bahnschrift Light Condensed", 10)).place(x=10, y=250)
    widget2 = Frame(f2, width=563, height=150, bg='#353b4e', bd=0.5, relief=GROOVE)
    widget2.place(x=10, y=280)

    # label and frame 3 for top news
    Label(f2, text="Top News", fg='#bababa', bg="#3d4459", font=("Bahnschrift Light Condensed", 10)).place(x=10, y=445)
    widget3 = Frame(f2, width=563, height=500, bg='#353b4e', bd=0.5, relief=RIDGE)
    widget3.place(x=10, y=475)

    # listbox for top news
    listbox = Listbox(widget3, selectbackground='#14e0ff', selectforeground='#1a1426', selectborderwidth=3, font=("Bahnschrift Light Condensed", 12), bd=0, bg="#353b4e", justify=LEFT, relief=FLAT, highlightthickness=0, fg='white')
    listbox.place(relx=0, rely=0, relheight=1, relwidth=1)

    # function for creating buttons in side menu
    def button(x, y, text, image, activbcolor, bcolor, cmd):
        def on_press(e):
            myButton1['background'] = activbcolor
            myButton1['foreground'] = 'white'

        def on_leave(e):
            myButton1['background'] = bcolor
            myButton1['foreground'] = 'white'

        myButton1 = Button(widget1, text=text, image=image, width=170, height=50, fg='white', bd=0, bg=bcolor, activeforeground='white', activebackground=activbcolor, command=cmd, font=("Bahnschrift Light Condensed", 10), compound=LEFT, cursor='hand2')
        myButton1.bind('<Enter>', on_press)
        myButton1.bind('<Leave>', on_leave)
        myButton1.place(x=x, y=y)

    # threading in screenshot
    def threading_takeScreenShot():
        t1 = Thread(target=takeScreenShot)
        t1.start()

    # for capturing screenshot
    def takeScreenShot():
        global time_variable
        i = 3
        while time_variable:
            time.sleep(1)
            if i == 1:
                time_variable = False
            i -= 1
        try:
            myScreenShot = pyautogui.screenshot()
            filepath = filedialog.asksaveasfilename(defaultextension='.png')
            myScreenShot.save(filepath)
            time_variable = True
        except:
            messagebox.showinfo("Screen shot", "File not saved!")

    # Creating buttons as quick functions
    button(10, 10, "Google", _google_, '#56607e', "#3c4459", opening_google)
    button(194, 10, "Convert CUR", currency_exchanger, '#56607e', "#3c4459", opening_currency_convertor)
    button(378, 10, "Transfer text", file_transfer, '#56607e', "#3c4459", opening_text_file_sharing)
    button(10, 75, "Calculator", calculator, '#56607e', "#3c4459", opening_calculator)
    button(194, 75, "Calendar", calendar, '#56607e', "#3c4459", my_calender)
    button(378, 75, "Notepad", notepad, '#56607e', "#3c4459", opening_text_editor)
    button(10, 140, "QR Code", qr_code, '#56607e', "#3c4459", opening_qr_code_generator)
    button(194, 140, "Handwriting", handwriting, '#56607e', "#3c4459", opening_text_to_handwriting)
    button(378, 140, "Screenshot", screenshot, '#56607e', "#3c4459", threading_takeScreenShot)

    # for weather widget in side menu
    weather_in_c = Label(widget2, text="", image=weather_celcius, font=("Bahnschrift Light Condensed", 10), bg="#353b4e", fg="sky blue", compound=LEFT, width=550, height=70, justify=CENTER, anchor='w')
    weather_in_c.place(x=2, y=0)

    weather_in_f = Label(widget2, text="", image=weather_fehrenhite, font=("Bahnschrift Light Condensed", 10), bg="#353b4e", fg="sky blue", compound=LEFT, width=550, height=70, justify=CENTER, anchor='w')
    weather_in_f.place(x=2, y=72)

    # threading in current weather
    def threading_current_weather():
        t1 = Thread(target=current_weather)
        t1.start()

    # for getting current weather
    def current_weather():
        try:
            url = "https://www.google.com/search?q=tempreture"
            r = requests.get(url)
            data = BeautifulSoup(r.text, "html.parser")
            ans_ = data.find("div", class_="BNeawe").text
            weather_in_c.config(text="   " + ans_, fg="white", font=("Bahnschrift Light Condensed", 10))

            url2 = "https://www.google.com/search?q=temperature+in+fahrenheit"
            r2 = requests.get(url2)
            data2 = BeautifulSoup(r2.text, "html.parser")
            ans_2 = data2.find("div", class_="BNeawe").text
            weather_in_f.config(text="   " + ans_2, fg="white", font=("Bahnschrift Light Condensed", 10))
        except:
            weather_in_c.config(text="   No internet", font=("Bahnschrift Light Condensed", 10), fg='orange')
            weather_in_f.config(text="   No internet", font=("Bahnschrift Light Condensed", 10), fg='orange')

    threading_current_weather()
    # ______________________________________________________________________

    # threading in get news function
    def threading_get_news():
        t1 = Thread(target=get_news)
        t1.start()

    # for top news in the side menu
    def get_news():
        try:
            # API key for sports news
            news_url = "Enter your sports news api key here"
            news = requests.get(news_url).text
            news_dict = json.loads(news)
            arts = news_dict['articles']
            news_no = 1
            listbox.insert(END, "   SPORTS NEWS :")
            for article in arts:
                if news_no > 10:
                    break
                else:
                    listbox.insert(END, f"\n   News {news_no} : {article['description']}")
                news_no = news_no + 1
            listbox.insert(END, "")

            # API key for business news
            business_url = "Enter your business news api key here"
            news2 = requests.get(business_url).text
            news_dict2 = json.loads(news2)
            arts = news_dict2['articles']
            news_no2 = 1
            listbox.insert(END, "   BUSINESS NEWS : ")
            for article in arts:
                if news_no2 > 10:
                    break
                else:
                    listbox.insert(END, f"\n   News {news_no2} : {article['description']}")
                news_no2 = news_no2 + 1
            listbox.insert(END, "")

            # API key for tech news
            tech_url = "Enter your tech news api key here"
            news3 = requests.get(tech_url).text
            news_dict3 = json.loads(news3)
            arts = news_dict3['articles']
            news_no3 = 1
            listbox.insert(END, "   TECH NEWS : ")
            for article in arts:
                if news_no3 > 10:
                    break
                else:
                    listbox.insert(END, f"\n   News {news_no3} : {article['description']}")
                news_no3 = news_no3 + 1
        except:
            listbox.insert(END, "   Opps...")
            listbox.insert(END, "   No Internet")
            listbox.insert(END, "   Try again later!")

    threading_get_news()
    # ___________________________________________________________________

    # for closing side menu
    def delete_f2():
        f2.destroy()

    Button(f2, image=side_widget, command=delete_f2, activebackground='#3d4459', bg='#3d4459', bd=0, cursor='hand2').place(x=10, y=980)


# loading side menu icon
side_widget = PhotoImage(file="A:\\My Projects\\Android Subsystem for Windows (Python)\\main\\side_widget.png")

# button for opening side menu
Button(root, command=side_menu, image=side_widget, bd=0, bg='#232733', activebackground='#232733', cursor='hand2').place(x=22, y=1026)

# =============== loading all side menu icons ===============
_google_ = PhotoImage(file="A:\\My Projects\\Android Subsystem for Windows (Python)\\main\\App icons\\Side widget app icons\\google.png")
currency_exchanger = PhotoImage(file="A:\\My Projects\\Android Subsystem for Windows (Python)\\main\\App icons\\Side widget app icons\\currency_exchange.png")
calculator = PhotoImage(file="A:\\My Projects\\Android Subsystem for Windows (Python)\\main\\App icons\\Side widget app icons\\calculator.png")
calendar = PhotoImage(file="A:\\My Projects\\Android Subsystem for Windows (Python)\\main\\App icons\\Side widget app icons\\calendar.png")
file_transfer = PhotoImage(file="A:\\My Projects\\Android Subsystem for Windows (Python)\\main\\App icons\\Side widget app icons\\file_transfer.png")
handwriting = PhotoImage(file="A:\\My Projects\\Android Subsystem for Windows (Python)\\main\\App icons\\Side widget app icons\\handwriting.png")
notepad = PhotoImage(file="A:\\My Projects\\Android Subsystem for Windows (Python)\\main\\App icons\\Side widget app icons\\notepad.png")
qr_code = PhotoImage(file="A:\\My Projects\\Android Subsystem for Windows (Python)\\main\\App icons\\Side widget app icons\\qr_code.png")
screenshot = PhotoImage(file="A:\\My Projects\\Android Subsystem for Windows (Python)\\main\\App icons\\Side widget app icons\\screenshot.png")
weather_celcius = PhotoImage(file="A:\\My Projects\\Android Subsystem for Windows (Python)\\main\\App icons\\Side widget app icons\\weather_in_celcius.png")
weather_fehrenhite = PhotoImage(file="A:\\My Projects\\Android Subsystem for Windows (Python)\\main\\App icons\\Side widget app icons\\weather_in_fehrenhite.png")

# =========================== Side menu widgets and functions end =============================
# ---------------------------------------- X -----------------------------------------


# top frame for status bar
top_frame = Frame(root, bg="#202020", height=25, width=1500)
top_frame.pack(side=TOP, fill=X)

# showing current time in status bar
time_label = Label(top_frame, text="", fg='white', bg="#202020")
time_label.place(x=10, y=0)
my_time()

# showing date and time in home screen
main_time_label = Label(root, text="", fg='white', bg="#232733", font="arial 25")
main_time_label.pack(pady=(150, 0))
date_label = Label(root, text="", fg='white', bg="#232733", font="arial 10")
date_label.pack()
main_time()

# showing project name in status bar
title = Label(top_frame, text="Android sub-system", fg='white', bg="#202020")
title.place(x=875, y=0)

# loading connection icons
wifi_connected = PhotoImage(file="A:\\My Projects\\Android Subsystem for Windows (Python)\\main\\adapter_icons\\wifi_connected.png")
wifi_not_connected = PhotoImage(file="A:\\My Projects\\Android Subsystem for Windows (Python)\\main\\adapter_icons\\wifi_not_connected.png")

# creating connection labels
connection = Label(top_frame, bg="#202020")
connection.place(x=1450, y=0)

show_connection = Label(top_frame, bg="#202020", fg='white')
show_connection.place(x=1500, y=0)


# function for checking connection
def connect(host='http://google.com'):
    try:
        urllib.request.urlopen(host)
        return True
    except:
        return False


# threading in checking connection
def threading_check_connection():
    t1 = Thread(target=check_connection)
    t1.start()


# function for updating icons according connection is true or false
def check_connection():
    try:
        if connect():
            connection.config(image=wifi_connected)
            show_connection.config(text="Connected", fg='sky blue')
        else:
            connection.config(image=wifi_not_connected)
            show_connection.config(text="No internet", fg='orange')
    except:
        pass


threading_check_connection()

# weather icon for home screen
weather_icon = PhotoImage(file="A:\\My Projects\\Android Subsystem for Windows (Python)\\main\\weather.png")

# temperature label for home screen
temperature = Label(root, text="", image=weather_icon, font=("Bahnschrift Light Condensed", 15), bg="#232733", fg="#dcb859", compound=LEFT)
temperature.place(x=1250, y=65)


# threading in temperature function
def threading_current_temperature():
    t1 = Thread(target=current_temperature)
    t1.start()


# getting current temperature for home screen
def current_temperature():
    try:
        url = "https://www.google.com/search?q=tempreture"
        r = requests.get(url)
        data = BeautifulSoup(r.text, "html.parser")
        ans_ = data.find("div", class_="BNeawe").text
        temperature.config(text="   "+ans_, fg="#dcb859", font=("Bahnschrift Light Condensed", 15))
    except:
        temperature.config(text="   No internet", font=("Bahnschrift Light Condensed", 10), fg='yellow')


threading_current_temperature()


# for refreshing
def refresh():
    threading_check_connection()
    threading_current_temperature()


# refreshing icon and button
refresh_icon = PhotoImage(file="A:\\My Projects\\Android Subsystem for Windows (Python)\\main\\adapter_icons\\refresh_button.png")
refresh_button = Button(top_frame, image=refresh_icon, bg="#202020", activebackground="#202020", bd=0, relief=FLAT, command=refresh, cursor='hand2')
refresh_button.place(x=1400, y=3)


# _____________________ For Battery Status __________________________
def convertTime(seconds):
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    return "%d: %02d: %02d" % (hours, minutes, seconds)


def threading_battery_status():
    t1 = Thread(target=battery_status)
    t1.start()


# for getting battery information
def battery_status():
    global battery_png, battery_label
    battery = psutil.sensors_battery()
    percent = battery.percent

    label.config(text=f"{percent}%")
    plug_in = battery.power_plugged
    if plug_in:
        label_plug.config(text="Plugged in", fg='gold')
    elif not plug_in:
        if 0 <= percent <= 35:
            label_plug.config(text="low battery", fg='red')
        elif percent == 100:
            label_plug.config(text="full battery", fg='light green')
        else:
            label_plug.config(text="")

    battery_label = Label(top_frame, background="#202020")
    battery_label.place(x=1770, y=0)

    label.after(1000, battery_status)

    if battery.power_plugged:
        battery_png = PhotoImage(
            file="A:\\My Projects\\Android Subsystem for Windows (Python)\\main\\adapter_icons\\charging.png")
        battery_label.config(image=battery_png)
    else:
        if 0 <= percent <= 35:
            battery_png = PhotoImage(
                file="A:\\My Projects\\Android Subsystem for Windows (Python)\\main\\adapter_icons\\low_battery.png")
            battery_label.config(image=battery_png)
        elif 36 <= percent <= 75:
            battery_png = PhotoImage(
                file="A:\\My Projects\\Android Subsystem for Windows (Python)\\main\\adapter_icons\\half_battery.png")
            battery_label.config(image=battery_png)
        else:
            battery_png = PhotoImage(
                file="A:\\My Projects\\Android Subsystem for Windows (Python)\\main\\adapter_icons\\full_battery.png")
            battery_label.config(image=battery_png)


label = Label(top_frame, bg='#202020', fg='white')
label.place(x=1815, y=0)
label_plug = Label(top_frame, bg='#202020', width=10, justify=CENTER, fg='white')
label_plug.place(x=1650, y=0)

threading_battery_status()
# __________________________________________________________________________________


# for exiting from android sub-system
def close_sub_system():
    root.destroy()
    exit()


# creating exit button
exit_button_image = PhotoImage(file="A:\\My Projects\\Android Subsystem for Windows (Python)\\main\\exit_button.png")
exit_button = Button(top_frame, image=exit_button_image, bd=0, relief=FLAT, bg='#202020', activebackground='#202020', command=close_sub_system, cursor='hand2')
exit_button.pack(side=RIGHT, padx=5)

# creating google search widget
google_search_image = PhotoImage(file="A:\\My Projects\\Android Subsystem for Windows (Python)\\main\\google_search_bar.png")
google_search_bar = Label(root, image=google_search_image, bg="#232733")
google_search_bar.place(x=725, y=60)

google_image = PhotoImage(file="A:\\My Projects\\Android Subsystem for Windows (Python)\\main\\google_icon.png")
google_search_button = Button(root, image=google_image, bg='#141518', activebackground='#141518', bd=0, relief=FLAT, cursor='hand2', command=opening_google)
google_search_button.place(x=750, y=84)
google_search_bar_button = Button(root, text=" ", bg='#141518', activebackground='#141518', width=35, padx=5, pady=7, bd=0, relief=FLAT, cursor='hand2', command=opening_google)
google_search_bar_button.place(x=783, y=75)
google_mic_image = PhotoImage(file="A:\\My Projects\\Android Subsystem for Windows (Python)\\main\\google_mic.png")
google_mic_button = Button(root, image=google_mic_image, bg='#141518', activebackground='#141518', bd=0, relief=FLAT, cursor='hand2', command=opening_google)
google_mic_button.place(x=1140, y=84)

bottom_frame = Frame(root, bg="#161323", height=70, bd=0.5, relief=RIDGE)
bottom_frame.pack(side=BOTTOM, fill=X, padx=610, pady=5)


# Todo: _______________ ***** Designing Task Bar ***** _______________

# loading all image icons for app's button
main_ai_icon = PhotoImage(file="A:\\My Projects\\Android Subsystem for Windows (Python)\\main\\App icons\\All Icons\\AI_Assistant.png")
main_browser_icon = PhotoImage(file="A:\\My Projects\\Android Subsystem for Windows (Python)\\main\\App icons\\All Icons\\browser.png")
main_calculator_icon = PhotoImage(file="A:\\My Projects\\Android Subsystem for Windows (Python)\\main\\App icons\\All Icons\\calculator.png")
main_calendar_icon = PhotoImage(file="A:\\My Projects\\Android Subsystem for Windows (Python)\\main\\App icons\\All Icons\\calendar.png")
main_camera_icon = PhotoImage(file="A:\\My Projects\\Android Subsystem for Windows (Python)\\main\\App icons\\All Icons\\camera.png")
main_convertor_icon = PhotoImage(file="A:\\My Projects\\Android Subsystem for Windows (Python)\\main\\App icons\\All Icons\\convertor.png")
main_covid_update_icon = PhotoImage(file="A:\\My Projects\\Android Subsystem for Windows (Python)\\main\\App icons\\All Icons\\covid_update.png")
main_currency_convertor_icon = PhotoImage(file="A:\\My Projects\\Android Subsystem for Windows (Python)\\main\\App icons\\All Icons\\currency_convertor.png")
main_encryption_messaging_icon = PhotoImage(file="A:\\My Projects\\Android Subsystem for Windows (Python)\\main\\App icons\\All Icons\\encryption_messaging.png")
main_explore_world_icon = PhotoImage(file="A:\\My Projects\\Android Subsystem for Windows (Python)\\main\\App icons\\All Icons\\explore_world.png")
main_file_manager_icon = PhotoImage(file="A:\\My Projects\\Android Subsystem for Windows (Python)\\main\\App icons\\All Icons\\file_manager.png")
main_file_transfer_icon = PhotoImage(file="A:\\My Projects\\Android Subsystem for Windows (Python)\\main\\App icons\\All Icons\\file_transfer.png")
main_google_translator_icon = PhotoImage(file="A:\\My Projects\\Android Subsystem for Windows (Python)\\main\\App icons\\All Icons\\Google_Translator.png")
main_image_editor_icon = PhotoImage(file="A:\\My Projects\\Android Subsystem for Windows (Python)\\main\\App icons\\All Icons\\image_editor.png")
main_image_viewer_icon = PhotoImage(file="A:\\My Projects\\Android Subsystem for Windows (Python)\\main\\App icons\\All Icons\\Image_viewer.png")
main_internet_speed_test_icon = PhotoImage(file="A:\\My Projects\\Android Subsystem for Windows (Python)\\main\\App icons\\All Icons\\internet_speed_test.png")
main_messaging_icon = PhotoImage(file="A:\\My Projects\\Android Subsystem for Windows (Python)\\main\\App icons\\All Icons\\messaging.png")
main_mobile_number_tracker_icon = PhotoImage(file="A:\\My Projects\\Android Subsystem for Windows (Python)\\main\\App icons\\All Icons\\mobile_number_tracker.png")
main_music_player_icon = PhotoImage(file="A:\\My Projects\\Android Subsystem for Windows (Python)\\main\\App icons\\All Icons\\music_player.png")
main_pdf_viewer_icon = PhotoImage(file="A:\\My Projects\\Android Subsystem for Windows (Python)\\main\\App icons\\All Icons\\pdf_viewer.png")
main_phone_icon = PhotoImage(file="A:\\My Projects\\Android Subsystem for Windows (Python)\\main\\App icons\\All Icons\\phone.png")
main_qr_code_icon = PhotoImage(file="A:\\My Projects\\Android Subsystem for Windows (Python)\\main\\App icons\\All Icons\\qr_code.png")
main_screen_recorder_icon = PhotoImage(file="A:\\My Projects\\Android Subsystem for Windows (Python)\\main\\App icons\\All Icons\\screen_recorder.png")
main_spelling_checker_icon = PhotoImage(file="A:\\My Projects\\Android Subsystem for Windows (Python)\\main\\App icons\\All Icons\\spelling_checker.png")
main_system_info_icon = PhotoImage(file="A:\\My Projects\\Android Subsystem for Windows (Python)\\main\\App icons\\All Icons\\system_info.png")
main_text_editor_icon = PhotoImage(file="A:\\My Projects\\Android Subsystem for Windows (Python)\\main\\App icons\\All Icons\\text_editor.png")
main_video_downloader_icon = PhotoImage(file="A:\\My Projects\\Android Subsystem for Windows (Python)\\main\\App icons\\All Icons\\video_downloader.png")
main_video_player_icon = PhotoImage(file="A:\\My Projects\\Android Subsystem for Windows (Python)\\main\\App icons\\All Icons\\video_player.png")
main_voice_recorder_icon = PhotoImage(file="A:\\My Projects\\Android Subsystem for Windows (Python)\\main\\App icons\\All Icons\\voice_recoder.png")
main_weather_icon = PhotoImage(file="A:\\My Projects\\Android Subsystem for Windows (Python)\\main\\App icons\\All Icons\\weather.png")
main_white_board_icon = PhotoImage(file="A:\\My Projects\\Android Subsystem for Windows (Python)\\main\\App icons\\All Icons\\white_board.png")
main_world_clock_icon = PhotoImage(file="A:\\My Projects\\Android Subsystem for Windows (Python)\\main\\App icons\\All Icons\\world_clock.png")

main_google_group_icon = PhotoImage(file="A:\\My Projects\\Android Subsystem for Windows (Python)\\main\\App icons\\google_products.png")
main_apps_group_icon = PhotoImage(file="A:\\My Projects\\Android Subsystem for Windows (Python)\\main\\App icons\\apps.png")

# Power icons
power_icon = PhotoImage(file="A:\\My Projects\\Android Subsystem for Windows (Python)\\main\\adapter_icons\\Power icons\\power.png")
shutdown_icon = PhotoImage(file="A:\\My Projects\\Android Subsystem for Windows (Python)\\main\\adapter_icons\\Power icons\\shutdown.png")
sleep_icon = PhotoImage(file="A:\\My Projects\\Android Subsystem for Windows (Python)\\main\\adapter_icons\\Power icons\\sleep.png")
restart_icon = PhotoImage(file="A:\\My Projects\\Android Subsystem for Windows (Python)\\main\\adapter_icons\\Power icons\\restart.png")
restart_time_icon = PhotoImage(file="A:\\My Projects\\Android Subsystem for Windows (Python)\\main\\adapter_icons\\Power icons\\restart_time.png")


# creating android menu
def android_menu():
    Frame(root, width=720, height=685, bg='#232733').place(x=600, y=300)

    bg_label_ = Label(root, image=background, bg="#232733")
    bg_label_.place(x=700, y=300)
    bg_label2 = Label(root, image=background2, bg="#232733")
    bg_label2.place(x=906, y=515)
    Label(root, text="HSR", bg="#232733", font="Papyrus 15", fg="#c38ae2").place(x=914, y=615)

    f3 = Frame(root, width=700, height=650, bg='#111721', bd=5, relief=RIDGE)
    f3.place(x=610, y=335)

    lower_frame = Frame(f3, width=690, height=100, bg='#171c28', bd=1, relief=SOLID)
    lower_frame.place(x=0, y=540)

    icon_frame = Frame(f3, width=690, height=420, bg='#20242f')
    icon_frame.place(x=0, y=60)

    # __________ For power option __________
    # Creating frame for power buttons
    def power_menu():
        global power_frame
        power_frame = Frame(lower_frame, width=438, height=76, bg='#425174', highlightbackground='#b7b7b7', highlightthickness=1)
        power_frame.place(x=15, y=12)

        def restart():
            power_frame.destroy()
            os.system("shutdown /r /t 1")

        def restart_time():
            power_frame.destroy()
            os.system("shutdown /r /t 10")

        def logout():
            power_frame.destroy()
            os.system("shutdown -l")

        def shutdown():
            power_frame.destroy()
            os.system("shutdown /s /t 1")

        def power_button(x, y, text, image, activ_background_color, background_color, cmd):
            def on_press(e):
                myButton['background'] = activ_background_color
                myButton['foreground'] = 'black'

            def on_leave(e):
                myButton['background'] = background_color
                myButton['foreground'] = 'black'

            myButton = Button(power_frame, text=text, image=image, width=100, height=70, justify=CENTER, fg='black', bd=0, bg=background_color, activeforeground='black', activebackground=activ_background_color, command=cmd, cursor='hand2', compound=TOP)

            myButton.bind('<Enter>', on_press)
            myButton.bind('<Leave>', on_leave)

            myButton.place(x=x, y=y)

        power_button(0, 0, "Shut down", shutdown_icon, '#495a81', '#425174', shutdown)
        power_button(110, 0, "Sign out", sleep_icon, '#495a81', '#425174', logout)
        power_button(220, 0, "Restart", restart_icon, '#495a81', '#425174', restart)
        power_button(330, 0, "Restart time", restart_time_icon, '#495a81', '#425174', restart_time)

    # button for opening power options
    Button(lower_frame, image=power_icon, bg="#171c28", activebackground="#171c28", bd=0, relief=FLAT, command=power_menu).place(x=15, y=25)
    # _____________________________________________________________

    # button function for first android widget
    def button(x, y, image, text, activbcolor, bcolor, cmd):
        def on_press(e):
            myButton1['background'] = activbcolor
            myButton1['foreground'] = 'white'

        def on_leave(e):
            myButton1['background'] = bcolor
            myButton1['foreground'] = 'white'

        myButton1 = Button(icon_frame, image=image, text=text, justify=CENTER, fg='white', bd=0, bg=bcolor, activeforeground='white', activebackground=activbcolor, command=cmd, compound=TOP, width=125, height=125)

        myButton1.bind('<Enter>', on_press)
        myButton1.bind('<Leave>', on_leave)

        myButton1.place(x=x, y=y)

    # creating buttons in first android widget
    button(10, 10, main_ai_icon, "AI Assistant", '#282e3b', '#20242f', opening_ai_assistant)
    button(145, 10, main_browser_icon, "Browser", '#282e3b', '#20242f', opening_browser)
    button(280, 10, main_calculator_icon, "Calculator", '#282e3b', '#20242f', opening_calculator)
    button(415, 10, main_calendar_icon, "Calendar", '#282e3b', '#20242f', my_calender)
    button(550, 10, main_camera_icon, "Camera", '#282e3b', '#20242f', opening_camera)

    button(10, 145, main_convertor_icon, "Convertor", '#282e3b', '#20242f', opening_convertor)
    button(145, 145, main_covid_update_icon, "Covid update", '#282e3b', '#20242f', opening_covid_news)
    button(280, 145, main_currency_convertor_icon, "Currency", '#282e3b', '#20242f', opening_currency_convertor)
    button(415, 145, main_spelling_checker_icon, "Check spelling", '#282e3b', '#20242f', opening_spelling_checker)
    button(550, 145, main_world_clock_icon, "Clock", '#282e3b', '#20242f', opening_world_clock)

    button(10, 280, main_image_editor_icon, "Editor", '#282e3b', '#20242f', opening_image_editor)
    button(145, 280, main_explore_world_icon, "Explore world", '#282e3b', '#20242f', opening_country_info)
    button(280, 280, main_file_manager_icon, "File manager", '#282e3b', '#20242f', opening_file_manager)
    button(415, 280, main_image_viewer_icon, "Image", '#282e3b', '#20242f', opening_image_viewer)
    button(550, 280, main_internet_speed_test_icon, "Internet speed", '#282e3b', '#20242f', opening_interet_speed_test)

    # second android widget
    def android_menu_2():
        icon_set_1.config(fg="#525252", bg="#19202c", activebackground="#19202c", activeforeground="#525252")
        icon_set_2.config(fg="#ffffff", bg='#302c4e', activeforeground="#ffffff", activebackground="#302c4e")
        icon_set_3.config(fg="#525252", bg="#19202c", activebackground="#19202c", activeforeground="#525252")

        icon_frame_2 = Frame(f3, width=690, height=420, bg='#20242f')
        icon_frame_2.place(x=0, y=60)

        # button2 function for second android widget
        def button2(x, y, image, text, activbcolor, bcolor, cmd):
            def on_press(e):
                myButton2['background'] = activbcolor
                myButton2['foreground'] = 'white'

            def on_leave(e):
                myButton2['background'] = bcolor
                myButton2['foreground'] = 'white'

            myButton2 = Button(icon_frame_2, image=image, text=text, justify=CENTER, fg='white', bd=0, bg=bcolor, activeforeground='white', activebackground=activbcolor, command=cmd, compound=TOP, width=125, height=125)

            myButton2.bind('<Enter>', on_press)
            myButton2.bind('<Leave>', on_leave)

            myButton2.place(x=x, y=y)

        # creating buttons in second android widget
        button2(10, 10, main_messaging_icon, "Message", '#282e3b', '#20242f', opening_message)
        button2(145, 10, main_music_player_icon, "Music player", '#282e3b', '#20242f', opening_music_player)
        button2(280, 10, main_pdf_viewer_icon, "Pdf viewer", '#282e3b', '#20242f', opening_pdf_viewer)
        button2(415, 10, main_phone_icon, "Phone", '#282e3b', '#20242f', opening_phonebook)
        button2(550, 10, main_qr_code_icon, "QR Code", '#282e3b', '#20242f', opening_qr_code_generator)

        button2(10, 145, main_screen_recorder_icon, "Record screen", '#282e3b', '#20242f', opening_screen_recorder)
        button2(145, 145, main_system_info_icon, "System info", '#282e3b', '#20242f', opening_sys_info)
        button2(280, 145, main_file_transfer_icon, "SendText", '#282e3b', '#20242f', opening_text_file_sharing)
        button2(415, 145, main_google_translator_icon, "Translator", '#282e3b', '#20242f', opening_google_translator)
        button2(550, 145, main_mobile_number_tracker_icon, "Track number", '#282e3b', '#20242f', opening_mobile_number_tracker)

        button2(10, 280, main_encryption_messaging_icon, "Text encryption", '#282e3b', '#20242f', opening_encryption_decryption)
        button2(145, 280, main_text_editor_icon, "Text editor", '#282e3b', '#20242f', opening_text_editor)
        button2(280, 280, main_video_downloader_icon, "V downloader", '#282e3b', '#20242f', opening_v_downloader)
        button2(415, 280, main_video_player_icon, "Video player", '#282e3b', '#20242f', opening_video_player)
        button2(550, 280, main_voice_recorder_icon, "Voice recorder", '#282e3b', '#20242f', opening_voice_recorder)

    # third android widget
    def android_menu_3():
        icon_set_1.config(fg="#525252", bg="#19202c", activebackground="#19202c", activeforeground="#525252")
        icon_set_2.config(fg="#525252", bg="#19202c", activebackground="#19202c", activeforeground="#525252")
        icon_set_3.config(fg="#ffffff", bg='#302c4e', activeforeground="#ffffff", activebackground="#302c4e")
        icon_frame_3 = Frame(f3, width=690, height=420, bg='#20242f')
        icon_frame_3.place(x=0, y=60)

        # button3 function for third android widget
        def button3(x, y, image, text, activbcolor, bcolor, cmd):
            def on_press(e):
                myButton3['background'] = activbcolor
                myButton3['foreground'] = 'white'

            def on_leave(e):
                myButton3['background'] = bcolor
                myButton3['foreground'] = 'white'

            myButton3 = Button(icon_frame_3, image=image, text=text, justify=CENTER, fg='white', bd=0, bg=bcolor, activeforeground='white', activebackground=activbcolor, command=cmd, compound=TOP, width=125, height=125)

            myButton3.bind('<Enter>', on_press)
            myButton3.bind('<Leave>', on_leave)

            myButton3.place(x=x, y=y)

        # creating buttons in third android widget
        button3(10, 10, main_weather_icon, "Weather", '#282e3b', '#20242f', opening_weather)
        button3(145, 10, main_white_board_icon, "White board", '#282e3b', '#20242f', opening_white_board)

    # buttons for switching android widget
    icon_set_1 = Button(f3, text='●', font=15, width=3, height=1, command=android_menu, bg="#302c4e", activebackground="#302c4e", fg='#ffffff', activeforeground='white', bd=0, relief=FLAT)
    icon_set_1.place(x=280, y=495)
    icon_set_2 = Button(f3, text='●', font=15, width=3, height=1, command=android_menu_2, bg="#19202c", activebackground="#19202c", fg='#525252', activeforeground='white', bd=0, relief=FLAT)
    icon_set_2.place(x=330, y=495)
    icon_set_3 = Button(f3, text='●', font=15, width=3, height=1, command=android_menu_3, bg="#19202c", activebackground="#19202c", fg='#525252', activeforeground='white', bd=0, relief=FLAT)
    icon_set_3.place(x=380, y=495)

    # for closing android widget
    def delete_f3():
        f3.destroy()

    Button(f3, image=close_android_menu_image, command=delete_f3, activebackground='#111721', bg='#111721', bd=0, cursor='hand2').place(x=327, y=0)


close_android_menu_image = PhotoImage(file="A:\\My Projects\\Android Subsystem for Windows (Python)\\main\\close_android_menu.png")


# ********** Designing android button for task bar **********

# Open Android app widgets with Hower image animation
def change_android_pic(e):
    my_pic = PhotoImage(file="A:\\My Projects\\Android Subsystem for Windows (Python)\\main\\android_large.png")
    Android.config(image=my_pic)
    Android.image = my_pic
    Android.place(x=0, y=0)


def change_back_android(e):
    my_pic = PhotoImage(file="A:\\My Projects\\Android Subsystem for Windows (Python)\\main\\android_small.png")
    Android.config(image=my_pic)
    Android.image = my_pic
    Android.place(x=10, y=8)


# creating android button
android_Image = PhotoImage(file="A:\\My Projects\\Android Subsystem for Windows (Python)\\main\\android_small.png")
Android = Button(bottom_frame, image=android_Image, bg='#161323', bd=0, relief=FLAT, activebackground='#161323', command=android_menu)
Android.place(x=10, y=8)
Android.bind("<Enter>", change_android_pic)
Android.bind("<Leave>", change_back_android)

# shortcut icon frame for home screen icons
shortcut_icon_frame = Frame(root, width=114, height=955, bg="#2a3244", bd=1, relief=GROOVE)
shortcut_icon_frame.place(x=1800, y=44)

# loading google product icons
GOOGLE_app = PhotoImage(file="A:\\My Projects\\Android Subsystem for Windows (Python)\\main\\App icons\\Google\\google.png")
YOUTUBE_app = PhotoImage(file="A:\\My Projects\\Android Subsystem for Windows (Python)\\main\\App icons\\Google\\youtube.png")
PLAYSTORE_app = PhotoImage(file="A:\\My Projects\\Android Subsystem for Windows (Python)\\main\\App icons\\Google\\playstore.png")
MAP_app = PhotoImage(file="A:\\My Projects\\Android Subsystem for Windows (Python)\\main\\App icons\\Google\\map.png")
PHOTOS_app = PhotoImage(file="A:\\My Projects\\Android Subsystem for Windows (Python)\\main\\App icons\\Google\\photos.png")
DRIVE_app = PhotoImage(file="A:\\My Projects\\Android Subsystem for Windows (Python)\\main\\App icons\\Google\\drive.png")
GMAIL_app = PhotoImage(file="A:\\My Projects\\Android Subsystem for Windows (Python)\\main\\App icons\\Google\\gmail.png")
CALENDAR_app = PhotoImage(file="A:\\My Projects\\Android Subsystem for Windows (Python)\\main\\App icons\\Google\\calander.png")

# loading app icons
CLOCK_app = PhotoImage(file="A:\\My Projects\\Android Subsystem for Windows (Python)\\main\\App icons\\App widget\\clock-icon.png")
WEATHER_app = PhotoImage(file="A:\\My Projects\\Android Subsystem for Windows (Python)\\main\\App icons\\App widget\\Weather-icon.png")
WORLD_INFO_app = PhotoImage(file="A:\\My Projects\\Android Subsystem for Windows (Python)\\main\\App icons\\App widget\\world_info.png")
CONVERTOR_app = PhotoImage(file="A:\\My Projects\\Android Subsystem for Windows (Python)\\main\\App icons\\App widget\\convertor.png")
VOICE_RECORDER_app = PhotoImage(file="A:\\My Projects\\Android Subsystem for Windows (Python)\\main\\App icons\\App widget\\voice_recorder.png")
SCREEN_RECORDER_app = PhotoImage(file="A:\\My Projects\\Android Subsystem for Windows (Python)\\main\\App icons\\App widget\\screen_recorder.png")
BASE_CONVERTOR_app = PhotoImage(file="A:\\My Projects\\Android Subsystem for Windows (Python)\\main\\App icons\\App widget\\base_convertor.png")
ROTATE_SCREEN_app = PhotoImage(file="A:\\My Projects\\Android Subsystem for Windows (Python)\\main\\App icons\\App widget\\rotate-screen.png")


# google widget for group of google products
def google_widget():
    Frame(root, width=480, height=575, bg='#232733').place(x=1320, y=440)
    google_frame = Frame(root, width=220, height=555, bg='#36454F')
    google_frame.place(x=1570, y=450)

    header = Frame(google_frame, width=220, height=68, bg='#2a373f')
    header.place(x=0, y=0)

    Label(header, text="Google", bg="#2a373f", fg="#ffffff", font="default 13").place(x=10, y=15)

    def button(x, y, text, image, activ_backcolor, back_color, cmd):
        def on_press(e):
            myButton1['background'] = activ_backcolor
            myButton1['foreground'] = '#FFFFF0'

        def on_leave(e):
            myButton1['background'] = back_color
            myButton1['foreground'] = '#FFFFF0'

        myButton1 = Button(google_frame, text=text, image=image, width=90, height=90, fg='#FFFFF0', bd=0, bg=back_color, activeforeground='#FFFFF0', activebackground=activ_backcolor, command=cmd, compound=TOP)

        myButton1.bind('<Enter>', on_press)
        myButton1.bind('<Leave>', on_leave)

        myButton1.place(x=x, y=y)

    button(10, 85, "Google", GOOGLE_app, '#41505b', '#36454F', opening_google)
    button(117, 85, "YouTube", YOUTUBE_app, '#41505b', '#36454F', opening_youtube)
    button(10, 205, "Play store", PLAYSTORE_app, '#41505b', '#36454F', opening_playstore)
    button(117, 205, "Map", MAP_app, '#41505b', '#36454F', opening_map)
    button(10, 325, "Photos", PHOTOS_app, '#41505b', '#36454F', opening_photos)
    button(117, 325, "Drive", DRIVE_app, '#41505b', '#36454F', opening_drive)
    button(10, 445, "Gmail", GMAIL_app, '#41505b', '#36454F', opening_gmail)
    button(117, 445, "Calendar", CALENDAR_app, '#41505b', '#36454F', opening_calendar)

    def delete():
        google_frame.destroy()

    Button(header, text="×", command=delete, activebackground='#2a373f', bg='#2a373f', fg='white', bd=0, activeforeground='white', font="default 17", cursor='hand2').place(x=180, y=0)


# app widget for group of some application
def app_widget():
    Frame(root, width=480, height=575, bg='#232733').place(x=1320, y=440)
    app_frame = Frame(root, width=220, height=555, bg='#36454F')
    app_frame.place(x=1570, y=450)

    header = Frame(app_frame, width=220, height=68, bg='#2a373f')
    header.place(x=0, y=0)

    Label(header, text="Apps", bg="#2a373f", fg="#ffffff", font="default 13").place(x=10, y=15)

    def button(x, y, text, image, activ_backcolor, back_color, cmd):
        def on_press(e):
            myButton1['background'] = activ_backcolor
            myButton1['foreground'] = '#FFFFF0'

        def on_leave(e):
            myButton1['background'] = back_color
            myButton1['foreground'] = '#FFFFF0'

        myButton1 = Button(app_frame, text=text, image=image, width=90, height=90, fg='#FFFFF0', bd=0, bg=back_color, activeforeground='#FFFFF0', activebackground=activ_backcolor, command=cmd, compound=TOP)

        myButton1.bind('<Enter>', on_press)
        myButton1.bind('<Leave>', on_leave)

        myButton1.place(x=x, y=y)

    button(10, 85, "Clock", CLOCK_app, '#41505b', '#36454F', opening_world_clock)
    button(117, 85, "Weather", WEATHER_app, '#41505b', '#36454F', opening_weather)
    button(10, 205, "Explore", WORLD_INFO_app, '#41505b', '#36454F', opening_country_info)
    button(117, 205, "Convertor", CONVERTOR_app, '#41505b', '#36454F', opening_convertor)
    button(10, 325, "Voice", VOICE_RECORDER_app, '#41505b', '#36454F', opening_voice_recorder)
    button(117, 325, "Screen", SCREEN_RECORDER_app, '#41505b', '#36454F', opening_screen_recorder)
    button(10, 445, "Base", BASE_CONVERTOR_app, '#41505b', '#36454F', opening_base_convertor)
    button(117, 445, "Rotate", ROTATE_SCREEN_app, '#41505b', '#36454F', opening_screen_rotator)

    def delete():
        app_frame.destroy()

    Button(header, text="×", command=delete, activebackground='#2a373f', bg='#2a373f', fg='white', bd=0, activeforeground='white', font="default 17", cursor='hand2').place(x=180, y=0)


# Setting icons on main window
Button(shortcut_icon_frame, image=main_ai_icon, text="Assistant", width=100, height=100, fg='white', activeforeground='white', bd=0, relief=FLAT, compound=TOP, bg="#2a3244", activebackground="#2a3244", command=opening_ai_assistant).place(x=5, y=5)
Button(shortcut_icon_frame, image=main_browser_icon, text="Browser", width=100, height=100, fg='white', activeforeground='white', bd=0, relief=FLAT, compound=TOP, bg="#2a3244", activebackground="#2a3244", command=opening_browser).place(x=5, y=125)
Button(shortcut_icon_frame, image=main_file_manager_icon, text="File manager", width=100, height=100, fg='white', activeforeground='white', bd=0, relief=FLAT, compound=TOP, bg="#2a3244", activebackground="#2a3244", command=opening_file_manager).place(x=5, y=245)
Button(shortcut_icon_frame, image=main_google_group_icon, text="Google", width=100, height=100, fg='white', activeforeground='white', bd=0, relief=FLAT, compound=TOP, bg="#2a3244", activebackground="#2a3244", command=google_widget).place(x=5, y=365)
Button(shortcut_icon_frame, image=main_apps_group_icon, text="Apps", width=100, height=100, fg='white', activeforeground='white', bd=0, relief=FLAT, compound=TOP, bg="#2a3244", activebackground="#2a3244", command=app_widget).place(x=5, y=485)
Button(shortcut_icon_frame, image=main_music_player_icon, text="Music", width=100, height=100, fg='white', activeforeground='white', bd=0, relief=FLAT, compound=TOP, bg="#2a3244", activebackground="#2a3244", command=opening_music_player).place(x=5, y=605)
Button(shortcut_icon_frame, image=main_pdf_viewer_icon, text="Pdf viewer", width=100, height=100, fg='white', activeforeground='white', bd=0, relief=FLAT, compound=TOP, bg="#2a3244", activebackground="#2a3244", command=opening_pdf_viewer).place(x=5, y=725)
Button(shortcut_icon_frame, image=main_text_editor_icon, text="Text editor", width=100, height=100, fg='white', activeforeground='white', bd=0, relief=FLAT, compound=TOP, bg="#2a3244", activebackground="#2a3244", command=opening_text_editor).place(x=5, y=845)

# for searching system apps
name = StringVar()
version = StringVar()
location = StringVar()
Install_date = StringVar()
publisher = StringVar()


# ********** Designing search button for task bar **********
# Open search widget with Hower image animation
def change_search_pic(e):
    my_pic = PhotoImage(file="A:\\My Projects\\Android Subsystem for Windows (Python)\\main\\search_large.png")
    Search.config(image=my_pic)
    Search.image = my_pic
    Search.place(x=70, y=0)


def change_back_search(e):
    my_pic = PhotoImage(file="A:\\My Projects\\Android Subsystem for Windows (Python)\\main\\search_small.png")
    Search.config(image=my_pic)
    Search.image = my_pic
    Search.place(x=80, y=8)


# function to attach output
def app():
    try:
        name_label.config(text="Name : ")
        version_label.config(text="Version : ")
        location_label.config(text="Location : ")
        install_date_label.config(text="Install date : ")
        publisher_label.config(text="Publisher : ")
        for item in winapps.search_installed(app_entry.get().lower()):
            name.set(item.name)
            version.set(item.version)
            location.set(str(item.install_location))
            Install_date.set(str(item.install_date))
            publisher.set(item.publisher)

        path = location.get()
        os.startfile(path)
    except:
        messagebox.showinfo("Search", "File location not found for given entry!")


# GUI for searching
def file_searcher_window():
    Frame(root, width=700, height=650, bg='#232733').place(x=610, y=335)

    bg_label_ = Label(root, image=background, bg="#232733")
    bg_label_.place(x=700, y=300)
    bg_label2 = Label(root, image=background2, bg="#232733")
    bg_label2.place(x=906, y=515)
    Label(root, text="HSR", bg="#232733", font="Papyrus 15", fg="#c38ae2").place(x=914, y=615)

    f4 = Frame(root, width=720, height=685, bg='#20242f', bd=5, relief=RIDGE)
    f4.place(x=600, y=300)
    lower_frame = Frame(f4, width=709, height=50, bg="#181b23", bd=0.5, relief=GROOVE)
    lower_frame.place(x=0, y=625)

    name.set("")
    version.set("")
    location.set("")
    Install_date.set("")
    publisher.set("")

    # Creating label for each information
    # name using widget Label
    Label(f4, text="Enter App name : ", bg="#20242f", font="Aparajita 14", fg='white').place(x=10, y=10)
    global app_entry
    app_entry = Entry(f4, width=47, font="Aparajita 14", bg="#141518", fg="white", relief=RIDGE, bd=2)
    app_entry.bind("<Return>", lambda e: app())
    app_entry.place(x=180, y=10)

    global name_label, version_label, location_label, install_date_label, publisher_label

    name_label = Label(f4, bg="#20242f", fg='orange')
    name_label.place(x=10, y=150)
    version_label = Label(f4, bg="#20242f", fg='orange')
    version_label.place(x=10, y=190)
    location_label = Label(f4, bg="#20242f", fg='orange')
    location_label.place(x=10, y=230)
    install_date_label = Label(f4, bg="#20242f", fg='orange')
    install_date_label.place(x=10, y=270)
    publisher_label = Label(f4, bg="#20242f", fg='orange')
    publisher_label.place(x=10, y=310
                          )

    # Creating label for class variable
    # name using widget Entry
    Label(f4, text="", textvariable=name, bg="#20242f", fg='gold').place(x=150, y=150)
    Label(f4, text="", textvariable=version, bg="#20242f", fg='gold').place(x=150, y=190)
    Label(f4, text="", textvariable=location, bg="#20242f", fg='gold').place(x=150, y=230)
    Label(f4, text="", textvariable=Install_date, bg="#20242f", fg='gold').place(x=150, y=270)
    Label(f4, text="", textvariable=publisher, bg="#20242f", fg='gold').place(x=150, y=310)

    # creating a button using the widget
    show_button = Button(f4, text="Show", bg="#20242f", command=app, activebackground="#20242f", fg='white', activeforeground='white', cursor='hand2', bd=0)
    show_button.place(x=550, y=60)

    Button(lower_frame, text="Search file", bg="#181b23", command=open_file_searcher, activebackground="#20242f", fg='white', activeforeground='white', cursor='hand2', bd=0).place(x=10, y=3)

    def delete_f4():
        Frame(root, width=725, height=685, bg='#232733').place(x=600, y=300)
        bg_label_ = Label(root, image=background, bg="#232733")
        bg_label_.place(x=700, y=300)
        bg_label2 = Label(root, image=background2, bg="#232733")
        bg_label2.place(x=906, y=515)
        Label(root, text="HSR", bg="#232733", font="Papyrus 15", fg="#c38ae2").place(x=914, y=615)

        name.set("")
        version.set("")
        location.set("")
        Install_date.set("")
        publisher.set("")

        name_label.config(text="")
        version_label.config(text="")
        location_label.config(text="")
        install_date_label.config(text="Install ")
        publisher_label.config(text="")

        f4.destroy()

    Button(f4, text="Close", command=delete_f4, activebackground='#20242f', bg='#20242f', bd=0, cursor='hand2',fg='white', activeforeground='white').place(x=650, y=60)


# for opening file searcher
def open_file_searcher():
    Frame(root, width=720, height=685, bg='#232733').place(x=600, y=300)
    bg_label_ = Label(root, image=background, bg="#232733")
    bg_label_.place(x=700, y=300)
    bg_label2 = Label(root, image=background2, bg="#232733")
    bg_label2.place(x=906, y=515)
    Label(root, text="HSR", bg="#232733", font="Papyrus 15", fg="#c38ae2").place(x=914, y=615)
    os.startfile("A:\\My Projects\\Android Subsystem for Windows (Python)\\File Searcher\\file_searcher.pyw")


# creating search button
search_Image = PhotoImage(file="A:\\My Projects\\Android Subsystem for Windows (Python)\\main\\search_small.png")
Search = Button(bottom_frame, image=search_Image, bg='#161323', bd=0, relief=FLAT, activebackground='#161323', command=file_searcher_window)
Search.place(x=80, y=8)
Search.bind("<Enter>", change_search_pic)
Search.bind("<Leave>", change_back_search)


# ********** Designing system info button for task bar **********
# Open system info app with Hower image animation
def change_info_pic(e):
    my_pic = PhotoImage(file="A:\\My Projects\\Android Subsystem for Windows (Python)\\main\\system_info_large.png")
    Info.config(image=my_pic)
    Info.image = my_pic
    Info.place(x=140, y=0)


def change_back_info(e):
    my_pic = PhotoImage(file="A:\\My Projects\\Android Subsystem for Windows (Python)\\main\\system_info_small.png")
    Info.config(image=my_pic)
    Info.image = my_pic
    Info.place(x=150, y=8)


# creating system info button
info_Image = PhotoImage(file="A:\\My Projects\\Android Subsystem for Windows (Python)\\main\\system_info_small.png")
Info = Button(bottom_frame, image=info_Image, bg='#161323', bd=0, relief=FLAT, activebackground='#161323', command=opening_sys_info)
Info.place(x=150, y=8)
Info.bind("<Enter>", change_info_pic)
Info.bind("<Leave>", change_back_info)


# ********** Designing AI Assistant button for task bar **********
# Open AI Assistant with Hower image animation
def change_ai_assistant_pic(e):
    my_pic = PhotoImage(file="A:\\My Projects\\Android Subsystem for Windows (Python)\\main\\AI_Assistant_large.png")
    AI_Assistant.config(image=my_pic)
    AI_Assistant.image = my_pic
    AI_Assistant.place(x=210, y=0)


def change_back_ai_assistant(e):
    my_pic = PhotoImage(file="A:\\My Projects\\Android Subsystem for Windows (Python)\\main\\AI_Assistant_small.png")
    AI_Assistant.config(image=my_pic)
    AI_Assistant.image = my_pic
    AI_Assistant.place(x=220, y=8)


# Creating AI assistant button
AI_Image = PhotoImage(file="A:\\My Projects\\Android Subsystem for Windows (Python)\\main\\AI_Assistant_small.png")
AI_Assistant = Button(bottom_frame, image=AI_Image, command=opening_ai_assistant, bg='#161323', bd=0, relief=FLAT, activebackground='#161323')
AI_Assistant.place(x=220, y=8)
AI_Assistant.bind("<Enter>", change_ai_assistant_pic)
AI_Assistant.bind("<Leave>", change_back_ai_assistant)


# ********** Designing phone button for task bar **********
# Open phone app with Hower image animation
def change_phone_pic(e):
    my_pic = PhotoImage(file="A:\\My Projects\\Android Subsystem for Windows (Python)\\main\\phone_large.png")
    Phone.config(image=my_pic)
    Phone.image = my_pic
    Phone.place(x=280, y=0)


def change_back_phone(e):
    my_pic = PhotoImage(file="A:\\My Projects\\Android Subsystem for Windows (Python)\\main\\phone_small.png")
    Phone.config(image=my_pic)
    Phone.image = my_pic
    Phone.place(x=290, y=8)


# creating phone button
phone_Image = PhotoImage(file="A:\\My Projects\\Android Subsystem for Windows (Python)\\main\\phone_small.png")
Phone = Button(bottom_frame, image=phone_Image, bg='#161323', bd=0, relief=FLAT, activebackground='#161323', command=opening_phonebook)
Phone.place(x=290, y=8)
Phone.bind("<Enter>", change_phone_pic)
Phone.bind("<Leave>", change_back_phone)


# ********** Designing message button for task bar **********
# Open message app with Hower image animation
def change_message_pic(e):
    my_pic = PhotoImage(file="A:\\My Projects\\Android Subsystem for Windows (Python)\\main\\message_large.png")
    Message.config(image=my_pic)
    Message.image = my_pic
    Message.place(x=350, y=0)


def change_back_message(e):
    my_pic = PhotoImage(file="A:\\My Projects\\Android Subsystem for Windows (Python)\\main\\message_small.png")
    Message.config(image=my_pic)
    Message.image = my_pic
    Message.place(x=360, y=8)


# creating message button
message_Image = PhotoImage(file="A:\\My Projects\\Android Subsystem for Windows (Python)\\main\\message_small.png")
Message = Button(bottom_frame, image=message_Image, bg='#161323', bd=0, relief=FLAT, activebackground='#161323', command=opening_message)
Message.place(x=360, y=8)
Message.bind("<Enter>", change_message_pic)
Message.bind("<Leave>", change_back_message)


# ********** Designing google translator button for task bar **********
# Open Google Translator with Hower image animation
def change_google_translator_pic(e):
    my_pic = PhotoImage(file="A:\\My Projects\\Android Subsystem for Windows (Python)\\main\\Google-Translator_large.png")
    Google_Translator.config(image=my_pic)
    Google_Translator.image = my_pic
    Google_Translator.place(x=420, y=0)


def change_back_google_translator(e):
    my_pic = PhotoImage(file="A:\\My Projects\\Android Subsystem for Windows (Python)\\main\\Google-Translator_small.png")
    Google_Translator.config(image=my_pic)
    Google_Translator.image = my_pic
    Google_Translator.place(x=430, y=8)


# Creating google translator button
google_translator_Image = PhotoImage(file="A:\\My Projects\\Android Subsystem for Windows (Python)\\main\\Google-Translator_small.png")
Google_Translator = Button(bottom_frame, image=google_translator_Image, command=opening_google_translator, bg='#161323', bd=0, relief=FLAT, activebackground='#161323')
Google_Translator.place(x=430, y=8)
Google_Translator.bind("<Enter>", change_google_translator_pic)
Google_Translator.bind("<Leave>", change_back_google_translator)


# ********** Designing browser button for task bar **********
# Open browser with Hower image animation
def change_browser_pic(e):
    my_pic = PhotoImage(file="A:\\My Projects\\Android Subsystem for Windows (Python)\\main\\browser_large.png")
    Browser.config(image=my_pic)
    Browser.image = my_pic
    Browser.place(x=490, y=0)


def change_back_browser(e):
    my_pic = PhotoImage(file="A:\\My Projects\\Android Subsystem for Windows (Python)\\main\\browser_small.png")
    Browser.config(image=my_pic)
    Browser.image = my_pic
    Browser.place(x=500, y=8)


# creating browser button
browser_Image = PhotoImage(file="A:\\My Projects\\Android Subsystem for Windows (Python)\\main\\browser_small.png")
Browser = Button(bottom_frame, image=browser_Image, bg='#161323', bd=0, relief=FLAT, activebackground='#161323', command=opening_browser)
Browser.place(x=500, y=8)
Browser.bind("<Enter>", change_browser_pic)
Browser.bind("<Leave>", change_back_browser)


# ********** Designing file manager button for task bar **********
# Open file manager with Hower image animation
def change_file_explorer_pic(e):
    my_pic = PhotoImage(file="A:\\My Projects\\Android Subsystem for Windows (Python)\\main\\file_explorer_large.png")
    File_explorer.config(image=my_pic)
    File_explorer.image = my_pic
    File_explorer.place(x=560, y=0)


def change_back_file_explorer(e):
    my_pic = PhotoImage(file="A:\\My Projects\\Android Subsystem for Windows (Python)\\main\\file_explorer_small.png")
    File_explorer.config(image=my_pic)
    File_explorer.image = my_pic
    File_explorer.place(x=570, y=8)


# creating file manager button
file_explorer_Image = PhotoImage(file="A:\\My Projects\\Android Subsystem for Windows (Python)\\main\\file_explorer_small.png")
File_explorer = Button(bottom_frame, image=file_explorer_Image, bg='#161323', bd=0, relief=FLAT, activebackground='#161323', command=opening_file_manager)
File_explorer.place(x=570, y=8)
File_explorer.bind("<Enter>", change_file_explorer_pic)
File_explorer.bind("<Leave>", change_back_file_explorer)


# ********** Designing camera button for task bar **********
# Open camera app with Hower image animation
def change_camera_pic(e):
    my_pic = PhotoImage(file="A:\\My Projects\\Android Subsystem for Windows (Python)\\main\\camera_large.png")
    Camera.config(image=my_pic)
    Camera.image = my_pic
    Camera.place(x=630, y=0)


def change_back_camera(e):
    my_pic = PhotoImage(file="A:\\My Projects\\Android Subsystem for Windows (Python)\\main\\camera_small.png")
    Camera.config(image=my_pic)
    Camera.image = my_pic
    Camera.place(x=640, y=8)


# Creating camera button
camera_Image = PhotoImage(file="A:\\My Projects\\Android Subsystem for Windows (Python)\\main\\camera_small.png")
Camera = Button(bottom_frame, image=camera_Image, bg='#161323', bd=0, relief=FLAT, activebackground='#161323', command=opening_camera)
Camera.place(x=640, y=8)
Camera.bind("<Enter>", change_camera_pic)
Camera.bind("<Leave>", change_back_camera)


root.mainloop()
