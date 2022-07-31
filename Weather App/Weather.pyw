# Import useful modules
from tkinter import *
from geopy.geocoders import Nominatim
from tkinter import ttk, messagebox
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz
from threading import Thread

# Create function to show result in degree_fehrenheit
def result_in_fahrenheit():
    try:
        result = (get_temp*9/5)+32
        t.config(text=(result, "°F"))
        c.config(text=(condition, "|", "FEELS", "LIKE", result, "°F"))
    except:
        messagebox.showinfo("Weather Temperature", "First search any valid location")

# Handle threading of get_weather function
def Threading_get_weather():
    t1 = Thread(target=get_weather)
    t1.start()

# Creating function to get weather data
def get_weather():
    try:
        city = search.get()
        geolocator = Nominatim(user_agent="geoapiExercises")
        location = geolocator.geocode(city)
        obj = TimezoneFinder()
        result = obj.timezone_at(lng=location.longitude, lat=location.latitude)
        home = pytz.timezone(result)
        local_time = datetime.now(home)
        my_time = int(local_time.strftime("%H"))
        current_time = local_time.strftime("%I:%M %p")
        clock.config(text=current_time)
        name.config(text="CURRENT WEATHER")

        city_name.config(text=city)

        # weather api
        api = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=0a39243a1ad5ce042d806a940901cf21"

        # getting information
        json_data = requests.get(api).json()
        global condition
        condition = json_data['weather'][0]['main']
        get_description = json_data['weather'][0]['description']
        global get_temp
        get_temp = int(json_data['main']['temp']-273.15)
        get_pressure = json_data['main']['pressure']
        get_humidity = json_data['main']['humidity']
        get_wind = json_data['wind']['speed']

        # showing result on screen
        t.config(text=(get_temp, "°C"))
        c.config(text=(condition, "|", "FEELS", "LIKE", get_temp, "°C"))
        wind.config(text=get_wind)
        humidity.config(text=get_humidity)
        description.config(text=get_description)
        pressure.config(text=get_pressure)

        # showing result according time and weather using conditions
        if int(my_time) > 0 and int(my_time) < 6:
            root.config(bg="#323232")
            top_frame.config(bg="#323232")
            setting_button.config(bg="#323232", activebackground="#323232", fg='white', activeforeground='white')
            name.config(bg="#323232")
            clock.config(bg="#323232", fg="white")
            search_bar.config(bg="#323232")
            weather_image_label.config(bg="#323232")
            t.config(bg="#323232", fg="white")
            c.config(bg="#323232", fg="orange")

            bottom_frame.config(bg="#272727")
            label1.config(fg="gold", bg="#272727")
            label2.config(fg="gold", bg="#272727")
            label3.config(fg="gold", bg="#272727")
            label4.config(fg="gold", bg="#272727")
            wind.config(fg="white", bg="#272727")
            humidity.config(fg="white", bg="#272727")
            description.config(fg="white", bg="#272727")
            pressure.config(fg="white", bg="#272727")

            city_name.config(fg="white", bg="#323232")
            day_night_image.config(file="A:\\My Projects\\Android Subsystem for Windows (Python)\\Weather App\\moon.png")
            day_night.config(bg="#323232")
            day_night_name.config(text="Night", fg='white', bg="#323232")

            if str(condition) == "Clear":
                weather_image.config(file="A:\\My Projects\\Android Subsystem for Windows (Python)\\Weather App\\night.png")
            elif str(condition) == "Clouds" or str(condition) == "Cloudy":
                weather_image.config(file="A:\\My Projects\\Android Subsystem for Windows (Python)\\Weather App\\night_cloudy.png")
            elif str(condition) == "Snowy" or str(condition) == "Smoke" or str(condition) == "Haze":
                weather_image.config(file="A:\\My Projects\\Android Subsystem for Windows (Python)\\Weather App\\cool_night.png")
            elif str(condition) == "Rainy" or str(condition) == "Rain":
                weather_image.config(file="A:\\My Projects\\Android Subsystem for Windows (Python)\\Weather App\\night_rain.png")
            else:
                weather_image.config(file="A:\\My Projects\\Android Subsystem for Windows (Python)\\Weather App\\night.png")

        elif int(my_time) > 6 and int(my_time) < 18:
            root.config(bg="#d9f2ff")
            top_frame.config(bg="#d9f2ff")
            setting_button.config(bg="#d9f2ff", activebackground="#d9f2ff", fg="black", activeforeground='black')
            name.config(bg="#d9f2ff")
            clock.config(bg="#d9f2ff", fg="black")
            search_bar.config(bg="#d9f2ff")
            weather_image_label.config(bg="#d9f2ff")
            t.config(bg="#d9f2ff", fg="dark blue")
            c.config(bg="#d9f2ff", fg="dark red")

            bottom_frame.config(bg="#94e1ff")
            label1.config(fg="#b33b00", bg="#94e1ff")
            label2.config(fg="#b33b00", bg="#94e1ff")
            label3.config(fg="#b33b00", bg="#94e1ff")
            label4.config(fg="#b33b00", bg="#94e1ff")
            wind.config(fg="black", bg="#94e1ff")
            humidity.config(fg="black", bg="#94e1ff")
            description.config(fg="black", bg="#94e1ff")
            pressure.config(fg="black", bg="#94e1ff")

            city_name.config(fg="black", bg="#d9f2ff")
            day_night_image.config(file="A:\\My Projects\\Android Subsystem for Windows (Python)\\Weather App\\sun.png")
            day_night.config(bg="#d9f2ff")
            day_night_name.config(text="Day", fg='black', bg="#d9f2ff")

            if str(condition) == "Clear":
                weather_image.config(file="A:\\My Projects\\Android Subsystem for Windows (Python)\\Weather App\\default.png")
            elif str(condition) == "Clouds" or str(condition) == "Cloudy":
                weather_image.config(file="A:\\My Projects\\Android Subsystem for Windows (Python)\\Weather App\\cloudy.png")
            elif str(condition) == "Snowy" or str(condition) == "Smoke" or str(condition) == "Haze":
                weather_image.config(file="A:\\My Projects\\Android Subsystem for Windows (Python)\\Weather App\\light.png")
            elif str(condition) == "Rainy" or str(condition) == "Rain":
                weather_image.config(file="A:\\My Projects\\Android Subsystem for Windows (Python)\\Weather App\\rain.png")
            elif str(condition) == "Sunny":
                weather_image.config(file="A:\\My Projects\\Android Subsystem for Windows (Python)\\Weather App\\sunny.png")
            else:
                weather_image.config(file="A:\\My Projects\\Android Subsystem for Windows (Python)\\Weather App\\sunny.png")

        elif int(my_time) > 18 and int(my_time) < 24:
            root.config(bg="#323232")
            top_frame.config(bg="#323232")
            setting_button.config(bg="#323232", activebackground="#323232", fg="white", activeforeground='white')
            name.config(bg="#323232")
            clock.config(bg="#323232", fg="white")
            search_bar.config(bg="#323232")
            weather_image_label.config(bg="#323232")
            t.config(bg="#323232", fg="white")
            c.config(bg="#323232", fg="orange")

            bottom_frame.config(bg="#272727")
            label1.config(fg="gold", bg="#272727")
            label2.config(fg="gold", bg="#272727")
            label3.config(fg="gold", bg="#272727")
            label4.config(fg="gold", bg="#272727")
            wind.config(fg="white", bg="#272727")
            humidity.config(fg="white", bg="#272727")
            description.config(fg="white", bg="#272727")
            pressure.config(fg="white", bg="#272727")

            city_name.config(fg="white", bg="#323232")
            day_night_image.config(file="A:\\My Projects\\Android Subsystem for Windows (Python)\\Weather App\\moon.png")
            day_night.config(bg="#323232")
            day_night_name.config(text="Night", fg='white', bg="#323232")

            if str(condition) == "Clear":
                weather_image.config(file="A:\\My Projects\\Android Subsystem for Windows (Python)\\Weather App\\night.png")
            elif str(condition) == "Clouds" or str(condition) == "Cloudy":
                weather_image.config(file="A:\\My Projects\\Android Subsystem for Windows (Python)\\Weather App\\night_cloudy.png")
            elif str(condition) == "Snowy" or str(condition) == "Smoke" or str(condition) == "Haze":
                weather_image.config(file="A:\\My Projects\\Android Subsystem for Windows (Python)\\Weather App\\cool_night.png")
            elif str(condition) == "Rainy" or str(condition) == "Rain":
                weather_image.config(file="A:\\My Projects\\Android Subsystem for Windows (Python)\\Weather App\\night_rain.png")
            else:
                weather_image.config(file="A:\\My Projects\\Android Subsystem for Windows (Python)\\Weather App\\night.png")

        else:
            root.config(bg="#323232")
            top_frame.config(bg="#323232")
            setting_button.config(bg="#323232", activebackground="#323232", fg="white", activeforeground='white')
            name.config(bg="#323232")
            clock.config(bg="#323232", fg="white")
            search_bar.config(bg="#323232")
            weather_image_label.config(bg="#323232")
            t.config(bg="#323232", fg="white")
            c.config(bg="#323232", fg="orange")

            bottom_frame.config(bg="#272727")
            label1.config(fg="gold", bg="#272727")
            label2.config(fg="gold", bg="#272727")
            label3.config(fg="gold", bg="#272727")
            label4.config(fg="gold", bg="#272727")
            wind.config(fg="white", bg="#272727")
            humidity.config(fg="white", bg="#272727")
            description.config(fg="white", bg="#272727")
            pressure.config(fg="white", bg="#272727")

            city_name.config(fg="white", bg="#323232")
            day_night_image.config(file="A:\\My Projects\\Android Subsystem for Windows (Python)\\Weather App\\moon.png")
            day_night.config(bg="#323232")
            day_night_name.config(text="Night", fg='white', bg="#323232")

            if str(condition) == "Clear":
                weather_image.config(file="A:\\My Projects\\Android Subsystem for Windows (Python)\\Weather App\\night.png")
            elif str(condition) == "Clouds" or str(condition) == "Cloudy":
                weather_image.config(file="A:\\My Projects\\Android Subsystem for Windows (Python)\\Weather App\\night_cloudy.png")
            elif str(condition) == "Snowy" or str(condition) == "Smoke" or str(condition) == "Haze":
                weather_image.config(file="A:\\My Projects\\Android Subsystem for Windows (Python)\\Weather App\\cool_night.png")
            elif str(condition) == "Rainy" or str(condition) == "Rain":
                weather_image.config(file="A:\\My Projects\\Android Subsystem for Windows (Python)\\Weather App\\night_rain.png")
            else:
                weather_image.config(file="A:\\My Projects\\Android Subsystem for Windows (Python)\\Weather App\\night.png")

    except:
        messagebox.showerror("Weather", "Invalid entry or please check your internet connection!")


