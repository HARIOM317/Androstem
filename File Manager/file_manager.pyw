# Importing useful packages
from tkinter import *
import tkinter.filedialog as fd
import tkinter.messagebox as mb
import os
import shutil
from zipfile import ZipFile

# Creating main window
root = Tk()
root.title("File Manager")
root.geometry('800x550+250+50')
root.resizable(False, False)
root.wm_iconbitmap("A:\\My Projects\\Android Subsystem for Windows (Python)\\File Manager\\file_manager_logo.ico")
root.config(bg="#212224")


# _______________________ TOP FRAME __________________________
top_frame = Frame(root, height=80, bg="#d0ddff", bd=0, relief=SOLID)
top_frame.pack(side=TOP, fill=X)

# Creating top_button function to create top buttons
def top_button(x, y, image, text, activbcolor, bcolor, cmd):
    def on_press(e):
        myButton1['background'] = activbcolor
        myButton1['foreground'] = 'black'

    def on_leave(e):
        myButton1['background'] = bcolor
        myButton1['foreground'] = 'black'

    myButton1 = Button(top_frame, image=image, text=text, fg='black', bd=0, bg=bcolor, activeforeground='black', activebackground=activbcolor, command=cmd, cursor='hand2', compound=TOP, height=78, width=80, justify=CENTER)
    myButton1.bind('<Enter>', on_press)
    myButton1.bind('<Leave>', on_leave)
    myButton1.place(x=x, y=y)

sourceLocation = StringVar()
destinationLocation = StringVar()

''' Creating functions for top frame buttons '''

# for open the file
def open_file():
    file = fd.askopenfilename(title='Choose a file of any type', filetypes=[("All files", "*.*")])
    os.startfile(os.path.abspath(file))

# for cut and paste the file
def Create_cut_and_paste_Widgets():
    try:
        Frame(middle_frame2, height=300, width=625, bg='#eaeeff').place(x=0, y=0)

        link_Label = Label(middle_frame2, text="Select The File To Move : ", bg="#eaeeff", font="Georgia 10")
        link_Label.place(x=10, y=50)
        root.sourceText = Entry(middle_frame2, width=40, textvariable=sourceLocation, font="Georgia 10", bd=0.5, relief=SOLID)
        root.sourceText.place(x=180, y=50)
        source_browseButton = Button(middle_frame2, text="Browse", command=SourceBrowse, font="Georgia 10", bd=0, relief=FLAT, fg='dark blue', activeforeground="dark blue", bg="#eaeeff", activebackground="#eaeeff", cursor='hand2')
        source_browseButton.place(x=555, y=46)

        destinationLabel = Label(middle_frame2, text="Select The Destination : ", bg="#eaeeff", font="Georgia 10")
        destinationLabel.place(x=10, y=100)
        root.destinationText = Entry(middle_frame2, width=40, textvariable=destinationLocation, font="Georgia 10", bd=0.5, relief=SOLID)
        root.destinationText.place(x=180, y=100)
        dest_browseButton = Button(middle_frame2, text="Browse", command=DestinationBrowse, font="Georgia 10", bd=0, relief=FLAT, fg='dark blue', activeforeground="dark blue", bg="#eaeeff", activebackground="#eaeeff", cursor='hand2')
        dest_browseButton.place(x=555, y=96)

        moveButton = Button(middle_frame2, text="Move File", command=MoveFile, font="Georgia 13", width=10, bd=2, relief=RIDGE, bg="#eaeeff", activebackground="#eaeeff", fg="dark red", activeforeground="dark red", cursor='hand2')
        moveButton.place(x=250, y=150)
    except:
        mb.showinfo("Cut and Paste", "Please first browse location of source and destination file!")
def SourceBrowse():
    root.files_list = list(fd.askopenfilenames(initialdir="A:"))
    root.sourceText.insert('1', root.files_list)
def DestinationBrowse():
    destinationdirectory = fd.askdirectory(initialdir="D:")
    root.destinationText.insert('1', destinationdirectory)
