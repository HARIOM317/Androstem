# Import useful libraries
from tkinter import *
from tkinter.messagebox import *
from threading import *
import speedtest


# handle threading of check_speed function
def Threading():
    try:
        t1 = Thread(target=check_speed)
        t1.start()
    except:
        showerror("Internet speed tester", "Something went wrong!")


# create check_speed function to check the internet uploading and downloading speed
def check_speed():
    try:
        label.config(text="Calculating...")
        test = speedtest.Speedtest()    # Calling Speedtest() function
        # For uploading speed
        Uploading_speed = round(test.upload()/(1024*1024), 2)
        upload.config(text=Uploading_speed)
        # For downloading speed
        Downloading_speed = round(test.download()/(1024*1024), 2)
        download.config(text=Downloading_speed)
        Downloading.config(text=Downloading_speed)
        # for ping address
        servernames = []
        test.get_servers(servernames)
        ping.config(text=test.results.ping)
        label.config(text="")
    except Exception as e:
        # Show if device is not connect throw internet
        showerror("Internet Speed Tester", "Something happened wrong!")
        label.config(text="")


if __name__ == '__main__':
    # Creating window
    root = Tk()
    root.title("Internet Speed Testing Tool")
    root.geometry('360x600+500+10')
    root.resizable(False, False)
    root.attributes('-alpha', 0.99)
    root.config(bg="#0f111a")
    root.wm_iconbitmap("A:\\My Projects\Android Subsystem for Windows (Python)\\Internet Speed Tester\\speed_tester_logo.ico")

    # create a top frame
    topFrame = Frame(root, bg='#101421')
    topFrame.pack(side=TOP, fill=X, anchor='ne')
    # loading the box image in Top variable
    Top = PhotoImage(file='A:\\My Projects\Android Subsystem for Windows (Python)\\Internet Speed Tester\\box.png')
    # Creating labels for set the top image
    Label(topFrame, image=Top, bg="#101421").pack(side=LEFT, anchor='ne', padx=10, pady=20)
    Label(topFrame, image=Top, bg="#101421").pack(side=LEFT, anchor='ne', padx=25, pady=20)
    Label(topFrame, image=Top, bg="#101421").pack(side=LEFT, anchor='ne', padx=10, pady=20)
    # Create labels for set the words
    Label(topFrame, text="PING", font="arial 10 bold", bg='#101421', fg='#7FFFD4').place(x=35, y=5)
    Label(topFrame, text="DOWNLOAD", font="arial 10 bold", bg='#101421', fg='#7FFFD4').place(x=138, y=5)
    Label(topFrame, text="UPLOAD", font="arial 10 bold", bg='#101421', fg='#7FFFD4').place(x=273, y=5)
    # create labels for set the units
    Label(topFrame, text="MS", font="arial 8 bold", bg="#101421", fg='#F5F5DC').place(x=44, y=70)
    Label(topFrame, text="MBPS", font="arial 8 bold", bg="#101421", fg='#F5F5DC').place(x=162, y=70)
    Label(topFrame, text="MBPS", font="arial 8 bold", bg="#101421", fg='#F5F5DC').place(x=285, y=70)
    # create label for showing the ping address
    ping = Label(topFrame, text="00", font="arial 8 bold", bg="#101421", fg='#FAF0BE')
    ping.place(x=55, y=60, anchor=CENTER)
    # create label for showing the downloading speed
    download = Label(topFrame, text="00", font="arial 8 bold", bg="#101421", fg='#FAF0BE')
    download.place(x=180, y=60, anchor=CENTER)
    # create label for showing the uploading speed
    upload = Label(topFrame, text="00", font="arial 8 bold", bg="#101421", fg='#FAF0BE')
    upload.place(x=303, y=60, anchor=CENTER)

    # loading main speed image
    main_image = PhotoImage(file='A:\\My Projects\Android Subsystem for Windows (Python)\\Internet Speed Tester\\speed.png')
    Label(root, image=main_image, bg='#0f111a').place(x=10, y=130)
    # Creating labels for set Downloading and MBPS words
    Label(root, text="Downloading", font=("Bahnschrift Light Condensed", 23, 'bold'), bg="#0f111a", fg='light blue').place(x=107, y=315)
    Label(root, text="MBPS", font="Gabriola 16 bold", bg="#0f111a", fg='light blue').place(x=160, y=425)

    # create label for showing the main downloading speed
    Downloading = Label(root, text="00", font="arial 30 bold", bg="#0f111a", fg='#08E8DE')
    Downloading.place(x=185, y=395, anchor=CENTER)

    # create label for showing its process to calculate internet speed
    label = Label(root, fg='orange', bg='#0f111a', font=("Monotype Corsiva", 16), text="")
    label.place(x=130, y=565)

    # Create a button to start testing the internet speed
    button = Button(root, text="Start", fg='white', bg='#11131d', font=15, cursor='hand2', command=Threading, pady=5, padx=5, activeforeground='alice blue', activebackground="#171927", bd=2, relief=RIDGE)
    button.place(x=150, y=510)

    root.mainloop()