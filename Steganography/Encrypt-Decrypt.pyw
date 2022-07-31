# Importing required packages
from tkinter import *
from tkinter import messagebox, filedialog
import base64
import pickle
from PIL import Image, ImageTk
import os
from stegano import lsb
from datetime import datetime
from threading import Thread


# function for encrypting message
def encrypt():
    try:
        code = password.get()
        with open('A:\\My Projects\\Android Subsystem for Windows (Python)\\Steganography\\password.pkl', 'wb') as f:
            pickle.dump(code, f)
        with open('A:\\My Projects\\Android Subsystem for Windows (Python)\\Steganography\\password.pkl', 'rb') as f:
            my_pass = pickle.load(f)

        if code == "":
            messagebox.showinfo("Encrypter", "Please enter your secret key.")
        elif code == my_pass:
            encrypted_message.delete(1.0, END)
            message = text_message.get(1.0, END)
            encode_message = message.encode("ascii")
            base64_bytes = base64.b64encode(encode_message)
            encrypter = base64_bytes.decode('ascii')
            encrypted_message.insert(END, encrypter)
            messagebox.showinfo("Encrypter", "Encrypted successfully!")
        else:
            messagebox.showerror("Encrypter", "Something went wrong!")
    except:
        messagebox.showerror("Encrypter", "Something went wrong!")


# function for decrypting message
def decrypt():
    try:
        code = password.get()
        with open('A:\\My Projects\\Android Subsystem for Windows (Python)\\Steganography\\password.pkl', 'rb') as f:
            my_pass = pickle.load(f)

        if code == my_pass:
            encrypted_message.delete(1.0, END)
            message = text_message.get(1.0, END)
            encode_message = message.encode("ascii")
            base64_bytes = base64.b64decode(encode_message)
            decrypter = base64_bytes.decode('ascii')
            encrypted_message.insert(END, decrypter)
            messagebox.showinfo("Decrypter", "Decrypted successfully!")
        elif code == "":
            messagebox.showinfo("Decrypter", "Please enter the password!")
        else:
            messagebox.showerror("Decrypter", "Invalid password!")
    except:
        messagebox.showerror("Decrypter", "Something went wrong!")


# function for resetting message and key
def reset():
    text_message.delete(1.0, END)
    encrypted_message.delete(1.0, END)
    password.set("")


# function for home button
def home():
    bottom_frame = Frame(root, width=900, height=500, background="#252a40")
    bottom_frame.place(x=0, y=50)

    Label(bottom_frame, text="Enter your message", font=("Bahnschrift Light Condensed", 15), bg="#252a40", fg='white').place(x=10, y=5)

    global text_message
    text_message = Text(bottom_frame, font=("Yu Gothic Light", 15), width=80, height=6, bd=1, relief=SOLID, background='#3b4366', fg='white', wrap=WORD)
    text_message.place(x=8, y=50)

    Label(bottom_frame, text="Enter secret key", font=("Bahnschrift Light Condensed", 15), bg="#252a40", fg="white").place(x=5, y=225)

    global password
    password = StringVar()
    entry = Entry(bottom_frame, width=50, bd=0, relief=FLAT, font=("Bahnschrift Light Condensed", 15), show="●", textvariable=password, highlightbackground='black', highlightthickness=1, highlightcolor='#00c6ff', justify=CENTER, background="#93a7fe", fg='white')
    entry.place(x=150, y=228)

    global encrypted_message
    encrypted_message = Text(bottom_frame, font=("Yu Gothic Light", 15), width=80, height=6, bd=1, relief=SOLID, background='#3b4366', fg='white', wrap=WORD)
    encrypted_message.place(x=8, y=275)

    encrypt_button = Button(bottom_frame, text=" Encrypt", image=encrypt_icon, bd=0, relief=FLAT, command=encrypt, compound=LEFT, width=100, height=50, bg='#252a40', activebackground='#252a40', font=("Bahnschrift Light Condensed", 12), fg="white", activeforeground='white')
    encrypt_button.place(x=250, y=439)

    decrypt_button = Button(bottom_frame, text=" Decrypt", image=decrypt_icon, bd=0, relief=FLAT, command=decrypt, compound=LEFT, width=100, height=50, bg='#252a40', activebackground='#252a40', font=("Bahnschrift Light Condensed", 12), fg="white", activeforeground='white')
    decrypt_button.place(x=400, y=439)

    reset_button = Button(bottom_frame, text=" Reset", image=reset_icon, bd=0, relief=FLAT, command=reset, compound=LEFT, width=100, height=50, bg='#252a40', activebackground='#252a40', font=("Bahnschrift Light Condensed", 12), fg="white", activeforeground='white')
    reset_button.place(x=550, y=439)
