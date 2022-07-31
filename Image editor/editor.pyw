# Importing required packages
from tkinter import *
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk, ImageEnhance
import numpy as np
from threading import Thread
import imageio
import scipy.ndimage
import cv2
import os
from datetime import datetime

# declaring global variables
filename = ""
originalImage = ""


# function for yellow effect
def yellow_effect():
    try:
        opencvImage = cv2.cvtColor(np.array(originalImage), cv2.COLOR_RGB2BGR)
        opencvImage[:, :, 0] = 20
        global output_image
        output_image = Image.fromarray(cv2.cvtColor(opencvImage, cv2.COLOR_BGR2RGB))
        displayImage(output_image)
    except:
        pass


# function for black and white effect
def black_and_white_effect():
    try:
        opencvImage = cv2.cvtColor(np.array(originalImage), cv2.COLOR_BGR2GRAY)
        global output_image
        output_image = Image.fromarray(cv2.cvtColor(opencvImage, cv2.COLOR_GRAY2BGR))
        displayImage(output_image)
    except:
        pass


# function for blue and green effect
def blue_effect():
    try:
        opencvImage = cv2.cvtColor(np.array(originalImage), cv2.COLOR_RGB2BGR)
        opencvImage[:, :, 2] = 300
        global output_image
        output_image = Image.fromarray(cv2.cvtColor(opencvImage, cv2.COLOR_BGR2RGB))
        displayImage(output_image)
    except:
        pass


# function for pink effect
def pink_effect():
    try:
        opencvImage = cv2.cvtColor(np.array(originalImage), cv2.COLOR_RGB2BGR)
        opencvImage[:, :, 1] = 50
        global output_image
        output_image = Image.fromarray(cv2.cvtColor(opencvImage, cv2.COLOR_BGR2RGB))
        displayImage(output_image)
    except:
        pass


# function for orange effect
def orange_effect():
    try:
        opencvImage = cv2.cvtColor(np.array(originalImage), cv2.COLOR_RGB2BGR)
        opencvImage[:, :, 2] = 150
        global output_image
        output_image = Image.fromarray(cv2.cvtColor(opencvImage, cv2.COLOR_BGR2RGB))
        displayImage(output_image)
    except:
        pass


# function for none effect
def none_effect():
    try:
        opencvImage = cv2.cvtColor(np.array(originalImage), cv2.COLOR_RGB2BGR)
        global output_image
        output_image = Image.fromarray(cv2.cvtColor(opencvImage, cv2.COLOR_BGR2RGB))
        displayImage(output_image)
    except:
        pass


# function for showing image on screen
def displayImage(display_image):
    try:
        global image_width, image_height
        ImagetoDisplay = display_image.resize((520, 520))
        ImagetoDisplay = ImageTk.PhotoImage(ImagetoDisplay)
        showWindow.config(image=ImagetoDisplay)
        showWindow.photo_ref = ImagetoDisplay
        image_height = ImagetoDisplay.height()
        image_width = ImagetoDisplay.width()
        showWindow.place(x=0, y=0)
    except:
        messagebox.showerror("error", "something went wrong!")


# function for importing image
def import_image():
    try:
        global originalImage, filename
        filename = filedialog.askopenfilename()
        originalImage = Image.open(filename)
        displayImage(originalImage)

        brightness_control()

        crop_button.config(state=NORMAL)
        color_button.config(state=NORMAL)
        brush_button.config(state=NORMAL)
        rotate_button.config(state=NORMAL)
        saveButton.config(state=NORMAL)
        effect_Button.config(state=NORMAL)
    except:
        messagebox.showerror("error", "something went wrong!")


# function for saving image
def save_image():
    try:
        save_file = filedialog.asksaveasfile(defaultextension=".jpg")
        output_image.save(save_file)
    except:
        messagebox.showerror("error", "Only .jpg file supported!")


# function for controlling the brightness
def brightness(brightness_pos):
    try:
        brightness_pos = float(brightness_pos)
        global output_image
        enhancer = ImageEnhance.Brightness(originalImage)
        output_image = enhancer.enhance(brightness_pos)
        displayImage(output_image)
    except:
        pass