def MoveFile():
    try:
        files_list = root.files_list
        destination_location = destinationLocation.get()
        for f in files_list:
            shutil.move(f, destination_location)
        mb.showinfo("Cut and Paste", "Successfully cut and paste the file")
    except:
        mb.showerror("Cut and Paste", "Something went wrong!")

# for copy and paste the file
def copy_file():
    file_to_copy = fd.askopenfilename(title='Choose a file to copy', filetypes=[("All files", "*.*")])
    dir_to_copy_to = fd.askdirectory(title="In which folder to copy to?")
    try:
        shutil.copy(file_to_copy, dir_to_copy_to)
        mb.showinfo(title='File copied!', message='Your desired file has been copied to your desired location')
    except:
        mb.showerror(title='Error!', message='We were unable to copy your file to the desired location. Please try again')

# for delete the file
def delete_file():
    file = fd.askopenfilename(title='Choose a file to delete', filetypes=[("All files", "*.*")])
    warning = mb.askyesno("Warning", "Are you sure to permanently delete this file?")
    if warning:
        os.remove(os.path.abspath(file))
        mb.showinfo(title='File deleted', message='Your desired file has been deleted')

# for rename the file
def Create_rename_Widgets():
    try:
        Frame(middle_frame2, height=300, width=625, bg='#eaeeff').place(x=0, y=0)
        select_button = Button(middle_frame2, text="Select file", command=SourceBrowse_rename, font="Georgia 10", bd=2, relief=GROOVE, fg='dark blue', activeforeground="dark blue", bg="#eaeeff", activebackground="#eaeeff", cursor='hand2')
        select_button.place(x=280, y=46)
        global old_name
        new_name_label = Label(middle_frame2, text="Enter new name with extension : ", bg="#eaeeff", font="Georgia 10")
        new_name_label.place(x=15, y=100)
        global new_name
        new_name = Entry(middle_frame2, width=40, font="Georgia 10", bd=0.5, relief=SOLID)
        new_name.place(x=240, y=100)

        Rename = Button(middle_frame2, text="Rename", font="Georgia 13", width=10, bd=2, relief=GROOVE, bg="#eaeeff", activebackground="#eaeeff", fg="dark red", activeforeground="dark red", cursor='hand2', command=RenameFile)
        Rename.place(x=265, y=150)
    except:
        mb.showinfo("Cut and Paste", "Please first browse location of source and destination file!")
def SourceBrowse_rename():
    global old_name, path
    old_name = fd.askopenfilename(title='Choose a file to rename', filetypes=[("All files", "*.*")])
    path = os.path.dirname(old_name)
def RenameFile():
    try:
        name = new_name.get()
        os.rename(old_name, path + "/" + name)
        mb.showinfo("Rename", "Successfully rename the file")
    except Exception as e:
        print(e)
        mb.showerror("Cut and Paste", "Something went wrong!")

# for open the folder
def open_folder():
    folder = fd.askdirectory(title="Select Folder to open")
    os.startfile(folder)

# for delete the folder
def delete_folder():
    folder_to_delete = fd.askdirectory(title='Choose a folder to delete')
    warning = mb.askyesno("Warning", "Are you sure to permanently delete this folder and it's all file?")
    if warning:
        shutil.rmtree(folder_to_delete)
        mb.showinfo("Folder Deleted", "Your desired folder has been deleted")

# for move the folder
def move_folder():
    folder_to_move = fd.askdirectory(title='Select the folder you want to move')
    mb.showinfo(message='You just selected the folder to move, now please select the desired destination where you want to move the folder to')
    destination = fd.askdirectory(title='Where to move the folder to')
    try:
        shutil.move(folder_to_move, destination)
        mb.showinfo("Folder moved", 'Your desired folder has been moved to the location you wanted')
    except:
        mb.showerror('Error', 'We could not move your folder. Please make sure that the destination exists')

