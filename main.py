import tkinter as tk
from tkinter import *
from tkinter import messagebox
import requests
import time
from PIL import Image, ImageTk


home = Tk()
home.geometry('300x550')
home.resizable(0, 0)
home.title('Orų programėlė')
home.iconbitmap('sunrise.ico')
dt = time.strftime("%H:%M")


meniu = Menu(home)
home.config(menu=meniu)
submeniu = Menu(meniu, tearoff = 0)
meniu.add_cascade(label="Meniu", menu=submeniu)
submeniu.add_command(
    label='Exit',
    command=home.destroy)


def search():
    global icon
    city = textfield.get()
    if city == '':
        return messagebox.showerror('Klaida', 'įveskite miestą')
    else:
        url = "http://api.openweathermap.org/data/2.5/weather?"
        api_key = "421e28f9e40b05f6974d0fdc39099dec"
        cityname = city
        lang = 'lt'
        units = 'Metric'
        complete_url = url + "appid=" + api_key + '&units=' + units + '&lang=' + lang + "&q=" + cityname
        response = requests.get(complete_url)
        x = response.json()
        if x["cod"] :
            y = x["main"]
            z = x["weather"]
            icon = x['weather'][0]["icon"]
            citywind = x["wind"]["speed"]
            citytemp = y["temp"]
            cityhumidity = y["humidity"]
            cityweather_description = z[0]["description"]

            icon = ImageTk.PhotoImage(Image.open(f"weather_icons\\{icon}.png"))
            panel = Label(home, image=icon)
            panel.place(x=90, y=100)

            Label(home, font='Times 42 bold',foreground="red",text='' + str(round(citytemp)) + '°C').place(x=110, y=230)
            Label(home, font='Times 21 bold', text='' + textfield.get()).place(x=110, y=300)
            Label(home, font='Times 12 bold', bg="#1ab5ef",text='' + str(citywind) + ' m/s').place(x=30, y=410)
            Label(home, font='Times 12 bold', bg="#1ab5ef",text='' + str(cityweather_description)).place(x=100, y=410)
            Label(home, font='Times 12 bold',bg="#1ab5ef", text='' + str(cityhumidity) + '%').place(x=220, y=410)


img = Image.open('apple-iphone-13-pro-max-2021-medium.png')
img = img.resize((300, 500), Image.Resampling.LANCZOS)
img_photo = ImageTk.PhotoImage(img)
bg_lbl = tk.Label(home, image=img_photo)
bg_lbl.place(x=0, y=0)

Search_image=PhotoImage(file="search.png")
myimage=Label(image=Search_image)
myimage.place(x=20,y=40)

textfield=tk.Entry(home, justify="center",font=("Times", 15, "bold"),bg="#404040", border=0,fg="white",)
textfield.place(x=90, y=50,width=130, height=35)
textfield.focus()

Search_icon=PhotoImage(file="search_icon.png")
myimage_icon=Button(image=Search_icon, borderwidth=0, cursor="hand2", bg="#404040",command=search)
myimage_icon.place(x=210, y=50,width=45, height=35)

logo_image=PhotoImage(file="unknown.png")
myimage=Label(image=logo_image)
myimage.place(x=90,y=120)

blue_image=PhotoImage(file="box.png")
myimage=Label(image=blue_image)
myimage.place(x=20,y=370)

wind=Label(text="Vėjas",bg="#1ab5ef",fg="white", font=("arial", 12, "bold"))
wind.place(x=30, y=385)
description=Label(text="Šiuo metu",bg="#1ab5ef", fg="white", font=("arial", 12, "bold"))
description.place(x=100, y=385)
humidity=Label(text="Drėgmė",bg="#1ab5ef",fg="white" , font=("arial", 12, "bold"))
humidity.place(x=200, y=385)
time=Label(home, font='Times 12 bold', text='' + str(dt)).place(x=215, y=15)


home.mainloop()