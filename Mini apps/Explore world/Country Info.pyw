# Importing useful packages
from tkinter import *
from tkinter.messagebox import showinfo, showerror
from countryinfo import CountryInfo
import webbrowser


# function for getting information of any country
def country_info():
    try:
        name = country_name.get()
        country = CountryInfo(name)

        searching_country_name = country.name()
        searching_country.config(text=searching_country_name)

        # updating basic info
        capital_name = country.capital()
        capital_name_label.config(text=capital_name, fg="black")

        calling_code = country.calling_codes()
        calling_codes_label.config(text=calling_code, fg="black")

        total_populations = country.population()
        total_populations_label.config(text=total_populations, fg="black")

        sub_region_name = country.subregion()
        sub_region_label.config(text=sub_region_name, fg="black")

        region_name = country.region()
        region_name_label.config(text=region_name, fg="black")

        currency_name = country.currencies()
        currency_name_label.config(text=currency_name, fg="black")

        native_name = country.native_name()
        native_name_label.config(text=native_name, fg="black")

        language_ = country.languages()
        language_label.config(text=language_, fg="black")
        # ________________________________________________________________________

        # for updating list box
        listbox.delete(0, END)

        alternative_name = country.alt_spellings()
        listbox.insert(END, f"Alternative names                      {alternative_name}")

        area = country.area()
        listbox.insert(END, f"Area                                              {area} square kilometer")

        provinces_ = country.provinces()
        listbox.insert(END, f"Provinces                                     {provinces_}")

        Borders = country.borders()
        listbox.insert(END, f"Borders                                        {Borders}")

        lat_lng = country.latlng()
        listbox.insert(END, f"Latitude and longitude               {lat_lng}")

        capital_lat_lng = country.capital_latlng()
        listbox.insert(END, f"Capital latitude and longitude  {capital_lat_lng}")

        country_demonym = country.demonym()
        listbox.insert(END, f"Demonym                                     {country_demonym}")

        iso = country.iso()
        listbox.insert(END, f"ISO                                                {iso}")

        languages = country.languages()
        listbox.insert(END, f"Languages                                   {languages}")

        timezone = country.timezones()
        listbox.insert(END, f"Timezones                                    {timezone}")

        tld = country.tld()
        listbox.insert(END, f"TLD                                                {tld}")
    except:
        showerror("Country information", "Incorrect country name!")


# function for searching wikipedia of given country
def My_wikipedia():
    try:
        name = country_name.get()
        url = "https://en.wikipedia.org/wiki/"+name
        webbrowser.open(url)
    except:
        showinfo("Wikipedia", "Check your internet connection")


# Creating window
root = Tk()
root.geometry('1000x600+150+20')
root.config(bg="#00b0fc")
root.resizable(False, False)
root.title("Country Information")
root.wm_iconbitmap("A:\\My Projects\\Android Subsystem for Windows (Python)\\Mini apps\\Explore world\\explore_world_icon.ico")

# set labels and buttons in top bar
Label(root, text="Country name : ", font=("Bahnschrift Light Condensed", 15), bg="#00b0fc").place(x=10, y=10)
country_name = Entry(root, width=25, bd=0.5, relief=SOLID, font=("Bahnschrift Light Condensed", 15))
country_name.bind("<Return>", lambda e: country_info())         # bind with enter key
country_name.place(x=130, y=10)
Button(root, text="Search", bd=0, relief=FLAT, bg='#00b0fc', activebackground="#00b0fc", command=country_info, font=("Bahnschrift Light Condensed", 15)).place(x=350, y=3)
Button(root, text="Wikipedia", bd=0, relief=FLAT, bg='#00b0fc', activebackground="#00b0fc", command=My_wikipedia, font=("Bahnschrift Light Condensed", 15)).place(x=420, y=3)
searching_country = Label(root, text="", bg="#00b0fc", font=("Bahnschrift Light Condensed", 25, 'bold'), fg='white')
searching_country.place(x=700, y=0)

