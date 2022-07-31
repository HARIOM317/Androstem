# Import useful packages
from tkinter import *
from tkinter import ttk
import platform
import psutil
import screen_brightness_control
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
import threading
import subprocess
import pyautogui
import wmi

# Creating GUI
root = Tk()
root.title("Sys-Info")
root.geometry("1400x800+200+100")
root.resizable(False, False)
root.config(bg="#e1e1e1", bd=7, relief=SUNKEN)
root.wm_iconbitmap("A:\\My Projects\\Android Subsystem for Windows (Python)\\System Information app\\system_info_icon.ico")

# Creating frames
LHS = Frame(root, width=500, height=770, bg="white", highlightbackground="#adacb1", highlightthickness=1)
LHS.place(x=10, y=10)

RHS = Frame(root, width=860, height=650, bg="#f4f5f5", highlightbackground="#adacb1", highlightthickness=1)
RHS.place(x=520, y=10)

RHB = Frame(root, width=860, height=110, bg="#f4f5f5", highlightbackground="#adacb1", highlightthickness=1)
RHB.place(x=520, y=670)

# system name
my_system = platform.uname()
l1 = Label(LHS, text=my_system.node, bg='white', justify=CENTER, font=("Bahnschrift Light Condensed", 15))
l1.place(x=175, y=10)

# Laptop image
laptop_image = PhotoImage(file="A:\\My Projects\\Android Subsystem for Windows (Python)\\System Information app\\my_laptop.png")
laptop = Label(LHS, image=laptop_image, background="white")
laptop.place(x=106, y=50)

# system version
l2 = Label(LHS, text=f"Version : {my_system.version}", bg='white', justify=CENTER, font=("Bahnschrift Light Condensed", 12), width=45)
l2.place(x=20, y=300)

# system os
l3 = Label(LHS, text=f"System : {my_system.system}", bg='white', justify=CENTER, font=("Bahnschrift Light Condensed", 12), width=45)
l3.place(x=20, y=340)

# machine type
l4 = Label(LHS, text=f"Machine : {my_system.machine}", bg='white', justify=CENTER, font=("Bahnschrift Light Condensed", 12), width=45)
l4.place(x=20, y=380)

# function for creating buttons
def button(x, y, text, image, activbcolor, bcolor, cmd):
    def on_press(e):
        myButton1['background'] = activbcolor
        myButton1['foreground'] = 'dark blue'
    def on_leave(e):
        myButton1['background'] = bcolor
        myButton1['foreground'] = 'black'

    myButton1 = Button(LHS, text=text, image=image, width=476, height=32, justify=LEFT, fg='black', bd=0, bg=bcolor, activeforeground='dark blue', activebackground=activbcolor, command=cmd, font=("Bahnschrift Light Condensed", 12, 'bold'), padx=10, compound=LEFT, anchor='w', cursor='hand2')

    myButton1.bind('<Enter>', on_press)
    myButton1.bind('<Leave>', on_leave)

    myButton1.place(x=x, y=y)

refresh_icon = PhotoImage(file="A:\\My Projects\\Android Subsystem for Windows (Python)\\System Information app\\icons\\refresh.png")

def threading_system_info():
    t1 = threading.Thread(target=system_info)
    t1.start()

# for getting system information
def system_info():
    Frame(RHS, width=858, height=648, bg="#f4f5f5", bd=1, relief=SOLID).place(x=0, y=0)
    Id = subprocess.check_output(['systeminfo']).decode('utf-8').split('\n')
    new = []

    for item in Id:
        new.append(str(item.split("\r")[:-1]))

    listbox = Listbox(RHS, selectbackground='#13c0ff', selectforeground='dark blue', selectborderwidth=3, font=("Bahnschrift Light Condensed", 12), bd=0, bg="#f4f5f5", justify=LEFT)
    listbox.place(relx=0, rely=0, relheight=1, relwidth=1)
    scrollbar = Scrollbar(listbox, orient=VERTICAL, command=listbox.yview)
    scrollbar.pack(side=RIGHT, fill=Y)
    listbox.config(yscrollcommand=scrollbar.set)
    i = 1
    listbox.insert(END, "_"*42 + "System Information" + "_"*42)
    listbox.insert(END, "\n")
    while i < len(new)-1:
        listbox.insert(END, "        "+new[i][2:-2])
        i += 1

