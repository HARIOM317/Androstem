# Importing useful packages
from tkinter import *
import qrcode
from tkinter import filedialog, messagebox
import cv2
from pyzbar.pyzbar import decode
import webbrowser
import validators
import os


# creating help function to show information messagebox for tips
def help():
    messagebox.showinfo("Help", "Click on Create QR Code and select any particular type to create a QR Code and use scan to browse an image for scanning QR Code\n\nNOTE: create black qr code with white backgroung for a better experience")


# creating close function for closing the open frame
def close():
    sc_frame = Frame(root, bg='#495A69', width=500, height=450)
    sc_frame.place(x=120, y=87)


# Creating email_Validator function to check that given email address is valid or not
def email_Validator(Email_Address):
    # creating some variables and initialize them with 0
    j = 0
    k = 0
    l = 0
    # Check if length of email is 0 or not
    if len(Email_Address) == 0:
        pass
    # Check if length of email is more than or equal to 6 or not
    elif len(Email_Address) >= 6:
        # Check that first character of email is an alphabet or not
        if Email_Address[0].isalpha():
            # Check that '@' character is present in email and number of @ symbol is 1 or not
            if ("@" in Email_Address) and (Email_Address.count('@') == 1):
                # Checking the position of '.'
                if (Email_Address[-4] == '.') ^ (Email_Address[-3] == '.'):
                    # Checking more conditions for a valid email address
                    for i in Email_Address:
                        if i == i.isspace():
                            j = 1
                        elif i.isalpha():
                            if i == i.upper():
                                k = 1
                        elif i.isdigit():
                            continue
                        elif i == "_" or i == "." or i == "@":
                            continue
                        else:
                            l = 1
                    # Show error messagebox if get value of j, k, or l is 1
                    if j == 1 or k == 1 or l == 1:
                        messagebox.showerror("Email Validator", "Invalid Email Address")
                else:
                    # Show error messagebox if position of '.' is not correct
                    messagebox.showerror("Email Validator", "Invalid Email \n'.' Position is not correct")
            else:
                # Show error messagebox if only one @ symbol is not present in email
                messagebox.showerror("Email Validator", "Invalid Email \nOne '@' symbol required!")
        else:
            # Show error messagebox if first character of email is not an alphabet
            messagebox.showerror("Email Validator", "Invalid Email \nFirst character of email should be an alphabet")
    else:
        # Show error messagebox if length of email address is less than 6 or not 0
        messagebox.showerror("Email Validator", "Invalid Email \nLength of email should be more than equal to 6")


# Creating scan_image function to open a qr code image for scanning
def scan_image():
    # Creating a frame
    sc_frame = Frame(root, bg='white', width=500, height=450)
    sc_frame.place(x=120, y=87)
    # Create button to open an image and scan them
    Button(sc_frame, text="Browse QR Code", command=scan, cursor='hand2', padx=5, font=("Gabriola", 25), fg="#ff5b00", bg='white', bd=0, relief=RIDGE, activeforeground='#b23f00', activebackground='white').place(x=150, y=380)
    global my_text
    my_text = StringVar()
    # Show a message if the image is not opened
    myMessage = Message(sc_frame, textvariable=my_text, padx=10, pady=10, width=400, font=("Gabriola", 16), fg='dark blue', bg='white')
    myMessage.place(x=10, y=20)


# Creating scan function to scan qr code
def scan():
    try:
        # Open file dialog box to select an image
        file = filedialog.askopenfilename(title="Select QR Code", filetypes=(("png file", "*.png"), ("All files", "*.*")))
        img = cv2.imread(file)
        # Decoding the image
        for barcode in decode(img):
            myData = barcode.data.decode('utf-8')
            valid = validators.url(myData)
            if valid == True:
                # If an url is present in qr code, and also it's valid then open it in web browser and set url on screen
                webbrowser.open(myData)
                my_text.set(myData)
            else:
                # If an url is not valid, but it is an url and present in qr code than open it in web browser and set url on screen
                if myData.endswith('.com') or myData.endswith('.in') or myData.endswith('.org'):
                    webbrowser.open(myData)
                my_text.set(myData)
        # Show qr code on window
        global Image
        Image = PhotoImage(file=file)
        Image_view.config(image=Image)
    except Exception as e:
        messagebox.showinfo("Open QR Code", "No such image found!")


