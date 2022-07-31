# Importing useful modules
from tkinter import *
from tkinter import ttk, messagebox
from threading import Thread
import json
import requests


# Handle Threading
def threading_convert():
    t1 = Thread(target=convert)
    t1.start()


# create convert function
def convert():
    try:
        # Using the API
        url = "https://currency-converter18.p.rapidapi.com/api/v1/convert"
        currency_1 = combo_box1.get()
        currency_2 = combo_box2.get()
        _amount = value.get()

        # _____________________ For Currency 1 _____________________
        if currency_1 == "Albania Lek, ALL":
            currency_1 = "ALL"
        elif currency_1 == "Afghanistan Afghani, AFN":
            currency_1 = "AFN"
        elif currency_1 == "Argentina Peso, ARS":
            currency_1 = "ARS"
        elif currency_1 == "Aruba Guilder, AWG":
            currency_1 = "AWG"
        elif currency_1 == "Australia Dollar, AUD":
            currency_1 = "AUD"
        elif currency_1 == "Azerbaijan Manat, AZN":
            currency_1 = "AZN"
        elif currency_1 == "Bahamas Dollar, BSD":
            currency_1 = "BSD"
        elif currency_1 == "Barbados Dollar, BBD":
            currency_1 = "BBD"
        elif currency_1 == "Belarus Ruble, BYN":
            currency_1 = "BYN"
        elif currency_1 == "Belize Dollar, BZD":
            currency_1 = "BZD"
        elif currency_1 == "Bermuda Dollar, BMD":
            currency_1 = "BMD"
        elif currency_1 == "Bolivia Bolíviano, BOB":
            currency_1 = "BOB"
        elif currency_1 == "Bosnia and Herzegovina Convertible Mark, BAM":
            currency_1 = "BAM"
        elif currency_1 == "Botswana Pula, BWP":
            currency_1 = "BWP"
        elif currency_1 == "Bulgaria Lev, BGN":
            currency_1 = "BGN"
        elif currency_1 == "Brazil Real, BRL":
            currency_1 = "BRL"
        elif currency_1 == "Brunei Darussalam Dollar, BND":
            currency_1 = "BND"
        elif currency_1 == "Cambodia Riel, KHR":
            currency_1 = "KHR"
        elif currency_1 == "Canada Dollar, CAD":
            currency_1 = "CAD"
        elif currency_1 == "Cayman Islands Dollar, KYD":
            currency_1 = "KYD"
        elif currency_1 == "Chile Peso, CLP":
            currency_1 = "CLP"
        elif currency_1 == "China Yuan Renminbi, CNY":
            currency_1 = "CNY"
        elif currency_1 == "Colombia Peso, COP":
            currency_1 = "COP"
        elif currency_1 == "Costa Rica Colon, CRC":
            currency_1 = "CRC"
        elif currency_1 == "Croatia Kuna, HRK":
            currency_1 = "HRK"
        elif currency_1 == "Cuba Peso, CUP":
            currency_1 = "CUP"
        elif currency_1 == "Czech Republic Koruna, CZK":
            currency_1 = "CZK"
        elif currency_1 == "Denmark Krone, DKK":
            currency_1 = "DKK"
        elif currency_1 == "Dominican Republic Peso, DOP":
            currency_1 = "DOP"
        elif currency_1 == "East Caribbean Dollar, XCD":
            currency_1 = "XCD"
        elif currency_1 == "Egypt Pound, EGP":
            currency_1 = "EGP"
        elif currency_1 == "El Salvador Colon, SVC":
            currency_1 = "SVC"
        elif currency_1 == "Euro Member Countries, EUR":
            currency_1 = "EUR"
        elif currency_1 == "Falkland Islands (Malvinas) Pound, FKP":
            currency_1 = "FKP"
        elif currency_1 == "Fiji Dollar, FJD":
            currency_1 = "FJD"
        elif currency_1 == "Ghana Cedi, GHS":
            currency_1 = "GHS"
        elif currency_1 == "Gibraltar Pound, GIP":
            currency_1 = "GIP"
        elif currency_1 == "Guatemala Quetzal, GTQ":
            currency_1 = "GTQ"
        elif currency_1 == "Guernsey Pound, GGP":
            currency_1 = "GGP"
        elif currency_1 == "Guyana Dollar, GYD":
            currency_1 = "GYD"
        elif currency_1 == "Honduras Lempira, HNL":
            currency_1 = "HNL"
        elif currency_1 == "Hong Kong Dollar, HKD":
            currency_1 = "HKD"
        elif currency_1 == "Hungary Forint, HUF":
            currency_1 = "HUF"
        elif currency_1 == "Iceland Krona, ISK":
            currency_1 = "ISK"
        elif currency_1 == "India Rupee, INR":
            currency_1 = "INR"
        elif currency_1 == "Indonesia Rupiah, IDR":
            currency_1 = "IDR"
        elif currency_1 == "Iran Rial, IRR":
            currency_1 = "IRR"
        elif currency_1 == "Isle of Man Pound, IMP":
            currency_1 = "IMP"
        elif currency_1 == "Israel Shekel, ILS":
            currency_1 = "ILS"
        elif currency_1 == "Jamaica Dollar, JMD":
            currency_1 = "JMD"
        elif currency_1 == "Japan Yen, JPY":
            currency_1 = "JPY"
        elif currency_1 == "Jersey Pound, JEP":
            currency_1 = "JEP"
        elif currency_1 == "Kazakhstan Tenge, KZT":
            currency_1 = "KZT"
        elif currency_1 == "Korea (South) Won, KRW":
            currency_1 = "KRW"
        elif currency_1 == "Kyrgyzstan Som, KGS":
            currency_1 = "KGS"
        elif currency_1 == "Laos Kip, LAK":
            currency_1 = "LAK"
        elif currency_1 == "Lebanon Pound, LBP":
            currency_1 = "LBP"
        elif currency_1 == "Liberia Dollar, LRD":
            currency_1 = "LRD"
        elif currency_1 == "Macedonia Denar, MKD":
            currency_1 = "MKD"
        elif currency_1 == "Malaysia Ringgit, MYR":
            currency_1 = "MYR"
        elif currency_1 == "Mauritius Rupee, MUR":
            currency_1 = "MUR"
        elif currency_1 == "Mexico Peso, MXN":
            currency_1 = "MXN"
        elif currency_1 == "Mozambique Metical, MZN":
            currency_1 = "MZN"
        elif currency_1 == "Namibia Dollar, NAD":
            currency_1 = "NAD"
        elif currency_1 == "Nepal Rupee, NPR":
            currency_1 = "NPR"
        elif currency_1 == "Netherlands Antilles Guilder, ANG":
            currency_1 = "ANG"
        elif currency_1 == "New Zealand Dollar, NZD":
            currency_1 = "NZD"
        elif currency_1 == "Nicaragua Cordoba, NIO":
            currency_1 = "NIO"
        elif currency_1 == "Nigeria Naira, NGN":
            currency_1 = "NGN"
        elif currency_1 == "Norway Krone, NOK":
            currency_1 = "NOK"
        elif currency_1 == "Oman Rial, OMR":
            currency_1 = "OMR"
        elif currency_1 == "Pakistan Rupee, PKR":
            currency_1 = "PKR"
        elif currency_1 == "Panama Balboa, PAB":
            currency_1 = "PAB"
        elif currency_1 == "Paraguay Guarani, PYG":
            currency_1 = "PYG"
        elif currency_1 == "Peru Sol, PEN":
            currency_1 = "PEN"
        elif currency_1 == "Philippines Peso, PHP":
            currency_1 = "PHP"
        elif currency_1 == "Poland Zloty, PLN":
            currency_1 = "PLN"
        elif currency_1 == "Qatar Riyal, QAR":
            currency_1 = "QAR"
        elif currency_1 == "Romania Leu, RON":
            currency_1 = "RON"
        elif currency_1 == "Russia Ruble, RUB":
            currency_1 = "RUB"
        elif currency_1 == "Saint Helena Pound, SHP":
            currency_1 = "SHP"
        elif currency_1 == "Saudi Arabia Riyal, SAR":
            currency_1 = "SAR"
        elif currency_1 == "Serbia Dinar, RSD":
            currency_1 = "RSD"
        elif currency_1 == "Seychelles Rupee, SCR":
            currency_1 = "SCR"
        elif currency_1 == "Singapore Dollar, SGD":
            currency_1 = "SGD"
        elif currency_1 == "Solomon Islands Dollar, SBD":
            currency_1 = "SBD"
        elif currency_1 == "Somalia Shilling, SOS":
            currency_1 = "SOS"
        elif currency_1 == "South Africa Rand, ZAR":
            currency_1 = "ZAR"
        elif currency_1 == "Sri Lanka Rupee, LKR":
            currency_1 = "LKR"
        elif currency_1 == "Sweden Krona, SEK":
            currency_1 = "SEK"
        elif currency_1 == "Switzerland Franc, CHF":
            currency_1 = "CHF"
        elif currency_1 == "Suriname Dollar, SRD":
            currency_1 = "SRD"
        elif currency_1 == "Taiwan New Dollar, TWD":
            currency_1 = "TWD"
        elif currency_1 == "Thailand Baht, THB":
            currency_1 = "THB"
        elif currency_1 == "Trinidad and Tobago Dollar, TTD":
            currency_1 = "TTD"
        elif currency_1 == "Turkey Lira, TRY":
            currency_1 = "TRY"
        elif currency_1 == "Ukraine Hryvnia, UAH":
            currency_1 = "UAH"
        elif currency_1 == "United Kingdom Pound, GBP":
            currency_1 = "GBP"
        elif currency_1 == "United States Dollar, USD":
            currency_1 = "USD"
        elif currency_1 == "Uruguay Peso, UYU":
            currency_1 = "UYU"
        elif currency_1 == "Uzbekistan Som, UZS":
            currency_1 = "UZS"
        elif currency_1 == "Viet Nam Dong, VND":
            currency_1 = "VND"
        elif currency_1 == "Yemen Rial, YER":
            currency_1 = "YER"
        elif currency_1 == "Zambia Kwacha, ZMW":
            currency_1 = "ZMW"

        # _____________________ For Currency 2 _____________________
        if currency_2 == "Albania Lek, ALL":
            currency_2 = "ALL"
            symbol = "Lek"
        elif currency_2 == "Afghanistan Afghani, AFN":
            currency_2 = "AFN"
            symbol = "؋"
        elif currency_2 == "Argentina Peso, ARS":
            currency_2 = "ARS"
            symbol = "$"
        elif currency_2 == "Aruba Guilder, AWG":
            currency_2 = "AWG"
            symbol = "ƒ"
        elif currency_2 == "Australia Dollar, AUD":
            currency_2 = "AUD"
            symbol = "$"
        elif currency_2 == "Azerbaijan Manat, AZN":
            currency_2 = "AZN"
            symbol = "₼"
        elif currency_2 == "Bahamas Dollar, BSD":
            currency_2 = "BSD"
            symbol = "$"
        elif currency_2 == "Barbados Dollar, BBD":
            currency_2 = "BBD"
            symbol = "$"
        elif currency_2 == "Belarus Ruble, BYN":
            currency_2 = "BYN"
            symbol = "Br"
        elif currency_2 == "Belize Dollar, BZD":
            currency_2 = "BZD"
            symbol = "BZ$"
        elif currency_2 == "Bermuda Dollar, BMD":
            currency_2 = "BMD"
            symbol = "$"
        elif currency_2 == "Bolivia Bolíviano, BOB":
            currency_2 = "BOB"
            symbol = "$b"
        elif currency_2 == "Bosnia and Herzegovina Convertible Mark, BAM":
            currency_2 = "BAM"
            symbol = "KM"
        elif currency_2 == "Botswana Pula, BWP":
            currency_2 = "BWP"
            symbol = "P"
        elif currency_2 == "Bulgaria Lev, BGN":
            currency_2 = "BGN"
            symbol = "лв"
        elif currency_2 == "Brazil Real, BRL":
            currency_2 = "BRL"
            symbol = "R$"
        elif currency_2 == "Brunei Darussalam Dollar, BND":
            currency_2 = "BND"
            symbol = "$"
        elif currency_2 == "Cambodia Riel, KHR":
            currency_2 = "KHR"
            symbol = "៛"
        elif currency_2 == "Canada Dollar, CAD":
            currency_2 = "CAD"
            symbol = "$"
        elif currency_2 == "Cayman Islands Dollar, KYD":
            currency_2 = "KYD"
            symbol = "$"
        elif currency_2 == "Chile Peso, CLP":
            currency_2 = "CLP"
            symbol = "$"
        elif currency_2 == "China Yuan Renminbi, CNY":
            currency_2 = "CNY"
            symbol = "¥"
        elif currency_2 == "Colombia Peso, COP":
            currency_2 = "COP"
            symbol = "$"
        elif currency_2 == "Costa Rica Colon, CRC":
            currency_2 = "CRC"
            symbol = "₡"
        elif currency_2 == "Croatia Kuna, HRK":
            currency_2 = "HRK"
            symbol = "kn"
        elif currency_2 == "Cuba Peso, CUP":
            currency_2 = "CUP"
            symbol = "₱"
        elif currency_2 == "Czech Republic Koruna, CZK":
            currency_2 = "CZK"
            symbol = "Kč"
        elif currency_2 == "Denmark Krone, DKK":
            currency_2 = "DKK"
            symbol = "kr"
        elif currency_2 == "Dominican Republic Peso, DOP":
            currency_2 = "DOP"
            symbol = "RD$"
        elif currency_2 == "East Caribbean Dollar, XCD":
            currency_2 = "XCD"
            symbol = "$"
        elif currency_2 == "Egypt Pound, EGP":
            currency_2 = "EGP"
            symbol = "£"
        elif currency_2 == "El Salvador Colon, SVC":
            currency_2 = "SVC"
            symbol = "$"
        elif currency_2 == "Euro Member Countries, EUR":
            currency_2 = "EUR"
            symbol = "€"
        elif currency_2 == "Falkland Islands (Malvinas) Pound, FKP":
            currency_2 = "FKP"
            symbol = "£"
        elif currency_2 == "Fiji Dollar, FJD":
            currency_2 = "FJD"
            symbol = "$"
        elif currency_2 == "Ghana Cedi, GHS":
            currency_2 = "GHS"
            symbol = "¢"
        elif currency_2 == "Gibraltar Pound, GIP":
            currency_2 = "GIP"
            symbol = "£"
        elif currency_2 == "Guatemala Quetzal, GTQ":
            currency_2 = "GTQ"
            symbol = "Q"
        elif currency_2 == "Guernsey Pound, GGP":
            currency_2 = "GGP"
            symbol = "£"
        elif currency_2 == "Guyana Dollar, GYD":
            currency_2 = "GYD"
            symbol = "$"
        elif currency_2 == "Honduras Lempira, HNL":
            currency_2 = "HNL"
            symbol = "L"
        elif currency_2 == "Hong Kong Dollar, HKD":
            currency_2 = "HKD"
            symbol = "$"
        elif currency_2 == "Hungary Forint, HUF":
            currency_2 = "HUF"
            symbol = "Ft"
        elif currency_2 == "Iceland Krona, ISK":
            currency_2 = "ISK"
            symbol = "kr"
        elif currency_2 == "India Rupee, INR":
            currency_2 = "INR"
            symbol = "₹"
        elif currency_2 == "Indonesia Rupiah, IDR":
            currency_2 = "IDR"
            symbol = "Rp"
        elif currency_2 == "Iran Rial, IRR":
            currency_2 = "IRR"
            symbol = "﷼"
        elif currency_2 == "Isle of Man Pound, IMP":
            currency_2 = "IMP"
            symbol = "£"
        elif currency_2 == "Israel Shekel, ILS":
            currency_2 = "ILS"
            symbol = "₪"
        elif currency_2 == "Jamaica Dollar, JMD":
            currency_2 = "JMD"
            symbol = "J$"
        elif currency_2 == "Japan Yen, JPY":
            currency_2 = "JPY"
            symbol = "¥"
        elif currency_2 == "Jersey Pound, JEP":
            currency_2 = "JEP"
            symbol = "£"
        elif currency_2 == "Kazakhstan Tenge, KZT":
            currency_2 = "KZT"
            symbol = "лв"
        elif currency_2 == "Korea (South) Won, KRW":
            currency_2 = "KRW"
            symbol = "₩"
        elif currency_2 == "Kyrgyzstan Som, KGS":
            currency_2 = "KGS"
            symbol = "лв"
        elif currency_2 == "Laos Kip, LAK":
            currency_2 = "LAK"
            symbol = "₭"
        elif currency_2 == "Lebanon Pound, LBP":
            currency_2 = "LBP"
            symbol = "£"
        elif currency_2 == "Liberia Dollar, LRD":
            currency_2 = "LRD"
            symbol = "$"
        elif currency_2 == "Macedonia Denar, MKD":
            currency_2 = "MKD"
            symbol = "ден"
        elif currency_2 == "Malaysia Ringgit, MYR":
            currency_2 = "MYR"
            symbol = "RM"
        elif currency_2 == "Mauritius Rupee, MUR":
            currency_2 = "MUR"
            symbol = "₨"
        elif currency_2 == "Mexico Peso, MXN":
            currency_2 = "MXN"
            symbol = "$"
        elif currency_2 == "Mozambique Metical, MZN":
            currency_2 = "MZN"
            symbol = "MT"
        elif currency_2 == "Namibia Dollar, NAD":
            currency_2 = "NAD"
            symbol = "$"
        elif currency_2 == "Nepal Rupee, NPR":
            currency_2 = "NPR"
            symbol = "₨"
        elif currency_2 == "Netherlands Antilles Guilder, ANG":
            currency_2 = "ANG"
            symbol = "ƒ"
        elif currency_2 == "New Zealand Dollar, NZD":
            currency_2 = "NZD"
            symbol = "$"
        elif currency_2 == "Nicaragua Cordoba, NIO":
            currency_2 = "NIO"
            symbol = "C$"
        elif currency_2 == "Nigeria Naira, NGN":
            currency_2 = "NGN"
            symbol = "₦"
        elif currency_2 == "Norway Krone, NOK":
            currency_2 = "NOK"
            symbol = "kr"
        elif currency_2 == "Oman Rial, OMR":
            currency_2 = "OMR"
            symbol = "﷼"
        elif currency_2 == "Pakistan Rupee, PKR":
            currency_2 = "PKR"
            symbol = "₨"
        elif currency_2 == "Panama Balboa, PAB":
            currency_2 = "PAB"
            symbol = "B/."
        elif currency_2 == "Paraguay Guarani, PYG":
            currency_2 = "PYG"
            symbol = "Gs"
        elif currency_2 == "Peru Sol, PEN":
            currency_2 = "PEN"
            symbol = "S/."
        elif currency_2 == "Philippines Peso, PHP":
            currency_2 = "PHP"
            symbol = "₱"
        elif currency_2 == "Poland Zloty, PLN":
            currency_2 = "PLN"
            symbol = "zł"
        elif currency_2 == "Qatar Riyal, QAR":
            currency_2 = "QAR"
            symbol = "﷼"
        elif currency_2 == "Romania Leu, RON":
            currency_2 = "RON"
            symbol = "lei"
        elif currency_2 == "Russia Ruble, RUB":
            currency_2 = "RUB"
            symbol = "₽"
        elif currency_2 == "Saint Helena Pound, SHP":
            currency_2 = "SHP"
            symbol = "£"
        elif currency_2 == "Saudi Arabia Riyal, SAR":
            currency_2 = "SAR"
            symbol = "﷼"
        elif currency_2 == "Serbia Dinar, RSD":
            currency_2 = "RSD"
            symbol = "Дин."
        elif currency_2 == "Seychelles Rupee, SCR":
            currency_2 = "SCR"
            symbol = "₨"
        elif currency_2 == "Singapore Dollar, SGD":
            currency_2 = "SGD"
            symbol = "$"
        elif currency_2 == "Solomon Islands Dollar, SBD":
            currency_2 = "SBD"
            symbol = "$"
        elif currency_2 == "Somalia Shilling, SOS":
            currency_2 = "SOS"
            symbol = "S"
        elif currency_2 == "South Africa Rand, ZAR":
            currency_2 = "ZAR"
            symbol = "R"
        elif currency_2 == "Sri Lanka Rupee, LKR":
            currency_2 = "LKR"
            symbol = "₨"
        elif currency_2 == "Sweden Krona, SEK":
            currency_2 = "SEK"
            symbol = "kr"
        elif currency_2 == "Switzerland Franc, CHF":
            currency_2 = "CHF"
            symbol = "CHF"
        elif currency_2 == "Suriname Dollar, SRD":
            currency_2 = "SRD"
            symbol = "$"
        elif currency_2 == "Taiwan New Dollar, TWD":
            currency_2 = "TWD"
            symbol = "NT$"
        elif currency_2 == "Thailand Baht, THB":
            currency_2 = "THB"
            symbol = "฿"
        elif currency_2 == "Trinidad and Tobago Dollar, TTD":
            currency_2 = "TTD"
            symbol = "TT$"
        elif currency_2 == "Turkey Lira, TRY":
            currency_2 = "TRY"
            symbol = "₺"
        elif currency_2 == "Ukraine Hryvnia, UAH":
            currency_2 = "UAH"
            symbol = "₴"
        elif currency_2 == "United Kingdom Pound, GBP":
            currency_2 = "GBP"
            symbol = "£"
        elif currency_2 == "United States Dollar, USD":
            currency_2 = "USD"
            symbol = "$"
        elif currency_2 == "Uruguay Peso, UYU":
            currency_2 = "UYU"
            symbol = "$U"
        elif currency_2 == "Uzbekistan Som, UZS":
            currency_2 = "UZS"
            symbol = "лв"
        elif currency_2 == "Viet Nam Dong, VND":
            currency_2 = "VND"
            symbol = "₫"
        elif currency_2 == "Yemen Rial, YER":
            currency_2 = "YER"
            symbol = "﷼"
        elif currency_2 == "Zambia Kwacha, ZMW":
            currency_2 = "ZMW"
            symbol = "ZK"

        querystring = {"from": currency_1, "to": currency_2, "amount": _amount}
        headers = {
            "X-RapidAPI-Host": "currency-converter18.p.rapidapi.com",
            "X-RapidAPI-Key": "be6bf1c37fmshfd620f5f2da1fe3p12acb3jsn35d73b325b3a"
        }
        response = requests.request("GET", url, headers=headers, params=querystring)
        data = json.loads(response.text)
        converted_amount = data["result"]["convertedAmount"]
        formatted_amount = symbol + " {:,.3f}".format(converted_amount)
        result.config(text=formatted_amount)
    except:
        messagebox.showinfo("Currency Convertor", "Something went wrong!")