# function for controlling the contrast
def contrast(contrast_pos):
    try:
        contrast_pos = float(contrast_pos)
        global output_image
        enhancer = ImageEnhance.Contrast(originalImage)
        output_image = enhancer.enhance(contrast_pos)
        displayImage(output_image)
    except:
        pass


# function for controlling the color
def color(color_pos):
    try:
        color_pos = float(color_pos)
        global output_image
        enhancer = ImageEnhance.Color(originalImage)
        output_image = enhancer.enhance(color_pos)
        displayImage(output_image)
    except:
        pass


# function for controlling the sharpness
def sharpness(color_pos):
    try:
        color_pos = float(color_pos)
        global output_image
        enhancer = ImageEnhance.Sharpness(originalImage)
        output_image = enhancer.enhance(color_pos)
        displayImage(output_image)
    except:
        pass


# threading in brightness_control function
def threading_brightness_control():
    t1 = Thread(target=brightness_control)
    t1.start()


# creating GUI for controlling light
def brightness_control():
    my_frame = Frame(root, width=450, height=520, bg="#272727", highlightbackground="#1f1f1f", highlightthickness=2)
    my_frame.place(x=545, y=70)

    Label(my_frame, text="Color", font=("Bahnschrift Light Condensed", 18), bg="#272727", fg="white").place(x=5, y=10)

    brightnessSlider = Scale(my_frame, bg="#272727", fg='white', troughcolor='#484644', label="Brightness", from_=0, to=2, orient=HORIZONTAL, length=400, width=5, sliderlength=10, sliderrelief=FLAT, highlightcolor="#272727", highlightthickness=0, highlightbackground="#272727", bd=0, relief=FLAT, activebackground="#b5adeb", font=("Bahnschrift Light Condensed", 15), command=brightness, resolution=0.01)
    brightnessSlider.set(1)
    brightnessSlider.place(x=23, y=100)

    contrastSlider = Scale(my_frame, bg="#272727", fg='white', troughcolor='#484644', label="Contrast", from_=0, to=2, orient=HORIZONTAL, length=400, width=5, sliderlength=10, sliderrelief=FLAT, highlightcolor="#272727", highlightthickness=0, highlightbackground="#272727", bd=0, relief=FLAT, activebackground="#b5adeb", font=("Bahnschrift Light Condensed", 15), command=contrast, resolution=0.01)
    contrastSlider.set(1)
    contrastSlider.place(x=23, y=200)

    colorSlider = Scale(my_frame, bg="#272727", fg='white', troughcolor='#484644', label="Saturation", from_=0, to=2, orient=HORIZONTAL, length=400, width=5, sliderlength=10, sliderrelief=FLAT, highlightcolor="#272727", highlightthickness=0, highlightbackground="#272727", bd=0, relief=FLAT, activebackground="#b5adeb", font=("Bahnschrift Light Condensed", 15), command=color, resolution=0.01)
    colorSlider.set(1)
    colorSlider.place(x=23, y=300)

    sharpnessSlider = Scale(my_frame, bg="#272727", fg='white', troughcolor='#484644', label="Sharpness", from_=-10, to=10, orient=HORIZONTAL, length=400, width=5, sliderlength=10, sliderrelief=FLAT, highlightcolor="#272727", highlightthickness=0, highlightbackground="#272727", bd=0, relief=FLAT, activebackground="#b5adeb", font=("Bahnschrift Light Condensed", 15), command=sharpness, resolution=0.01)
    sharpnessSlider.set(1)
    sharpnessSlider.place(x=23, y=400)


# threading in brushing function
def threading_brushing():
    t1 = Thread(target=brushing)
    t1.start()


