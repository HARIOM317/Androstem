# Import useful packages
from tkinter import *
from threading import *
from tkinter import messagebox
from tkinter import ttk
from googletrans import Translator, LANGUAGES
import pyttsx3
import speech_recognition as sr

# initialize pyttsx3
engine = pyttsx3.init()


# handle threading of speak_input_text function
def Threading_speak_input():
    try:
        t1 = Thread(target=speak_input_text)
        t1.start()
    except:
        messagebox.showerror("Google Translator", "Something went wrong!")

# Create speak_input_text function to speak the input text
def speak_input_text():
    text = input_text.get(1.0, END)
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[2].id)
    engine.setProperty('rate', 150)
    engine.say(text)
    engine.runAndWait()

# handle threading of speak_output_text function
def Threading_speak_output():
    try:
        t1 = Thread(target=speak_output_text)
        t1.start()
    except:
        messagebox.showerror("Google Translator", "Something went wrong!")

# Create speak_output_text function to speak the ouotput text
def speak_output_text():
    text = output_text.get(1.0, END)
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[2].id)
    engine.setProperty('rate', 150)
    engine.say(text)
    engine.runAndWait()

# Create speak function to speak query
def speak(audio):
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[2].id)
    engine.setProperty('rate', 150)
    engine.say(audio)
    engine.runAndWait()

# handle threading of TakeCommand function for mic
def Threading_mic():
    try:
        t1 = Thread(target=TakeCommand)
        t1.start()
    except:
        messagebox.showerror("Google Translator", "Something went wrong!")

# Create TakeCommand function for using the mic
def TakeCommand():
    lang = combobox_source.get()
    source_lang = lang[0:2]
    r = sr.Recognizer()
    with sr.Microphone() as source:
        speak("Listening...")
        r.adjust_for_ambient_noise(source)  # Remove source noise
        r.pause_threshold = 1
        audio = r.listen(source)    # Listen user query
    try:
        speak("Recognizing...")
        query = r.recognize_google(audio, language=source_lang)
        speak(f"You mean, {query}")

    except Exception as e:
        messagebox.showinfo("Google translator", "Sorry sir I didn't understand what you said. Please try again.")
        return "None"

    input_text.delete(1.0, END)
    input_text.insert(END, query)
    answer()
    return query

# Define Change_Language function to change the language
def Change_Language(text="Type", src="English", dest="Hindi"):
    # Store the data
    text1 = text
    src1 = src
    dest1 = dest
    trans = Translator()
    trans1 = trans.translate(text, src=src1, dest=dest)
    return trans1.text

def Threading_answer():
    try:
        t1 = Thread(target=answer)
        t1.start()
    except:
        messagebox.showerror("Google Translator", "Something went wrong!")

# Create answer function for getting the translated result
def answer():
    try:
        source = combobox_source.get()
        destination = combobox_destination.get()
        msg = input_text.get(1.0, END)
        getText = Change_Language(text=msg, src=source, dest=destination)
        output_text.delete(1.0, END)
        output_text.insert(END, getText)
    except Exception as e:
        messagebox.showerror("Google translator", "Something went wrong")

# Define exchange function to exchange both languages
def exchange():
    v1 = combobox_source.get()
    v2 = combobox_destination.get()
    combobox_source.set(v2)
    combobox_destination.set(v1)


# Start execution from here
if __name__ == '__main__':
    # Create instance of Tk class
    root = Tk()
    root.title("Google Translator")     # Set Title
    root.geometry("1050x620+100+0")       # Set layout
    root.config(bg="#303946")       # Set Background color
    root.attributes('-alpha', 0.98)  # Transparent 2% or 0.02%
    root.wm_iconbitmap("A:\\My Projects\\Android Subsystem for Windows (Python)\\Google Translator\\google_translator_icon.ico")

    # Set a heading
    heading = Label(root, text="Google Translator", bg="#303946", fg='white', font=("Pristina", 35))
    heading.pack()

    # Create mic button and set image on it
    mic_image = PhotoImage(file='A:\\My Projects\\Android Subsystem for Windows (Python)\\Google Translator\\mic.png')
    mic_button = Button(root, image=mic_image, command=Threading_mic, bg='#303946', activebackground="#16a6ff", bd=0, cursor='hand2').place(x=20, y=20)

    # Create some frames
    input_frame = Frame(root).pack(side=BOTTOM)
    output_frame = Frame(root).pack(side=BOTTOM)
    bottom_frame = Frame(root).pack(side=BOTTOM)

    # _________________________________ INPUT AREA __________________________________

    # Create input label to set Input
    input_label = Label(root, text="Input", font=("Monotype Corsiva", 25), bg="#303946", fg="gold")
    input_label.pack()

    # setr speak image in speak_image variable
    speak_image = PhotoImage(file='A:\\My Projects\\Android Subsystem for Windows (Python)\\Google Translator\\speaker.png')
    # Create speak_input_button to speak input text
    speak_input_button = Button(input_frame, image=speak_image, command=Threading_speak_input, bg="#303946", bd=0, activebackground='#16a6ff', cursor='hand2')
    speak_input_button.pack()

    # Create input text to write input text for translating it into another language
    input_text = Text(input_frame, font=("Aparajita", 15), wrap=WORD, fg="#ffffff", height=5, bg='#212834', bd=2, relief=RIDGE, padx=10)
    input_text.pack(padx=100, pady=(5, 0), fill=X)

    # _________________________________ OUTPUT AREA __________________________________

    # Create output label to set Output
    output_label = Label(root, text="Output", font=("Monotype Corsiva", 25), bg="#303946", fg="gold")
    output_label.pack()

    # Create speak_output_button to speak output text
    speak_output_button = Button(output_frame, image=speak_image, command=Threading_speak_output, bg="#303946", bd=0, activebackground='#16a6ff', cursor='hand2')
    speak_output_button.pack()

    # Create output text to write output text after translating it into another language
    output_text = Text(output_frame, font=("Aparajita", 15), wrap=WORD, fg="#ffffff", height=5, bg='#212834', bd=2, relief=RIDGE, padx=10)
    output_text.pack(padx=100, pady=(5, 0), fill=X)

    # set all languages in a list
    language_list = list(LANGUAGES.values())

    # create first combobox to show all available languages
    combobox_source = ttk.Combobox(bottom_frame, values=language_list, height=5, width=10, font="Georgia 10")
    combobox_source.pack(side=LEFT, anchor='ne', padx=100, pady=20)    # Set position of combobox
    combobox_source.set("english")  # Set english as default value of combo box

    # create second combobox to show all available languages
    combobox_destination = ttk.Combobox(bottom_frame, values=language_list, height=5, width=10, font="Georgia 10")
    combobox_destination.pack(side=RIGHT, anchor='ne', padx=100, pady=20)    # Set position of combobox
    combobox_destination.set("hindi")  # Set hindi as default value of combo box

    # Create exchange button and set image on it
    exchange_image = PhotoImage(file='A:\\My Projects\\Android Subsystem for Windows (Python)\\Google Translator\\exchange.png')
    exchange_language_button = Button(bottom_frame, image=exchange_image, command=exchange, bg='#303946', bd=0, activebackground='#303946', cursor='hand2')
    exchange_language_button.pack()

    # Create translate button
    translate_button = Button(bottom_frame, text="Translate", command=Threading_answer, bg='#303946', fg='orange', font=("Gabriola", 40, 'bold'), bd=0, activeforeground='gold', activebackground='#303946', relief=FLAT, cursor='hand2')
    translate_button.pack()

    root.mainloop()