# images for top buttons
open_button = PhotoImage(file="A:\\My Projects\\Android Subsystem for Windows (Python)\\File Manager\\Icons\\open_file.png")
cut_button = PhotoImage(file="A:\\My Projects\\Android Subsystem for Windows (Python)\\File Manager\\Icons\\cut_file.png")
copy_button = PhotoImage(file="A:\\My Projects\\Android Subsystem for Windows (Python)\\File Manager\\Icons\\copy_file.png")
rename_button = PhotoImage(file="A:\\My Projects\\Android Subsystem for Windows (Python)\\File Manager\\Icons\\rename_file.png")
delete_button = PhotoImage(file="A:\\My Projects\\Android Subsystem for Windows (Python)\\File Manager\\Icons\\delete_file.png")
open_folder_button = PhotoImage(file="A:\\My Projects\\Android Subsystem for Windows (Python)\\File Manager\\Icons\\open_folder.png")
move_folder_button = PhotoImage(file="A:\\My Projects\\Android Subsystem for Windows (Python)\\File Manager\\Icons\\move_folder.png")
delete_folder_button = PhotoImage(file="A:\\My Projects\\Android Subsystem for Windows (Python)\\File Manager\\Icons\\delete_folder.png")

# creating top buttons
top_button(8, 0, open_button, "Open file", '#dbe9ff', '#d0ddff', open_file)
top_button(108, 0, cut_button, "Cut & Paste", '#dbe9ff', '#d0ddff', Create_cut_and_paste_Widgets)
top_button(208, 0, copy_button, "Copy & Paste", '#dbe9ff', '#d0ddff', copy_file)
top_button(308, 0, rename_button, "Rename file", '#dbe9ff', '#d0ddff', Create_rename_Widgets)
top_button(408, 0, delete_button, "Delete file", '#dbe9ff', '#d0ddff', delete_file)
top_button(508, 0, open_folder_button, "Open folder", '#dbe9ff', '#d0ddff', open_folder)
top_button(608, 0, move_folder_button, "Move folder", '#dbe9ff', '#d0ddff', move_folder)
top_button(708, 0, delete_folder_button, "Delete folder", '#dbe9ff', '#d0ddff', delete_folder)


# _______________________ SIDE FRAME __________________________
side_frame = Frame(root, width=175, height=1000, bg='#fafafa', bd=0.5, relief=GROOVE)
side_frame.pack(side=LEFT, fill=Y)

# Creating side_button function to create side buttons
def side_button(x, y, image, text, activbcolor, bcolor, cmd):
    def on_press(e):
        myButton2['background'] = activbcolor
        myButton2['foreground'] = 'black'

    def on_leave(e):
        myButton2['background'] = bcolor
        myButton2['foreground'] = 'black'

    myButton2 = Button(side_frame, image=image, text=text,  bd=0, bg=bcolor, activebackground=activbcolor, command=cmd, cursor='hand2', compound=LEFT, width=170, anchor='w')
    myButton2.bind('<Enter>', on_press)
    myButton2.bind('<Leave>', on_leave)
    myButton2.place(x=x, y=y)

# Icons for side buttons
desktop_folder_icon = PhotoImage(file="A:\\My Projects\\Android Subsystem for Windows (Python)\\File Manager\\Icons\\desktop_folder.png")
document_folder_icon = PhotoImage(file="A:\\My Projects\\Android Subsystem for Windows (Python)\\File Manager\\Icons\\documents_folder.png")
download_folder_icon = PhotoImage(file="A:\\My Projects\\Android Subsystem for Windows (Python)\\File Manager\\Icons\\download_folder.png")
music_folder_icon = PhotoImage(file="A:\\My Projects\\Android Subsystem for Windows (Python)\\File Manager\\Icons\\music_folder.png")
picture_folder_icon = PhotoImage(file="A:\\My Projects\\Android Subsystem for Windows (Python)\\File Manager\\Icons\\picture_folder.png")
video_folder_icon = PhotoImage(file="A:\\My Projects\\Android Subsystem for Windows (Python)\\File Manager\\Icons\\video_folder.png")

''' Creating functions side frame buttons which are folders'''

