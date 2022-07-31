# Importing useful packages
from tkinter import *
from tkinter.messagebox import showinfo
from threading import Thread
from tkinter.ttk import Combobox
import os
# handle exception in pywhatkit
try:
    import pywhatkit
except:
    pass

# Creating window
root = Tk()
root.geometry("1300x800+300+30")
root.resizable(False, False)
root.title("Convert text to handwriting")
root.wm_iconbitmap("A:/My Projects/Android Subsystem for Windows (Python)/Mini apps/Text to Handwriting/handwriting_icon.ico")

# Text box
typing_text = Text(root, wrap=WORD, undo=True, bd=0.5, relief=SOLID, font=("Bahnschrift SemiLight Condensed", 15), padx=20, pady=20, height=15)
typing_text.pack(side=BOTTOM, fill=X, padx=20, pady=(55, 20))


# threading in handwriting function
def threading_handwriting():
    t1 = Thread(target=create_handwritten_notes)
    t1.start()


# function for converting text to handwriting
def create_handwritten_notes():
    try:
        if not os.path.exists(f'A:/My Projects/Android Subsystem for Windows (Python)/Mini apps/Text to Handwriting/Handwritten assignment'):
            os.mkdir(f"A:/My Projects/Android Subsystem for Windows (Python)/Mini apps/Text to Handwriting/Handwritten assignment")
        color = combobox.get()
        if color == 'blue':
            color = (0, 0, 138)
        elif color == 'black':
            color = (0, 0, 0)
        else:
            color = (230, 63, 50)
        name = filename.get()
        text = typing_text.get('1.0', END)
        saving_label.config(text="Saving...")
        pywhatkit.text_to_handwriting(text, f"A:/My Projects/Android Subsystem for Windows (Python)/Mini apps/Text to Handwriting/Handwritten assignment/{name}.png", color)
        saving_label.config(text="")
        showinfo("Handwriting", "Successfully saved!")
    except:
        saving_label.config(text="")
        showinfo("Handwriting", "Something went wrong!")


# label 1
Label(root, text="Color", font=("Bahnschrift SemiLight Condensed", 15)).pack(side=LEFT, pady=20, padx=(50, 0))

# combobox for color
combobox = Combobox(root, values=['blue', 'black', 'red'], width=10, height=3, font=("Bahnschrift SemiLight Condensed", 15))
combobox.pack(side=LEFT, padx=20, pady=20)
combobox.set('blue')

# label 2
Label(root, text="File name", font=("Bahnschrift SemiLight Condensed", 15)).pack(side=LEFT, pady=20, padx=(230, 0))
filename = Entry(root, width=20, font=("Bahnschrift SemiLight Condensed", 15), bd=0.5, relief=SOLID)
filename.pack(side=LEFT, padx=20, pady=20)

# save button
save_button = Button(root, text="Save", command=threading_handwriting, font=("Bahnschrift SemiLight Condensed", 15), padx=12, bg='#f3ece8', activebackground='#f3ece8', borderwidth=2, relief=RIDGE, cursor='hand2')
save_button.pack(side=LEFT, padx=(230, 50), pady=20)

saving_label = Label(root, text="", fg='dark blue', font=("Bahnschrift SemiLight Condensed", 15))
saving_label.place(x=20, y=150)

root.mainloop()
