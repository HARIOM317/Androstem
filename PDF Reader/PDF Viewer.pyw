# Import useful library
from tkinter import *
from threading import *
from tkinter import filedialog, messagebox
from tkinter.filedialog import *
from tkPDFViewer import tkPDFViewer as pdf
import PyPDF2
from PyPDF2 import PdfFileMerger, PdfFileReader
from pathlib import Path
import os
import pyttsx3
from gtts import gTTS
from googletrans import Translator
from fpdf import FPDF

# ____________________***** Create pdf from txt file *****____________________


# Creating crete_txt_to_pdf function for creating pdf file from txt file of one page (only)
def create_txt_to_pdf():
    show_label.config(text="Creating...")
    name = filename_txt2pdf.get()
    try:
        if not os.path.exists(f'A:\\My Projects\\Android Subsystem for Windows (Python)\\PDF Reader\\Txt to PDF'):
            os.mkdir(f"A:\\My Projects\\Android Subsystem for Windows (Python)\\PDF Reader\\Txt to PDF")
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Times")
        filepath = filedialog.askopenfilename(filetypes=[("Txt Files", "*.txt")])
        fd = open(filepath, 'r')
        for i in fd:
            pdf.cell(50, 10, txt=i, ln=1, align='L')
        pdf.output(f"A:\\My Projects\\Android Subsystem for Windows (Python)\\PDF Reader\\Txt to PDF\\{name}.pdf")
        messagebox.showinfo("PDF", "Pdf has been created successfully!")
    except:
        messagebox.showinfo("PDF", "No such file found!")
        show_label.config(text="")
    show_label.config(text="")


# Handling threading of create_txt_to_pdf function
def Threading_txt_to_pdf():
    try:
        t1 = Thread(target=create_txt_to_pdf)
        t1.start()
    except:
        messagebox.showerror("PDF Viewer", "Something went wrong!")


# Create GUI (Labels, Frames, Buttons etc.) of txt to pdf
def txt_to_pdf():
    main_frame = Frame(root, bd=5, bg='#f0f0f0', width=730, height=630)
    main_frame.place(x=100, y=0)

    top_frame = Frame(main_frame, width=720, height=50, bg='#0063b1')
    top_frame.place(x=0, y=20)
    Label(top_frame, text="Create .txt file into .pdf file", bg='#0063b1', font=("Gabriola", 25), fg='#00F6FA').place(x=230, y=-8)
    Label(main_frame, text="File name", font=("Bahnschrift Light Condensed", 15, 'bold')).place(x=10, y=100)
    global filename_txt2pdf
    filename_txt2pdf = Entry(main_frame, width=25, font=("Bahnschrift Light Condensed", 15), bd=2, relief=GROOVE, fg='dark red')
    filename_txt2pdf.place(x=100, y=100)
    txt2pdf_button = Button(main_frame, text="Choose file", font=("Bahnschrift Light Condensed", 15, 'bold'), bd=2, relief=GROOVE, cursor='hand2', command=Threading_txt_to_pdf)
    txt2pdf_button.place(x=10, y=150)

    global show_label
    show_label = Label(main_frame, text="", font=("Monotype Corsiva", 25), fg="Orange")
    show_label.place(x=300, y=250)

# ____________________***** Create pdf from docx file *****____________________


# Creating crete_docx_to_pdf function for creating pdf file from docx file
def create_docx_to_pdf():
    os.startfile("A:\\My Projects\\Android Subsystem for Windows (Python)\\PDF Reader\\docx_to_pdf.py")


# Create GUI (Labels, Frames, Buttons etc.) of docx to pdf
def docx_to_pdf():
    main_frame = Frame(root, bd=5, bg='#f0f0f0', width=730, height=630)
    main_frame.place(x=100, y=0)

    top_frame = Frame(main_frame, width=720, height=50, bg='#0063b1')
    top_frame.place(x=0, y=20)
    Label(top_frame, text="Create .docx file into .pdf file", bg='#0063b1', font=("Gabriola", 25), fg='#00F6FA').place(x=225, y=-8)

    docx2pdf_button = Button(main_frame, text="Choose file", font=("Bahnschrift Light Condensed", 15, 'bold'), bd=2, relief=GROOVE, cursor='hand2', command=create_docx_to_pdf)
    docx2pdf_button.place(x=320, y=120)


