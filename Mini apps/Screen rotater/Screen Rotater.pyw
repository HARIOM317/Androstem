from tkinter import *
import rotatescreen

def Screen_rotation(side):
    screen = rotatescreen.get_primary_display()
    if side == 'up':
        screen.set_landscape()
    elif side == 'right':
        screen.set_portrait_flipped()
    elif side == 'down':
        screen.set_landscape_flipped()
    elif side == 'left':
        screen.set_portrait()

root = Tk()
root.title("Screen Rotater")
root.geometry("300x300+450+150")
root.config(bg='#202020')
root.resizable(False, False)
root.wm_iconbitmap("A:\\My Projects\\Android Subsystem for Windows (Python)\\Mini apps\\Screen rotater\\rotate-screen_icon.ico")

Label(root, text="Recommended", font="Aparajita 12", fg="sky blue", bg="#202020").place(x=107, y=30)
Button(root, text="Up", command=lambda: Screen_rotation('up'), bg='#2b2b2b', fg='white', font='Georgia 18 italic', width=5, bd=2, relief=RIDGE, cursor='hand2', activebackground="#2b2b2b", activeforeground="white").grid(row=0, column=1, pady=(55, 10), padx=10)
Button(root, text="Left", command=lambda: Screen_rotation('left'), bg='#2b2b2b', fg='white', font='Georgia 18 italic', width=5, bd=2, relief=RIDGE, cursor='hand2', activebackground="#2b2b2b", activeforeground="white").grid(row=1, column=0, pady=10, padx=10)
Button(root, text="Right", command=lambda: Screen_rotation('right'), bg='#2b2b2b', fg='white', font='Georgia 18 italic', width=5, bd=2, relief=RIDGE, cursor='hand2', activebackground="#2b2b2b", activeforeground="white").grid(row=1, column=2, pady=10, padx=10)
Button(root, text="Down", command=lambda: Screen_rotation('down'), bg='#2b2b2b', fg='white', font='Georgia 18 italic', width=5, bd=2, relief=RIDGE, cursor='hand2', activebackground="#2b2b2b", activeforeground="white").grid(row=2, column=1, pady=10, padx=10)

root.mainloop()