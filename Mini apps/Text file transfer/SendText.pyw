# Importing required packages
from tkinter import *
import socket
from tkinter import filedialog, messagebox
import os
from threading import Thread


# Creating main window
root = Tk()
root.geometry("400x580+450+20")
root.config(bg="#f0f0f0")
root.title("SendText")
root.resizable(False, False)
root.wm_iconbitmap("A:\\My Projects\\Android Subsystem for Windows (Python)\\Mini apps\\Text file transfer\\file_transfer.ico")


# function for sending file
def send():
    send_button.config(bg="#f0f0f0", activebackground="#f0f0f0")
    receive_button.config(bg="#fcfcfc", activebackground="#fcfcfc")

    my_frame = Frame(bottom_frame, width=376, height=366, bg='#ffffff')
    my_frame.place(x=0, y=0)

    lower_frame = Frame(my_frame, width=366, height=50, bg='#048cd1', highlightbackground='#e8e8e8', highlightthickness=2)
    lower_frame.place(x=5, y=311)

    share_info = Label(lower_frame, text="Share text file", font=("Bahnschrift Light Condensed", 20), bg="#048cd1", fg='white')
    share_info.place(x=10, y=3)

    # opening filedialog box
    def select_file():
        global filename
        filename = filedialog.askopenfilename(initialdir=os.getcwd(), title="Select File", filetypes=(("Text file", "*.txt"), ("Music", "*.mp3"), ("All Files", "*.*")))

    # threading in sender method
    def threading_sender():
        t1 = Thread(target=sender)
        t1.start()

    # function for sending selected file
    def sender():
        try:
            s = socket.socket()
            hosting = socket.gethostname()
            port = 8080
            s.bind((hosting, port))
            s.listen(1)
            share_info.config(text="Waiting for any incoming connection")
            conn, addr = s.accept()
            file = open(filename, 'rb')
            file_data = file.read(1024)
            share_info.config(text="Sending...")
            conn.send(file_data)
            messagebox.showinfo("Share", "Data has been transmitted successfully!")
            share_info.config(text="Share text file")
        except:
            messagebox.showerror("Share", "Something went wrong!")
            share_info.config(text="Share text file")

    host = socket.gethostname()
    Label(my_frame, text=f"ID- {host}", font=("Bahnschrift Light Condensed", 25), bg="#fafafa", highlightbackground='#f0f0f0', highlightthickness=2, fg='dark blue').place(x=85, y=15)

    Button(my_frame, text="+ Select file", width=10, font=("Bahnschrift Light Condensed", 20), bg="#ffffff", activebackground="#ffffff", bd=1, relief=FLAT, cursor='hand2', fg='dark green', activeforeground='dark green', overrelief=GROOVE, command=select_file).place(x=130, y=120)
    Button(my_frame, text="SEND", width=8, font=("Bahnschrift Light Condensed", 20), bg="#ffffff", activebackground="#ffffff", bd=1, relief=FLAT, cursor='hand2', fg='green', activeforeground='dark green', overrelief=GROOVE, command=threading_sender).place(x=140, y=180)


# function for receiving file
def receive():
    send_button.config(bg="#fcfcfc", activebackground="#fcfcfc")
    receive_button.config(bg="#f0f0f0", activebackground="#f0f0f0")

    my_frame = Frame(bottom_frame, width=376, height=366, bg='#ffffff')
    my_frame.place(x=0, y=0)

    lower_frame = Frame(my_frame, width=366, height=50, bg='#048cd1', highlightbackground='#e8e8e8', highlightthickness=2)
    lower_frame.place(x=5, y=311)

    receive_info = Label(lower_frame, text="Receive text file", font=("Bahnschrift Light Condensed", 20), bg="#048cd1", fg='white')
    receive_info.place(x=10, y=3)

    if not os.path.exists("A:\\My Projects\\Android Subsystem for Windows (Python)\\Mini apps\\Text file transfer\\Received"):
        os.mkdir("A:\\My Projects\\Android Subsystem for Windows (Python)\\Mini apps\\Text file transfer\\Received")

    # threading in receiver method
    def threading_receiver():
        t1 = Thread(target=receiver)
        t1.start()

    # function for receiving file
    def receiver():
        try:
            ID = senderID.get()
            filename1 = incoming_file.get()

            s = socket.socket()
            receive_info.config(text="Receiving...")
            port = 8080
            s.connect((ID, port))
            file = open(f"A:\\My Projects\\Android Subsystem for Windows (Python)\\Mini apps\\Text file transfer\\Received\\{filename1}", 'wb')
            file_data = s.recv(1024)
            file.write(file_data)
            file.close()
            messagebox.showinfo("Share", "File has been received successfully!")
            receive_info.config(text="Receive text file")
        except:
            messagebox.showerror("Error", "Something went wrong!")
            receive_info.config(text="Receive text file")

    Label(my_frame, text='Sender ID', font=("Bahnschrift Light Condensed", 20), bg="#ffffff").place(x=20, y=50)
    senderID = Entry(my_frame, width=20, bd=0, relief=FLAT, font=("Bahnschrift Light Condensed", 20), highlightcolor='#00aaff', highlightthickness=1, highlightbackground='black')
    senderID.place(x=130, y=50)
    senderID.focus()

    Label(my_frame, text='File name', font=("Bahnschrift Light Condensed", 20), bg="#ffffff").place(x=20, y=100)
    incoming_file = Entry(my_frame, width=20, bd=0, relief=FLAT, font=("Bahnschrift Light Condensed", 20), highlightcolor='#00aaff', highlightthickness=1, highlightbackground='black')
    incoming_file.place(x=130, y=100)

    Button(my_frame, text="Receive", font=("Bahnschrift Light Condensed", 20), bd=1, relief=SOLID, overrelief=GROOVE, width=15, height=1, bg="#fafafa", activebackground="#fafafa", command=threading_receiver).place(x=100, y=195)


top_frame = Frame(root, width=380, height=180, bg='#ffffff', highlightbackground='#e8e8e8', highlightthickness=2)
top_frame.place(x=10, y=10)

bottom_frame = Frame(root, width=380, height=370, bg='#ffffff', highlightbackground='#e8e8e8', highlightthickness=2, highlightcolor="#e8e8e8")
bottom_frame.place(x=10, y=200)

# loading button icons
send_icon = PhotoImage(file="A:\\My Projects\\Android Subsystem for Windows (Python)\\Mini apps\\Text file transfer\\send.png")
receive_icon = PhotoImage(file="A:\\My Projects\\Android Subsystem for Windows (Python)\\Mini apps\\Text file transfer\\receive.png")

send_button = Button(top_frame, text="Send", image=send_icon, width=165, height=150, compound=TOP, font=("Bahnschrift Light Condensed", 25), command=send, bd=2, relief=GROOVE, overrelief=RIDGE, bg="#f0f0f0", activebackground="#f0f0f0")
send_button.place(x=9, y=9)

receive_button = Button(top_frame, text="Receive", image=receive_icon, width=165, height=150, compound=TOP, font=("Bahnschrift Light Condensed", 25), command=receive, bd=2, relief=GROOVE, overrelief=RIDGE, bg="#fcfcfc", activebackground="#fcfcfc")
receive_button.place(x=194, y=9)

# calling send function
send()

root.mainloop()