# for getting cpu information
def cpu_info():
    Frame(RHS, width=858, height=648, bg="#f4f5f5", bd=1, relief=SOLID).place(x=0, y=0)

    computer = wmi.WMI()
    proc_info = computer.Win32_Processor()[0]

    label_0 = Label(RHS, text="CPU : {0}".format(proc_info.Name), bg='#f4f5f5', justify=CENTER, font=("Bahnschrift Light Condensed", 12))
    label_0.place(x=20, y=20)

    label_1 = Label(RHS, text=f"Processor : {my_system.processor}", bg='#f4f5f5', justify=CENTER,
                    font=("Bahnschrift Light Condensed", 12))
    label_1.place(x=20, y=70)

    label_2 = Label(RHS, text=f"Logical processors : {psutil.cpu_count()}", bg='#f4f5f5', justify=CENTER, font=("Bahnschrift Light Condensed", 12))
    label_2.place(x=20, y=120)

    label_3 = Label(RHS, text=f"Cores : {psutil.cpu_count(logical=FALSE)}", bg='#f4f5f5', justify=CENTER, font=("Bahnschrift Light Condensed", 12))
    label_3.place(x=20, y=170)
    current, min, max = psutil.cpu_freq()

    label_4 = Label(RHS, text=f"CPU percent : {psutil.cpu_percent()} %", bg='#f4f5f5', justify=CENTER,
                    font=("Bahnschrift Light Condensed", 12))
    label_4.place(x=20, y=220)

    label_5 = Label(RHS, text=f"Base speed : {round(max/1000, 2)} GHz", bg='#f4f5f5', justify=CENTER, font=("Bahnschrift Light Condensed", 12))
    label_5.place(x=20, y=270)

    label_6 = Label(RHS, text=f"Speed : {round(current/1000, 2)} GHz", bg='#f4f5f5', justify=CENTER, font=("Bahnschrift Light Condensed", 12))
    label_6.place(x=20, y=320)

    label_7 = Label(RHS, text=f"Min speed : {round(min/1000, 2)} GHz", bg='#f4f5f5', justify=CENTER, font=("Bahnschrift Light Condensed", 12))
    label_7.place(x=20, y=370)

    refresh_button = Button(RHS, text=" Refresh", image=refresh_icon, justify=LEFT, compound=LEFT, anchor='w', height=35, font=("Bahnschrift Light Condensed", 12), cursor='hand2', bd=0, relief=FLAT, bg="#f4f5f5", activebackground="#f4f5f5", command=cpu_info)
    refresh_button.place(x=740, y=20)

# for getting memory information
def memory_info():
    Frame(RHS, width=858, height=648, bg="#f4f5f5", bd=1, relief=SOLID).place(x=0, y=0)

    label_1 = Label(RHS, text=f"Total RAM : {round(psutil.virtual_memory().total/(1024*1024*1024), 2)} GB", bg='#f4f5f5', justify=CENTER, font=("Bahnschrift Light Condensed", 12))
    label_1.place(x=20, y=20)

    label_2 = Label(RHS, text=f"RAM used : {round(psutil.virtual_memory()[3]/(1024*1024*1024), 2)} GB", bg='#f4f5f5', justify=CENTER, font=("Bahnschrift Light Condensed", 12))
    label_2.place(x=20, y=70)

    label_3 = Label(RHS, text=f"RAM free : {round(psutil.virtual_memory()[4]/(1024*1024*1024), 2)} GB", bg='#f4f5f5', justify=CENTER, font=("Bahnschrift Light Condensed", 12))
    label_3.place(x=20, y=120)

    label_4 = Label(RHS, text=f"Percent : {psutil.virtual_memory().percent} %", bg='#f4f5f5', justify=CENTER, font=("Bahnschrift Light Condensed", 12))
    label_4.place(x=20, y=170)

    refresh_button = Button(RHS, text=" Refresh", image=refresh_icon, justify=LEFT, compound=LEFT, anchor='w', height=35, font=("Bahnschrift Light Condensed", 12), cursor='hand2', bd=0, relief=FLAT, bg="#f4f5f5", activebackground="#f4f5f5", command=memory_info)
    refresh_button.place(x=740, y=20)

def get_size(bytes, suffix="B"):
    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < factor:
            return f"{bytes:.2f}{unit}{suffix}"
        bytes /= factor