# Staring point of program
if __name__ == '__main__':
    root = Tk()
    root.title("Weather")
    root.config(bg="#d9f2ff")
    root.resizable(False, False)
    root.wm_iconbitmap("A:\\My Projects\\Android Subsystem for Windows (Python)\\Weather App\\weather_icon.ico")
    root.attributes('-alpha', 0.97)  # Transparent 3% or 0.03%
    root.geometry("900x500+200+50")

    # time
    name = Label(root, font=("Bahnschrift Condensed", 15), bg="#d9f2ff", fg="#43d9e0")
    name.place(x=30, y=100)
    clock = Label(root, font=("Bahnschrift Condensed", 20), bg="#d9f2ff")
    clock.place(x=30, y=130)
    city_name = Message(root, bg="#d9f2ff", fg="black", width=100, justify=CENTER)
    city_name.place(x=30, y=170)

    top_frame = Frame(root, bg='#d9f2ff', height=70)
    top_frame.pack(fill=X)
    bar = PhotoImage(file="A:\\My Projects\\Android Subsystem for Windows (Python)\\Weather App\\search_bar.png")
    search_bar = Label(top_frame, image=bar, bg="#d9f2ff")
    search_bar.place(x=5, y=-5)
    search = Entry(top_frame, width=20, font=("Cambria", 25), bg='white', bd=0, relief=FLAT, justify=CENTER)
    search.bind("<Return>", lambda e: Threading_get_weather())
    search.place(x=50, y=15)
    search_icon = PhotoImage(file="A:\\My Projects\\Android Subsystem for Windows (Python)\\Weather App\\search_icon.png")
    search_button = Button(top_frame, image=search_icon, bd=0, relief=FLAT, bg='white', activebackground="white", command=Threading_get_weather)
    search_button.place(x=420, y=10)
    setting_button = Button(top_frame, text="Show Result in °F", bd=0, relief=FLAT, bg='#d9f2ff', activebackground="#d9f2ff", command=result_in_fahrenheit, font=("Bahnschrift Light Condensed", 12))
    setting_button.place(x=790, y=10)

    weather_image = PhotoImage(file="A:\\My Projects\\Android Subsystem for Windows (Python)\\Weather App\\default.png")
    weather_image_label = Label(root, image=weather_image, bg="#d9f2ff")
    weather_image_label.place(x=200, y=100)

    bottom_frame = Frame(root, bg='#94e1ff', height=100)
    bottom_frame.pack(fill=X, pady=10, padx=10, side=BOTTOM)
    label1 = Label(bottom_frame, font=("Bahnschrift Condensed", 15), fg='#b33b00', bg="#94e1ff", text="WIND")
    label1.place(x=25, y=5)
    label2 = Label(bottom_frame, font=("Bahnschrift Condensed", 15), fg='#b33b00', bg="#94e1ff", text="HUMIDITY")
    label2.place(x=250, y=5)
    label3 = Label(bottom_frame, font=("Bahnschrift Condensed", 15), fg='#b33b00', bg="#94e1ff", text="DESCRIPTION")
    label3.place(x=500, y=5)
    label4 = Label(bottom_frame, font=("Bahnschrift Condensed", 15), fg='#b33b00', bg="#94e1ff", text="PRESSURE")
    label4.place(x=775, y=5)

    # temperature
    t = Label(root, font=("Bahnschrift SemiBold Condensed", 75), bg="#d9f2ff", fg="dark blue")
    t.place(x=500, y=150)
    # Condition
    c = Label(root, font=("Bahnschrift Light Condensed", 15), bg="#d9f2ff", fg="dark red")
    c.place(x=500, y=260)

    wind = Label(bottom_frame, font=("Bahnschrift Condensed", 20), fg='black', bg="#94e1ff", text="...")
    wind.place(x=25, y=35)
    humidity = Label(bottom_frame, font=("Bahnschrift Condensed", 20), fg='black', bg="#94e1ff", text="...")
    humidity.place(x=250, y=35)
    description = Label(bottom_frame, font=("Bahnschrift Condensed", 20), fg='black', bg="#94e1ff", text="...")
    description.place(x=500, y=35)
    pressure = Label(bottom_frame, font=("Bahnschrift Condensed", 20), fg='black', bg="#94e1ff", text="...")
    pressure.place(x=775, y=35)

    day_night_image = PhotoImage()
    day_night = Label(root, image=day_night_image, bg="#d9f2ff")
    day_night.place(x=800, y=80)
    day_night_name = Label(root, bg="#d9f2ff", font="Gabriola 25")
    day_night_name.place(x=810, y=150)

    root.mainloop()
