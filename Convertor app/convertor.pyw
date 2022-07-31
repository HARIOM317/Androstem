# Importing all useful packages
import datetime
from threading import Thread
from tkinter import *
from tkinter import filedialog, messagebox

# handling exception if system is not connected throw internet
try:
    from pywhatkit import image_to_ascii_art
except:
    pass
import PyPDF2
import pyttsx3
import cv2
import os


# it will open that file which will convert video to audio
def open_video_to_audio():
    os.startfile("A:\\My Projects\\Android Subsystem for Windows (Python)\\Convertor app\\video_to_audio.py")


# threading in video_to_gif function
def open_video_to_gif():
    os.startfile("A:\\My Projects\\Android Subsystem for Windows (Python)\\Convertor app\\video_to_gif.py")


# threading in video_to_gif function
def threading_pdf_to_audio():
    t1 = Thread(target=converting_pdf_to_audio)
    t1.start()


# function for converting pdf to audio files
def converting_pdf_to_audio():
    book = filedialog.askopenfilename(title="Select PDF")
    try:
        if not os.path.exists("A:\\My Projects\\Android Subsystem for Windows (Python)\\Convertor app\\PDF to AudioFiles"):
            os.mkdir("A:\\My Projects\\Android Subsystem for Windows (Python)\\Convertor app\\PDF to AudioFiles")

        root.title("Converting... (It may take some time. Please don't perform any other operation!)")

        pdfreader = PyPDF2.PdfFileReader(book)
        pages = pdfreader.numPages
        current_time = datetime.datetime.now().strftime("%d%m%y%H%M%S")

        player = pyttsx3.init('sapi5')
        voices = player.getProperty('voices')
        player.setProperty('voice', voices[2].id)
        player.setProperty('rate', 150)

        name = f"AudioFile_{current_time}"

        if not os.path.exists(f"A:\\My Projects\\Android Subsystem for Windows (Python)\\Convertor app\\PDF to AudioFiles\\{name}"):
            os.mkdir('A:\\My Projects\\Android Subsystem for Windows (Python)\\Convertor app\\PDF to AudioFiles\\'+name)

        for num in range(0, pages):
            page = pdfreader.getPage(num)
            text = page.extractText()
            player.runAndWait()
            player.save_to_file(text, f'A:\\My Projects\\Android Subsystem for Windows (Python)\\Convertor app\\PDF to AudioFiles\\{name}\\AudioFile_page_{num}.mp3')

        messagebox.showinfo("PDF to AudioFiles", "All AudioFiles created and saved successfully in (A:\\My Projects\\Android Subsystem for Windows (Python)\\Convertor app\\PDF to AudioFiles) location.")
        root.title("Convertor")
    except:
        messagebox.showerror("PDF to AudioFiles", "Something went wrong!")
        root.title("Convertor")


# threading in image_to_ascii function
def threading_image_to_ascii():
    t1 = Thread(target=converting_image_to_ascii)
    t1.start()


# function for converting image to ascii
def converting_image_to_ascii():
    try:
        if not os.path.exists("A:\\My Projects\\Android Subsystem for Windows (Python)\\Convertor app\\Image to ASCII"):
            os.mkdir("A:\\My Projects\\Android Subsystem for Windows (Python)\\Convertor app\\Image to ASCII")
        img = filedialog.askopenfilename(title="Select an Image")
        root.title("Converting... (It may take some time)")
        current_time = datetime.datetime.now().strftime("%d%m%y%H%M%S")
        image_to_ascii_art(img, f'A:\\My Projects\\Android Subsystem for Windows (Python)\\Convertor app\\Image to ASCII\\ASCII_Art_{current_time}')

        root.title("Convertor")
        messagebox.showinfo("Image to ASCII", "File saved successfully in (A:\\My Projects\\Android Subsystem for Windows (Python)\\Convertor app\\Image to ASCII) location")
    except:
        root.title("Convertor")
        messagebox.showerror("Image to ASCII", "Something went wrong or Please check your internet connection")
# _______________________________________________________________________


# function for converting image in cartoon effects
def converting_image_to_cartoon():
    try:
        if not os.path.exists("A:\\My Projects\\Android Subsystem for Windows (Python)\\Convertor app\\Cartoon images"):
            os.mkdir("A:\\My Projects\\Android Subsystem for Windows (Python)\\Convertor app\\Cartoon images")

        photo = filedialog.askopenfilename(title="Select image")
        img = cv2.imread(photo)

        grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        grey = cv2.medianBlur(grey, 5)
        edges = cv2.adaptiveThreshold(grey, 225, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9)

        color = cv2.bilateralFilter(img, 9, 250, 250)
        cartoon = cv2.bitwise_and(color, color, mask=edges)

        # cartoon
        cv2.imshow("Image", img)
        cv2.imshow("Cartoon", cartoon)

        current_time = datetime.datetime.now().strftime("%d%m%y%H%M%S")
        # Saving image
        cv2.imwrite(f"A:\\My Projects\\Android Subsystem for Windows (Python)\\Convertor app\\Cartoon images\\cartoon_{current_time}.jpg", cartoon)
        cv2.waitKey(0)
        messagebox.showinfo("Image to Cartoon", "Image saved successfully in (A:\\My Projects\\Android Subsystem for Windows (Python)\\Convertor app\\Cartoon images) directory.")
    except:
        messagebox.showerror("Image to Cartoon", "Something went wrong!")


