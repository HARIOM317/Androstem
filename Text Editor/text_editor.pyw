# Importing required packages
from tkinter import *
from tkinter import filedialog, font, colorchooser, messagebox
import win32print

# declaring global variable
global open_status_name
open_status_name = False


# function for creating a new file
def new_file():
    my_text.delete('1.0', END)
    root.title("New file")
    status_bar.config(text="New file   ")

    global open_status_name
    open_status_name = False


# function for opening a file
def open_file():
    try:
        my_text.delete("1.0", END)
        text_file = filedialog.askopenfilename(initialdir="A:/", title="Open file",
                                               filetypes=[("Text file", "*.txt"), ("HTML file", "*.html"),
                                                          ("All files", "*.*")])

        if text_file:
            global open_status_name
            open_status_name = text_file

        name = text_file
        status_bar.config(text=name)
        root.title(f"{name} - Text editor")

        # opening file
        text_file = open(text_file, 'r')
        stuff = text_file.read()

        my_text.insert(END, stuff)
        text_file.close()
    except:
        messagebox.showinfo("Open file", "file not found!")


# function for save the file
def save_file():
    global open_status_name
    if open_status_name:
        text_file = open(open_status_name, 'w')
        text_file.write(my_text.get(1.0, END))
        text_file.close()

        status_bar.config(text=f"Saved : {open_status_name}     ")
    else:
        save_as_file()


# function for save as the file
def save_as_file():
    text_file = filedialog.asksaveasfilename(defaultextension=".*", initialdir="A:/", title="Save file",
                                             filetypes=[("Text file", "*.txt"), ("HTML file", "*.html"),
                                                        ("All files", "*.*")])

    if text_file:
        name = text_file
        status_bar.config(text="Saved - " + name)
        root.title(f"{name} - Text editor")

        # saving the file
        text_file = open(text_file, 'w')
        text_file.write(my_text.get(1.0, END))
        text_file.close()


# function for print file by default printer
def print_file():
    printer_name = win32print.GetDefaultPrinter()
    status_bar.config(text=printer_name)


# function for cut the selected texts
def Cut():
    my_text.event_generate(("<<Cut>>"))


# function for copy the selected texts
def Copy():
    my_text.event_generate(("<<Copy>>"))


# function for paste the copied texts
def Paste():
    my_text.event_generate(("<<Paste>>"))


# function redo the texts
def Redo():
    my_text.event_generate(("<<Redo>>"))


# function undo the texts
def Undo():
    my_text.event_generate(("<<Undo>>"))


# function for bold the selected texts
def bold_texts():
    try:
        bold_font = font.Font(my_text, my_text.cget("font"))
        bold_font.config(weight="bold")

        my_text.tag_configure("bold", font=bold_font)

        current_tags = my_text.tag_names("sel.first")

        if "bold" in current_tags:
            my_text.tag_remove("bold", "sel.first", "sel.last")
        else:
            my_text.tag_add("bold", "sel.first", "sel.last")
    except:
        messagebox.showinfo("Bold", "text not selected!")


# function for italic the selected texts
def italic_texts():
    try:
        italic_font = font.Font(my_text, my_text.cget("font"))
        italic_font.config(slant="italic")

        my_text.tag_configure("italic", font=italic_font)

        current_tags = my_text.tag_names("sel.first")

        if "italic" in current_tags:
            my_text.tag_remove("italic", "sel.first", "sel.last")
        else:
            my_text.tag_add("italic", "sel.first", "sel.last")
    except:
        messagebox.showinfo("Italic", "text not selected!")


# function for select all texts
def select_all():
    my_text.tag_add('sel', '1.0', 'end')


# function for clear all texts
def clear_all():
    my_text.delete(1.0, END)


# function for changing the selected text color
def text_color():
    try:
        my_color = colorchooser.askcolor()[1]
        if my_color:
            status_bar.config(text=my_color)

            font_color = font.Font(my_text, my_text.cget("font"))
            font_color.config(slant="italic")

            my_text.tag_configure("colored", font=font_color, foreground=my_color)

            current_tags = my_text.tag_names("sel.first")

            if "colored" in current_tags:
                my_text.tag_remove("colored", "sel.first", "sel.last")
            else:
                my_text.tag_add("colored", "sel.first", "sel.last")
    except:
        messagebox.showinfo("Font color", "text not selected!")


# function for changing the font color
def background_color():
    my_color = colorchooser.askcolor()[1]
    if my_color:
        my_text.config(bg=my_color)


# function for changing the background color
def foreground_color():
    my_color = colorchooser.askcolor()[1]
    if my_color:
        my_text.config(fg=my_color)


# function for enable the dark mode
def dark_mode():
    root.config(bg="#272727")
    status_frame.config(bg="#1f1f1f")
    status_bar.config(bg="#1f1f1f", fg='white')
    my_frame.config(bg="#272727", relief=SOLID)
    my_text.config(bg='#272727', fg='white')
    tool_bar_frame.config(bg="#202020")

    bold_button.config(bg='#202020', activebackground="#202020", fg="white", activeforeground='white')
    italic_button.config(bg='#202020', activebackground="#202020", fg="white", activeforeground='white')
    text_color_button.config(bg='#202020', activebackground="#202020", fg="white", activeforeground='white')

    file_menu.config(bg="#353535", fg='white')
    edit_menu.config(bg="#353535", fg='white')
    color_menu.config(bg="#353535", fg='white')
    option_menu.config(bg="#353535", fg='white')
    help_menu.config(bg="#353535", fg='white')