# Creating frame 1 for basic information of given country
Basic_info1 = Frame(root, width=500, height=150, bg="#ececec")
Basic_info1.place(x=0, y=50)

Label(Basic_info1, text="Capital ", font=("Bahnschrift Condensed", 15), bg="#ececec", fg="gray").place(x=10, y=5)
capital_name_label = Label(Basic_info1, text="Unknown", font=("Bahnschrift Condensed", 15), bg="#ececec", fg="light gray")
capital_name_label.place(x=120, y=5)

Label(Basic_info1, text="Calling codes ", font=("Bahnschrift Condensed", 15), bg="#ececec", fg="gray").place(x=10, y=40)
calling_codes_label = Label(Basic_info1, text="Unknown", font=("Bahnschrift Condensed", 15), bg="#ececec", fg="light gray")
calling_codes_label.place(x=120, y=40)

Label(Basic_info1, text="Populations ", font=("Bahnschrift Condensed", 15), bg="#ececec", fg="gray").place(x=10, y=75)
total_populations_label = Label(Basic_info1, text="Unknown", font=("Bahnschrift Condensed", 15), bg="#ececec", fg="light gray")
total_populations_label.place(x=120, y=75)

Label(Basic_info1, text="Sub-Region ", font=("Bahnschrift Condensed", 15), bg="#ececec", fg="gray").place(x=10, y=110)
sub_region_label = Label(Basic_info1, text="Unknown", font=("Bahnschrift Condensed", 15), bg="#ececec", fg="light gray")
sub_region_label.place(x=120, y=110)

# Creating frame 2 for basic information of given country
Basic_info2 = Frame(root, width=500, height=150, bg="#ececec")
Basic_info2.place(x=500, y=50)

Label(Basic_info2, text="Region ", font=("Bahnschrift Condensed", 15), bg="#ececec", fg="gray").place(x=10, y=5)
region_name_label = Label(Basic_info2, text="Unknown", font=("Bahnschrift Condensed", 15), bg="#ececec", fg="light gray")
region_name_label.place(x=120, y=5)

Label(Basic_info2, text="Currency ", font=("Bahnschrift Condensed", 15), bg="#ececec", fg="gray").place(x=10, y=40)
currency_name_label = Label(Basic_info2, text="Unknown", font=("Bahnschrift Condensed", 15), bg="#ececec", fg="light gray")
currency_name_label.place(x=120, y=40)

Label(Basic_info2, text="Native name ", font=("Bahnschrift Condensed", 15), bg="#ececec", fg="gray").place(x=10, y=75)
native_name_label = Label(Basic_info2, text="Unknown", font=("Bahnschrift Condensed", 15), bg="#ececec", fg="light gray")
native_name_label.place(x=120, y=75)

Label(Basic_info2, text="Language ", font=("Bahnschrift Condensed", 15), bg="#ececec", fg="gray").place(x=10, y=110)
language_label = Label(Basic_info2, text="Unknown", font=("Bahnschrift Condensed", 15), bg="#ececec", fg="light gray")
language_label.place(x=120, y=110)


# Creating Information_area for listbox
Information_area = Frame(root, width=1000, height=400, bg="#fbfbfb")
Information_area.place(x=0, y=200)

# listbox for other information of country
listbox = Listbox(Information_area, selectbackground='#12fff0', selectforeground='dark blue', selectborderwidth=4, font=("Bahnschrift Light Condensed", 16), bd=1, relief=SOLID, bg="#fbfbfb", justify=LEFT, highlightthickness=0)
listbox.place(relx=0, rely=0, relheight=1, relwidth=1)

# Scrollbar in listbox
scrollbar = Scrollbar(listbox, orient=HORIZONTAL, command=listbox.xview)
scrollbar.pack(side=BOTTOM, fill=X)
listbox.config(xscrollcommand=scrollbar.set)

root.mainloop()