# creating GUI for color effects
def brushing():
    my_frame = Frame(root, width=450, height=520, bg="#272727", highlightbackground="#1f1f1f", highlightthickness=2)
    my_frame.place(x=545, y=70)

    def button(x, y, text, activ_back_color, back_color, cmd):
        def on_press(e):
            myButton1['background'] = activ_back_color
            myButton1['foreground'] = 'white'

        def on_leave(e):
            myButton1['background'] = back_color
            myButton1['foreground'] = 'white'

        myButton1 = Button(my_frame, text=text, command=cmd, cursor='hand2', font=("Bahnschrift Light Condensed", 35), width=10, height=2, bd=2, relief=RIDGE, overrelief=SUNKEN, fg='white', activeforeground='white', bg=back_color, activebackground=activ_back_color, justify=CENTER)

        myButton1.bind('<Enter>', on_press)
        myButton1.bind('<Leave>', on_leave)

        myButton1.place(x=x, y=y)

    button(18, 10, "Yellow", "#393939", "#303030", yellow_effect)
    button(18, 180, "B & W", "#393939", "#303030", black_and_white_effect)
    button(18, 350, "Blue", "#393939", "#303030", blue_effect)

    button(230, 10, "Pink", "#393939", "#303030", pink_effect)
    button(230, 180, "Orange", "#393939", "#303030", orange_effect)
    button(230, 350, "Original", "#393939", "#303030", none_effect)


# function for cropping the image
def crop_image(left, top, right, bottom):
    try:
        global output_image, originalImage, filename
        edit_img = Image.open(filename)
        output_image = edit_img.crop((left, top, image_width - right, image_height - bottom))

        originalImage = ImageTk.PhotoImage(output_image)
        showWindow.config(image=originalImage)

        displayImage(output_image)
    except:
        messagebox.showerror("error", "something went wrong!")


# GUI for image cropper
def cropping(w, h):
    try:
        my_frame = Frame(root, width=450, height=520, bg="#272727", highlightbackground="#1f1f1f", highlightthickness=2)
        my_frame.place(x=545, y=70)

        Label(my_frame, text="Crop", font=("Bahnschrift Light Condensed", 18), bg="#272727", fg="white").place(x=5, y=10)
        Label(my_frame, text="Size should be less than 520x520 for best result", font=("Bahnschrift Light Condensed", 10), bg="#272727", fg="gold").place(x=120, y=15)

        left_scale = Scale(my_frame, bg="#272727", fg='white', troughcolor='#484644', label="Left", from_=0, to=w, orient=HORIZONTAL, length=400, width=5, sliderlength=10, sliderrelief=GROOVE, highlightcolor="#272727", highlightthickness=0, highlightbackground="#272727", bd=0, relief=FLAT, activebackground="#b5adeb", font=("Bahnschrift Light Condensed", 15), command=lambda x: crop_image(left_scale.get(), top_scale.get(), right_scale.get(), bottom_scale.get()))
        left_scale.place(x=23, y=100)

        right_scale = Scale(my_frame, bg="#272727", fg='white', troughcolor='#484644', label="Right", from_=0, to=w, orient=HORIZONTAL, length=400, width=5, sliderlength=10, sliderrelief=GROOVE, highlightcolor="#272727", highlightthickness=0, highlightbackground="#272727", bd=0, relief=FLAT, activebackground="#b5adeb", font=("Bahnschrift Light Condensed", 15),  command=lambda x: crop_image(left_scale.get(), top_scale.get(), right_scale.get(), bottom_scale.get()))
        right_scale.place(x=23, y=200)

        top_scale = Scale(my_frame, bg="#272727", fg='white', troughcolor='#484644', label="Top", from_=0, to=h, orient=HORIZONTAL, length=400, width=5, sliderlength=10, sliderrelief=GROOVE,  highlightcolor="#272727", highlightthickness=0, highlightbackground="#272727", bd=0,  relief=FLAT, activebackground="#b5adeb", font=("Bahnschrift Light Condensed", 15),  command=lambda x: crop_image(left_scale.get(), top_scale.get(), right_scale.get(), bottom_scale.get()))
        top_scale.place(x=23, y=300)

        bottom_scale = Scale(my_frame, bg="#272727", fg='white', troughcolor='#484644', label="Bottom", from_=0, to=h, orient=HORIZONTAL, length=400, width=5, sliderlength=10, sliderrelief=GROOVE, highlightcolor="#272727", highlightthickness=0, highlightbackground="#272727", bd=0, relief=FLAT, activebackground="#b5adeb", font=("Bahnschrift Light Condensed", 15),   command=lambda x: crop_image(left_scale.get(), top_scale.get(), right_scale.get(), bottom_scale.get()))
        bottom_scale.place(x=23, y=400)
    except:
        messagebox.showerror("error", "something went wrong!")