# ____________________***** Create document from pdf file *****____________________


# Creating crete_pdf_to_docx function for creating docx file from pdf file
def create_pdf_to_docx():
    os.startfile("A:\\My Projects\\Android Subsystem for Windows (Python)\\PDF Reader\\pdf_to_docx.py")


# Create GUI (Labels, Frames, Buttons etc.) of pdf to docx
def pdf_to_docx():
    main_frame = Frame(root, bd=5, bg='#f0f0f0', width=730, height=630)
    main_frame.place(x=100, y=0)

    top_frame = Frame(main_frame, width=720, height=50, bg='#0063b1')
    top_frame.place(x=0, y=20)
    Label(top_frame, text="Create .pdf file into .docx file", bg='#0063b1', font=("Gabriola", 25), fg='#00F6FA').place(x=225, y=-8)

    pdf2docx_button = Button(main_frame, text="Choose file", font=("Bahnschrift Light Condensed", 15, 'bold'), bd=2, relief=GROOVE, cursor='hand2', command=create_pdf_to_docx)
    pdf2docx_button.place(x=320, y=120)


# Create the function for making pdf files using txt file and docx file
def create_pdf_file():
    main_frame = Frame(root, bd=5, bg='#f0f0f0', width=730, height=630)
    main_frame.place(x=100, y=0)

    Button(main_frame, text="Txt to Pdf (Only Single Page)", font=("Monotype Corsiva", 20), width=50, pady=5, cursor='hand2', bd=2, relief=GROOVE, command=txt_to_pdf).place(x=5, y=50)
    Button(main_frame, text="Docx to Pdf", font=("Monotype Corsiva", 20), width=50, pady=5, cursor='hand2', bd=2, relief=GROOVE, command=docx_to_pdf).place(x=5, y=120)
    Button(main_frame, text="Pdf to Docx", font=("Monotype Corsiva", 20), width=50, pady=5, cursor='hand2', bd=2, relief=GROOVE, command=pdf_to_docx).place(x=5, y=190)


# making a list for storing path of merging pdfs
filelist = []
# initializing pdf_merger object
pdf_merger = PdfFileMerger()


# Create function for exiting the program
def exit_program():
    message = messagebox.showinfo("Pdf reader", "Exiting program \nYour data may be loss!")
    if message == 'ok':
        root.destroy()


# Create help function to show help messagebox for help
def help_():
    messagebox.showinfo("Help", '''Click on 'Open' to open a pdf file and 'Exit' to exit program.
    
    If you want to merge more then 2 pdf files than you can use 'Merge PDF' function.
            
    Audiobook: you can also make audiobook if your pdf file is written in english, and also you can convert it into hindi
            
            
    NOTE: Audiobook will be create page by page of pdf in a specific folder.
    It means that number of audio files depends that how many pages are available in your pdf file
    
    You can also create pdf using txt file and docx file and from pdf file you can also create document file''')


# Define browsFiles function to read the pdf file
def browsFiles():
    main_frame = Frame(root, bd=5, bg='#f0f0f0', width=730, height=630)
    main_frame.place(x=100, y=0)
    try:
        filename = filedialog.askopenfilename(title="Select PDF File", filetypes=(("PDF File", "*.pdf"), ("PDF File", "*.PDF")))
        v1 = pdf.ShowPdf()
        v2 = v1.pdf_view(root, pdf_location=open(filename, 'r'), width=75, height=38)
        v2.place(x=180, y=0)
    except Exception as e:
        home()
        messagebox.showerror("Open Pdf", "No such file found!")