# Creating my_r function to create my qr code
def my_qr():
    qr_frame = Frame(root, bg='white', width=500, height=450)
    qr_frame.place(x=120, y=87)

    global my_title
    Label(qr_frame, text="QR Code Name", fg='black', bg='white', font=("Javanese Text", 15, 'italic')).place(x=10, y=0)
    my_title = Entry(qr_frame, width=30, font=("Cambria", 15, 'italic'), relief=GROOVE, bd=2, fg='dark blue')
    my_title.place(x=150, y=10)

    global full_name
    Label(qr_frame, text="Full Name", fg='black', bg='white', font=("Javanese Text", 15, 'italic')).place(x=10, y=40)
    full_name = Entry(qr_frame, width=30, font=("Cambria", 15, 'italic'), relief=GROOVE, bd=2, fg='dark blue')
    full_name.place(x=150, y=50)

    global organization
    Label(qr_frame, text="Organization", fg='black', bg='white', font=("Javanese Text", 15, 'italic')).place(x=10, y=80)
    organization = Entry(qr_frame, width=30, font=("Cambria", 15, 'italic'), relief=GROOVE, bd=2, fg='dark blue')
    organization.place(x=150, y=90)

    global address
    Label(qr_frame, text="Address", fg='black', bg='white', font=("Javanese Text", 15, 'italic')).place(x=10, y=120)
    address = Entry(qr_frame, width=30, font=("Cambria", 15, 'italic'), relief=GROOVE, bd=2, fg='dark blue')
    address.place(x=150, y=130)

    global phone
    Label(qr_frame, text="Phone", fg='black', bg='white', font=("Javanese Text", 15, 'italic')).place(x=10, y=160)
    phone = Entry(qr_frame, width=30, font=("Cambria", 15, 'italic'), relief=GROOVE, bd=2, fg='dark blue')
    phone.place(x=150, y=170)

    global email
    Label(qr_frame, text="Email", fg='black', bg='white', font=("Javanese Text", 15, 'italic')).place(x=10, y=200)
    email = Entry(qr_frame, width=30, font=("Cambria", 15, 'italic'), relief=GROOVE, bd=2, fg='dark blue')
    email.place(x=150, y=210)

    global notes
    Label(qr_frame, text="Notes", fg='black', bg='white', font=("Javanese Text", 15, 'italic')).place(x=10, y=240)
    notes = Text(qr_frame, width=30, height=5, font=("Cambria", 15, 'italic'), relief=GROOVE, bd=2, fg='dark blue', wrap=WORD)
    notes.place(x=150, y=250)

    Button(qr_frame, text="Generate", bg='white', fg='dark red', command=generate_my_qr, font=("Monotype Corsiva", 30), bd=0, activeforeground='orange', activebackground='white', cursor='hand2').place(x=180, y=370)


# Generating my qr code
def generate_my_qr():
    # Get values of all entry widgets of my_qr function
    file_name = my_title.get()
    name = full_name.get()
    org = organization.get()
    add = address.get()
    contact = phone.get()
    email_address = email.get()
    my_notes = notes.get(1.0, END)
    qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_H, box_size=6, border=2)

    # Adding data in qr code
    qr.add_data(name+"\n")
    qr.add_data(org+"\n")
    qr.add_data(add+"\n")
    if contact.isnumeric() and len(contact) == 10 or len(contact) == 0:
        qr.add_data(contact+"\n")
    else:
        messagebox.showerror("Phone Number", "Invalid Phone Number")
    if email_Validator(email_address):
        qr.add_data(email_address + "\n")
    qr.add_data(email_address + "\n")
    qr.add_data(my_notes)
    # Make and save the qr code image
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save("A:\\My Projects\\Android Subsystem for Windows (Python)\\QR Code\\QR Code Generator\\"+str(file_name)+".png")
    # Show qr code on the screen
    global Image
    Image = PhotoImage(file="A:\\My Projects\\Android Subsystem for Windows (Python)\\QR Code\\QR Code Generator\\"+str(file_name)+".png")
    Image_view.config(image=Image)