# for opening desktop folder
def open_desktop_folder():
    os.startfile("C:\\Users\\hariom mewada\\OneDrive\\Desktop")

# for opening music folder
def open_music_folder():
    os.startfile("C:\\Users\\hariom mewada\\Music")

# for opening pictures folder
def open_picture_folder():
    os.startfile("C:\\Users\\hariom mewada\\OneDrive\\Pictures")

# for opening downloads folder
def open_download_folder():
    os.startfile("C:\\Users\\hariom mewada\\Downloads")

# for opening documents folder
def open_documents_folder():
    os.startfile("C:\\Users\\hariom mewada\\OneDrive\\Documents")

# for opening videos folder
def open_video_folder():
    os.startfile("C:\\Users\\hariom mewada\\Videos")

# creating side buttons or folder
side_button(0, 20, desktop_folder_icon, "Desktop", '#14e0ff', '#fafafa', open_desktop_folder)
side_button(0, 85, music_folder_icon, "Music", '#14e0ff', '#fafafa', open_music_folder)
side_button(0, 150, picture_folder_icon, "Picture", '#14e0ff', '#fafafa', open_picture_folder)
side_button(0, 215, download_folder_icon, "Download", '#14e0ff', '#fafafa', open_download_folder)
side_button(0, 280, document_folder_icon, "Document", '#14e0ff', '#fafafa', open_documents_folder)
side_button(0, 345, video_folder_icon, "Video", '#14e0ff', '#fafafa', open_video_folder)


# _______________________ MIDDLE FRAME 1 __________________________
middle_frame1 = Frame(root, height=170, bg="#eaeeff", bd=0.5, relief=SUNKEN)
middle_frame1.pack(fill=X)

# Creating middle_button function for opening any drive
def middle_button(x, y, image, text, activbcolor, bcolor, cmd):
    def on_press(e):
        myButton3['background'] = activbcolor
        myButton3['foreground'] = 'black'

    def on_leave(e):
        myButton3['background'] = bcolor
        myButton3['foreground'] = 'black'

    myButton3 = Button(middle_frame1, image=image, text=text,  bd=0, bg=bcolor, activebackground=activbcolor, command=cmd, cursor='hand2', compound=TOP, width=150, justify=CENTER)
    myButton3.bind('<Enter>', on_press)
    myButton3.bind('<Leave>', on_leave)
    myButton3.place(x=x, y=y)

# Drive image
drive_icon = PhotoImage(file="A:\\My Projects\\Android Subsystem for Windows (Python)\\File Manager\\Icons\\drive_icon.png")

# for opening drive A
def open_drive_a():
    os.startfile("A:")

# for opening drive C
def open_drive_c():
    os.startfile("C:")

# for opening drive D
def open_drive_d():
    os.startfile("D:")

# for opening drive D
def open_drive_e():
    os.startfile("E:")


# Creating drives which are available in computer
middle_button(4, 50, drive_icon, "Drive A", '#dadce2', '#e5f3ff', open_drive_a)
middle_button(158, 50, drive_icon, "Drive C", '#dadce2', '#e5f3ff', open_drive_c)
middle_button(312, 50, drive_icon, "Drive D", '#dadce2', '#e5f3ff', open_drive_d)
middle_button(466, 50, drive_icon, "Drive E", '#dadce2', '#e5f3ff', open_drive_e)

# creating function for organize all files and folder of selected directory in lower frame
def Create_file_organize_Widgets():
    Frame(middle_frame2, height=300, width=625, bg='#eaeeff').place(x=0, y=0)

    select_button = Button(middle_frame2, text="Select unorganized directory", command=select_unorganize_folder, font="Georgia 10", bd=2, relief=GROOVE, fg='dark blue', activeforeground="dark blue", bg="#eaeeff", activebackground="#eaeeff", cursor='hand2')
    select_button.place(x=100, y=100)

    global organize_button
    organize_button = Button(middle_frame2, text="Organize", font="Georgia 13", width=10, bd=2, relief=GROOVE, bg="#eaeeff", activebackground="#eaeeff", fg="dark red", activeforeground="dark red", cursor='hand2', command=organize_folder, state=DISABLED)
    organize_button.place(x=350, y=95)

