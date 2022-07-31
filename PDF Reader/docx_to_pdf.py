from docx2pdf import convert
import os
from tkinter import filedialog, messagebox
from datetime import datetime

name = datetime.now().strftime("%d%H%M%S")
try:
    if not os.path.exists(f'A:\\My Projects\\Android Subsystem for Windows (Python)\\PDF Reader\\Docx to PDF'):
        os.mkdir(f"A:\\My Projects\\Android Subsystem for Windows (Python)\\PDF Reader\\Docx to PDF")
    filepath = filedialog.askopenfilename(filetypes=[("Document Files", "*.docx")])
    convert(filepath, f'A:\\My Projects\\Android Subsystem for Windows (Python)\\PDF Reader\\Docx to PDF\\pdf_{name}.pdf')
    messagebox.showinfo("PDF", "Pdf has been created successfully!")
except:
    messagebox.showinfo("PDF", "No such file found!")
