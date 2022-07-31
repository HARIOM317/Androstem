# Import useful library
from tkinter import *
from tkinter.messagebox import *
import math

# A useful variables
font = ('Book Antiqua', 18)


# create EnterClick function to handle click event
def EnterClick(event):
    e = Event()
    e.widget = equal_button
    click_button(e)


# create a click_button function for doing any operation on normal calculator
def click_button(event):
    e = Event()
    global scValue
    text = event.widget.cget("text")

    # Set all the conditions for normal calculator
    if text == "^":
        textField.insert(END, "**")
        return
    elif text == '=':
        if scValue.get().isdigit():
            value = int(scValue.get())
        else:
            try:
                value = eval(textField.get())
            except Exception as e:
                print(e)
                value = "Invalid Syntax"
                showerror("Error", e)
        scValue.set(value)
        textField.update()
    elif text == 'AC':
        scValue.set("")
        textField.update()
    elif text == '×':
        ex = textField.get()
        ex = ex[0:len(ex)-1]
        textField.delete(0, END)
        textField.insert(0, ex)
    else:
        scValue.set(scValue.get() + text)
        textField.update()


# Creating a window
root = Tk()
root.resizable(False, False)
root.title("Calculator")
root.config(bg='#e4e4e4')
root.wm_iconbitmap("A:\\My Projects\\Android Subsystem for Windows (Python)\\Calculator\\CalculatorIcon.ico")
root.geometry("247x398+600+20")
root.attributes('-alpha', 0.98)     # Transparent 2% or 0.02%

# create Text field
scValue = StringVar()
scValue.set("")
textField = Entry(root, textvariable=scValue, font="'Aparajita' 14", justify=RIGHT, relief=FLAT, fg='#002147', bg="#e4e4e4")
textField.pack(side=TOP, pady=10, padx=10, fill=X)

# <<<<<<<<<< Create Frame for All Buttons >>>>>>>>>>
Button_Frame = Frame(root)
Button_Frame.pack(side=TOP)

# _________________________________ NORMAL CALCULATOR __________________________________

# Add all button
clear_button = Button(Button_Frame, text='AC', font=font, width=3, pady=5, padx=5, relief=RIDGE, bg="orange", activebackground="orange", bd=0.5, activeforeground='white')
clear_button.grid(row=0, column=0)
clear_button.bind("<Button-1>", click_button)

bracket = Button(Button_Frame, text='()', font=font, width=3, pady=5, padx=5, relief=RIDGE, bg="#323846", fg="white", activebackground="#323846", bd=0.5, activeforeground='white')
bracket.grid(row=0, column=1)
bracket.bind("<Button-1>", click_button)

power2_button = Button(Button_Frame, text='**2', font=font, width=3, pady=5, padx=5, relief=RIDGE, bg="#323846", fg="white", activebackground="#323846", bd=0.5, activeforeground='white')
power2_button.grid(row=0, column=2)
power2_button.bind("<Button-1>", click_button)

back_button = Button(Button_Frame, text='×', font=font, width=3, pady=5, padx=5, relief=RIDGE, bg="#323846", fg='white', activebackground="#323846", bd=0.5, activeforeground='white')
back_button.grid(row=0, column=3)
back_button.bind("<Button-1>", click_button)

# Create 1 - 9 buttons using a loop
temp = 1
for i in range(1, 4):
    for j in range(3):
        num_button = Button(Button_Frame, text=str(temp), font=font, width=3, pady=5, padx=5, relief=RIDGE, bd=0.5)
        num_button.grid(row=i, column=j)
        temp += 1
        num_button.bind("<Button-1>", click_button)

double_zero_button = Button(Button_Frame, text='00', font=font, width=3, pady=5, padx=5, relief=RIDGE, bd=0.5)
double_zero_button.grid(row=4, column=0)
double_zero_button.bind("<Button-1>", click_button)

zero_button = Button(Button_Frame, text='0', font=font, width=3, pady=5, padx=5, relief=RIDGE, bd=0.5)
zero_button.grid(row=4, column=1)
zero_button.bind("<Button-1>", click_button)

double_slash_button = Button(Button_Frame, text='//', font=font, width=3, pady=5, padx=5, relief=RIDGE, bd=0.5)
double_slash_button.grid(row=4, column=2)
double_slash_button.bind("<Button-1>", click_button)

devide_button = Button(Button_Frame, text='/', font=font, width=3, pady=5, padx=5, relief=RIDGE, fg="white", bg='#2f4155', activebackground="#2f4155", activeforeground="white", bd=0.5)
devide_button.grid(row=1, column=3)
devide_button.bind("<Button-1>", click_button)

multiply_button = Button(Button_Frame, text='*', font=font, width=3, pady=5, padx=5, relief=RIDGE, fg="white", bg='#2f4155', activebackground="#2f4155", activeforeground="white", bd=0.5)
multiply_button.grid(row=2, column=3)
multiply_button.bind("<Button-1>", click_button)

