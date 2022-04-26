import tkinter as tk
from tkinter import *
from tkinter import messagebox
import requests
import time
from PIL import Image, ImageTk

api_key = "421e28f9e40b05f6974d0fdc39099dec"

home = Tk()
home.geometry('900x800')
home.resizable(0, 0)
home.title('Orų programėlė')
# home.configure(bg="#f0f0f0")
dt = time.strftime("%H:%M")

def search():
    city = textfield.get()
    if city == '':
        return messagebox.showerror('Klaida', 'įveskite miestą')
    else:
        url = "http://api.openweathermap.org/data/2.5/weather?"
        cityname = city
        lang = 'lt'
        units = 'Metric'
        complete_url = url + "appid=" + api_key + '&units=' + units + '&lang=' + lang + "&q=" + cityname
        response = requests.get(complete_url)
        x = response.json()
        if x["cod"] :
            y = x["main"]
            z = x["weather"]
            cityname = x["sys"]["country"]
            citywind = x["wind"]["speed"]
            citytemp = y["temp"]
            cityhumidity = y["humidity"]
            cityweather_description = z[0]["description"]

            Label1=Label(home, font='Helvetica 42 bold',foreground="red",text='' + str(round(citytemp)) + '°C')
            Label1.place(x=420, y=380)
            Label2=Label(home, font='Helvetica 21 bold', text= textfield.get())
            Label2.place(x=420, y=320)
            Label3=Label(home, font='Helvetica 12 bold', bg="#1ab5ef",text='' + str(citywind) + ' m/s')
            Label3.place(x=350, y=500)
            Label4=Label(home, font='Helvetica 12 bold', bg="#1ab5ef",text='' + str(cityweather_description))
            Label4.place(x=440, y=500)
            Label5 = Label(home, font='Helvetica 12 bold',bg="#1ab5ef", text='' + str(cityhumidity))
            Label5.place(x=540, y=500)



img = Image.open('apple-iphone-13-pro-max-2021-medium.png')
img = img.resize((300, 500), Image.ANTIALIAS)
img_photo = ImageTk.PhotoImage(img)
bg_lbl = tk.Label(home, image=img_photo)
bg_lbl.place(x=320, y=100)


Search_image=PhotoImage(file="search.png")
myimage=Label(image=Search_image)
myimage.place(x=340,y=150)

textfield=tk.Entry(home, justify="center",font=("poppins", 15, "bold"),bg="#404040", border=0,fg="white",)
textfield.place(x=360, y=160,width=130, height=35)
textfield.focus()

Search_icon=PhotoImage(file="search_icon.png")
myimage_icon=Button(image=Search_icon, borderwidth=0, cursor="hand2", bg="#404040",command=search)
myimage_icon.place(x=530, y=160,width=45, height=35)

logo_image=PhotoImage(file="clipart248259.png")
myimage=Label(image=logo_image)
myimage.place(x=420,y=220)

blue_image=PhotoImage(file="box.png")
myimage=Label(image=blue_image)
myimage.place(x=340,y=460)

w=Label(text="Vejas",bg="#1ab5ef",fg="white", font=("arial", 12, "bold"))
w.place(x=350, y=475)
b=Label(text="Šiuo metu",bg="#1ab5ef", fg="white", font=("arial", 12, "bold"))
b.place(x=420, y=475)
r=Label(text="Drėgmė",bg="#1ab5ef",fg="white" , font=("arial", 12, "bold"))
r.place(x=520, y=475)

home.mainloop()