# function for enable the light mode
def light_mode():
    root.config(bg="SystemButtonFace")
    status_frame.config(bg="#f3f3f3")
    status_bar.config(bg="#f3f3f3", fg='black')
    my_frame.config(bg="#f9f9f9", relief=RIDGE)
    my_text.config(bg='#f9f9f9', fg='black')
    tool_bar_frame.config(bg="#f3f3f3")

    bold_button.config(bg='#f3f3f3', fg='black')
    italic_button.config(bg='#f3f3f3', fg='black')
    text_color_button.config(bg='#f3f3f3', fg='black')

    file_menu.config(bg="#f9f9f9", fg='black')
    edit_menu.config(bg="#f9f9f9", fg='black')
    color_menu.config(bg="#f9f9f9", fg='black')
    option_menu.config(bg="#f9f9f9", fg='black')
    help_menu.config(bg="#f9f9f9", fg='black')


# function for about the text editor
def About():
    messagebox.showinfo("Text editor",
                        f'''Text editor by HSR \n

Notepad 2021.3.2 (Community Edition) 
Runtime version: 11.0.13+7-b1751.25 amd64
VM: Opensource 64-Bit Server VM by HSR.

Powered By: Open Source Community
Copyright © 2010–2030 HSR''')


# Creating window
root = Tk()
root.title("Text editor")
root.geometry("1000x620+150+10")
root.resizable(False, False)
root.wm_iconbitmap("A:\\My Projects\\Android Subsystem for Windows (Python)\\Text Editor\\TextEditor.ico")

# creating a toolbar
tool_bar_frame = Frame(root, width=1000, height=50, bg="#f3f3f3")
tool_bar_frame.pack(fill=X)

# creating frame for text widget
my_frame = Frame(root, width=1000, height=520, bg='#f9f9f9', bd=1, relief=RIDGE)
my_frame.pack(fill=X)

# frame for status bar
status_frame = Frame(root, width=1000, height=37, bg='#f3f3f3')
status_frame.pack(fill=X, side=BOTTOM)

# adding status bar to bottom
status_bar = Label(status_frame, text="Ready   ", anchor='e', bg="#f3f3f3")
status_bar.place(x=10, y=10)

# Creating a scrollbar
text_scroll = Scrollbar(my_frame, width=10)
text_scroll.pack(side=RIGHT, fill=Y)

# Creating a Text widget
my_text = Text(my_frame, width=50, height=22, font=("Cambria", 15), selectbackground="sky blue",
               selectforeground='black', undo=True, yscrollcommand=text_scroll.set, relief=FLAT, bg='#f9f9f9', wrap=WORD)
my_text.pack(fill=BOTH)
# configure scrollbar
text_scroll.config(command=my_text.yview)

# Creating menu bar
my_menu = Menu(root)
root.config(menu=my_menu)

# adding file menu
file_menu = Menu(my_menu, tearoff=False, font=("Bahnschrift Light Condensed", 13), bg="#f9f9f9")
my_menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_command(label="Save as", command=save_as_file)
file_menu.add_separator()
file_menu.add_command(label="Print", command=print_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

# adding edit menu
edit_menu = Menu(my_menu, tearoff=False, font=("Bahnschrift Light Condensed", 13), bg="#f9f9f9")
my_menu.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Cut", command=Cut)
edit_menu.add_command(label="Copy", command=Copy)
edit_menu.add_command(label="Paste", command=Paste)
edit_menu.add_separator()
edit_menu.add_command(label="Undo", command=Undo)
edit_menu.add_command(label="Redo", command=Redo)
edit_menu.add_separator()
edit_menu.add_command(label="Select all", command=select_all)
edit_menu.add_command(label="Clear all", command=clear_all)

# adding color menu
color_menu = Menu(my_menu, tearoff=False, font=("Bahnschrift Light Condensed", 13), bg="#f9f9f9")
my_menu.add_cascade(label="Color", menu=color_menu)
color_menu.add_command(label="Font color", command=text_color)
color_menu.add_command(label="Foreground color", command=foreground_color)
color_menu.add_command(label="Background color", command=background_color)

# adding option menu
option_menu = Menu(my_menu, tearoff=False, font=("Bahnschrift Light Condensed", 13), bg="#f9f9f9")
my_menu.add_cascade(label="Option", menu=option_menu)
option_menu.add_command(label="Dark mode", command=dark_mode)
option_menu.add_command(label="Light mode", command=light_mode)

# adding help menu
help_menu = Menu(my_menu, tearoff=False, font=("Bahnschrift Light Condensed", 13), bg="#f9f9f9")
my_menu.add_cascade(label="Help", menu=help_menu)
help_menu.add_command(label="About text editor", command=About)

# creating buttons
bold_button = Button(tool_bar_frame, text="B", command=bold_texts, bd=0, relief=FLAT, bg="#f3f3f3", activebackground="#f3f3f3", font="Cambria 20 bold")
bold_button.place(x=20, y=0)

italic_button = Button(tool_bar_frame, text="I", command=italic_texts, bd=0, relief=FLAT, bg="#f3f3f3", activebackground="#f3f3f3", font="Cambria 20 bold italic")
italic_button.place(x=70, y=0)

text_color_button = Button(tool_bar_frame, text="A", command=text_color, bd=0, relief=FLAT, bg="#f3f3f3", activebackground="#f3f3f3", font="arial 18 bold underline")
text_color_button.place(x=120, y=1)

root.mainloop()
