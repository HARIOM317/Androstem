# Importing required packages
from tkinter import *
from tkinter.messagebox import showerror
import requests
from bs4 import BeautifulSoup
from threading import Thread


# threading in get data function
def threading_get_data():
    t1 = Thread(target=get_data)
    t1.start()


# function for getting regional data of covid-19
def get_data():
    try:
        root.title("Searching...")
        url = "https://www.worldometers.info/coronavirus/"
        r = requests.get(url)
        # parsing content
        soup = BeautifulSoup(r.content, 'html.parser')
        table_body = soup.find('tbody')         # finding table body in html code
        table_rows = table_body.find_all('tr')          # finding all table rows
        country = country_name.get().lower()

        # condition for empty entry box
        if country == "":
            country = "world"

        # finding table data
        for i in table_rows:
            id = i.find_all('td')
            if id[1].text.strip().lower() == country:
                # Updating all labels
                label1.config(fg="#c6c5c2")
                label2.config(fg="#c6c5c2")
                label3.config(fg="#c6c5c2")
                label4.config(fg="#c6c5c2")
                label5.config(fg="#c6c5c2")
                label6.config(fg="#c6c5c2")
                label7.config(fg="#c6c5c2")
                label8.config(fg="#c6c5c2")
                label9.config(fg="#c6c5c2")
                label10.config(fg="#c6c5c2")
                label11.config(fg="#c6c5c2")
                label12.config(fg="#c6c5c2")
                label13.config(fg="#c6c5c2")
                label14.config(fg="#c6c5c2")

                region_label.config(text=f"{id[1].text.strip()}", fg="#ffffff")
                total_cases_label.config(text=f"{id[2].text.strip()}", fg="#ffffff")
                new_cases_label.config(text=f"{id[3].text.strip()}", fg="#ffffff")
                total_deaths_label.config(text=f"{id[4].text.strip()}", fg="#ffffff")
                new_deaths_label.config(text=f"{id[5].text.strip()}", fg="#ffffff")
                total_recovered_label.config(text=f"{id[6].text.strip()}", fg="#ffffff")
                new_recovered_label.config(text=f"{id[7].text.strip()}", fg="#ffffff")
                active_cases_label.config(text=f"{id[8].text.strip()}", fg="#ffffff")
                serious_cases_label.config(text=f"{id[9].text.strip()}", fg="#ffffff")
                cases_1M_pop_label.config(text=f"{id[10].text.strip()}", fg="#ffffff")
                deaths_1M_pop_label.config(text=f"{id[11].text.strip()}", fg="#ffffff")
                total_tests_label.config(text=f"{id[12].text.strip()}", fg="#ffffff")
                tests_1M_pop_label.config(text=f"{id[13].text.strip()}", fg="#ffffff")
                population_label.config(text=f"{id[14].text.strip()}", fg="#ffffff")

                root.title("Covid-Update")
    except:
        # if you are no connected throw internet
        showerror("Error", "Check your internet connection")
        root.title("Covid-Update")


# creating window
root = Tk()
root.title("Covid-Update")
root.geometry("850x500+300+50")
root.config(bg="#191919")
root.resizable(False, False)
root.wm_iconbitmap("A:\\My Projects\\Android Subsystem for Windows (Python)\\Covid update\\covid_update.ico")

# Creating frames
top_frame = Frame(root, width=860, height=55, bg="#202020", bd=1, relief=GROOVE)
top_frame.place(x=-5, y=-5)

bottom_frame1 = Frame(root, width=425, height=370, bg="#191919")
bottom_frame1.place(x=0, y=130)

bottom_frame2 = Frame(root, width=425, height=370, bg="#191919")
bottom_frame2.place(x=425, y=130)

Label(top_frame, text="Search region name for covid information", font=("Bahnschrift Light Condensed", 25), bg="#202020", fg="gray").place(x=190, y=5)

# loading images
search_bar_icon = PhotoImage(file="A:\\My Projects\\Android Subsystem for Windows (Python)\\Covid update\\search_bar.png")
search_button_icon = PhotoImage(file="A:\\My Projects\\Android Subsystem for Windows (Python)\\Covid update\\search_icon.png")

# search bar
search_bar = Label(root, image=search_bar_icon, bd=0, bg="#191919")
search_bar.place(x=185, y=50)

# creating entry box
country_name = StringVar()
entry_box = Entry(root, font=("Bahnschrift Light Condensed", 25), width=25, bd=0, relief=FLAT, bg="#121212", fg="#24fff9", textvariable=country_name)
entry_box.focus()
entry_box.bind("<Return>", lambda e: get_data())        # binding with enter key
entry_box.place(x=215, y=66)

# search button
Button(root, image=search_button_icon, bg="#121212", activebackground="#121212", bd=0, relief=FLAT, command=threading_get_data).place(x=570, y=60)