# ___________________________________________________________________


# function for open image to show or hide message
def showimage():
    try:
        global filename
        filename = filedialog.askopenfilename(initialdir=os.getcwd(),
                                              title="Select Image",
                                              filetypes=(("PNG File", "*.png"),
                                                         ("JPG File", "*.jpg"),
                                                         ("All Files", "*.txt")))
        img = Image.open(filename)
        img = img.resize((250, 250))
        img = ImageTk.PhotoImage(img)

        image_label.configure(image=img, width=250, height=250)
        image_label.image = img

        hide_button.config(state=NORMAL)
        if filename.endswith(".png"):
            show_button.config(state=NORMAL)
        else:
            show_button.config(state=DISABLED)
    except:
        messagebox.showinfo("Open image", "No image found!")


# threading in hide function
def threading_hide():
    t1 = Thread(target=Hide)
    t1.start()


# function for hide data in image
def Hide():
    try:
        global secret
        message = text_widget.get(1.0, END)
        secret = lsb.hide(str(filename), message)
        save_button.config(state=NORMAL)
        messagebox.showinfo("Hide message", "message hide successfully!")
    except:
        messagebox.showinfo("Message", "No message written in image!")


# threading in show function
def threading_show():
    t1 = Thread(target=Show)
    t1.start()


# function for show data from image
def Show():
    try:
        clear_message = lsb.reveal(filename)
        text_widget.delete(1.0, END)
        text_widget.insert(END, clear_message)
    except:
        messagebox.showinfo("Message", "No message found!")


# function for save image after hiding secret text message in image
def save():
    try:
        if not os.path.exists("A:\\My Projects\\Android Subsystem for Windows (Python)\\Steganography\\Hidden images"):
            os.mkdir("A:\\My Projects\\Android Subsystem for Windows (Python)\\Steganography\\Hidden images")
        root.title("Saving...")
        current_time = datetime.now().strftime("%d%H%M%S")
        secret.save(f"A:\\My Projects\\Android Subsystem for Windows (Python)\\Steganography\\Hidden images\\hidden_{current_time}.png")
        messagebox.showinfo("Hidden text in image", "Image saved successfully in (A:\\My Projects\\Android Subsystem for Windows (Python)\\Steganography\\Hidden images) directory")
        root.title("Encryption-Decryption (Steganography)")
    except:
        messagebox.showerror("Save image", "Something went wrong!")
        root.title("Encryption-Decryption (Steganography)")


# threading in save function
def threading_save():
    t1 = Thread(target=save)
    t1.start()


# function for creating GUI for hiding text message in image
def text_in_image():
    bottom_frame = Frame(root, width=900, height=500, background="#252a40")
    bottom_frame.place(x=0, y=50)

    frame1 = Frame(bottom_frame, width=435, height=400, bg='#1a1e2e', highlightbackground='#93a7fe', highlightthickness=1)
    frame1.place(x=10, y=10)

    global image_label
    image_label = Label(frame1, bg="#1a1e2e")
    image_label.place(x=90, y=70)

    frame2 = Frame(bottom_frame, width=435, height=400, bg='white', highlightbackground='black', highlightthickness=1, highlightcolor='orange')
    frame2.place(x=455, y=10)

    global text_widget
    text_widget = Text(frame2, font=("Bahnschrift Light Condensed", 15), bg="white", fg="black", relief=FLAT, wrap=WORD, bd=0)
    text_widget.place(x=5, y=5, width=410, height=388)

    scrollbar1 = Scrollbar(frame2)
    scrollbar1.place(x=415, y=5, height=388)

    scrollbar1.configure(command=text_widget.yview)
    text_widget.configure(yscrollcommand=scrollbar1.set)

    frame3 = Frame(bottom_frame, width=880, height=70, bg='#454f7a', highlightbackground='gray', highlightthickness=1)
    frame3.place(x=10, y=420)

    open_button = Button(frame3, text="Open Image", width=25, font=("Bahnschrift Light Condensed", 15), bg="#353c5d", fg="white", bd=1, relief=SOLID, activebackground='#353c5d', activeforeground='white', overrelief=GROOVE, command=showimage)
    open_button.place(x=5, y=15)

    global save_button
    save_button = Button(frame3, text="Save Image", width=25, font=("Bahnschrift Light Condensed", 15), bg="#353c5d", fg="white", bd=1, relief=SOLID, activebackground='#353c5d', activeforeground='white', overrelief=GROOVE, command=threading_save, state=DISABLED)
    save_button.place(x=225, y=15)

    global hide_button
    hide_button = Button(frame3, text="Hide Data", width=25, font=("Bahnschrift Light Condensed", 15), bg="#353c5d", fg="white", bd=1, relief=SOLID, activebackground='#353c5d', activeforeground='white', overrelief=GROOVE, command=threading_hide, state=DISABLED)
    hide_button.place(x=445, y=15)

    global show_button
    show_button = Button(frame3, text="Show Data", width=25, font=("Bahnschrift Light Condensed", 15), bg="#353c5d", fg="white", bd=1, relief=SOLID, activebackground='#353c5d', activeforeground='white', overrelief=GROOVE, command=threading_show, state=DISABLED)
    show_button.place(x=665, y=15)
