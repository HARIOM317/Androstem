# Import Libraries
from tkinter import *
import os
from tkinter import filedialog
from PIL import Image, ImageTk
from tkinter.messagebox import *
from threading import Thread


# Creating a ShowImages Class and inherit it to Frame class
class ShowImages(Frame):
    # Make a constructor
    def __init__(self, root):
        # Create geometry for window and set some properties
        super().__init__()
        self.root = root
        self.root.title('Photos')
        self.root.geometry('1000x630+100+5')
        self.root.resizable(False, False)
        self.root.configure(bg="#2a2c35")
        self.root.wm_iconbitmap("A:\\My Projects\\Android Subsystem for Windows (Python)\\Image Viewer\\Photos_icon.ico")

        # create a top frame
        self.frame = Frame(self.root, background='#011627', pady=10)
        self.frame.pack(side=TOP, fill=X)

        # create a files variable for showing the image name
        files = ""

        self.var = StringVar()
        self.var.set(files.title())
        # create a name label to indicate the image name
        self.nameLabel = Label(self.frame, textvariable=self.var, bd=0, fg='white', bg='#011627', width=80, font=("arial", 10, 'bold'))
        self.nameLabel.pack(pady=10)

        # Create a label to set the 'Well Come' on the screen
        self.imageLabel1 = Label(self.root, text="Well Come ", font=("Monotype Corsiva", 100, 'bold'), fg='Alice Blue', bg='#2a2c35')
        self.imageLabel1.pack(padx=100, pady=150, anchor='s')

        # Create another label to set the 'Import Images to Continue' on the screen
        self.imageLabel2 = Label(self.root, text="Import Images to Continue", font=("Gabriola", 20, 'italic'), fg='white', bg='#2a2c35')
        self.imageLabel2.place(x=380, y=350)

        # Load previous image and next image icon
        self.prev_image_icon = PhotoImage(file='A:\\My Projects\\Android Subsystem for Windows (Python)\\Image Viewer\\PreviousImage.png')
        self.next_image_icon = PhotoImage(file='A:\\My Projects\\Android Subsystem for Windows (Python)\\Image Viewer\\NextImage.png')
        # Load an icon for browse images from directory and make a label for it.
        self.browse_image = PhotoImage(file='A:\\My Projects\\Android Subsystem for Windows (Python)\\Image Viewer\\Browse.png')

        # Create open_image function to open a single image
        def open_image():
            try:
                filename = filedialog.askopenfilename(initialdir=os.getcwd(), title="Select Image File", filetypes=(("JPG File", "*.jpg"), ("PNG File", "*.png"), ("All Files", "*.*")))
                self.img = Image.open(filename)
                self.img = self.img.resize((800, 550))
                self.img = ImageTk.PhotoImage(self.img)
                self.lbl = Label(self.root, image=self.img)
                self.lbl.place(x=100, y=68)
                self.var.set("Photos - "+filename.title())
            except Exception as e:
                showerror("Photos", "No Image Found!")

        def threading_compress_image():
            t1 = Thread(target=compress_image)
            t1.start()

        def compress_image():
            try:
                file_path = filedialog.askopenfilename()
                img = Image.open(file_path)
                myHeight, myWidth = img.size
                img = img.resize((myHeight, myWidth), Image.ANTIALIAS)
                save_path = filedialog.asksaveasfilename(defaultextension='.jpg')
                img.save(save_path)
                showinfo("Image compressor", "Image compressed successfully!")
            except:
                showerror("Image compressor", "Something went wrong!")

        #  create loadImages function to load the images from any directory
        def loadImages():
            try:
                directory = filedialog.askdirectory()
                os.chdir(directory)  # it permits to change the current directory
                allImages = os.listdir()
                allImages.reverse()
                self.listImages = Listbox(self.root)

                for image in allImages:  # it returns the list of images
                    pos = 0
                    if image.endswith(('.png', '.jpg', '.jpeg', '.ico')):
                        self.listImages.insert(pos, image)
                        pos += 1

                self.listImages.selection_set(0)    # It selects 0th index image
                self.listImages.see(0)      # It shows 0th index image
                self.listImages.activate(0)     # It will activate the 0th index image
                self.listImages.selection_anchor(0)     # It will set selection_anchor 0 for image

                image = self.listImages.curselection()
                images = self.listImages.get(image[0])      # Open first image of directory
                self.img1 = Image.open(images)
                self.img1 = self.img1.resize((800, 550))
                self.img = ImageTk.PhotoImage(self.img1, )
                self.imageLabel = Label(self.root)
                self.imageLabel.place(x=100, y=68)
                self.imageLabel["compound"] = LEFT
                self.imageLabel["image"] = self.img
                self.var.set("Photos - "+images)

                # Create button for previous image
                self.button1 = Button(self.root, image=self.prev_image_icon, bd=0, bg='gray72', command=previousImage, background='#2a2c35', relief=FLAT, activebackground='#2a2c35')
                self.button1.place(x=5, y=270)
                # Create button for next image
                self.button2 = Button(self.root, image=self.next_image_icon, bd=0, bg='gray72', command=nextImage, background='#2a2c35', relief=FLAT, activebackground='#2a2c35')
                self.button2.place(x=915, y=270)

            except Exception as e:
                showerror("Photos", "No Image Found!")

        # Create a function for showing the next image
        def nextImage():
            try:
                next_one = self.listImages.curselection()
                next_one = next_one[0] + 1
                image = self.listImages.get(next_one)
                self.img1 = Image.open(image)
                self.img1 = self.img1.resize((800, 550))
                self.img = ImageTk.PhotoImage(self.img1)
                self.imageLabel = Label(self.root)
                self.imageLabel.place(x=100, y=68)
                self.imageLabel["compound"] = LEFT
                self.imageLabel["image"] = self.img
                self.listImages.select_clear(0, END)
                self.listImages.activate(next_one)
                self.listImages.selection_set(next_one, last=None)
                self.var.set("Photos - "+image)

                # Create button for previous image
                self.button1 = Button(self.root, image=self.prev_image_icon, bd=0, bg='gray72', command=previousImage, background='#2a2c35', relief=FLAT, activebackground='#2a2c35')
                self.button1.place(x=5, y=270)
                # Create button for next image
                self.button2 = Button(self.root, image=self.next_image_icon, bd=0, bg='gray72', command=nextImage, background='#2a2c35', relief=FLAT, activebackground='#2a2c35')
                self.button2.place(x=915, y=270)
            except:
                showinfo("Photos", "No any next image found!")

        # Create a function for showing the previous image
        def previousImage():
            try:
                next_one = self.listImages.curselection()
                next_one = next_one[0] - 1
                image = self.listImages.get(next_one)
                self.img1 = Image.open(image)
                self.img1 = self.img1.resize((800, 550))
                self.img = ImageTk.PhotoImage(self.img1, )
                self.imageLabel = Label(self.root)
                self.imageLabel.place(x=100, y=68)
                self.imageLabel["compound"] = LEFT
                self.imageLabel["image"] = self.img
                self.listImages.select_clear(0, END)
                self.listImages.activate(next_one)
                self.listImages.selection_set(next_one, last=None)
                self.var.set("Photos - "+image)

                # Create button for previous image
                self.button1 = Button(self.root, image=self.prev_image_icon, bd=0, bg='gray72', command=previousImage, background='#2a2c35', relief=FLAT, activebackground='#2a2c35')
                self.button1.place(x=5, y=270)
                # Create button for next image
                self.button2 = Button(self.root, image=self.next_image_icon, bd=0, bg='gray72', command=nextImage, background='#2a2c35', relief=FLAT, activebackground='#2a2c35')
                self.button2.place(x=915, y=270)
            except:
                showinfo("Photos", "No any previous image found!")

        # Binding right and left arrow key to change the images
        self.root.bind('<Right>', lambda x: nextImage())
        self.root.bind('<Left>', lambda x: previousImage())

        # Create Browse button to open directory for importing all images.
        self.buttonBrowse = Button(self.frame, image=self.browse_image, bd=0, bg='#011627', fg='white', activebackground='#011627', activeforeground='white', command=loadImages, cursor='hand2', text="Browse Photo", compound=LEFT, font="default 10 bold")
        self.buttonBrowse.place(x=8, y=0)

        # Create open_image button to open a single image.
        self.open_image = Button(self.root, text="Open Image", bd=2, bg='#2a2c35', activebackground='#2a2c35', fg='white', activeforeground='white', relief=RIDGE, pady=5, padx=5, command=open_image, cursor='hand2', width=9)
        self.open_image.place(x=10, y=75)

        # Create compress_image button to compress a single image.
        self.compress_image = Button(self.root, text="Compress", bd=2, bg='#2a2c35', activebackground='#2a2c35', fg='white', activeforeground='white', relief=RIDGE, pady=5, padx=5, cursor='hand2', width=9, command=threading_compress_image)
        self.compress_image.place(x=10, y=120)

        # Create an Exit button to exit from program
        self.Exit = Button(self.frame, text="Exit", bd=2, fg='white', font=("French Script MT", 18), bg='#011627', command=self.root.destroy, activebackground='#011627', activeforeground='white', cursor='hand2', padx=10, relief=RIDGE)
        self.Exit.place(x=930, y=-4)

# Start execution from here
if __name__ == "__main__":
    root = Tk()
    root.attributes('-alpha', 0.98)  # Transparent 2% or 0.02%
    photos = ShowImages(root)
    root.mainloop()