# Creating all labels
# for bottom frame 1
label1 = Label(bottom_frame1, text="Region", font=("Bahnschrift Light Condensed", 20), bg="#191919", fg="gray")
label1.place(x=10, y=10)
label2 = Label(bottom_frame1, text="Total cases", font=("Bahnschrift Light Condensed", 20), bg="#191919", fg="gray")
label2.place(x=10, y=60)
label3 = Label(bottom_frame1, text="New cases", font=("Bahnschrift Light Condensed", 20), bg="#191919", fg="gray")
label3.place(x=10, y=110)
label4 = Label(bottom_frame1, text="Total deaths", font=("Bahnschrift Light Condensed", 20), bg="#191919", fg="gray")
label4.place(x=10, y=160)
label5 = Label(bottom_frame1, text="New deaths", font=("Bahnschrift Light Condensed", 20), bg="#191919", fg="gray")
label5.place(x=10, y=210)
label6 = Label(bottom_frame1, text="Total recovered", font=("Bahnschrift Light Condensed", 20), bg="#191919", fg="gray")
label6.place(x=10, y=260)
label7 = Label(bottom_frame1, text="New recovered", font=("Bahnschrift Light Condensed", 20), bg="#191919", fg="gray")
label7.place(x=10, y=310)

# for bottom frame 2
label8 = Label(bottom_frame2, text="Active cases", font=("Bahnschrift Light Condensed", 20), bg="#191919", fg="gray")
label8.place(x=10, y=10)
label9 = Label(bottom_frame2, text="Serious", font=("Bahnschrift Light Condensed", 20), bg="#191919", fg="gray")
label9.place(x=10, y=60)
label10 = Label(bottom_frame2, text="Total cases 1M pop", font=("Bahnschrift Light Condensed", 20), bg="#191919", fg="gray")
label10.place(x=10, y=110)
label11 = Label(bottom_frame2, text="Deaths 1M pop", font=("Bahnschrift Light Condensed", 20), bg="#191919", fg="gray")
label11.place(x=10, y=160)
label12 = Label(bottom_frame2, text="Total tests", font=("Bahnschrift Light Condensed", 20), bg="#191919", fg="gray")
label12.place(x=10, y=210)
label13 = Label(bottom_frame2, text="Tests 1M pop", font=("Bahnschrift Light Condensed", 20), bg="#191919", fg="gray")
label13.place(x=10, y=260)
label14 = Label(bottom_frame2, text="Population", font=("Bahnschrift Light Condensed", 20), bg="#191919", fg="gray")
label14.place(x=10, y=310)

# labels for correct data
region_label = Label(bottom_frame1, text="None", font=("Bahnschrift Light Condensed", 20), bg="#191919", fg="#635f5a")
region_label.place(x=160, y=10)

total_cases_label = Label(bottom_frame1, text="None", font=("Bahnschrift Light Condensed", 20), bg="#191919", fg="#635f5a")
total_cases_label.place(x=160, y=60)

new_cases_label = Label(bottom_frame1, text="None", font=("Bahnschrift Light Condensed", 20), bg="#191919", fg="#635f5a")
new_cases_label.place(x=160, y=110)

total_deaths_label = Label(bottom_frame1, text="None", font=("Bahnschrift Light Condensed", 20), bg="#191919", fg="#635f5a")
total_deaths_label.place(x=160, y=160)

new_deaths_label = Label(bottom_frame1, text="None", font=("Bahnschrift Light Condensed", 20), bg="#191919", fg="#635f5a")
new_deaths_label.place(x=160, y=210)

total_recovered_label = Label(bottom_frame1, text="None", font=("Bahnschrift Light Condensed", 20), bg="#191919", fg="#635f5a")
total_recovered_label.place(x=160, y=260)

new_recovered_label = Label(bottom_frame1, text="None", font=("Bahnschrift Light Condensed", 20), bg="#191919", fg="#635f5a")
new_recovered_label.place(x=160, y=310)

active_cases_label = Label(bottom_frame2, text="None", font=("Bahnschrift Light Condensed", 20), bg="#191919", fg="#635f5a")
active_cases_label.place(x=185, y=10)

serious_cases_label = Label(bottom_frame2, text="None", font=("Bahnschrift Light Condensed", 20), bg="#191919", fg="#635f5a")
serious_cases_label.place(x=185, y=60)

cases_1M_pop_label = Label(bottom_frame2, text="None", font=("Bahnschrift Light Condensed", 20), bg="#191919", fg="#635f5a")
cases_1M_pop_label.place(x=185, y=110)

deaths_1M_pop_label = Label(bottom_frame2, text="None", font=("Bahnschrift Light Condensed", 20), bg="#191919", fg="#635f5a")
deaths_1M_pop_label.place(x=185, y=160)

total_tests_label = Label(bottom_frame2, text="None", font=("Bahnschrift Light Condensed", 20), bg="#191919", fg="#635f5a")
total_tests_label.place(x=185, y=210)

tests_1M_pop_label = Label(bottom_frame2, text="None", font=("Bahnschrift Light Condensed", 20), bg="#191919", fg="#635f5a")
tests_1M_pop_label.place(x=185, y=260)

population_label = Label(bottom_frame2, text="None", font=("Bahnschrift Light Condensed", 20), bg="#191919", fg="#635f5a")
population_label.place(x=185, y=310)

root.mainloop()