# ______________________________________________________


# function for encrypt and decrypt image
def encrypt_image():
    try:
        file1 = filedialog.askopenfile(mode='r', filetypes=[("jpg file", "*.jpg"), ("png file", "*.png")])

        if file1 is not None:
            file_name = file1.name
            key = image_password.get()

            if key == "":
                messagebox.showinfo("Password", "Please enter a key first!")

            if 0 < int(key) <= 250:
                with open("image password.txt", 'a') as f:
                    f.write(key+"\n")

            my_file = open(file_name, 'rb')
            image = my_file.read()
            my_file.close()

            image = bytearray(image)

            for index, value in enumerate(image):
                image[index] = value ^ int(key)

            my_file2 = open(file_name, 'wb')
            my_file2.write(image)
            my_file2.close()
            messagebox.showinfo("Encryption & Decryption", "Successfully done!")
    except:
        messagebox.showerror("Encryption & Decryption", "Something went wrong!")


# function for creating GUI for encrypt and decrypt image
def encrypt_decrypt_image():
    bottom_frame = Frame(root, width=900, height=500, background="#252a40")
    bottom_frame.place(x=0, y=50)

    Label(bottom_frame, text="Note : key should be a small positive number digit which is less then or equal to 250", font=("Bahnschrift Light Condensed", 15), bg="#252a40", fg='orange').place(x=170, y=20)

    Label(bottom_frame, text="Enter key number", font=("Bahnschrift Light Condensed", 25), bg="#252a40", fg='white').place(x=170, y=150)

    global image_password
    image_password = Entry(bottom_frame, width=25, font=("Bahnschrift Light Condensed", 25), show="●", bg="#93a7fe", highlightbackground='black', highlightcolor='#00c6ff', highlightthickness=1, bd=0, relief=FLAT)
    image_password.place(x=380, y=150)

    browse_image_button = Button(bottom_frame, text="Browse image", font=("Bahnschrift Light Condensed", 25), bg="#252a40", activebackground="#252a40", fg="white", activeforeground="white", bd=0, relief=FLAT, cursor="hand2", command=encrypt_image)
    browse_image_button.place(x=380, y=250)


# Creating main window
root = Tk()
root.geometry("900x550+180+20")
root.title('Encryption-Decryption (Steganography)')
root.resizable(False, False)
root.wm_iconbitmap("A:\\My Projects\\Android Subsystem for Windows (Python)\\Steganography\\message_encryption_icon.ico")

top_frame = Frame(root, width=900, height=50, background="#0f111a")
top_frame.place(x=0, y=0)

home_icon = PhotoImage(file="A:\\My Projects\\Android Subsystem for Windows (Python)\\Steganography\\Icons\\home_icon.png")
home_button = Button(top_frame, image=home_icon, bg="#0f111a", activebackground="#0f111a", bd=0, relief=FLAT, cursor='hand2', command=home)
home_button.place(x=10, y=7)

Button(top_frame, text="Hide text in image", font=("Bahnschrift Light Condensed", 15), bg="#0f111a", activebackground="#0f111a", fg='white', activeforeground='white', bd=0, relief=FLAT, cursor='hand2', command=text_in_image).place(x=590, y=5)
Button(top_frame, text="Encrypt-Decrypt image", font=("Bahnschrift Light Condensed", 15), bg="#0f111a", activebackground="#0f111a", fg='white', activeforeground='white', bd=0, relief=FLAT, cursor='hand2', command=encrypt_decrypt_image).place(x=730, y=5)

encrypt_icon = PhotoImage(file="A:\\My Projects\\Android Subsystem for Windows (Python)\\Steganography\\Icons\\encrypt_button.png")
decrypt_icon = PhotoImage(file="A:\\My Projects\\Android Subsystem for Windows (Python)\\Steganography\\Icons\\decrypt_button.png")
reset_icon = PhotoImage(file="A:\\My Projects\\Android Subsystem for Windows (Python)\\Steganography\\Icons\\reset_button.png")

# open as default
home()

root.mainloop()
