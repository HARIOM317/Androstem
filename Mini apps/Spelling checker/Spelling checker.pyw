# Importing libraries
from tkinter import *
from tkinter.messagebox import showinfo
from textblob import TextBlob
from pydictionary import Dictionary
from threading import Thread


# threading
def threading_check_spelling():
    t1 = Thread(target=check_spelling)
    t1.start()


# Creating check_spelling function for checking correct spelling and show its synonyms and antonyms
def check_spelling():
    try:
        # Get enter word
        word = enter_text.get()

        # initialize variable of TextBlob class
        a = TextBlob(word)
        # Get correct word in right object
        right = str(a.correct())

        # Updating labels and frames
        correct_label.config(text="Correct Text")
        synonyms_frame.config(text="Synonyms", bd=2, relief=RIDGE)
        antonyms_frame.config(text="Antonyms", bd=2, relief=RIDGE)
        correct_spelling.config(text=right)

        # Get synonyms and antonyms of correct word
        dict = Dictionary(right)
        synonyms_list = dict.synonyms()
        antonyms_list = dict.antonyms()
        synonyms.config(text=str(synonyms_list))
        antonyms.config(text=str(antonyms_list))
    except EncodingWarning:
        showinfo("Internet Connection", "Please check your internet connection")


if __name__ == '__main__':
    # Creating window
    root = Tk()
    root.title("Spelling Checker")
    root.geometry("800x550+250+40")
    root.config(bg='#dae6f6')
    root.wm_iconbitmap("A:\\My Projects\\Android Subsystem for Windows (Python)\\Mini apps\\Spelling checker\\spellchecker_icon.ico")
    # Set heading
    heading = Label(root, text="Spelling Checker", font=("Monotype Corsiva", 40), bg='#dae6f6', fg='#364971')
    heading.pack()
    # Set entry box
    enter_text = Entry(root, justify=CENTER, width=30, font=("Cambria", 25), bg='white', border=0, relief=FLAT, highlightcolor='#00a9ff', highlightthickness=2, highlightbackground='#00deff')
    enter_text.bind("<Return>", lambda e: threading_check_spelling())
    enter_text.pack(pady=10)
    enter_text.focus()
    # Set check button
    button = Button(root, text="Check", font=('Bahnschrift Light Condensed', 20, 'bold'), fg='black', bg='light blue', bd=0.5, relief=SOLID, activebackground='sky blue', command=threading_check_spelling, cursor='hand2')
    button.pack()
    # Set correct text label
    correct_label = Label(root, text="", font=("Georgia", 15), bg="#dae6f6", fg="#364971")
    correct_label.pack(pady=(20, 0))
    # Set correct spelling
    correct_spelling = Label(root, font=("Georgia", 35, 'bold'), bg="#dae6f6", fg='#364971')
    correct_spelling.pack()

    # Creating frame for synonyms
    synonyms_frame = LabelFrame(root, font="Georgia 15", bg="#dae6f6", bd=0)
    synonyms_frame.pack(pady=(20, 10), anchor="w", padx=50)
    # Showing synonyms as message
    synonyms = Message(synonyms_frame, text="", bd=0, relief=GROOVE, font=("Aparajita", 20, 'italic'), fg='dark red', width=750, bg="#dae6f6")
    synonyms.pack(padx=10, pady=10)

    # Creating frame for antonyms
    antonyms_frame = LabelFrame(root, font="Georgia 15", bg="#dae6f6", bd=0)
    antonyms_frame.pack(anchor='w', padx=50)
    # Showing antonyms as message
    antonyms = Message(antonyms_frame, text="", bd=0, relief=GROOVE, font=("Aparajita", 20, 'italic'), fg='dark red', width=750, bg="#dae6f6")
    antonyms.pack(padx=10, pady=10)

    root.mainloop()