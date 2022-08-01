# Importing useful packages
from tkinter import *
from tkinter.messagebox import showinfo, showerror
from twilio.rest import Client
from threading import Thread


# use threading
def threading_send_message():
    t1 = Thread(target=send_message)
    t1.start()


# function for sending message
def send_message():
    try:
        number = mobile_number.get()
        message = text_message.get(1.0, END)
        client = Client("Enter your twilio account SID here", "your twilio auth tokan")
        client.messages.create(to=number, from_="your twilio account number", body=message)
        showinfo("Message", "Message sent successfully!")
    except:
        showerror("Message", "Something went wrong or please check your internet connection!")


# Creating GUI
if __name__ == '__main__':
    root = Tk()
    root.geometry('800x500+250+100')
    root.title("Message")
    root.config(bg="#fafafa")
    root.wm_iconbitmap("A:\\My Projects\\Android Subsystem for Windows (Python)\\Message app\\message_logo.ico")

    top_frame = Frame(root, height=50, bg='#0a7bc9')
    top_frame.pack(side=TOP, fill=X)

    bottom_frame = Frame(root, height=30, bg='#f0f0f0', bd=2, relief=GROOVE)
    bottom_frame.pack(side=BOTTOM, fill=X, padx=(331, 18))

    Label(top_frame, text="My messaging", font=("Juice ITC", 25, 'bold'), bg="#0a7bc9", fg='white').pack()

    Label(root, text="Mobile Number", font="Aparajita 16", bg="#fafafa").pack(side=LEFT, padx=20, pady=20, anchor='nw')
    country_code = StringVar()
    mobile_number = Entry(width=14, font="Aparajita 16", textvariable=country_code, bd=2, relief=GROOVE)
    country_code.set("+91 ")
    mobile_number.pack(side=LEFT, padx=20, pady=20, anchor='nw')

    my_message = LabelFrame(root, text="Message", font="Georgia 12", bg='#fafafa', relief=RIDGE, bd=0.5)
    my_message.pack(padx=20, pady=(10, 0), fill=BOTH, expand=YES)

    text_message = Text(my_message, bg='white', font="Georgia 12", wrap=WORD, padx=10, pady=10)
    text_message.pack(fill=BOTH, expand=YES)

    Button(bottom_frame, text="Send", bg="#f0f0f0", bd=0, relief=FLAT, cursor='hand2', fg='dark blue', font=("default 10 bold"), command=threading_send_message).pack(side=RIGHT)

    root.mainloop()
