# Importing required packages
from tkinter import *
from tkinter import messagebox
import csv
import os

# register function for creating a new account
def register():
    with open("A:\\My Projects\\Android Subsystem for Windows (Python)\\users.csv", "a", newline="") as f:
        writer = csv.writer(f, delimiter=",")
        name = username.get()
        password = create_password.get()
        password2 = confirm_password.get()

        if password == password2:
            writer.writerow([name, password])
            messagebox.showinfo("Account", "Account created successfully")
        else:
            messagebox.showerror("Account", "Passwords are different")


# login function for login in existing account
def login():
    name = user.get()
    password = code.get()

    with open("A:\\My Projects\\Android Subsystem for Windows (Python)\\users.csv", "r") as f:
        reader = csv.reader(f, delimiter=",")
        for row in reader:
            if row == [name, password]:
                os.startfile("A:\\My Projects\\Android Subsystem for Windows (Python)\\main\\Main.pyw")
                return True
    messagebox.showerror("Login", "Invalid username or password")
    return False


# sign_in function for creating a GUI window for sign in
def sign_in():
    root.title("Login (Android sub-system for windows)")
    heading.config(text="Sign in")
    main_frame = Frame(root, bg='white', width=500, height=300)
    main_frame.place(x=75, y=80)

    def on_enter(e):
        name = user.get()
        frame1.config(bg='#00d3ff')
        if name == "Username":
            user.delete(0, 'end')
            user.config(fg='black')

    def on_leave(e):
        name = user.get()
        frame1.config(bg='black')
        if name == "":
            user.insert(0, 'Username')
            user.config(fg='gray')

    global user
    user = Entry(main_frame, width=36, border=0, relief=FLAT, font=("Microsoft New Tai Lue", 15), fg='gray')
    user.place(x=50, y=40)
    user.insert(0, 'Username')
    user.bind("<FocusIn>", on_enter)
    user.bind("<FocusOut>", on_leave)
    frame1 = Frame(main_frame, width=410, height=2, bg='black')
    frame1.place(x=45, y=67)

    def on_enter2(e):
        password = code.get()
        frame2.config(bg='#00d3ff')
        if password == "Password":
            code.delete(0, 'end')
            code.config(fg='black')
            code.config(show="●")

    def on_leave2(e):
        password = code.get()
        frame2.config(bg='black')
        if password == "":
            code.insert(0, 'Password')
            code.config(show="")
            code.config(fg='gray')

    global code
    code = Entry(main_frame, width=36, border=0, relief=FLAT, font=("Microsoft New Tai Lue", 15), fg='gray')
    code.place(x=50, y=100)
    code.insert(0, 'Password')
    code.bind("<FocusIn>", on_enter2)
    code.bind("<FocusOut>", on_leave2)
    frame2 = Frame(main_frame, width=410, height=2, bg='black')
    frame2.place(x=45, y=127)

    Button(main_frame, width=35, pady=7, text="Sign in", bg='#00a9ff', fg='#ffffff', border=0, relief=FLAT, activebackground="#00a9ff", activeforeground='#ffffff', font=("Calibri", 15), command=login).place(x=70, y=160)

    Label(main_frame, text="Don't have an account?", bg='white', font=("default", 10), fg='#000000').place(x=140, y=245)

    sign_up_button = Button(main_frame, width=6, text="Sign up", bg='white', fg='#0089ff', border=0, relief=FLAT, activebackground="white", activeforeground='#0089ff', cursor='hand2', font=("default", 10), command=sign_up)
    sign_up_button.place(x=300, y=245)


# sign_up function for creating a GUI window for sign up
def sign_up():
    root.title("Create account (Android sub-system for windows)")
    heading.config(text="Sign up")
    new_frame = Frame(root, bg='white', width=500, height=300)
    new_frame.place(x=75, y=80)

    def on_enter_key(e):
        name = username.get()
        frame1.config(bg="#00d3ff")
        if name == "Username":
            username.delete(0, 'end')
            username.config(fg='black')

    def on_leave_key(e):
        frame1.config(bg="black")
        name = username.get()
        if name == "":
            username.insert(0, 'Username')
            username.config(fg='gray')

    global username
    username = Entry(new_frame, width=36, border=0, relief=FLAT, font=("Microsoft New Tai Lue", 15), fg='gray')
    username.place(x=50, y=10)
    username.insert(0, 'Username')
    username.bind("<FocusIn>", on_enter_key)
    username.bind("<FocusOut>", on_leave_key)
    frame1 = Frame(new_frame, width=410, height=2, bg='black')
    frame1.place(x=45, y=37)

    def on_enter_key2(e):
        password = create_password.get()
        frame2.config(bg="#00d3ff")
        if password == "Password":
            create_password.delete(0, 'end')
            create_password.config(fg='black')
            create_password.config(show="●")

    def on_leave_key2(e):
        password = create_password.get()
        frame2.config(bg="black")
        if password == "":
            create_password.insert(0, 'Password')
            create_password.config(fg='gray')
            create_password.config(show="")

    global create_password
    create_password = Entry(new_frame, width=36, border=0, relief=FLAT, font=("Microsoft New Tai Lue", 15), fg='gray')
    create_password.place(x=50, y=70)
    create_password.insert(0, 'Password')
    create_password.bind("<FocusIn>", on_enter_key2)
    create_password.bind("<FocusOut>", on_leave_key2)
    frame2 = Frame(new_frame, width=410, height=2, bg='black')
    frame2.place(x=45, y=97)

    def on_enter_key3(e):
        password = confirm_password.get()
        frame3.config(bg="#00d3ff")
        if password == "Confirm password":
            confirm_password.delete(0, 'end')
            confirm_password.config(fg='black')
            confirm_password.config(show="●")

    def on_leave_key3(e):
        password = confirm_password.get()
        frame3.config(bg="black")
        if password == "":
            confirm_password.insert(0, 'Confirm password')
            confirm_password.config(fg='gray')
            confirm_password.config(show="")

    global confirm_password
    confirm_password = Entry(new_frame, width=36, border=0, relief=FLAT, font=("Microsoft New Tai Lue", 15), fg='gray')
    confirm_password.place(x=50, y=130)
    confirm_password.insert(0, 'Confirm password')
    confirm_password.bind("<FocusIn>", on_enter_key3)
    confirm_password.bind("<FocusOut>", on_leave_key3)
    frame3 = Frame(new_frame, width=410, height=2, bg='black')
    frame3.place(x=45, y=157)

    Button(new_frame, width=35, pady=7, text="Sign up", bg='#00a9ff', fg='#ffffff', border=0, relief=FLAT, activebackground="#00a9ff", activeforeground='#ffffff', font=("Calibri", 15), command=register).place(x=70, y=190)

    Label(new_frame, text="Already have an account?", bg='white', font=("default", 10), fg='#000000').place(x=140, y=260)

    sign_in_button = Button(new_frame, width=6, text="Sign in", bg='white', fg='#0089ff', border=0, relief=FLAT, activebackground="white", activeforeground='#0089ff', cursor='hand2', font=("default", 10), command=sign_in)
    sign_in_button.place(x=300, y=260)


# creating main (root) window
root = Tk()
root.title("Login (Android sub-system for windows)")
root.geometry("650x400+250+50")
root.resizable(False, False)
root.config(bg='white')
root.wm_iconbitmap("A:\\My Projects\\Android Subsystem for Windows (Python)\\android_icon.ico")

heading = Label(root, text="Sign in", fg="#0089ff", bg='white', font=("Microsoft YaHei UI Light", 23, 'bold'))
heading.place(x=285, y=10)

sign_in()

root.mainloop()