minus_button = Button(Button_Frame, text='-', font=font, width=3, pady=5, padx=5, relief=RIDGE, fg="white", bg='#2f4155', activebackground="#2f4155", activeforeground="white", bd=0.5)
minus_button.grid(row=3, column=3)
minus_button.bind("<Button-1>", click_button)

plus_button = Button(Button_Frame, text='+', font=font, width=3, pady=5, padx=5, relief=RIDGE, fg="white", bg='#2f4155', activebackground="#2f4155", activeforeground="white", bd=0.5)
plus_button.grid(row=4, column=3)
plus_button.bind("<Button-1>", click_button)

remainder_button = Button(Button_Frame, text='%', font=font, width=3, pady=5, padx=5, relief=RIDGE, bg='sky blue', activebackground='sky blue', bd=0.5)
remainder_button.grid(row=5, column=0)
remainder_button.bind("<Button-1>", click_button)

power_button = Button(Button_Frame, text='^', font=font, width=3, pady=5, padx=5, relief=RIDGE, bg='sky blue', activebackground='sky blue', bd=0.5)
power_button.grid(row=5, column=1)
power_button.bind("<Button-1>", click_button)

dot_button = Button(Button_Frame, text='.', font=font, width=3, pady=5, padx=5, relief=RIDGE, bg='sky blue', activebackground='sky blue', bd=0.5)
dot_button.grid(row=5, column=2)
dot_button.bind("<Button-1>", click_button)

equal_button = Button(Button_Frame, text='=', font=font, width=3, pady=5, padx=5, relief=RIDGE, bg='dark blue', activebackground='dark blue', bd=0.5, fg='white', activeforeground='sky blue')
equal_button.grid(row=5, column=3)
equal_button.bind("<Button-1>", click_button)

textField.bind('<Return>', EnterClick)

# _________________________________ SCIENTIFIC CALCULATOR ______________________________

normal_calc = True


# create a calculate_sc function for doing any operation on scientific calculator
def calculate_sc(event):
    button = event.widget
    text = button['text']
    ex = textField.get()
    global answer
    answer = ''
    # Handle all operations
    try:
        if text == '√':
            answer = str(math.sqrt(float(ex)))

        elif text == 'x^2':
            answer = str(math.pow(float(ex), 2))

        elif text == 'n!':
            answer = str(math.factorial(int(ex)))

        elif text == 'π':
            answer = str(math.pi)

        elif text == 'log':
            answer = str(math.log10(float(ex)))

        elif text == 'ln':
            answer = str(math.log(float(ex)))

        elif text == '|x|':
            if float(ex) < 0:
                answer = str(-1*float(ex))
            elif float(ex) > 0:
                answer = str(float(ex))
            else:
                answer = str(0.0)

        elif text == 'e':
            answer = str(math.e)

        elif text == 'deg':
            answer = str(math.degrees(float(ex)))

        elif text == 'Red':
            answer = str(math.radians(float(ex)))

        elif text == 'exp':
            answer = str(math.exp(float(ex)))

        elif text == 'sin':
            answer = str(math.sin(math.radians(int(ex))))

        elif text == 'cos':
            answer = str(math.cos(math.radians(int(ex))))

        elif text == 'tan':
            answer = str(math.tan(math.radians(int(ex))))

        elif text == 'sin-1':
            answer = str((math.asin((float(ex)))*180)/math.pi)

        elif text == 'cos-1':
            answer = str((math.acos((float(ex))) * 180) / math.pi)

        elif text == 'tan-1':
            answer = str((math.atan((float(ex))) * 180) / math.pi)

        elif text == '1/x':
            answer = str(1/float(ex))
    except Exception as e:
        print(e)
        answer = "Not a number"

    textField.delete(0, END)
    textField.insert(0, answer)


# Create sc_click function to change the size of window when we will click on three dots
def sc_click():
    global normal_calc
    if normal_calc:
        # Scientific calc
        Button_Frame.pack_forget()
        # Add Scientificc calc
        sc_Frame.pack(side=TOP)
        Button_Frame.pack(side=TOP)
        root.geometry("368x547+600+20")
        normal_calc = False
    else:
        sc_Frame.pack_forget()
        root.geometry("247x378+600+20")
        normal_calc = True


sc_Frame = Frame(root)

# Create buttons for scientific calculator
sqrt_button = Button(sc_Frame, text='√', font=font, width=3, pady=5, padx=5, relief=RIDGE, bd=0.5)
sqrt_button.grid(row=0, column=0)
sqrt_button.bind("<Button-1>", calculate_sc)

pow_button = Button(sc_Frame, text='x^2', font=font, width=3, pady=5, padx=5, relief=RIDGE, bd=0.5)
pow_button.grid(row=0, column=1)
pow_button.bind("<Button-1>", calculate_sc)

