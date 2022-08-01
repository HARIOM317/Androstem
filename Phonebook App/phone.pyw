# Importing required packages
from tkinter import *
from tkinter import ttk, messagebox
import csv
import pyautogui    # for improving graphics
from twilio.rest import Client
from threading import Thread


# function for add new contact
def add(i):
    with open('A:\\My Projects\\Android Subsystem for Windows (Python)\\Phonebook App\\data.csv', 'a+', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(i)


# function for show all contacts
def view():
    data = []
    with open('A:\\My Projects\\Android Subsystem for Windows (Python)\\Phonebook App\\data.csv') as file:
        reader = csv.reader(file)
        for row in reader:
            data.append(row)
    return data


# function for remove a contact
def remove(i):
    def save(j):
        with open('A:\\My Projects\\Android Subsystem for Windows (Python)\\Phonebook App\\data.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(j)

    new_list = []
    telephone = i

    with open('A:\\My Projects\\Android Subsystem for Windows (Python)\\Phonebook App\\data.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            new_list.append(row)

            for element in row:
                if element == telephone:
                    new_list.remove(row)

    save(new_list)


# function for updating a contact
def update(i):
    def update_new_list(j):
        with open('A:\\My Projects\\Android Subsystem for Windows (Python)\\Phonebook App\\data.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(j)

    new_list = []
    telephone = i[0]

    with open('A:\\My Projects\\Android Subsystem for Windows (Python)\\Phonebook App\\data.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            new_list.append(row)
            for element in row:
                if element == telephone:
                    name = i[1]
                    telephone = i[2]

                    data = [name, telephone]
                    index = new_list.index(row)
                    new_list[index] = data

    update_new_list(new_list)


# function for search a contact
def search(i):
    data = []
    telephone = i

    with open('A:\\My Projects\\Android Subsystem for Windows (Python)\\Phonebook App\\data.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            for element in row:
                if element == telephone:
                    data.append(row)
    return data


# ============================= For contacts =================================
def contact():
    # updating contact and phone button color
    contact_button.config(fg="green", activeforeground="green", font="default 13 bold underline")
    phone_button.config(fg="black", activeforeground="black", font="default 13")

    # creating frames
    upper_frame = Frame(root, width=550, height=50, bg="#f7eeee")
    upper_frame.place(x=0, y=50)

    main_frame = Frame(root, width=550, height=250, bg="#f7eeee")
    main_frame.place(x=0, y=100)

    table_frame = Frame(root, width=550, height=550, bg='#f7eeee')
    table_frame.place(x=0, y=300)

    Label(main_frame, image=search_bar, bg="#f7eeee", width=550).place(x=0, y=0)

    new_frame = Frame(main_frame, width=550, height=115, bg='#f7eeee')
    new_frame.place(x=0, y=80)

    l_name = Label(new_frame, text="Name", height=1, width=20, font=("Ivy", 10), anchor=NW, fg='#121923')
    # entry widget for name
    e_name = Entry(new_frame, width=25, justify=LEFT, highlightthickness=2, relief=FLAT, highlightcolor='#00adff', highlightbackground='#121923', bd=0)

    l_telephone = Label(new_frame, text="Phone", height=1, font=("Ivy", 10), anchor=NW)
    # entry widget for number
    e_telephone = Entry(new_frame, width=25, justify=LEFT, highlightthickness=2, relief=FLAT, highlightcolor="#00adff", highlightbackground="#121923", bd=0)

    # GUI for showing all contacts
    def show():
        all_contact_button.config(text="")
        global tree
        list_header = ["Name", "Phone"]

        demo_list = view()

        tree = ttk.Treeview(table_frame, selectmode=EXTENDED, columns=list_header, show="headings", height=10)

        vsb = ttk.Scrollbar(table_frame, orient=VERTICAL, command=tree.yview)

        tree.config(yscrollcommand=vsb.set)

        tree.grid(row=0, column=0, sticky=NSEW, padx=(20, 0))
        vsb.grid(row=0, column=1, sticky=NS)

        tree.heading(0, text="Name", anchor=NW)
        tree.heading(1, text="Phone", anchor=NW)

        tree.column(0, width=345, anchor=NW)
        tree.column(1, width=160, anchor=NW)

        for item in demo_list:
            tree.insert('', 'end', values=item)

    # GUI for adding new contact
    def insert():
        Name = e_name.get()
        telephone = e_telephone.get()

        data = [Name, telephone]

        if Name == '' or telephone == '':
            messagebox.showwarning("Contact", "Please fill all the fields")
        else:
            add(data)
            messagebox.showinfo("Contact", "Successfully added!")
            e_name.delete(0, END)
            e_telephone.delete(0, END)

            contact()

    # button for showing all contacts
    all_contact_button = Button(main_frame, text="", bd=0, relief=FLAT, cursor='hand2', fg='black', activeforeground='black', bg="#f7eeee", activebackground="#f7eeee", command=show)
    all_contact_button.place(x=400, y=80)

    # GUI for searching contacts
    def to_search():
        all_contact_button.config(text="show all contacts")
        telephone = search_contact.get()

        data = search(telephone)

        def delete_command():
            tree.delete(*tree.get_children())

        delete_command()

        for item in data:
            tree.insert("", END, values=item)

        search_contact.delete(0, END)

    # search button
    search_button = Button(main_frame, image=search_icon, relief=FLAT, bg='#ffffff', activebackground="#ffffff", width=45, height=45, bd=0, command=to_search)
    search_button.place(x=445, y=15)

    # entry widget for typing contact or contact name for searching
    search_contact = Entry(main_frame, width=17, justify=LEFT, font=("Ivy", 20), relief=FLAT, bd=0, bg="#ffffff", highlightbackground="#ffffff")
    # binding with enter key
    search_contact.bind("<Return>", lambda e: to_search())
    search_contact.place(x=65, y=15)

    # GUI for creating new contact
    def create_contact():
        l_name.place(x=10, y=10)
        e_name.place(x=100, y=10)
        l_telephone.place(x=10, y=70)
        e_telephone.place(x=100, y=70)

        save_button = Button(new_frame, text="SAVE", font="default 10 bold", fg='dark green', cursor='hand2', bd=0, relief=FLAT, bg="#f7eeee", activebackground="#f7eeee", activeforeground='dark green', command=insert)
        save_button.place(x=390, y=70)

    # GUI for delete a contact
    def to_remove():
        try:
            tree_data = tree.focus()
            tree_dictionary = tree.item(tree_data)
            tree_list = tree_dictionary['values']
            tree_telephone = str(tree_list[1])

            remove(tree_telephone)

            messagebox.showinfo("Delete", "Contact has been deleted successfully!")

            for widget in table_frame.winfo_children():
                widget.destroy()

            show()

        except IndexError:
            messagebox.showerror("Error", "Select a contact first.")

    # function for calling to selected contact
    def call():
        try:
            tree_data = tree.focus()
            tree_dictionary = tree.item(tree_data)
            tree_list = tree_dictionary['values']
            tree_telephone = str(tree_list[1])

            account_sid = "Your twilio account sid"
            auth_token = "Your twilio account auth token"
            client = Client(account_sid, auth_token)

            call = client.calls.create(
                twiml="<Response><Say>hello</Say></Response>",
                to="+91" + tree_telephone,
                from_="Your twilio account number"
            )
            messagebox.showinfo("Calling", "Call sent successfully")
        except:
            messagebox.showinfo("Calling", "Please select a contact first!"
                                           "\nNote : Make sure that your internet connection is OK.")

    # GUI for updating contact
    def to_update():
        try:
            l_name.place(x=10, y=10)
            e_name.place(x=100, y=10)
            l_telephone.place(x=10, y=70)
            e_telephone.place(x=100, y=70)

            tree_data = tree.focus()
            tree_dictionary = tree.item(tree_data)
            tree_list = tree_dictionary['values']

            Name = str(tree_list[0])
            Telephone = str(tree_list[1])

            e_name.insert(0, Name)
            e_telephone.insert(0, Telephone)

            def confirm():
                new_name = e_name.get()
                new_telephone = e_telephone.get()

                data = [new_telephone, new_name, new_telephone]

                update(data)
                messagebox.showinfo("Contact", "Contact updated successfully!")

                e_name.delete(0, END)
                e_telephone.delete(0, END)

                for widget in table_frame.winfo_children():
                    widget.destroy()

                b_confirm.destroy()
                contact()

            # confirm button
            b_confirm = Button(main_frame, text="Confirm", height=1, font=("default", 10, 'bold'), relief=FLAT, bg='#f7eeee', activebackground="#f7eeee", command=confirm, fg='Green', activeforeground="green", bd=0)
            b_confirm.place(x=390, y=150)
        except IndexError:
            messagebox.showerror("Error", "Select a contact first")

    # call button
    call_button = Button(upper_frame, image=call_throw_selection_icon, compound=LEFT, width=100, height=40, bd=0, relief=FLAT, cursor='hand2', bg="#f7eeee", activebackground="#f7eeee", fg='black', activeforeground='black', command=call)
    call_button.place(x=10, y=2)

    # add button
    add_button = Button(upper_frame, text=" Add", image=add_icon, compound=LEFT, width=100, height=40, bd=0, relief=FLAT, cursor='hand2', bg="#f7eeee", activebackground="#f7eeee", fg='black', activeforeground='black', command=create_contact)
    add_button.place(x=140, y=2)

    # delete button
    delete_button = Button(upper_frame, text=" Delete", image=delete_icon, compound=LEFT, width=100, height=40, bd=0, relief=FLAT, cursor='hand2', bg="#f7eeee", activebackground="#f7eeee", fg='black', activeforeground='black', command=to_remove)
    delete_button.place(x=290, y=2)

    # edit button
    edit_button = Button(upper_frame, text=" Edit", image=edit_icon, compound=LEFT, width=100, height=40, bd=0, relief=FLAT, cursor='hand2', bg="#f7eeee", activebackground="#f7eeee", fg='black', activeforeground='black', command=to_update)
    edit_button.place(x=440, y=2)

    # calling show function
    show()


# ============================= For Phone =================================
def phone():
    # updating phone and contact button color
    phone_button.config(fg="green", activeforeground="green", font="default 13 bold underline")
    contact_button.config(fg="black", activeforeground="black", font="default 13")

    # creating frames
    upper_frame = Frame(root, width=550, height=280, bg="#f7eeee")
    upper_frame.place(x=0, y=50)

    lower_frame = Frame(root, width=550, height=600, bg="white")
    lower_frame.place(x=0, y=330)

    mobile_number = StringVar()

    # entry widget for typing mobile number
    number_entry = Entry(upper_frame, width=15, font=("Bahnschrift Light Condensed", 30, 'bold'), textvariable=mobile_number, bg="#fff6f5", bd=0, relief=FLAT, highlightbackground='#f7c8c8', highlightcolor='#00c6ff', highlightthickness=2)
    mobile_number.set("+91 ")
    number_entry.place(x=30, y=20)

    # use threading in call_someone function
    def threading_call_someone():
        t1 = Thread(target=call_someone)
        t1.start()

    # function for calling someone
    def call_someone():
        try:
            account_sid = "Your twilio account sid"
            auth_token = "Your twilio account auth token"
            client = Client(account_sid, auth_token)
            number = number_entry.get()

            call = client.calls.create(
                twiml="<Response><Say>hello</Say></Response>",
                to=number,
                from_="Your twilio account number"
            )
            messagebox.showinfo("Calling", "Call sent successfully")
        except:
            messagebox.showinfo("Internet", "Check your internet connection or entered number is OK.")

    # button for call
    calling_button = Button(upper_frame, image=calling_icon, bd=0, relief=FLAT, bg="#f7eeee", activebackground="#f7eeee", command=threading_call_someone)
    calling_button.place(x=455, y=22)

    # function for clicking on buttons to get exact key number
    def click_button(event):
        e = Event()
        text = event.widget.cget("text")
        mobile_number.set(mobile_number.get() + text)
        number_entry.update()

    # Create 1 - 9 buttons using a loop
    temp = 1
    for i in range(1, 4):
        for j in range(3):
            num_button = Button(lower_frame, text=str(temp), font=("Bahnschrift Light Condensed", 30), width=7, pady=5, padx=5, relief=FLAT, bd=0, bg='#fafafa', activebackground='#fafafa')
            num_button.grid(row=i, column=j)
            temp += 1
            num_button.bind("<Button-1>", click_button)

    # star button
    star_button = Button(lower_frame, text="*", font=("Bahnschrift Light Condensed", 30), width=7, pady=5, padx=5, relief=FLAT, bd=0, bg='#fafafa', activebackground='#fafafa')
    star_button.grid(row=4, column=0)
    star_button.bind("<Button-1>", click_button)

    # zero button
    zero_button = Button(lower_frame, text="0", font=("Bahnschrift Light Condensed", 30), width=7, pady=5, padx=5, relief=FLAT, bd=0, bg='#fafafa', activebackground='#fafafa')
    zero_button.grid(row=4, column=1)
    zero_button.bind("<Button-1>", click_button)

    # hash button
    hash_button = Button(lower_frame, text="#", font=("Bahnschrift Light Condensed", 30), width=7, pady=5, padx=5, relief=FLAT, bd=0, bg='#fafafa', activebackground='#fafafa')
    hash_button.grid(row=4, column=2)
    hash_button.bind("<Button-1>", click_button)


# staring point
if __name__ == '__main__':
    # Creating window
    root = Tk()
    root.title("Phone")
    root.resizable(False, False)
    root.geometry("550x850+400+30")
    root.config(bg="#f7eeee")
    root.wm_iconbitmap("A:\\My Projects\\Android Subsystem for Windows (Python)\\Phonebook App\\phone_icon.ico")

    # updating Treeview widget
    style = ttk.Style()
    style.configure("Treeview.Heading", font=("Bahnschrift Light Condensed", 18, 'bold'))
    style.configure("Treeview", font=("Bahnschrift Light Condensed", 15), rowheight=50)

    # loading icon keys
    add_icon = PhotoImage(file="A:\\My Projects\\Android Subsystem for Windows (Python)\\Phonebook App\\Icons\\add_button.png")
    delete_icon = PhotoImage(file="A:\\My Projects\\Android Subsystem for Windows (Python)\\Phonebook App\\Icons\\delete_button.png")
    edit_icon = PhotoImage(file="A:\\My Projects\\Android Subsystem for Windows (Python)\\Phonebook App\\Icons\\edit_button.png")
    call_throw_selection_icon = PhotoImage(file="A:\\My Projects\\Android Subsystem for Windows (Python)\\Phonebook App\\Icons\\call.png")

    search_bar = PhotoImage(file="A:\\My Projects\\Android Subsystem for Windows (Python)\\Phonebook App\\search_bar.png")
    search_icon = PhotoImage(file="A:\\My Projects\\Android Subsystem for Windows (Python)\\Phonebook App\\Icons\\search_button.png")

    calling_icon = PhotoImage(file="A:\\My Projects\\Android Subsystem for Windows (Python)\\Phonebook App\\Icons\\calling_button_icon.png")

    # creating top frame for phone and contact button
    top_frame = Frame(root, width=550, height=60, bg="#f7eeee")
    top_frame.pack(side=TOP, fill=X)

    # phone button
    phone_button = Button(top_frame, text="Phone", font="default 13", width=10, bd=0, relief=FLAT, fg='black', bg="#f7eeee", activeforeground='black', activebackground='#f7eeee', cursor='hand2', command=phone)
    phone_button.place(x=50, y=2)

    # contact button
    contact_button = Button(top_frame, text="Contacts", font="default 13", width=10, bd=0, relief=FLAT, fg='black', bg="#f7eeee", activeforeground='black', activebackground='#f7eeee', cursor='hand2', command=contact)
    contact_button.place(x=345, y=2)

    # calling phone function  to show window as default
    phone()

    root.mainloop()