# Creating generate_qr function to set the buttons for creating several types of qr code
def generate_qr():
    qr_frame = Frame(root, bg='white', width=500, height=450)
    qr_frame.place(x=120, y=87)

    Button(qr_frame, text="URL", padx=10, width=32, font=("Monotype Corsiva", 20), relief=RIDGE, bd=2, bg='#EBEBFF', activebackground='#EBEBFF', activeforeground='dark blue', command=url, fg='black', cursor='hand2').place(x=11, y=30)
    Button(qr_frame, text="Text", padx=10, width=32, font=("Monotype Corsiva", 20), relief=RIDGE, bd=2, bg='#e6e6ff', activebackground='#e6e6ff', activeforeground='dark blue', command=text, fg='black', cursor='hand2').place(x=11, y=85)
    Button(qr_frame, text="Contact", padx=10, width=32, font=("Monotype Corsiva", 20), relief=RIDGE, bd=2, bg='#EBEBFF', activebackground='#EBEBFF', activeforeground='dark blue', command=my_qr, fg='black', cursor='hand2').place(x=11, y=140)
    Button(qr_frame, text="Email", padx=10, width=32, font=("Monotype Corsiva", 20), relief=RIDGE, bd=2, bg='#e6e6ff', activebackground='#e6e6ff', activeforeground='dark blue', command=my_email, fg='black', cursor='hand2').place(x=11, y=195)
    Button(qr_frame, text="Phone", padx=10, width=32, font=("Monotype Corsiva", 20), relief=RIDGE, bd=2, bg='#EBEBFF', activebackground='#EBEBFF', activeforeground='dark blue', command=contact, fg='black', cursor='hand2').place(x=11, y=250)
    Button(qr_frame, text="Wifi", padx=10, width=32, font=("Monotype Corsiva", 20), relief=RIDGE, bd=2, bg='#e6e6ff', activebackground='#e6e6ff', activeforeground='dark blue', command=wifi, fg='black', cursor='hand2').place(x=11, y=305)
    Button(qr_frame, text="My QR", padx=10, width=32, font=("Monotype Corsiva", 20), relief=RIDGE, bd=2, bg='#EBEBFF', activebackground='#EBEBFF', activeforeground='dark blue', command=my_qr, fg='black', cursor='hand2').place(x=11, y=360)


# Creating url function to create qr code for a URL
def url():
    qr_frame = Frame(root, bg='white', width=500, height=450)
    qr_frame.place(x=120, y=87)

    global title
    Label(qr_frame, text="Title", fg='dark red', bg='white', font=("Javanese Text", 15, 'italic')).place(x=10, y=40)
    title = Entry(qr_frame, width=33, font='Georgia 13 italic', justify=CENTER, relief=GROOVE, bd=2, fg='dark blue')
    title.place(x=150, y=50)

    global entry
    Label(qr_frame, text="URL", fg='dark red', bg='white', font=("Javanese Text", 15, 'italic')).place(x=10, y=90)
    entry = Entry(qr_frame, width=33, font='Georgia 13 italic', justify=CENTER, relief=GROOVE, bd=2, fg='dark blue')
    entry.place(x=150, y=100)

    global foreground
    f_color = StringVar()
    Label(qr_frame, text="Foreground", fg='dark red', bg='white', font=("Javanese Text", 15, 'italic')).place(x=10, y=140)
    foreground = Entry(qr_frame, width=33, font="Georgia 13 italic", textvariable=f_color, justify=CENTER, relief=GROOVE, bd=2, fg='dark blue')
    f_color.set("black")
    foreground.place(x=150, y=150)

    global background
    b_color = StringVar()
    Label(qr_frame, text="Background", fg='dark red', bg='white', font=("Javanese Text", 15, 'italic')).place(x=10, y=190)
    background = Entry(qr_frame, width=33, font="Georgia 13 italic", textvariable=b_color, justify=CENTER, relief=GROOVE, bd=2, fg='dark blue')
    b_color.set("white")
    background.place(x=150, y=200)

    global border
    qr_border = IntVar()
    Label(qr_frame, text="Border", fg='dark red', bg='white', font=("Javanese Text", 15, 'italic')).place(x=10, y=240)
    border = Entry(qr_frame, width=33, font="Georgia 13 italic", justify=CENTER, relief=GROOVE, bd=2, textvariable=qr_border, fg='dark blue')
    qr_border.set(2)
    border.place(x=150, y=250)

    Button(qr_frame, text="Generate", bg='white', fg='dark red', command=generate_url, font=("Monotype Corsiva", 30), bd=0, activebackground='white', activeforeground='orange', cursor='hand2').place(x=180, y=350)