# Create open_file function to open file dialog box to select a file for merging
def open_file(files):
    filepath = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])
    if not (filepath and Path(filepath).exists()):
        return
    files.append(filepath)
    # list out all filenames on screen
    label1["text"] = '\n'.join(str(f) for f in files)
    if len(files) >= 2 and merge_button['state'] == "disabled":
        merge_button["state"] = "normal"


# Create merge function to merge pdf files
def merge(files):
    for f in files:
        pdf_merger.append(PdfFileReader(open(f, "rb")))
    output_filename = entry_output_name.get()

    if not output_filename:
        output_filename = "Untitled.pdf"
    elif ".pdf" not in output_filename:
        output_filename += ".pdf"

    if not os.path.exists(f'A:\\My Projects\\Android Subsystem for Windows (Python)\\PDF Reader\\Merged PDF'):
        os.mkdir(f"A:\\My Projects\\Android Subsystem for Windows (Python)\\PDF Reader\\Merged PDF")

    pdf_merger.write(f"A:\\My Projects\\Android Subsystem for Windows (Python)\\PDF Reader\\Merged PDF\\{output_filename}")
    messagebox.showinfo("Merge pdf files", "merged successfully!")


# Create merge_pdf_files function to make frontend of merge pdf option
def merge_pdf_files():
    main_frame = Frame(root, bd=5, bg='#f0f0f0', width=730, height=630)
    main_frame.place(x=100, y=0)

    frame1 = Frame(main_frame, bd=0, bg='#f0f0f0')
    open_button = Button(main_frame, text="Open file", command=lambda: open_file(filelist), font=("Monotype Corsiva", 20, 'bold'), bd=2, relief=GROOVE, cursor='hand2')
    open_button.place(x=12, y=16)
    global label1
    label1 = Label(frame1, text="", font=("Garamond", 13))
    label1.grid(row=1, column=0, pady=75)
    frame1.place(x=10, y=10)

    frame2 = Frame(main_frame, bd=0, bg='#f0f0f0')
    label2 = Label(frame2, text="File name", font=("Gabriola", 20, 'bold'))
    label2.grid(row=0, column=0, sticky="ew", padx="5", pady="5")
    global entry_output_name
    entry_output_name = Entry(frame2, width=25, bd=2, relief=GROOVE, font=("Garamond", 18), fg='dark red')
    entry_output_name.grid(row=0, column=1, sticky="ew", padx=(0, 5))
    global merge_button
    merge_button = Button(frame2, text="Merge PDF", state="disabled", command=lambda: merge(filelist), font=("Monotype Corsiva", 20, 'bold'), bd=2, relief=GROOVE, cursor='hand2')
    merge_button.grid(row=0, column=2, sticky="ew", padx=20, pady=5)
    frame2.place(x=145, y=10)


# Create audiobook_english function to make frontend of audiobook in english option
def audiobook_english():
    main_frame = Frame(root, bd=5, bg='#f0f0f0', width=730, height=630)
    main_frame.place(x=100, y=0)

    top_frame = Frame(main_frame, width=720, height=50, bg='#0063b1')
    top_frame.place(x=0, y=20)
    Label(top_frame, text="Create English Audiobook", bg='#0063b1', font=("Gabriola", 25), fg='#00F6FA').place(x=240, y=-8)
    Label(main_frame, text="File name", font=("Bahnschrift Light Condensed", 15, 'bold')).place(x=10, y=100)
    global filename_english
    filename_english = Entry(main_frame, width=25, font=("Bahnschrift Light Condensed", 15), bd=2, relief=GROOVE, fg='dark red')
    filename_english.place(x=100, y=100)
    audiobook_button = Button(main_frame, text="Choose and Convert", font=("Bahnschrift Light Condensed", 15, 'bold'), bd=2, relief=GROOVE, command=Threading_read_english, cursor='hand2')
    audiobook_button.place(x=10, y=150)

    Button(main_frame, text="Hindi Audiobook", font=("Bahnschrift Light Condensed", 15, 'bold'), bd=0, relief=FLAT, fg='dark blue', command=audiobook_hindi, cursor='hand2').place(x=10, y=550)


