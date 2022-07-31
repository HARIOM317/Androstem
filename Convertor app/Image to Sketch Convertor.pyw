# import all the required modules
from tkinter import *
from tkinter import filedialog, messagebox
import numpy as np
import imageio
import scipy.ndimage
import cv2
import os


# function for opening filedialog box
def open_image():
    global file
    file = filedialog.askopenfilename()


# function for convert image into sketch
def convert():
    try:
        root.title("Converting...")
        # get name from entry widget
        name = file_name.get()
        # if name is not given by user then default name is default.png
        if name == "":
            name = "default"

        # if directory is not exist then create the directory
        if not os.path.exists("A:\\My Projects\\Android Subsystem for Windows (Python)\\Convertor app\\Image to Sketch"):
            os.mkdir("A:\\My Projects\\Android Subsystem for Windows (Python)\\Convertor app\\Image to Sketch")

        # read image
        ss = imageio.imread(file)
        gray_color = rgb2gray(ss)

        i = 255 - gray_color

        # for converting image into a blur image
        blur = scipy.ndimage.filters.gaussian_filter(i, sigma=13)

        # calling the function
        r = front_back(blur, gray_color)

        # save image
        cv2.imwrite(f'A:\\My Projects\\Android Subsystem for Windows (Python)\\Convertor app\\Image to Sketch\\{name}.png', r)

        root.title("Convert Image to Sketch art")
        # show message
        messagebox.showinfo("Image to Sketch", "Successfully converted and saved in (A:/My Projects/Android Subsystem for Windows (Python)/Convertor app/Image to Sketch) directory")
    except:
        root.title("Convert Image to Sketch art")
        messagebox.showerror("Image to Sketch", "Something went wrong!")


# function to convert image into sketch
def rgb2gray(rgb):
    return np.dot(rgb[..., :3], [0.2989, 0.5870, .1140])


def front_back(front, back):
    final_sketch = front * 255 / (255 - back)
    final_sketch[final_sketch > 255] = 255
    final_sketch[back == 255] = 255
    return final_sketch.astype('uint8')


# starting point
if __name__ == '__main__':
    # creating GUI
    root = Tk()
    root.geometry("500x300+450+100")
    root.title("Convert Image to Sketch art")
    root.config(bg="#ffffff")
    root.resizable(False, False)
    root.wm_iconbitmap("A:\\My Projects\\Android Subsystem for Windows (Python)\\Convertor app\\Convertor_icon.ico")

    # top frame for title
    top_frame = Frame(root, width=500, height=100, bg='#f0f0f0')
    top_frame.pack(pady=5, padx=5)

    # bottom frame
    bottom_frame = Frame(root, width=500, height=250, bg='#fafafa', bd=1, relief=SOLID)
    bottom_frame.pack(pady=5, padx=5)

    Label(top_frame, text="Convert image to sketch", font=("Bahnschrift Light Condensed", 15), bg="#f0f0f0", bd=2, relief=GROOVE, padx=10, pady=5).pack()

    Label(bottom_frame, text="File name", font=("Bahnschrift Light Condensed", 15), bg="#fafafa").place(x=10, y=10)
    # entry box for file name
    file_name = Entry(bottom_frame, width=30, font=("Bahnschrift Light Condensed", 15), bd=1, relief=SOLID)
    file_name.place(x=115, y=10)
    # button for browsing image
    browse_button = Button(bottom_frame, text="Browse", font=("Bahnschrift Light Condensed", 15), bd=2, relief=GROOVE, bg="#fafafa", activebackground="#fafafa", cursor='hand2', command=open_image)
    browse_button.place(x=400, y=5)

    # button for converting image into sketch
    Button(bottom_frame, text="Convert", font=("Bahnschrift Light Condensed", 25), bd=1, relief=GROOVE, bg="#fafafa", activebackground="#fafafa", cursor='hand2', command=convert).pack(side=BOTTOM, pady=(100, 60), padx=180)

    root.mainloop()