# Generating a qr code for url
def generate_url():
    name = title.get()
    text = entry.get()
    bd = border.get()

    qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_H, box_size=6, border=bd)

    if validators.url(text) or text.endswith('.com') or text.endswith('.in') or text.endswith('.org'):
        qr.add_data(text)
    else:
        messagebox.showerror("URL Validator", "Invalid URL")

    qr.make(fit=True)
    fg_color = foreground.get()
    bg_color = background.get()

    img = qr.make_image(fill_color=fg_color, back_color=bg_color)
    img.save("A:\\My Projects\\Android Subsystem for Windows (Python)\\QR Code\\QR Code Generator\\"+str(name)+".png")

    global Image
    Image = PhotoImage(file="A:\\My Projects\\Android Subsystem for Windows (Python)\\QR Code\\QR Code Generator\\"+str(name)+".png")
    Image_view.config(image=Image)


# Creating email function to create qr code for an email address
def my_email():
    qr_frame = Frame(root, bg='white', width=500, height=450)
    qr_frame.place(x=120, y=87)

    global title
    Label(qr_frame, text="QR Name", fg='dark red', bg='white', font=("Javanese Text", 15, 'italic')).place(x=10, y=40)
    title = Entry(qr_frame, width=33, font='Georgia 13 italic', justify=CENTER, relief=GROOVE, bd=2, fg='dark blue')
    title.place(x=150, y=50)

    global entry
    Label(qr_frame, text="Email Address", fg='dark red', bg='white', font=("Javanese Text", 15, 'italic')).place(x=10, y=90)
    entry = Entry(qr_frame, width=33, font='Georgia 13 italic', justify=CENTER, relief=GROOVE, bd=2, fg='dark blue')
    entry.place(x=150, y=100)

    global foreground
    f_color = StringVar()
    Label(qr_frame, text="Foreground", fg='dark red', bg='white', font=("Javanese Text", 15, 'italic')).place(x=10, y=140)
    foreground = Entry(qr_frame, width=33, font="Georgia 13 italic", textvariable=f_color, justify=CENTER, relief=GROOVE, bd=2, fg='dark blue')
    f_color.set("black")
    foreground.place(x=150, y=150)

    global background
    b_color = StringVar()
    Label(qr_frame, text="Background", fg='dark red', bg='white', font=("Javanese Text", 15, 'italic')).place(x=10, y=190)
    background = Entry(qr_frame, width=33, font="Georgia 13 italic", textvariable=b_color, justify=CENTER, relief=GROOVE, bd=2, fg='dark blue')
    b_color.set("white")
    background.place(x=150, y=200)

    global border
    qr_border = IntVar()
    Label(qr_frame, text="Border", fg='dark red', bg='white', font=("Javanese Text", 15, 'italic')).place(x=10, y=240)
    border = Entry(qr_frame, width=33, font="Georgia 13 italic", justify=CENTER, relief=GROOVE, bd=2, textvariable=qr_border, fg='dark blue')
    qr_border.set(2)
    border.place(x=150, y=250)

    Button(qr_frame, text="Generate", bg='white', fg='dark red', command=generate_email, font=("Monotype Corsiva", 30), bd=0, activebackground='white', activeforeground='orange', cursor='hand2').place(x=180, y=350)


# Generating a qr code for email address
def generate_email():
    name = title.get()
    text = entry.get()
    bd = border.get()

    qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_H, box_size=6, border=bd)

    if email_Validator(text):
        qr.add_data(text)
    qr.add_data(text)

    qr.make(fit=True)
    fg_color = foreground.get()
    bg_color = background.get()

    img = qr.make_image(fill_color=fg_color, back_color=bg_color)
    img.save("A:\\My Projects\\Android Subsystem for Windows (Python)\\QR Code\\QR Code Generator\\"+str(name)+".png")

    global Image
    Image = PhotoImage(file="A:\\My Projects\\Android Subsystem for Windows (Python)\\QR Code\\QR Code Generator\\"+str(name)+".png")
    Image_view.config(image=Image)