# opening text_to_handwriting program
def open_text_to_handwriting():
    os.startfile("A:\\My Projects\\Android Subsystem for Windows (Python)\\Mini apps\\Text to Handwriting\\Handwritting.pyw")


# opening image to sketch program
def open_image_to_sketch():
    os.startfile("A:\\My Projects\\Android Subsystem for Windows (Python)\\Convertor app\\Image to Sketch Convertor.pyw")


# opening currency convertor program
def open_currency_convertor():
    os.startfile("A:\\My Projects\\Android Subsystem for Windows (Python)\\Currency Convertor\\Currency converter.pyw")


# Starting point
if __name__ == '__main__':
    # Creating GUI
    root = Tk()
    root.title("Convertor")
    root.geometry("1000x500")
    root.resizable(False, False)
    root.wm_iconbitmap("A:\\My Projects\\Android Subsystem for Windows (Python)\\Convertor app\\Convertor_icon.ico")
    root.attributes('-alpha', 0.97)  # Transparent 3% or 0.03%

    # Loading all button images
    video_to_audio = PhotoImage(file="A:\\My Projects\\Android Subsystem for Windows (Python)\\Convertor app\\Icons\\video_to_audio.png")
    video_to_gif = PhotoImage(file="A:\\My Projects\\Android Subsystem for Windows (Python)\\Convertor app\\Icons\\video_to_gif.png")
    pdf_to_audio = PhotoImage(file="A:\\My Projects\\Android Subsystem for Windows (Python)\\Convertor app\\Icons\\pdf_to_audio.png")
    text_to_handwriting = PhotoImage(file="A:\\My Projects\\Android Subsystem for Windows (Python)\\Convertor app\\Icons\\text_to_handwriting.png")
    image_to_cartoon = PhotoImage(file="A:\\My Projects\\Android Subsystem for Windows (Python)\\Convertor app\\Icons\\image_to_cartoon.png")
    image_to_ascii = PhotoImage(file="A:\\My Projects\\Android Subsystem for Windows (Python)\\Convertor app\\Icons\\image_to_ascii.png")
    image_to_sketch = PhotoImage(file="A:\\My Projects\\Android Subsystem for Windows (Python)\\Convertor app\\Icons\\image_to_sketch.png")
    currency_convertor = PhotoImage(file="A:\\My Projects\\Android Subsystem for Windows (Python)\\Convertor app\\Icons\\currency_convertor.png")

    # creating all buttons
    Button(root, text="Video to Audio", image=video_to_audio, compound=TOP, width=244, height=244, bd=1, relief=GROOVE, bg='#ffc700', activebackground='#ffc700', command=open_video_to_audio).grid(row=0, column=0)
    Button(root, text="Video to GIF", image=video_to_gif, compound=TOP, width=244, height=244, bd=1, relief=GROOVE, bg="gold", activebackground='gold', command=open_video_to_gif).grid(row=0, column=1)
    Button(root, text="PDF to Audio", image=pdf_to_audio, compound=TOP, width=244, height=244, bd=1, relief=GROOVE, bg='orange', activebackground='orange', command=threading_pdf_to_audio).grid(row=0, column=2)
    Button(root, text="Text to Handwriting", image=text_to_handwriting, compound=TOP, width=244, height=244, bd=1, relief=GROOVE, bg="yellow", activebackground='yellow', command=open_text_to_handwriting).grid(row=0, column=3)
    Button(root, text="Image to Cartoon", image=image_to_cartoon, compound=TOP, width=244, height=244, bd=1, relief=GROOVE, bg='yellow', activebackground='yellow', command=converting_image_to_cartoon).grid(row=1, column=0)
    Button(root, text="Image to ASCII", image=image_to_ascii, compound=TOP, width=244, height=244, bd=1, relief=GROOVE, bg="orange", activebackground='orange', command=threading_image_to_ascii).grid(row=1, column=1)
    Button(root, text="Image to Sketch", image=image_to_sketch, compound=TOP, width=244, height=244, bd=1, relief=GROOVE, bg='gold', activebackground='gold', command=open_image_to_sketch).grid(row=1, column=2)
    Button(root, text="Currency Convertor", image=currency_convertor, compound=TOP, width=244, height=244, bd=1, relief=GROOVE, bg="#ffc700", activebackground='#ffc700', command=open_currency_convertor).grid(row=1, column=3)

    root.mainloop()