# for getting disk information
def disk_info():
    Frame(RHS, width=858, height=648, bg="#f4f5f5", bd=1, relief=SOLID).place(x=0, y=0)

    listbox = Listbox(RHS, selectbackground='#13c0ff', selectforeground='dark blue', selectborderwidth=3, font=("Bahnschrift Light Condensed", 12), bd=0, bg="#f4f5f5", justify=LEFT)
    listbox.place(relx=0, rely=0, relheight=1, relwidth=1)
    scrollbar = Scrollbar(listbox, orient=VERTICAL, command=listbox.yview)
    scrollbar.pack(side=RIGHT, fill=Y)
    listbox.config(yscrollcommand=scrollbar.set)

    # Disk Information
    listbox.insert(END, "_" * 45 + " Disk Information " + "_" * 45)
    listbox.insert(END, "Partitions and Usage:")
    # get all disk partitions
    partitions = psutil.disk_partitions()

    for partition in partitions:
        listbox.insert(END, "")
        listbox.insert(END, f"ʘ Device: {partition.device}")
        listbox.insert(END, "_____________________________________")
        listbox.insert(END, f"     Mountpoint: {partition.mountpoint}")
        listbox.insert(END, f"     File system type: {partition.fstype}")
        try:
            partition_usage = psutil.disk_usage(partition.mountpoint)
        except PermissionError:
            # this can be catched due to the disk that isn't ready
            continue
        listbox.insert(END, f"     Total Size: {get_size(partition_usage.total)}")
        listbox.insert(END, f"     Used: {get_size(partition_usage.used)}")
        listbox.insert(END, f"     Free: {get_size(partition_usage.free)}")
        listbox.insert(END, f"     Percentage: {partition_usage.percent}%")
    # get IO statistics since boot
    disk_io = psutil.disk_io_counters()
    listbox.insert(END, "")
    listbox.insert(END, f"Total read: {get_size(disk_io.read_bytes)}")
    listbox.insert(END, f"Total write: {get_size(disk_io.write_bytes)}")

# for getting network information
def network_info():
    Frame(RHS, width=858, height=648, bg="#f4f5f5", bd=1, relief=SOLID).place(x=0, y=0)

    listbox = Listbox(RHS, selectbackground='#13c0ff', selectforeground='dark blue', selectborderwidth=3, font=("Bahnschrift Light Condensed", 12), bd=0, bg="#f4f5f5", justify=LEFT)
    listbox.place(relx=0, rely=0, relheight=1, relwidth=1)
    scrollbar = Scrollbar(listbox, orient=VERTICAL, command=listbox.yview)
    scrollbar.pack(side=RIGHT, fill=Y)
    listbox.config(yscrollcommand=scrollbar.set)

    # Disk Information
    listbox.insert(END, "_" * 42 + " Network Information " + "_" * 42)

    # get all network interfaces (virtual and physical)
    if_addrs = psutil.net_if_addrs()
    for interface_name, interface_addresses in if_addrs.items():
        for address in interface_addresses:
            listbox.insert(END, f"  Interface :  {interface_name}")
            if str(address.family) == 'AddressFamily.AF_INET':
                listbox.insert(END, "")
                listbox.insert(END, f"        IP Address: {address.address}")
                listbox.insert(END, f"        Netmask: {address.netmask}")
                listbox.insert(END, f"        Broadcast IP: {address.broadcast}")
                listbox.insert(END, "")

            elif str(address.family) == 'AddressFamily.AF_PACKET':
                listbox.insert(END, "")
                listbox.insert(END, f"        MAC Address: {address.address}")
                listbox.insert(END, f"        Netmask: {address.netmask}")
                listbox.insert(END, f"        Broadcast MAC: {address.broadcast}")
                listbox.insert(END, "")

    # get IO statistics since boot
    net_io = psutil.net_io_counters()
    listbox.insert(END, "")
    listbox.insert(END, f"Total Bytes Sent: {get_size(net_io.bytes_sent)}")
    listbox.insert(END, f"Total Bytes Received: {get_size(net_io.bytes_recv)}")

# for getting gpu name
def gpu_info():
    Frame(RHS, width=858, height=648, bg="#f4f5f5", bd=1, relief=SOLID).place(x=0, y=0)

    computer = wmi.WMI()
    gpu_info = computer.Win32_VideoController()[0]

    label_1 = Label(RHS, text='Graphics Card: {0}'.format(gpu_info.Name), bg='#f4f5f5', justify=CENTER, font=("Bahnschrift Light Condensed", 15))
    label_1.place(x=20, y=20)


# icons for buttons
system_ = PhotoImage(file="A:\\My Projects\\Android Subsystem for Windows (Python)\\System Information app\\icons\\system.png")
cpu = PhotoImage(file="A:\\My Projects\\Android Subsystem for Windows (Python)\\System Information app\\icons\\CPU.png")
memory = PhotoImage(file="A:\\My Projects\\Android Subsystem for Windows (Python)\\System Information app\\icons\\RAM.png")
storage = PhotoImage(file="A:\\My Projects\\Android Subsystem for Windows (Python)\\System Information app\\icons\\storage.png")
network = PhotoImage(file="A:\\My Projects\\Android Subsystem for Windows (Python)\\System Information app\\icons\\network.png")
gpu = PhotoImage(file="A:\\My Projects\\Android Subsystem for Windows (Python)\\System Information app\\icons\\GPU.png")