# Creating text function to create qr code for text
def text():
    qr_frame = Frame(root, bg='white', width=500, height=450)
    qr_frame.place(x=120, y=87)

    global title
    Label(qr_frame, text="Title", fg='dark red', bg='white', font=("Javanese Text", 15, 'italic')).place(x=10, y=40)
    title = Entry(qr_frame, width=33, font='Georgia 13 italic', justify=CENTER, relief=GROOVE, bd=2, fg='dark blue')
    title.place(x=150, y=50)

    global text_entry
    Label(qr_frame, text="Text", fg='dark red', bg='white', font=("Javanese Text", 15, 'italic')).place(x=10, y=90)
    text_entry = Text(qr_frame, width=33, height=6, font='Georgia 13 italic', wrap=WORD, relief=GROOVE, bd=2, fg='dark blue')
    text_entry.place(x=150, y=100)

    global foreground
    f_color = StringVar()
    Label(qr_frame, text="Foreground", fg='dark red', bg='white', font=("Javanese Text", 15, 'italic')).place(x=10, y=240)
    foreground = Entry(qr_frame, width=33, font="Georgia 13 italic", textvariable=f_color, justify=CENTER, relief=GROOVE, bd=2, fg='dark blue')
    f_color.set("black")
    foreground.place(x=150, y=250)

    global background
    b_color = StringVar()
    Label(qr_frame, text="Background", fg='dark red', bg='white', font=("Javanese Text", 15, 'italic')).place(x=10, y=290)
    background = Entry(qr_frame, width=33, font="Georgia 13 italic", textvariable=b_color, justify=CENTER, relief=GROOVE, bd=2, fg='dark blue')
    b_color.set("white")
    background.place(x=150, y=300)

    global border
    qr_border = IntVar()
    Label(qr_frame, text="Border", fg='dark red', bg='white', font=("Javanese Text", 15, 'italic')).place(x=10, y=340)
    border = Entry(qr_frame, width=33, font="Georgia 13 italic", justify=CENTER, relief=GROOVE, bd=2, textvariable=qr_border, fg='dark blue')
    qr_border.set(1)
    border.place(x=150, y=350)

    Button(qr_frame, text="Generate", bg='white', fg='dark red', command=generate_text, font=("Monotype Corsiva", 30), bd=0, activebackground='white', activeforeground='orange', cursor='hand2').place(x=180, y=380)


# Generating a qr code for text
def generate_text():
    name = title.get()
    text = text_entry.get(1.0, END)
    bd = border.get()

    qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_H, box_size=5, border=bd)

    qr.add_data(text)

    qr.make(fit=True)
    fg_color = foreground.get()
    bg_color = background.get()

    img = qr.make_image(fill_color=fg_color, back_color=bg_color)
    img.save("A:\\My Projects\\Android Subsystem for Windows (Python)\\QR Code\\QR Code Generator\\"+str(name)+".png")

    global Image
    Image = PhotoImage(file="A:\\My Projects\\Android Subsystem for Windows (Python)\\QR Code\\QR Code Generator\\"+str(name)+".png")
    Image_view.config(image=Image)

# Creating contact function to create qr code for contact
def contact():
    qr_frame = Frame(root, bg='white', width=500, height=450)
    qr_frame.place(x=120, y=87)

    global title
    Label(qr_frame, text="Contact Name", fg='dark red', bg='white', font=("Javanese Text", 15, 'italic')).place(x=10, y=40)
    title = Entry(qr_frame, width=33, font='Georgia 13 italic', justify=CENTER, relief=GROOVE, bd=2, fg='dark blue')
    title.place(x=150, y=50)

    global entry
    Label(qr_frame, text="Phone", fg='dark red', bg='white', font=("Javanese Text", 15, 'italic')).place(x=10, y=90)
    entry = Entry(qr_frame, width=33, font='Georgia 13 italic', justify=CENTER, relief=GROOVE, bd=2, fg='dark blue')
    entry.place(x=150, y=100)

    global foreground
    f_color = StringVar()
    Label(qr_frame, text="Foreground", fg='dark red', bg='white', font=("Javanese Text", 15, 'italic')).place(x=10, y=140)
    foreground = Entry(qr_frame, width=33, font="Georgia 13 italic", textvariable=f_color, justify=CENTER, relief=GROOVE, bd=2, fg='dark blue')
    f_color.set("black")
    foreground.place(x=150, y=150)

    global background
    b_color = StringVar()
    Label(qr_frame, text="Background", fg='dark red', bg='white', font=("Javanese Text", 15, 'italic')).place(x=10, y=190)
    background = Entry(qr_frame, width=33, font="Georgia 13 italic", textvariable=b_color, justify=CENTER, relief=GROOVE, bd=2, fg='dark blue')
    b_color.set("white")
    background.place(x=150, y=200)

    global border
    qr_border = IntVar()
    Label(qr_frame, text="Border", fg='dark red', bg='white', font=("Javanese Text", 15, 'italic')).place(x=10, y=240)
    border = Entry(qr_frame, width=33, font="Georgia 13 italic", justify=CENTER, relief=GROOVE, bd=2, textvariable=qr_border, fg='dark blue')
    qr_border.set(2)
    border.place(x=150, y=250)

    Button(qr_frame, text="Generate", bg='white', fg='dark red', command=generate_contact, font=("Monotype Corsiva", 30), bd=0, activebackground='white', activeforeground='orange', cursor='hand2').place(x=180, y=350)