# for opening unorganized folder
def select_unorganize_folder():
    global dir_path
    dir_path = fd.askdirectory()
    organize_button.config(state=NORMAL)

# for organized folder
def organize_folder():
    try:
        files = os.listdir(dir_path)

        for file in files:
            filename, extension = os.path.splitext(file)
            extension = extension[1:]
            if os.path.exists(dir_path + "/" + extension):
                shutil.move(dir_path + "/" + file, dir_path + "/" + extension + "/" + file)
            else:
                os.makedirs(dir_path + "/" + extension)
                shutil.move(dir_path + "/" + file, dir_path + "/" + extension)
        mb.showinfo("File Organizer", "Files organized successfully!")
    except:
        mb.showinfo("File Organizer", "first select a unorganized directory!")

# button for file organizer
Button(middle_frame1, text="Organize all files", fg="black", activeforeground="black", bg="#eaeeff", activebackground="#eaeeff", bd=0, relief=FLAT, cursor='hand2', font="Georgia 10", command=Create_file_organize_Widgets).place(x=340, y=10)


# creating function for show all files and folder of selected directory in lower frame
def list_files_in_folder():
    Frame(middle_frame2, height=300, width=625, bg='#eaeeff').place(x=0, y=0)
    i = 0
    folder = fd.askdirectory(title='Select the folder whose files you want to list')
    files = os.listdir(os.path.abspath(folder))
    list_files_wn = Frame(middle_frame2, width=620, height=273, bg="#eaeeff", bd=0)
    list_files_wn.place(x=0, y=25)
    Label(middle_frame2, text=f'Files and folders in {folder}', bg="#eaeeff").place(x=10, y=0)
    listbox = Listbox(list_files_wn, selectbackground='SteelBlue', font=("Georgia", 10), bd=0, bg="#eaeeff", justify=LEFT)
    listbox.place(relx=0, rely=0, relheight=1, relwidth=1)
    scrollbar = Scrollbar(listbox, orient=VERTICAL, command=listbox.yview)
    scrollbar.pack(side=RIGHT, fill=Y)
    listbox.config(yscrollcommand=scrollbar.set)
    while i < len(files):
        listbox.insert(END, files[i])
        i += 1

Button(middle_frame1, text="List all files in a folder", fg="black", activeforeground="black", bg="#eaeeff", activebackground="#eaeeff", bd=0, relief=FLAT, cursor='hand2', font="Georgia 10", command=list_files_in_folder).place(x=470, y=10)

# function for extracting a zip file
def extract_zip():
    try:
        if not os.path.exists('A:\\My Projects\\Android Subsystem for Windows (Python)\\File Manager\\Files from zip folder'):
            os.mkdir("A:\\My Projects\\Android Subsystem for Windows (Python)\\File Manager\\Files from zip folder")

        file = fd.askopenfilename(title='Choose a zip file', filetypes=[("Zip files", "*.zip")])
        with ZipFile(file, 'r') as zip:
            location = "A:\\My Projects\\Android Subsystem for Windows (Python)\\File Manager\\Files from zip folder"
            zip.extractall(location)
            mb.showinfo("Zip extractor", "Successfully extract all zip files in (A:\My Projects\Android Subsystem for Windows (Python)\File Manager\Files from zip folder) directory")
    except:
        mb.showinfo("Zip extractor", "Something went wrong!")

Button(middle_frame1, text="Extract zip file", fg="black", activeforeground="black", bg="#eaeeff", activebackground="#eaeeff", bd=0, relief=FLAT, cursor='hand2', font="Georgia 10", command=extract_zip).place(x=220, y=10)


# _______________________ MIDDLE FRAME 2 __________________________
# Use this frame for showing files and other operations like cut, paste, rename...
middle_frame2 = Frame(root, height=300, bg="#eaeeff", bd=0.5, relief=SUNKEN)
middle_frame2.pack(fill=X)

root.mainloop()