# Starting point of program
if __name__ == '__main__':
    root = Tk()
    root.title("Currency Convertor")
    root.resizable(False, False)
    root.geometry("300x500+500+50")
    root.config(bg="#b7c5ce")
    root.wm_iconbitmap("A:\\My Projects\\Android Subsystem for Windows (Python)\\Currency Convertor\\currency_icon.ico")

    image = PhotoImage(file="A:\\My Projects\\Android Subsystem for Windows (Python)\\Currency Convertor\\currency.png")
    image_label = Label(root, image=image, bg='#b7c5ce')
    image_label.pack()
    text_label = Label(root, text="Currency Convertor", bg='#b7c5ce', font=("Pristina", 20), fg="dark blue")
    text_label.pack()

    currency = ["Albania Lek, ALL", "Afghanistan Afghani, AFN", "Argentina Peso, ARS", "Aruba Guilder, AWG", "Australia Dollar, AUD", "Azerbaijan Manat, AZN", "Bahamas Dollar, BSD", "Barbados Dollar, BBD", "Belarus Ruble, BYN", "Belize Dollar, BZD", "Bermuda Dollar, BMD", "Bolivia Bolíviano, BOB", "Bosnia and Herzegovina Convertible Mark, BAM", "Botswana Pula, BWP", "Bulgaria Lev, BGN", "Brazil Real, BRL", "Brunei Darussalam Dollar, BND", "Cambodia Riel, KHR", "Canada Dollar, CAD", "Cayman Islands Dollar, KYD", "Chile Peso, CLP", "China Yuan Renminbi, CNY", "Colombia Peso, COP", "Costa Rica Colon, CRC", "Croatia Kuna, HRK", "Cuba Peso, CUP", "Czech Republic Koruna, CZK", "Denmark Krone, DKK", "Dominican Republic Peso, DOP", "East Caribbean Dollar, XCD", "Egypt Pound, EGP", "El Salvador Colon, SVC", "Euro Member Countries, EUR", "Falkland Islands (Malvinas) Pound, FKP", "Fiji Dollar, FJD", "Ghana Cedi, GHS", "Gibraltar Pound, GIP", "Guatemala Quetzal, GTQ", "Guernsey Pound, GGP", "Guyana Dollar, GYD", "Honduras Lempira, HNL", "Hong Kong Dollar, HKD", "Hungary Forint, HUF", "Iceland Krona, ISK", "India Rupee, INR", "Indonesia Rupiah, IDR", "Iran Rial, IRR", "Isle of Man Pound, IMP", "Israel Shekel, ILS", "Jamaica Dollar, JMD", "Japan Yen, JPY", "Jersey Pound, JEP", "Kazakhstan Tenge, KZT", "Korea (South) Won, KRW", "Kyrgyzstan Som, KGS", "Laos Kip, LAK", "Lebanon Pound, LBP", "Liberia Dollar, LRD", "Macedonia Denar, MKD", "Malaysia Ringgit, MYR", "Mauritius Rupee, MUR", "Mexico Peso, MXN", "Mozambique Metical, MZN", "Namibia Dollar, NAD", "Nepal Rupee, NPR", "Netherlands Antilles Guilder, ANG", "New Zealand Dollar, NZD", "Nicaragua Cordoba, NIO", "Nigeria Naira, NGN", "Norway Krone, NOK", "Oman Rial, OMR", "Pakistan Rupee, PKR", "Panama Balboa, PAB", "Paraguay Guarani, PYG", "Peru Sol, PEN", "Philippines Peso, PHP", "Poland Zloty, PLN", "Qatar Riyal, QAR", "Romania Leu, RON", "Russia Ruble, RUB", "Saint Helena Pound, SHP", "Saudi Arabia Riyal, SAR", "Serbia Dinar, RSD", "Seychelles Rupee, SCR", "Singapore Dollar, SGD", "Solomon Islands Dollar, SBD", "Somalia Shilling, SOS", "South Africa Rand, ZAR", "Sri Lanka Rupee, LKR", "Sweden Krona, SEK", "Switzerland Franc, CHF", "Suriname Dollar, SRD", "Taiwan New Dollar, TWD", "Thailand Baht, THB", "Trinidad and Tobago Dollar, TTD", "Turkey Lira, TRY", "Ukraine Hryvnia, UAH", "United Kingdom Pound, GBP", "United States Dollar, USD", "Uruguay Peso, UYU", "Uzbekistan Som, UZS", "Viet Nam Dong, VND", "Yemen Rial, YER", "Zambia Kwacha, ZMW"]

    result = Label(root, width=22, height=2, anchor=CENTER, font=("Cambria", 20), bg='#a9b6bf', relief=SOLID)
    result.pack(padx=10, pady=10)

    From = Label(root, text="From", width=8, height=1, relief=FLAT, anchor=NW, font=("Aparajita", 16), bg='#b7c5ce')
    From.place(x=10, y=210)
    combo_box1 = ttk.Combobox(root, width=24, justify=CENTER, font=("Aparajita", 16), state='r', values=currency)
    combo_box1.place(x=70, y=210)
    combo_box1.set("India Rupee, INR")

    To = Label(root, text="To", width=8, height=1, relief=FLAT, anchor=NW, font=("Aparajita", 16), bg='#b7c5ce')
    To.place(x=10, y=260)
    combo_box2 = ttk.Combobox(root, width=24, justify=CENTER, font=("Aparajita", 16), state='r', values=currency)
    combo_box2.place(x=70, y=260)
    combo_box2.set("United States Dollar, USD")

    button = Button(root, text="Convert", bg='#b7c5ce', font=("Pristina", 25), command=threading_convert, bd=0, relief=FLAT, activebackground="#b7c5ce")
    button.pack(side=BOTTOM)

    value = Entry(root, width=22, justify=CENTER, font=("Cambria", 16), relief=SOLID, bg="#b7c5ce")
    value.bind("<Return>", lambda e: threading_convert())
    value.pack(side=BOTTOM, pady=(0, 50))
    amount = Label(root, text="Amount", relief=FLAT, anchor=NW, font=("Aparajita", 16), bg='#b7c5ce')
    amount.pack(side=BOTTOM)

    root.mainloop()