# Generating a qr code for contact
def generate_contact():
    try:
        name = title.get()
        text = entry.get()
        bd = border.get()

        qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_H, box_size=6, border=bd)

        if len(text) == 0:
            messagebox.showinfo("Contact", "Phone number required")

        elif text.isnumeric() and len(text) == 10:
            qr.add_data(name + "\n")
            qr.add_data(text)

            qr.make(fit=True)
            fg_color = foreground.get()
            bg_color = background.get()

            img = qr.make_image(fill_color=fg_color, back_color=bg_color)
            img.save("A:\\My Projects\\Android Subsystem for Windows (Python)\\QR Code\\QR Code Generator\\" + str(name) + ".png")

            global Image
            Image = PhotoImage(file="A:\\My Projects\\Android Subsystem for Windows (Python)\\QR Code\\QR Code Generator\\" + str(name) + ".png")
            Image_view.config(image=Image)

        else:
            messagebox.showerror("Contact QR Code", "Invalid phone number!")

    except Exception as e:
        messagebox.showerror("QR Code Error", "Something went wrong!")


# Creating wifi() function to create qr code for Wi-Fi
def wifi():
    qr_frame = Frame(root, bg='white', width=500, height=450)
    qr_frame.place(x=120, y=87)

    global title
    Label(qr_frame, text="QR Name", fg='dark red', bg='white', font=("Javanese Text", 15, 'italic')).place(x=10, y=40)
    title = Entry(qr_frame, width=33, font='Georgia 13 italic', justify=CENTER, relief=GROOVE, bd=2, fg='dark blue')
    title.place(x=150, y=50)

    global wifi_name
    Label(qr_frame, text="Wi Fi Name", fg='dark red', bg='white', font=("Javanese Text", 15, 'italic')).place(x=10, y=90)
    wifi_name = Entry(qr_frame, width=33, font='Georgia 13 italic', justify=CENTER, relief=GROOVE, bd=2, fg='dark blue')
    wifi_name.place(x=150, y=100)

    global password
    Label(qr_frame, text="Password", fg='dark red', bg='white', font=("Javanese Text", 15, 'italic')).place(x=10, y=140)
    password = Entry(qr_frame, width=33, font='Georgia 13 italic', justify=CENTER, relief=GROOVE, bd=2, fg='dark blue')
    password.place(x=150, y=150)

    global foreground
    f_color = StringVar()
    Label(qr_frame, text="Foreground", fg='dark red', bg='white', font=("Javanese Text", 15, 'italic')).place(x=10, y=190)
    foreground = Entry(qr_frame, width=33, font="Georgia 13 italic", textvariable=f_color, justify=CENTER, relief=GROOVE, bd=2, fg='dark blue')
    f_color.set("black")
    foreground.place(x=150, y=200)

    global background
    b_color = StringVar()
    Label(qr_frame, text="Background", fg='dark red', bg='white', font=("Javanese Text", 15, 'italic')).place(x=10, y=240)
    background = Entry(qr_frame, width=33, font="Georgia 13 italic", textvariable=b_color, justify=CENTER, relief=GROOVE, bd=2, fg='dark blue')
    b_color.set("white")
    background.place(x=150, y=250)

    global border
    qr_border = IntVar()
    Label(qr_frame, text="Border", fg='dark red', bg='white', font=("Javanese Text", 15, 'italic')).place(x=10, y=290)
    border = Entry(qr_frame, width=33, font="Georgia 13 italic", justify=CENTER, relief=GROOVE, bd=2, textvariable=qr_border, fg='dark blue')
    qr_border.set(2)
    border.place(x=150, y=300)

    Button(qr_frame, text="Generate", bg='white', fg='dark red', command=generate_wifi, font=("Monotype Corsiva", 30), bd=0, activebackground='white', activeforeground='orange', cursor='hand2').place(x=180, y=350)