# Create audiobook_english function to make frontend of audiobook in hindi option
def audiobook_hindi():
    main_frame = Frame(root, bd=5, bg='#f0f0f0', width=730, height=630)
    main_frame.place(x=100, y=0)

    top_frame = Frame(main_frame, width=720, height=50, bg='#0063b1')
    top_frame.place(x=0, y=20)
    Label(top_frame, text="Create Hindi Audiobook", bg='#0063b1', font=("Gabriola", 25), fg='#00F6FA').place(x=240, y=-8)
    Label(main_frame, text="File name", font=("Bahnschrift Light Condensed", 15, 'bold')).place(x=10, y=100)
    global filename_hindi
    filename_hindi = Entry(main_frame, width=25, font=("Bahnschrift Light Condensed", 15), bd=2, relief=GROOVE, fg='dark red')
    filename_hindi.place(x=100, y=100)
    Button(main_frame, text="Choose and Convert", font=("Bahnschrift Light Condensed", 15, 'bold'), bd=2, relief=GROOVE, command=Threading_read_hindi, cursor='hand2').place(x=10, y=150)


# create read_english function to make english audiobooks
def read_english():
    new_frame = Frame(root, width=300, height=50, bg='#f0f0f0')
    new_frame.place(x=300, y=250)
    label = Label(new_frame, text="Creating...", font=("Monotype Corsiva", 25, 'bold'), fg='dark blue', bg="#f0f0f0", bd=0)
    label.place(x=90, y=10)

    book = askopenfilename()

    try:
        pdfreader = PyPDF2.PdfFileReader(book)
        pages = pdfreader.numPages
        global filename_english
        name = filename_english.get()

        player = pyttsx3.init('sapi5')
        voices = player.getProperty('voices')
        player.setProperty('voice', voices[2].id)
        player.setProperty('rate', 150)

        if not name:
            name = "Untitled"

        if not os.path.exists(f'A:\\My Projects\\Android Subsystem for Windows (Python)\\PDF Reader\\English Audiobooks'):
            os.mkdir(f"A:\\My Projects\\Android Subsystem for Windows (Python)\\PDF Reader\\English Audiobooks")
        if not os.path.exists(f"A:\\My Projects\\Android Subsystem for Windows (Python)\\PDF Reader\\English Audiobooks\\{name}"):
            os.mkdir('A:\\My Projects\\Android Subsystem for Windows (Python)\\PDF Reader\\English Audiobooks\\'+name)

        for num in range(0, pages):
            page = pdfreader.getPage(num)
            text = page.extractText()
            player.runAndWait()
            player.save_to_file(text, f'A:\\My Projects\\Android Subsystem for Windows (Python)\\PDF Reader\\English Audiobooks\\{name}\\{name}_page_{num}.mp3')

        label.config(text="")
        messagebox.showinfo("Audiobook", "Audiobook created successfully")
    except:
        label.config(text="")
        messagebox.showinfo("Open file", "No such file found!")


def Threading_read_english():
    try:
        t1 = Thread(target=read_english)
        t1.start()
    except:
        messagebox.showerror("Alarm", "Something went wrong!")


def Threading_read_hindi():
    try:
        t1 = Thread(target=read_hindi)
        t1.start()
    except:
        messagebox.showerror("Alarm", "Something went wrong!")