# function for rotating image 90 degree
def rotate_90():
    try:
        global filename
        img = Image.open(filename)
        rotated_image1 = img.rotate(90)
        saving_name = filedialog.asksaveasfile(defaultextension='.jpg')
        rotated_image1.save(saving_name)
        rotated_image1.show()
        messagebox.showinfo("Rotation", "File rotated successfully!")
    except:
        messagebox.showerror("error", "something went wrong!")


# function for rotating image 180 degree
def rotate_180():
    try:
        global filename
        img = Image.open(filename)
        rotated_image1 = img.rotate(180)
        saving_name = filedialog.asksaveasfile(defaultextension='.jpg')
        rotated_image1.save(saving_name)
        rotated_image1.show()
        messagebox.showinfo("Rotation", "File rotated successfully!")
    except:
        messagebox.showerror("error", "something went wrong!")


# function for rotating image 270 degree
def rotate_270():
    try:
        global filename
        img = Image.open(filename)
        rotated_image1 = img.rotate(270)
        saving_name = filedialog.asksaveasfile(defaultextension='.jpg')
        rotated_image1.save(saving_name)
        rotated_image1.show()
        messagebox.showinfo("Rotation", "File rotated successfully!")
    except:
        messagebox.showerror("error", "something went wrong!")


# function for rotating image 360 degree
def rotate_360():
    try:
        global filename
        img = Image.open(filename)
        rotated_image1 = img.rotate(360)
        saving_name = filedialog.asksaveasfile(defaultextension='.jpg')
        rotated_image1.save(saving_name)
        rotated_image1.show()
        messagebox.showinfo("Rotation", "File rotated successfully!")
    except:
        messagebox.showerror("error", "something went wrong!")


# function for rotating image in any angle
def rotate_custom():
    try:
        global filename
        img = Image.open(filename)
        my_angle = angle.get()
        if my_angle == "":
            my_angle = 0
        rotated_image1 = img.rotate(int(my_angle))
        saving_name = filedialog.asksaveasfile(defaultextension='.jpg')
        rotated_image1.save(saving_name)
        rotated_image1.show()
        messagebox.showinfo("Rotation", "File rotated successfully!")
    except:
        messagebox.showerror("error", "something went wrong!")


# GUI for image rotation
def rotation():
    my_frame = Frame(root, width=450, height=520, bg="#272727", highlightbackground="#1f1f1f", highlightthickness=2)
    my_frame.place(x=545, y=70)

    Label(my_frame, text="Custom angle", font=("Bahnschrift Light Condensed", 25), bg="#272727", fg="white").place(x=10, y=380)
    global angle
    angle = Entry(my_frame, font=("Bahnschrift Light Condensed", 25), width=15, bd=0, relief=FLAT, highlightcolor='#00b0ff', highlightbackground='#00f1ff', highlightthickness=1, bg="#1d1d1d", fg='white')
    angle.place(x=220, y=380)

    Button(my_frame, text="Rotate", font=("Bahnschrift Light Condensed", 20), command=rotate_custom, bg="#272727", activebackground="#272727", fg="gold", activeforeground="orange", bd=0, relief=FLAT, cursor='hand2').place(x=190, y=450)

    def button(x, y, text, activ_back_color, back_color, cmd):
        def on_press(e):
            myButton1['background'] = activ_back_color
            myButton1['foreground'] = 'white'

        def on_leave(e):
            myButton1['background'] = back_color
            myButton1['foreground'] = 'white'

        myButton1 = Button(my_frame, text=text, command=cmd, cursor='hand2', font=("Bahnschrift Light Condensed", 35), width=10, height=2, bd=2, relief=RIDGE, overrelief=SUNKEN, fg='white', activeforeground='white', bg=back_color, activebackground=activ_back_color, justify=CENTER)

        myButton1.bind('<Enter>', on_press)
        myButton1.bind('<Leave>', on_leave)

        myButton1.place(x=x, y=y)

    button(18, 10, "90°", "#393939", "#303030", rotate_90)
    button(230, 10, "180°", "#393939", "#303030", rotate_180)
    button(18, 180, "270°", "#393939", "#303030", rotate_270)
    button(230, 180, "360°", "#393939", "#303030", rotate_360)


