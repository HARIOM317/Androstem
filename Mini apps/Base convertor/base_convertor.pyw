from tkinter import *
from tkinter import ttk, messagebox


# creating convert function for converting the base of given number
def convert():
    try:
        # updating labels and frame
        ans_frame.config(bd=2, relief=GROOVE, bg="#faffe9")
        binary_label.config(bg="#faffe9", text="Binary")
        binary_value.config(bg="#faffe9")
        octal_label.config(bg="#faffe9", text="Octal")
        octal_value.config(bg="#faffe9")
        decimal_label.config(bg="#faffe9", text="Decimal")
        decimal_value.config(bg="#faffe9")
        hexadecimal_label.config(bg="#faffe9", text="Hexadecimal")
        hexadecimal_value.config(bg="#faffe9")

        # converting base
        def number_to_decimal(number_, base_):
            decimal = int(number_, base_)
            binary = bin(decimal)
            octal = oct(decimal)
            hexadecimal = hex(decimal)
            # set values
            binary_value.config(text=str(binary[2:]), fg="black")
            octal_value.config(text=str(octal[2:]), fg="black")
            decimal_value.config(text=str(decimal), fg="black")
            hexadecimal_value.config(text=str(hexadecimal[2:]).upper(), fg="black")

        base = combobox.get()
        number = entry_value.get()

        if base == "BINARY":
            base = 2
        elif base == "OCTAL":
            base = 8
        elif base == "DECIMAL":
            base = 10
        else:
            base = 16

        number_to_decimal(number, base)
    except:
        messagebox.showinfo("Base convertor", "Invalid value")
        binary_value.config(text="None", fg='Gray')
        octal_value.config(text="None", fg='Gray')
        decimal_value.config(text="None", fg='Gray')
        hexadecimal_value.config(text="None", fg='Gray')


if __name__ == '__main__':
    # creating GUI
    root = Tk()
    root.title("Numeric base convertor")
    root.geometry("400x600+500+10")
    root.resizable(False, False)
    root.config(bg="#ffffff")
    root.wm_iconbitmap("A:\\My Projects\\Android Subsystem for Windows (Python)\\Mini apps\\Base convertor\\base_convertor_icon.ico")

    # frame for title
    title_frame = Frame(root, width=400, height=100, background="#fafafa", padx=10, border=2, relief=RIDGE)
    title_frame.pack(padx=10, pady=10)

    # frame for combobox, entry box and button
    main_frame = Frame(root, width=400, height=500, background="#f0f0f0", pady=10, border=1, relief=SOLID)
    main_frame.pack(padx=10, pady=(0, 10))

    # frame for answer
    ans_frame = Frame(main_frame, width=400, height=290, background="#f0f0f0", pady=10)
    ans_frame.pack(padx=5, pady=(180, 0))

    # set title frame with title
    title = Label(title_frame, text="Numeric base convertor", anchor=CENTER, font=("Pristina", 30, 'bold'), bg="#fafafa", fg='dark blue', width=400, pady=10)
    title.pack()

    # creating combobox
    bases = ['BINARY', 'OCTAL', 'DECIMAL', 'HEXADECIMAL']
    combobox = ttk.Combobox(main_frame, width=12, justify=CENTER, font=("Bahnschrift Light Condensed", 15), values=bases)
    combobox.set("DECIMAL")
    combobox.place(x=30, y=10)

    # creating entry box
    entry_value = Entry(main_frame, width=15, justify=CENTER, font=("Bahnschrift Light Condensed", 15), highlightthickness=1, relief=SOLID, border=1)
    entry_value.bind("<Return>", lambda e: convert())
    entry_value.place(x=225, y=10)

    # creating button
    convert_button = Button(main_frame, text="Convert", bg='#00afff', bd=1, relief=SOLID, font=("Bahnschrift Light Condensed", 20), overrelief=SUNKEN, command=convert, cursor='hand2', activebackground="#00afff")
    convert_button.place(x=145, y=60)

    # Number labels
    binary_label = Label(ans_frame, text="", width=12, anchor='nw', font=("Bahnschrift Light Condensed", 20), bg='#f0f0f0')
    binary_label.place(x=5, y=10)
    octal_label = Label(ans_frame, text="", width=12, anchor='nw', font=("Bahnschrift Light Condensed", 20), bg='#f0f0f0')
    octal_label.place(x=5, y=80)
    decimal_label = Label(ans_frame, text="", width=12, anchor='nw', font=("Bahnschrift Light Condensed", 20), bg='#f0f0f0')
    decimal_label.place(x=5, y=150)
    hexadecimal_label = Label(ans_frame, text="", width=12, anchor='nw', font=("Bahnschrift Light Condensed", 20), bg='#f0f0f0')
    hexadecimal_label.place(x=5, y=220)

    # value labels
    binary_value = Label(ans_frame, text="", width=28, anchor='nw', font=("Bahnschrift Light Condensed", 15), bg='#f0f0f0')
    binary_value.place(x=130, y=15)
    octal_value = Label(ans_frame, text="", width=28, anchor='nw', font=("Bahnschrift Light Condensed", 15), bg='#f0f0f0')
    octal_value.place(x=130, y=85)
    decimal_value = Label(ans_frame, text="", width=28, anchor='nw', font=("Bahnschrift Light Condensed", 15), bg='#f0f0f0')
    decimal_value.place(x=130, y=155)
    hexadecimal_value = Label(ans_frame, text="", width=28, anchor='nw', font=("Bahnschrift Light Condensed", 15), bg='#f0f0f0')
    hexadecimal_value.place(x=130, y=225)

    root.mainloop()
