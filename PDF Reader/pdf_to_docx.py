import os
from pdf2docx import Converter
from datetime import datetime
from tkinter import filedialog, messagebox

name = datetime.now().strftime("%d%H%M%S")
try:
    if not os.path.exists(f'A:\\My Projects\\Android Subsystem for Windows (Python)\\PDF Reader\\PDF to Docx'):
        os.mkdir(f"A:\\My Projects\\Android Subsystem for Windows (Python)\\PDF Reader\\PDF to Docx")
    filepath = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])
    cv = Converter(filepath)
    cv.convert(f"A:\\My Projects\\Android Subsystem for Windows (Python)\\PDF Reader\\PDF to Docx\\Document_{name}.docx")
    cv.close()
    messagebox.showinfo("PDF", "Pdf has been created successfully!")
except:
    messagebox.showinfo("PDF", "No such file found!")
