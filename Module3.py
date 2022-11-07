from tkinter import *
import requests
import psycopg2
from PIL import Image, ImageTk


conn = psycopg2.connect(
    host="localhost",
    database="stationszuil",
    user="postgres",
    password="123")

cursor = conn.cursor()

def test(option):

    url = f"https://api.openweathermap.org/data/2.5/weather?q={option}&units=metric&appid=f8c6ec40fa12b97fb7772e85d0c2516c"
    r = requests.get(url=url)
    weer = r.json()


    cursor.execute("SELECT bericht.bericht, bericht.datum, bericht.tijd, station.locatie, station.ovfiets, station.lift, station.toilet, station.pr FROM bericht INNER JOIN station ON bericht.stationid = station.stationid AND goedgekeurd = true ORDER by datum DESC, tijd DESC")
    info = cursor.fetchall()
    print(info)

    if len(info) > 0:

        station0['text'] = info[0][3]
        bericht0['text'] = info[0][0]

        if info[0][4]:
            faciliteiten0_0.configure(image=img0, width=35)
        if info[0][5]:
            faciliteiten0_1.configure(image=img1, width=35)
        if info[0][6]:
            faciliteiten0_2.configure(image=img2, width=35)
        if info[0][7]:
            faciliteiten0_3.configure(image=img3, width=35)

    if len(info) > 1:

        station1['text'] = info[1][3]
        bericht1['text'] = info[1][0]

        if info[1][4]:
            faciliteiten1_0.configure(image=img0, width=35)
        if info[1][5]:
            faciliteiten1_1.configure(image=img1, width=35)
        if info[1][6]:
            faciliteiten1_2.configure(image=img2, width=35)
        if info[1][7]:
            faciliteiten1_3.configure(image=img3, width=35)

    if len(info) > 2:

        station2['text'] = info[2][3]
        bericht2['text'] = info[2][0]

        if info[2][4]:
            faciliteiten2_0.configure(image=img0, width=35)
        if info[2][5]:
            faciliteiten2_1.configure(image=img1, width=35)
        if info[2][6]:
            faciliteiten2_2.configure(image=img2, width=35)
        if info[2][7]:
            faciliteiten2_3.configure(image=img3, width=35)

    if len(info) > 3:

        station3['text'] = info[3][3]
        bericht3['text'] = info[3][0]

        if info[3][4]:
            faciliteiten3_0.configure(image=img0, width=35)
        if info[3][5]:
            faciliteiten3_1.configure(image=img1, width=35)
        if info[3][6]:
            faciliteiten3_2.configure(image=img2, width=35)
        if info[3][7]:
            faciliteiten3_3.configure(image=img3, width=35)

    if len(info) > 4:

        station4['text'] = info[4][3]
        bericht4['text'] = info[4][0]

        if info[4][4]:
            faciliteiten4_0.configure(image=img0, width=35)
        if info[4][5]:
            faciliteiten4_1.configure(image=img1, width=35)
        if info[4][6]:
            faciliteiten4_2.configure(image=img2, width=35)
        if info[4][7]:
            faciliteiten4_3.configure(image=img3, width=35)


    temp['text'] = f"{round(weer['main']['temp'],1)}°C"
    humid['text'] = f"humidity: {weer['main']['humidity']}%"
    wind['text'] = f"wind speed: {weer['wind']['speed']}km"


window = Tk()
window.title("Stationshalscherm")
window.geometry("1100x600")
window.resizable(False, False)
window.configure(bg="midnight blue")

options = ["Amsterdam","Utrecht","Den Haag"]
drop = OptionMenu(window, StringVar(), *options, command=test)
drop.place(x=550,y=2,width=100)

img0 = ImageTk.PhotoImage(Image.open("icons/0.png").resize((35, 35)))
img1 = ImageTk.PhotoImage(Image.open("icons/1.png").resize((35, 35)))
img2 = ImageTk.PhotoImage(Image.open("icons/2.png").resize((35, 35)))
img3 = ImageTk.PhotoImage(Image.open("icons/3.png").resize((35, 35)))

weerframe = Frame(window)

temp = Label(weerframe, font=("Arial", 15), fg="white", anchor="n", bg="midnight blue")
humid = Label(weerframe, font=("Arial", 15), fg="white", anchor="n", bg="midnight blue")
wind = Label(weerframe, font=("Arial", 15), fg="white", anchor="n",  bg="midnight blue")
temp.grid(row=0, column=1, sticky="NESW")
humid.grid(row=1, column=1, sticky="NESW")
wind.grid(row=2, column=1, sticky="NESW")
weerframe.pack(pady=(40,15), padx=15, anchor='w')

frame = Frame(window)