# function for convert image into sketch
def convert_in_sketch():
    try:
        root.title("Converting...")
        # get name from entry widget
        name = datetime.now().strftime("%d%H%M%S")

        # if directory is not exist then create the directory
        if not os.path.exists("A:\\My Projects\\Android Subsystem for Windows (Python)\\Image editor\\Sketch"):
            os.mkdir("A:\\My Projects\\Android Subsystem for Windows (Python)\\Image editor\\Sketch")

        # read image
        ss = imageio.imread(filename)
        gray_color = rgb2gray(ss)

        i = 255 - gray_color

        # for converting image into a blur image
        blur = scipy.ndimage.filters.gaussian_filter(i, sigma=13)

        # calling the function
        r = front_back(blur, gray_color)

        # save image
        cv2.imwrite(f'A:\\My Projects\\Android Subsystem for Windows (Python)\\Image editor\\Sketch\\Sketch_{name}.png', r)

        root.title("Image editor")
        # show message
        messagebox.showinfo("Image to Sketch", "Successfully converted and saved in (A:/My Projects/Android Subsystem for Windows (Python)/Image editor/Sketch) directory.")
    except:
        root.title("Image editor")
        messagebox.showerror("Image to Sketch", "Something went wrong!")


# function to convert image into sketch
def rgb2gray(rgb):
    return np.dot(rgb[..., :3], [0.2989, 0.5870, .1140])


def front_back(front, back):
    final_sketch = front * 255 / (255 - back)
    final_sketch[final_sketch > 255] = 255
    final_sketch[back == 255] = 255
    return final_sketch.astype('uint8')


# function for converting image in cartoon effects
def image_to_cartoon():
    try:
        if not os.path.exists("A:\\My Projects\\Android Subsystem for Windows (Python)\\Image editor\\Cartoon"):
            os.mkdir("A:\\My Projects\\Android Subsystem for Windows (Python)\\Image editor\\Cartoon")

        photo = filename
        img = cv2.imread(photo)

        grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        grey = cv2.medianBlur(grey, 5)
        edges = cv2.adaptiveThreshold(grey, 225, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9)

        color = cv2.bilateralFilter(img, 9, 250, 250)
        cartoon = cv2.bitwise_and(color, color, mask=edges)

        current_time = datetime.now().strftime("%d%m%y%H%M%S")
        # Saving image
        cv2.imwrite(f"A:\\My Projects\\Android Subsystem for Windows (Python)\\Image editor\\Cartoon\\cartoon_{current_time}.jpg", cartoon)
        cv2.waitKey(0)
        messagebox.showinfo("Image to Cartoon", "Image saved successfully in (A:\\My Projects\\Android Subsystem for Windows (Python)\\Image editor\\Cartoon) directory.")
    except:
        messagebox.showerror("Image to Cartoon", "Something went wrong!")


# GUI for special effects on image like cartoon and sketch
def effects():
    my_frame = Frame(root, width=450, height=520, bg="#272727", highlightbackground="#1f1f1f", highlightthickness=2)
    my_frame.place(x=545, y=70)

    def button(x, y, text, activ_back_color, back_color, cmd):
        def on_press(e):
            myButton1['background'] = activ_back_color
            myButton1['foreground'] = 'white'

        def on_leave(e):
            myButton1['background'] = back_color
            myButton1['foreground'] = 'white'

        myButton1 = Button(my_frame, text=text, command=cmd, cursor='hand2', font=("Bahnschrift Light Condensed", 30), width=25, height=2, bd=2, relief=RIDGE, overrelief=SUNKEN, fg='white', activeforeground='white', bg=back_color, activebackground=activ_back_color, justify=CENTER)

        myButton1.bind('<Enter>', on_press)
        myButton1.bind('<Leave>', on_leave)

        myButton1.place(x=x, y=y)

    button(18, 18, "Sketch", "#393939", "#303030", convert_in_sketch)
    button(18, 168, "Cartoon", "#393939", "#303030", image_to_cartoon)
    button(18, 318, "Normal", "#393939", "#303030", none_effect)