# creating buttons
button(0, 485, "System", system_, "#14e0ff", '#f0f0f0', threading_system_info)
button(0, 530, "CPU", cpu, "#14e0ff", '#f0f0f0', cpu_info)
button(0, 575, "Memory", memory, "#14e0ff", '#f0f0f0', memory_info)
button(0, 620, "Storage", storage, "#14e0ff", '#f0f0f0', disk_info)
button(0, 665, "Network", network, "#14e0ff", '#f0f0f0', network_info)
button(0, 710, "GPU", gpu, "#14e0ff", '#f0f0f0', gpu_info)


# _____________________ Battery __________________________

def convertTime(seconds):
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    return "%d: %02d: %02d" % (hours, minutes, seconds)

def threading_none():
    t1 = threading.Thread(target=battery_status)
    t1.start()

# for getting battery information
def battery_status():
    global battery_png, battery_label
    battery = psutil.sensors_battery()
    percent = battery.percent

    label.config(text=f"{percent}%")
    plug_in = battery.power_plugged
    if plug_in:
        label_plug.config(text="Plugged in")
    elif not plug_in:
        if 0 <= percent <= 35:
            label_plug.config(text="low battery")
        elif percent == 100:
            label_plug.config(text="full battery")
        else:
            label_plug.config(text="")

    battery_label = Label(RHB, background="#f4f5f5")
    battery_label.place(x=740, y=10)

    label.after(1000, battery_status)

    if battery.power_plugged == True:
        battery_png = PhotoImage(file="A:\\My Projects\\Android Subsystem for Windows (Python)\\System Information app\\icons\\recharge_battery.png")
        battery_label.config(image=battery_png)
    else:
        if percent >= 0 and percent <= 35:
            battery_png = PhotoImage(file="A:\\My Projects\\Android Subsystem for Windows (Python)\\System Information app\\icons\\low_battery.png")
            battery_label.config(image=battery_png)
        elif percent >= 36 and percent <= 75:
            battery_png = PhotoImage(file="A:\\My Projects\\Android Subsystem for Windows (Python)\\System Information app\\icons\\half_battery.png")
            battery_label.config(image=battery_png)
        else:
            battery_png = PhotoImage(file="A:\\My Projects\\Android Subsystem for Windows (Python)\\System Information app\\icons\\full_battery.png")
            battery_label.config(image=battery_png)

label = Label(RHB, bg='#f4f5f5', font=("Bahnschrift Light Condensed", 15, 'bold'))
label.place(x=800, y=11)
label_plug = Label(RHB, bg='#f4f5f5', font="Default 10", width=10, justify=CENTER)
label_plug.place(x=737, y=60)

threading_none()

# _____________________ Speaker __________________________

volume_ = PhotoImage(file="A:\\My Projects\\Android Subsystem for Windows (Python)\\System Information app\\icons\\volume.png")
label_speaker = Label(RHB, image=volume_, bg="#f4f5f5")
label_speaker.place(x=10, y=10)

volume_value = DoubleVar()

# for getting volume value
def get_current_volume_value():
    return '{: .2f}'.format(volume_value.get())

# for changing the volume
def volume_changed(event):
    try:
        device = AudioUtilities.GetSpeakers()
        interface = device.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
        volume = cast(interface, POINTER(IAudioEndpointVolume))
        volume.SetMasterVolumeLevel(-float(get_current_volume_value()), None)
    except Exception as e:
        pass


style = ttk.Style()
style.configure("TScale", background="#f4f5f5")

volume = Scale(RHB, from_=60, to=0, orient=HORIZONTAL, command=volume_changed, variable=volume_value, showvalue=False, width=10, length=630, cursor='hand2', activebackground='orange', relief=FLAT, bd=0, troughcolor='#98ccfd', sliderrelief=RIDGE, sliderlength=40, highlightbackground='dark blue', highlightthickness=1, bg='gold')
volume.place(x=60, y=20)

volume.set(10)

# _________________________ Brightness ________________________

brightness_ = PhotoImage(file="A:\\My Projects\\Android Subsystem for Windows (Python)\\System Information app\\icons\\brightness.png")

label_brightness = Label(RHB, image=brightness_, bg="#f4f5f5")
label_brightness.place(x=10, y=60)

current_value = DoubleVar()

# get current brightness
def get_current_value():
    return "{: .2f}".format(current_value.get())

# for changing the brightness
def brightness_changed(event):
    screen_brightness_control.set_brightness(get_current_value())

brightness = Scale(RHB, from_=0, to=100, orient=HORIZONTAL, command=brightness_changed, variable=current_value, width=10, length=630, cursor='hand2', showvalue=False, activebackground='orange', relief=FLAT, bd=0, troughcolor='#98ccfd', sliderrelief=RIDGE, sliderlength=40, highlightbackground='dark blue', highlightthickness=1, bg='gold')
brightness.place(x=60, y=70)
brightness.set(40)

threading_system_info()

root.mainloop()