station0 = Label(frame, borderwidth=1, relief="solid", bg="lightgray", width=12, height=5)
station1 = Label(frame, borderwidth=1, relief="solid", height=5)
station2 = Label(frame, borderwidth=1, relief="solid", bg="lightgray", height=5)
station3 = Label(frame, borderwidth=1, relief="solid", height=5)
station4 = Label(frame, borderwidth=1, relief="solid", bg="lightgray", height=5)
station0.grid(row=0, column=0, sticky="NESW")
station1.grid(row=1, column=0, sticky="NESW")
station2.grid(row=2, column=0, sticky="NESW")
station3.grid(row=3, column=0, sticky="NESW")
station4.grid(row=4, column=0, sticky="NESW")

bericht0 = Label(frame, borderwidth=1, relief="solid", bg="lightgray", width=130)
bericht1 = Label(frame, borderwidth=1, relief="solid")
bericht2 = Label(frame, borderwidth=1, relief="solid", bg="lightgray")
bericht3 = Label(frame, borderwidth=1, relief="solid")
bericht4 = Label(frame, borderwidth=1, relief="solid", bg="lightgray")
bericht0.grid(row=0, column=1, sticky="NESW")
bericht1.grid(row=1, column=1, sticky="NESW")
bericht2.grid(row=2, column=1, sticky="NESW")
bericht3.grid(row=3, column=1, sticky="NESW")
bericht4.grid(row=4, column=1, sticky="NESW")

faciliteiten0 = Frame(frame, borderwidth=1, relief="solid", bg="lightgray")
faciliteiten0_0 = Label(faciliteiten0, bg="lightgray", width=4)
faciliteiten0_1 = Label(faciliteiten0, bg="lightgray", width=4)
faciliteiten0_2 = Label(faciliteiten0, bg="lightgray", width=4)
faciliteiten0_3 = Label(faciliteiten0, bg="lightgray", width=4)
faciliteiten0_0.grid(row=0, column=0, sticky="NESW")
faciliteiten0_1.grid(row=0, column=1, sticky="NESW")
faciliteiten0_2.grid(row=1, column=0, sticky="NESW")
faciliteiten0_3.grid(row=1, column=1, sticky="NESW")

faciliteiten1 = Frame(frame, borderwidth=1, relief="solid")
faciliteiten1_0 = Label(faciliteiten1, width=5)
faciliteiten1_1 = Label(faciliteiten1, width=5)
faciliteiten1_2 = Label(faciliteiten1, width=5)
faciliteiten1_3 = Label(faciliteiten1, width=5)
faciliteiten1_0.grid(row=0, column=0, sticky="NESW")
faciliteiten1_1.grid(row=0, column=1, sticky="NESW")
faciliteiten1_2.grid(row=1, column=0, sticky="NESW")
faciliteiten1_3.grid(row=1, column=1, sticky="NESW")

faciliteiten2 = Frame(frame, borderwidth=1, relief="solid", bg="lightgray")
faciliteiten2_0 = Label(faciliteiten2, width=4, bg="lightgray")
faciliteiten2_1 = Label(faciliteiten2, width=4, bg="lightgray")
faciliteiten2_2 = Label(faciliteiten2, width=4, bg="lightgray")
faciliteiten2_3 = Label(faciliteiten2, width=4, bg="lightgray")
faciliteiten2_0.grid(row=0, column=0, sticky="NESW")
faciliteiten2_1.grid(row=0, column=1, sticky="NESW")
faciliteiten2_2.grid(row=1, column=0, sticky="NESW")
faciliteiten2_3.grid(row=1, column=1, sticky="NESW")

faciliteiten3 = Frame(frame, borderwidth=1, relief="solid")
faciliteiten3_0 = Label(faciliteiten3, width=5)
faciliteiten3_1 = Label(faciliteiten3, width=5)
faciliteiten3_2 = Label(faciliteiten3, width=5)
faciliteiten3_3 = Label(faciliteiten3, width=5)
faciliteiten3_0.grid(row=0, column=0, sticky="NESW")
faciliteiten3_1.grid(row=0, column=1, sticky="NESW")
faciliteiten3_2.grid(row=1, column=0, sticky="NESW")
faciliteiten3_3.grid(row=1, column=1, sticky="NESW")

faciliteiten4 = Frame(frame, borderwidth=1, relief="solid", bg="lightgray")
faciliteiten4_0 = Label(faciliteiten4, width=5, bg="lightgray")
faciliteiten4_1 = Label(faciliteiten4, width=5, bg="lightgray")
faciliteiten4_2 = Label(faciliteiten4, width=5, bg="lightgray")
faciliteiten4_3 = Label(faciliteiten4, width=5, bg="lightgray")
faciliteiten4_0.grid(row=0, column=0, sticky="NESW")
faciliteiten4_1.grid(row=0, column=1, sticky="NESW")
faciliteiten4_2.grid(row=1, column=0, sticky="NESW")
faciliteiten4_3.grid(row=1, column=1, sticky="NESW")

faciliteiten0.grid(row=0, column=2, sticky="NESW")
faciliteiten1.grid(row=1, column=2, sticky="NESW")
faciliteiten2.grid(row=2, column=2, sticky="NESW")
faciliteiten3.grid(row=3, column=2, sticky="NESW")
faciliteiten4.grid(row=4, column=2, sticky="NESW")

frame.pack()

window.mainloop()