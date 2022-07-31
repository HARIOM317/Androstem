from tkinter import *
from tkinter import colorchooser

# Create select color function to select an extra color from color menu
def select_color():
    add_color = colorchooser.askcolor(title="Select Color")
    global color
    color = add_color[1]

# Create locate_xy function
def locate_xy(work):
    global current_x, current_y
    current_x = work.x
    current_y = work.y

# Create addLine function for drawing a line
def addLine(work):
    global current_x, current_y
    canvas.create_line((current_x, current_y, work.x, work.y), width=get_current_value(), fill=color, capstyle=ROUND, smooth=True)
    current_x, current_y = work.x, work.y

# Create show_color function for choose a color
def show_color(new_color):
    global color
    color = new_color

# Creare erase_all function for erase all drawing
def erase_all():
    canvas.delete('all')
    display_pallete()

# create display_pallete function for displaying color palletes
def display_pallete():
    id = colors.create_rectangle((10, 10, 30, 30), fill='Black')
    colors.tag_bind(id, '<Button-1>', lambda x: show_color('Black'))

    id = colors.create_rectangle((40, 10, 60, 30), fill='#6D351A')
    colors.tag_bind(id, '<Button-1>', lambda x: show_color('#6D351A'))

    id = colors.create_rectangle((70, 10, 90, 30), fill='gray')
    colors.tag_bind(id, '<Button-1>', lambda x: show_color('gray'))

    id = colors.create_rectangle((100, 10, 120, 30), fill='orange')
    colors.tag_bind(id, '<Button-1>', lambda x: show_color('orange'))

    id = colors.create_rectangle((130, 10, 150, 30), fill='#FF0800')
    colors.tag_bind(id, '<Button-1>', lambda x: show_color('#FF0800'))

    id = colors.create_rectangle((160, 10, 180, 30), fill='#8F00FF')
    colors.tag_bind(id, '<Button-1>', lambda x: show_color('#8F00FF'))

    id = colors.create_rectangle((190, 10, 210, 30), fill='#08E8DE')
    colors.tag_bind(id, '<Button-1>', lambda x: show_color('#08E8DE'))

    id = colors.create_rectangle((220, 10, 240, 30), fill='yellow')
    colors.tag_bind(id, '<Button-1>', lambda x: show_color('yellow'))

    id = colors.create_rectangle((250, 10, 270, 30), fill='green')
    colors.tag_bind(id, '<Button-1>', lambda x: show_color('green'))

    id = colors.create_rectangle((280, 10, 300, 30), fill='#DFFF00')
    colors.tag_bind(id, '<Button-1>', lambda x: show_color('#DFFF00'))

    id = colors.create_rectangle((310, 10, 330, 30), fill='blue')
    colors.tag_bind(id, '<Button-1>', lambda x: show_color('blue'))

    id = colors.create_rectangle((340, 10, 360, 30), fill='#F0F8FF')
    colors.tag_bind(id, '<Button-1>', lambda x: show_color('#F0F8FF'))

# create get_current_value function for getting the current thickness of brush
def get_current_value():
    return '{: .2f}'.format(current_value.get())

# create slider_changed function for change the color thickness
def slider_changed(event):
    value_label.config(text=get_current_value())

# Start execution of program from here
if __name__ == '__main__':
    root = Tk()
    root.title("White Board")
    root.geometry("1050x600+100+20")
    root.attributes('-alpha', 0.97)  # Transparant 3% or 0.03%
    root.config(bg="#f2f3f5")
    root.resizable(False, False)

    current_x = 0
    current_y = 0
    color = 'black'

    # Set Icon
    root.wm_iconbitmap("A:\\My Projects\\Android Subsystem for Windows (Python)\\White board\\whiteboard_icon.ico")

    # Create color boxes area
    color_boxes = PhotoImage(file="A:\\My Projects\\Android Subsystem for Windows (Python)\\White board\\color section.png")
    Label(root, image=color_boxes, bg="#f2f3f5").place(x=270, y=520)

    # create eraser
    eraser = PhotoImage(file='A:\\My Projects\\Android Subsystem for Windows (Python)\\White board\\eraser.png')
    Button(root, image=eraser, bg='white', bd=0, activebackground='white', command=erase_all, cursor='hand2').place(x=680, y=536)

    # create a add more color button
    add_color_image = PhotoImage(file='A:\\My Projects\\Android Subsystem for Windows (Python)\\White board\\Add-colorpng.png')
    Button(root, image=add_color_image, command=select_color, bd=0, bg='#f2f3f5', cursor='hand2').place(x=850, y=525)

    # Create a canvas for putting the color boxes in it
    colors = Canvas(root, bg="#ffffff", width=368, height=37, bd=0, cursor='hand2')
    colors.place(x=300, y=540)

    # calling display_pallete function
    display_pallete()

    # create working area
    canvas = Canvas(root, width=1026, height=510, background='white')
    canvas.place(x=10, y=10)
    # Bind working area with mouse left click and mouse motion
    canvas.bind("<Button-1>", locate_xy)
    canvas.bind("<B1-Motion>",addLine )

    # _______________ Create Slider ______________
    current_value = DoubleVar()
    slider = Scale(root, from_=1, to=100, orient=HORIZONTAL, command=slider_changed, variable=current_value, length=200, width=10, troughcolor='#FAF0BE', fg='red', activebackground='orange', digits=True, cursor='hand2', bg='#f2f3f5', relief=FLAT, bd=1, sliderrelief=RIDGE, sliderlength=10)
    slider.set(5)
    slider.place(x=50, y=530)

    # value label
    value_label = Label(root, text=get_current_value(), bg='#f2f3f5')
    value_label.place(x=5, y=546)

    root.mainloop()