# Import Useful Library
from tkinter import *
from tkinter import messagebox
import phonenumbers
from phonenumbers import geocoder, timezone, carrier
from timezonefinder import TimezoneFinder
from geopy.geocoders import Nominatim
from datetime import datetime
import pytz
from threading import Thread

# Use the Threading
def Threading_details():
    try:
        t1 = Thread(target=Track_Details)
        t1.start()
    except:
        messagebox.showinfo("Number Tracker", "Something went wrong!")

# Create Track_Details function for fetting mobile number details
def Track_Details():
    enter_number = entry_number.get()
    try:
        number = phonenumbers.parse(enter_number)

        if len(enter_number) != 10 and len(enter_number) != 13 and len(enter_number) != 14:
            messagebox.showerror("Phone number", "Something went wrong!")

        # Get Mobile number and country code
        number_with_code = phonenumbers.parse(enter_number)
        number_and_code.config(text=number_with_code, fg='white', font="arial 10 bold")

        # Get Country name
        locate = geocoder.description_for_number(number, 'en')
        country.config(text=f"Country: {locate}", fg='black')

        # Get ISP or Carrier name
        ISP = carrier.name_for_number(number, 'en')
        sim.config(text=f"SIM: {ISP}", fg='black')

        # Get Timezone
        time = timezone.time_zones_for_number(number)
        zone.config(text=f"Time Zone:  {time}", fg='black')

        # Get longitude and latitude
        geolocator = Nominatim(user_agent="geoapiExercises")
        location = geolocator.geocode(locate)

        lng = location.longitude
        lat = location.latitude

        longitude.config(text=f"Longitude: {lng}", fg='black')
        latitude.config(text=f"Latitude {lat}", fg='black')

        # get Current Time of mobile number
        obj = TimezoneFinder()
        result = obj.timezone_at(lng=location.longitude, lat=location.latitude)

        home = pytz.timezone(result)
        local_time = datetime.now(home)
        current_time = local_time.strftime("%I:%M:%p")
        clock.config(text=f"Current Time: {current_time}", fg='black')
    except:
        if len(enter_number) == 10:
            messagebox.showinfo("Phone number", "Make sure that you used correct +country code also")
        else:
            messagebox.showerror("Phone number", "Something went wrong")


root = Tk()
root.title("Phone number details finder")
root.geometry('365x584+500+50')
root.resizable(0,0)
root.attributes('-alpha', 0.98)  # Transparant 2% or 0.02%
root.config(background='#ba3a1c')
root.wm_iconbitmap("A:\\My Projects\\Android Subsystem for Windows (Python)\\Mobile Number Tracker\\find_logo.ico")

# Set a logo
logo = PhotoImage(file='A:\\My Projects\\Android Subsystem for Windows (Python)\\Mobile Number Tracker\\find-icon.png')
Label(root, image=logo, bg='#ba3a1c').place(x=120, y=30)

Heading = Label(root, text="Phone Number's Detail Finder", font=("Bahnschrift Condensed", 20), bg='#ba3a1c', fg='#560f07')
Heading.place(x=50, y=180)

Entry_back = PhotoImage(file='A:\\My Projects\\Android Subsystem for Windows (Python)\\Mobile Number Tracker\\search.png')
Label(root, image=Entry_back, bg='#ba3a1c').place(x=20, y=220)

entry = StringVar()
entry_number = Entry(root, textvariable=entry, width=15, bd=0, font="Georgia 20", justify=CENTER, fg='Red')
entry.set("+91")
entry_number.bind("<Return>", lambda e: Threading_details())
entry_number.place(x=50, y=250)

# Create Search Button
search_button = Button(root, text="Get Details", cursor='hand2', bg="#ff8c00", activebackground='orange', font=("Bahnschrift Light Condensed", 18), bd=1, relief=SUNKEN, command=Threading_details)
search_button.place(x=130, y=310)

# Bottom area
Label(root, bg='#a80000', width=100, height=20).place(x=0, y=365)

number_and_code = Label(root, text="       (Number and Country Code)", bg="#a80000", fg='black', font="Georgia 12 bold")
number_and_code.place(x=30, y=370)

country = Label(root, text="Country:", bg="#a80000", fg='white', font="arial 10 bold")
country.place(x=10, y=420)

sim = Label(root, text="SIM:", bg="#a80000", fg='white', font="arial 10 bold")
sim.place(x=200, y=420)

zone = Label(root, text="Time Zone:", bg="#a80000", fg='white', font="arial 10 bold")
zone.place(x=10, y=470)

clock = Label(root, text="Phone Time:", bg="#a80000", fg='white', font="arial 10 bold")
clock.place(x=200, y=470)

longitude = Label(root, text="Longitude:", bg="#a80000", fg='white', font="arial 10 bold")
longitude.place(x=10, y=520)

latitude = Label(root, text="Latitude:", bg="#a80000", fg='white', font="arial 10 bold")
latitude.place(x=200, y=520)

root.mainloop()