# Creating GUI
root = Tk()
root.geometry("1000x600+120+20")
root.title("Image editor")
root.resizable(False, False)
root.config(bg="#202020")
root.wm_iconbitmap("A:\\My Projects\\Android Subsystem for Windows (Python)\\Image editor\\image_editor.ico")

image_height = 0
image_width = 0

# creating frames
header_frame = Frame(root, width=990, height=50, bg="#1f1f1f", highlightbackground="#1d1d1d", highlightthickness=2)
header_frame.place(x=5, y=5)

left_frame = Frame(root, width=520, height=520, bg="#202020")
left_frame.place(x=5, y=70)

right_frame = Frame(root, width=450, height=520, bg="#272727", highlightbackground="#1f1f1f", highlightthickness=2)
right_frame.place(x=545, y=70)

# Loading icons
brightness_icon = PhotoImage(file="A:\\My Projects\\Android Subsystem for Windows (Python)\\Image editor\\Icons\\brightness.png")
color_brush_icon = PhotoImage(file="A:\\My Projects\\Android Subsystem for Windows (Python)\\Image editor\\Icons\\color_brush.png")
browse_icon = PhotoImage(file="A:\\My Projects\\Android Subsystem for Windows (Python)\\Image editor\\Icons\\browse.png")
save_icon = PhotoImage(file="A:\\My Projects\\Android Subsystem for Windows (Python)\\Image editor\\Icons\\save.png")
crop_icon = PhotoImage(file="A:\\My Projects\\Android Subsystem for Windows (Python)\\Image editor\\Icons\\crop.png")
rotate_icon = PhotoImage(file="A:\\My Projects\\Android Subsystem for Windows (Python)\\Image editor\\Icons\\rotate.png")
effect_icon = PhotoImage(file="A:\\My Projects\\Android Subsystem for Windows (Python)\\Image editor\\Icons\\effect.png")

# Creating buttons on header
crop_button = Button(header_frame, image=crop_icon, bd=0, relief=FLAT, bg="#1f1f1f", activebackground="#1f1f1f", state=DISABLED, command=lambda : cropping(w=image_width, h=image_height))
crop_button.place(x=390, y=7)

color_button = Button(header_frame, image=brightness_icon, bd=0, relief=FLAT, bg="#1f1f1f", activebackground="#1f1f1f", command=threading_brightness_control, state=DISABLED)
color_button.place(x=450, y=3)

brush_button = Button(header_frame, image=color_brush_icon, bd=0, relief=FLAT, bg="#1f1f1f", activebackground="#1f1f1f", command=threading_brushing, state=DISABLED)
brush_button.place(x=510, y=7)

rotate_button = Button(header_frame, image=rotate_icon, bd=0, relief=FLAT, bg="#1f1f1f", activebackground="#1f1f1f", state=DISABLED, command=rotation)
rotate_button.place(x=570, y=7)

importButton = Button(header_frame, text=" Browse", command=import_image, compound=LEFT, image=browse_icon, bg="#1f1f1f", activebackground="#1f1f1f", fg='white', activeforeground="white", bd=0, relief=FLAT, font=("Bahnschrift Light Condensed", 13))
importButton.place(x=10, y=3)

saveButton = Button(header_frame, text=" Save", command=save_image, image=save_icon, compound=LEFT, bg="#1f1f1f", activebackground="#1f1f1f", fg='white', activeforeground="white", bd=0, relief=FLAT, font=("Bahnschrift Light Condensed", 13), state=DISABLED)
saveButton.place(x=100, y=3)

effect_Button = Button(header_frame, text=" Effects", command=effects, image=effect_icon, compound=LEFT, bg="#1f1f1f", activebackground="#1f1f1f", fg='white', activeforeground="white", bd=0, relief=FLAT, font=("Bahnschrift Light Condensed", 13), state=DISABLED)
effect_Button.place(x=900, y=3)

# Label for showing image
showWindow = Label(left_frame, bg="#202020", bd=0)
showWindow.place(x=0, y=0)

root.mainloop()