factorial_button = Button(sc_Frame, text='n!', font=font, width=3, pady=5, padx=5, relief=RIDGE, bd=0.5)
factorial_button.grid(row=0, column=2)
factorial_button.bind("<Button-1>", calculate_sc)

pi_button = Button(sc_Frame, text='π', font=font, width=3, pady=5, padx=5, relief=RIDGE, bd=0.5)
pi_button.grid(row=0, column=3)
pi_button.bind("<Button-1>", calculate_sc)

log_button = Button(sc_Frame, text='log', font=font, width=3, pady=5, padx=5, relief=RIDGE, bd=0.5)
log_button.grid(row=0, column=4)
log_button.bind("<Button-1>", calculate_sc)

ln_button = Button(sc_Frame, text='ln', font=font, width=3, pady=5, padx=5, relief=RIDGE, bd=0.5)
ln_button.grid(row=0, column=5)
ln_button.bind("<Button-1>", calculate_sc)

mod_button = Button(sc_Frame, text='|x|', font=font, width=3, pady=5, padx=5, relief=RIDGE, bg="#fcfdff", bd=0.5, activebackground="#fcfdff")
mod_button.grid(row=1, column=0)
mod_button.bind("<Button-1>", calculate_sc)

e_button = Button(sc_Frame, text='e', font=font, width=3, pady=5, padx=5, relief=RIDGE, bg="#fcfdff", bd=0.5, activebackground="#fcfdff")
e_button.grid(row=1, column=1)
e_button.bind("<Button-1>", calculate_sc)

Rediun_button = Button(sc_Frame, text='Red', font=font, width=3, pady=5, padx=5, relief=RIDGE, bg="#fcfdff", bd=0.5, activebackground="#fcfdff")
Rediun_button.grid(row=1, column=2)
Rediun_button.bind("<Button-1>", calculate_sc)

degree_button = Button(sc_Frame, text='deg', font=font, width=3, pady=5, padx=5, relief=RIDGE, bg="#fcfdff", bd=0.5, activebackground="#fcfdff")
degree_button.grid(row=1, column=3)
degree_button.bind("<Button-1>", calculate_sc)

exp_button = Button(sc_Frame, text='exp', font=font, width=3, pady=5, padx=5, relief=RIDGE, bg="#fcfdff", bd=0.5, activebackground="#fcfdff")
exp_button.grid(row=1, column=4)
exp_button.bind("<Button-1>", calculate_sc)

one_upon_button = Button(sc_Frame, text='1/x', font=font, width=3, pady=5, padx=5, relief=RIDGE, bg="#fcfdff", bd=0.5, activebackground="#fcfdff")
one_upon_button.grid(row=1, column=5)
one_upon_button.bind("<Button-1>", calculate_sc)

sin_button = Button(sc_Frame, text='sin', font=font, width=3, pady=5, padx=5, relief=RIDGE, bd=0.5)
sin_button.grid(row=2, column=0, pady=(0, 3))
sin_button.bind("<Button-1>", calculate_sc)

cos_button = Button(sc_Frame, text='cos', font=font, width=3, pady=5, padx=5, relief=RIDGE, bd=0.5)
cos_button.grid(row=2, column=1, pady=(0, 3))
cos_button.bind("<Button-1>", calculate_sc)

tan_button = Button(sc_Frame, text='tan', font=font, width=3, pady=5, padx=5, relief=RIDGE, bd=0.5)
tan_button.grid(row=2, column=2, pady=(0, 3))
tan_button.bind("<Button-1>", calculate_sc)

inverse_sin_button = Button(sc_Frame, text='sin-1', font=font, width=3, pady=5, padx=5, relief=RIDGE, bd=0.5)
inverse_sin_button.grid(row=2, column=3, pady=(0, 3))
inverse_sin_button.bind("<Button-1>", calculate_sc)

inverse_cos_button = Button(sc_Frame, text='cos-1', font=font, width=3, pady=5, padx=5, relief=RIDGE, bd=0.5)
inverse_cos_button.grid(row=2, column=4, pady=(0, 3))
inverse_cos_button.bind("<Button-1>", calculate_sc)

inverse_tan_button = Button(sc_Frame, text='tan-1', font=font, width=3, pady=5, padx=5, relief=RIDGE, bd=0.5)
inverse_tan_button.grid(row=2, column=5, pady=(0, 3))
inverse_tan_button.bind("<Button-1>", calculate_sc)

menubar = Menu(root)
mode = Menu(menubar, tearoff=0, font=("default", 10), fg='dark blue', bg='white', activebackground='white', activeforeground='red', relief=FLAT)
mode.add_checkbutton(label="Scientific Calculator", command=sc_click)   # Add a check button

menubar.add_cascade(label="●●●", menu=mode)

root.config(menu=menubar)

root.mainloop()