# create read_english function to make hindi audiobooks
def read_hindi():
    new_frame = Frame(root, width=300, height=50, bg='#f0f0f0')
    new_frame.place(x=300, y=250)
    label = Label(new_frame, text="Creating...", font=("Monotype Corsiva", 25, 'bold'), fg='dark blue', bg="#f0f0f0", bd=0)
    label.place(x=90, y=10)

    mybook = askopenfilename()

    try:
        book = open(mybook, 'rb')
        pdfreader = PyPDF2.PdfFileReader(book)
        pages = pdfreader.getNumPages()
        name = filename_hindi.get()

        if not name:
            name = "Untitled"

        if not os.path.exists(f'A:\\My Projects\\Android Subsystem for Windows (Python)\\PDF Reader\\Hindi Audiobooks'):
            os.mkdir(f"A:\\My Projects\\Android Subsystem for Windows (Python)\\PDF Reader\\Hindi Audiobooks")
        if not os.path.exists(f"A:\\My Projects\\Android Subsystem for Windows (Python)\\PDF Reader\\Hindi Audiobooks\\{name}"):
            os.mkdir('A:\\My Projects\\Android Subsystem for Windows (Python)\\PDF Reader\\Hindi Audiobooks\\' + name)

        try:
            for num in range(0, pages):
                page = pdfreader.getPage(num)
                text = page.extractText()
                lang = 'hindi'
                if 'hindi' in lang:
                    transl = Translator()
                    texthindi = transl.translate(text, 'hi')
                    textm = texthindi.text
                    speech = gTTS(text=textm)
                    speech.save(f'A:\\My Projects\\Android Subsystem for Windows (Python)\\PDF Reader\\Hindi Audiobooks\\{name}\\{name}_page_{num}.mp3')
        except:
            messagebox.showerror("Hindi Audiobook", "Something went wrong \nCheck your internet connection!")

        label.config(text="")
        messagebox.showinfo("Hindi Audiobook", "Hindi Audiobook created successfully")
    except:
        label.config(text="")
        messagebox.showerror("Open pdf", "No such file found!")


# Creating a home function
def home():
    main_frame = Frame(root, bd=5, bg='#f0f0f0', width=730, height=630)
    main_frame.place(x=100, y=0)
    Button(main_frame, text="Open", font="Gabriola 25 bold", bd=2, relief=GROOVE, cursor='hand2', pady=0, padx=10, fg='dark blue', bg="#f6f6f6", command=browsFiles).place(x=300, y=25)
    Message(main_frame, text="Pdf Viewer", font=("Pristina", 80, 'bold'), fg="dark blue", bd=0, relief=RIDGE, width=600, bg="#f0f0f0").place(x=100, y=250)


# Program starting point
if __name__ == '__main__':
    # Create a root object of Tk class
    root = Tk()
    root.geometry('850x630+100+5')
    root.title("PDF Viewer")
    root.config(bg="#f0f0f0")
    root.attributes('-alpha', 0.97)
    root.resizable(False, False)
    root.wm_iconbitmap('A:\\My Projects\\Android Subsystem for Windows (Python)\\PDF Reader\\PDF_Icon.ico')

    # Creating side frame
    f1 = Frame(root, width=80, height=650, bg='#0e71c4')
    f1.place(x=0, y=0)

    # Creating side buttons
    def button(x, y, text, activbcolor, bcolor, cmd):
        def on_press(e):
            myButton1['background'] = activbcolor
            myButton1['foreground'] = 'white'

        def on_leave(e):
            myButton1['background'] = bcolor
            myButton1['foreground'] = '#FFFFF0'

        myButton1 = Button(f1, text=text, width=10, justify=CENTER, fg='white', bd=0, bg=bcolor, activeforeground='white', activebackground=activbcolor, command=cmd, font=("Bahnschrift Light Condensed", 14), pady=5, anchor='w', cursor='hand2')

        myButton1.bind('<Enter>', on_press)
        myButton1.bind('<Leave>', on_leave)
        myButton1.place(x=x, y=y)


    # set buttons in side menu bar
    button(0.5, 10, "Home", '#0765a2', '#0e71c4', home)
    button(0.5, 50, "Open PDF", '#0765a2', '#0e71c4', browsFiles)
    button(0.5, 90, "Create PDF", '#0765a2', '#0e71c4', create_pdf_file)
    button(0.5, 130, "Merge PDF", '#0765a2', '#0e71c4', merge_pdf_files)
    button(0.5, 170, "Audiobook", '#0765a2', '#0e71c4', audiobook_english)
    button(0.5, 210, "Help", '#0765a2', '#0e71c4', help_)
    button(0.5, 250, "Exit", '#0765a2', '#0e71c4', exit_program)

    # Calling the home function
    home()

    root.mainloop()