# Generating a qr code for Wi-Fi
def generate_wifi():
    name = title.get()
    text = wifi_name.get()
    Password = password.get()
    bd = border.get()

    qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_H, box_size=6, border=bd)

    qr.add_data(text+"\n")
    qr.add_data(Password)

    qr.make(fit=True)
    fg_color = foreground.get()
    bg_color = background.get()

    img = qr.make_image(fill_color=fg_color, back_color=bg_color)
    img.save("A:\\My Projects\\Android Subsystem for Windows (Python)\\QR Code\\QR Code Generator\\"+str(name)+".png")

    global Image
    Image = PhotoImage(file="A:\\My Projects\\Android Subsystem for Windows (Python)\\QR Code\\QR Code Generator\\"+str(name)+".png")
    Image_view.config(image=Image)


# Starting program from main function
if __name__ == '__main__':
    # Creating window
    root = Tk()
    root.title("QR Code Generator")
    root.geometry('1000x550+125+50')
    root.config(bg='#495A69')
    root.resizable(False, False)
    root.attributes('-alpha', 0.98)  # Transparant 2% or 0.02%
    root.wm_iconbitmap("A:\\My Projects\\Android Subsystem for Windows (Python)\\QR Code\\QR_Code_icon.ico")

    # create a frame for heading
    frame = Frame(root, height=70, bg='#36434e')
    frame.pack(fill=X)
    # create label to set the heading
    Label(frame, text="QR Code Generator", font=("Monotype Corsiva", 25, 'bold'), bg="#36434e", pady=15, fg='white').pack()

    # creating a side menu bar
    def toggle_menu():
        f1 = Frame(root, width=100, height=1000, bg='#36434e')
        f1.place(x=0, y=0)

        def button(x, y, text, activbcolor, bcolor, cmd):
            def on_press(e):
                myButton1['background'] = activbcolor
                myButton1['foreground'] = 'black'

            def on_leave(e):
                myButton1['background'] = bcolor
                myButton1['foreground'] = '#FFFFF0'

            myButton1 = Button(f1, text=text, width=10, justify=CENTER, fg='#FFFFF0', bd=0, bg=bcolor, activeforeground='black', activebackground=activbcolor, command=cmd, font=("Cambria", 12), pady=5, padx=10, anchor='w', cursor='hand2')

            myButton1.bind('<Enter>', on_press)
            myButton1.bind('<Leave>', on_leave)
            myButton1.place(x=x, y=y)

        # set buttons in side menu bar
        button(0, 80, "Scan Image", '#7c91ac', '#36434e', scan_image)
        button(0, 120, "My QR", '#7c91ac', '#36434e', my_qr)
        button(0, 160, "Create QR", '#7c91ac', '#36434e', generate_qr)
        button(0, 200, "Help", '#7c91ac', '#36434e', help)
        button(0, 240, "Exit", '#7c91ac', '#36434e', exit)

        # create delete function to close the menu bar
        def delete():
            f1.destroy()
        # create button to close the menu bar
        Button(f1, text="__________\n__________\n__________", command=delete, activebackground='#36434e', bg='#36434e', fg='white', bd=0, cursor='hand2').place(x=10, y=10)

    # create button to open the menu bar
    Button(root, command=toggle_menu, text="__________\n__________\n__________", bd=0, fg='white', bg='#36434e', activebackground='#36434e', cursor='hand2').place(
        x=10, y=10)

    # create label to show the qr code
    Image_view = Label(root, bg="#495a69")
    Image_view.pack(padx=5, pady=50, side=RIGHT)

    # Create button to open an image for scan
    Button(root, text="Scan", padx=5, font=("Bahnschrift Light Condensed", 20), bg="#495a69", activebackground="#495a69", fg='white', activeforeground="Orange", bd=0, command=scan_image, cursor='hand2').place(x=820, y=75)
    # Create button to close the open frame
    Button(root, text="Close", padx=5, font=("Bahnschrift Light Condensed", 20), bg="#495a69", activebackground="#495a69", fg='white', activeforeground="Orange", bd=0, command=close, cursor='hand2').place(x=900, y=75)

    root.mainloop()
