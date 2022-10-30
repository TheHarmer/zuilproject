import tkinter as tk
import requests
import psycopg2
from PIL import Image, ImageTk

conn = psycopg2.connect(
    host="localhost",
    database="stationszuil",
    user="postgres",
    password="123")

cursor = conn.cursor()

class GUI():

    def __init__(self):


        self.window = tk.Tk()
        self.window.title("Stationshalscherm")
        self.window.geometry("1200x600")
        self.window.resizable(False, False)
        self.options = ["Amsterdam","Utrecht","Den Haag"]
        self.drop = tk.OptionMenu(self.window, tk.StringVar(), *self.options, command=self.test)
        self.drop.place(x=550,y=2,width=100)
        self.frame = tk.Frame(self.window)
        # self.frame.columnconfigure(0, weight=15)
        # self.frame.columnconfigure(1, weight=20)
        # self.frame.columnconfigure(2, weight=50)
        # self.frame.columnconfigure(3, weight=20)
        self.tijd0 = tk.Label(self.frame, borderwidth=1, relief="solid", bg="lightgray", height=6, width=12)
        self.tijd1 = tk.Label(self.frame, borderwidth=1, relief="solid", height=6)
        self.tijd2 = tk.Label(self.frame, borderwidth=1, relief="solid", bg="lightgray", height=6)
        self.tijd3 = tk.Label(self.frame, borderwidth=1, relief="solid", height=6)
        self.tijd4 = tk.Label(self.frame, borderwidth=1, relief="solid", bg="lightgray", height=6)
        self.tijd0.grid(row=0, column=0, sticky="NESW")
        self.tijd1.grid(row=1, column=0, sticky="NESW")
        self.tijd2.grid(row=2, column=0, sticky="NESW")
        self.tijd3.grid(row=3, column=0, sticky="NESW")
        self.tijd4.grid(row=4, column=0, sticky="NESW")
        self.station0 = tk.Label(self.frame, borderwidth=1, relief="solid", bg="lightgray", width=12)
        self.station1 = tk.Label(self.frame, borderwidth=1, relief="solid")
        self.station2 = tk.Label(self.frame, borderwidth=1, relief="solid", bg="lightgray")
        self.station3 = tk.Label(self.frame, borderwidth=1, relief="solid")
        self.station4 = tk.Label(self.frame, borderwidth=1, relief="solid", bg="lightgray")
        self.station0.grid(row=0, column=1, sticky="NESW")
        self.station1.grid(row=1, column=1, sticky="NESW")
        self.station2.grid(row=2, column=1, sticky="NESW")
        self.station3.grid(row=3, column=1, sticky="NESW")
        self.station4.grid(row=4, column=1, sticky="NESW")
        self.bericht0 = tk.Label(self.frame, borderwidth=1, relief="solid", bg="lightgray", width=130)
        self.bericht1 = tk.Label(self.frame, borderwidth=1, relief="solid")
        self.bericht2 = tk.Label(self.frame, borderwidth=1, relief="solid", bg="lightgray")
        self.bericht3 = tk.Label(self.frame, borderwidth=1, relief="solid")
        self.bericht4 = tk.Label(self.frame, borderwidth=1, relief="solid", bg="lightgray")
        self.bericht0.grid(row=0, column=2, sticky="NESW")
        self.bericht1.grid(row=1, column=2, sticky="NESW")
        self.bericht2.grid(row=2, column=2, sticky="NESW")
        self.bericht3.grid(row=3, column=2, sticky="NESW")
        self.bericht4.grid(row=4, column=2, sticky="NESW")


        self.faciliteiten0 = tk.Frame(self.frame, borderwidth=1, relief="solid", bg="lightgray")
        self.faciliteiten0_0 = tk.Label(self.faciliteiten0, bg="lightgray", width=4)
        self.faciliteiten0_1 = tk.Label(self.faciliteiten0, bg="lightgray", width=4)
        self.faciliteiten0_2 = tk.Label(self.faciliteiten0, bg="lightgray", width=4)
        self.faciliteiten0_3 = tk.Label(self.faciliteiten0, bg="lightgray", width=4)
        self.faciliteiten0_0.grid(row=0, column=0, sticky="NESW")
        self.faciliteiten0_1.grid(row=0, column=1, sticky="NESW")
        self.faciliteiten0_2.grid(row=1, column=0, sticky="NESW")
        self.faciliteiten0_3.grid(row=1, column=1, sticky="NESW")

        self.faciliteiten1 = tk.Frame(self.frame, borderwidth=1, relief="solid")
        self.faciliteiten1_0 = tk.Label(self.faciliteiten1, width=5)
        self.faciliteiten1_1 = tk.Label(self.faciliteiten1, width=5)
        self.faciliteiten1_2 = tk.Label(self.faciliteiten1, width=5)
        self.faciliteiten1_3 = tk.Label(self.faciliteiten1, width=5)
        self.faciliteiten1_0.grid(row=0, column=0, sticky="NESW")
        self.faciliteiten1_1.grid(row=0, column=1, sticky="NESW")
        self.faciliteiten1_2.grid(row=1, column=0, sticky="NESW")
        self.faciliteiten1_3.grid(row=1, column=1, sticky="NESW")

        self.faciliteiten2 = tk.Frame(self.frame, borderwidth=1, relief="solid", bg="lightgray")
        self.faciliteiten2_0 = tk.Label(self.faciliteiten2, width=4, bg="lightgray")
        self.faciliteiten2_1 = tk.Label(self.faciliteiten2, width=4, bg="lightgray")
        self.faciliteiten2_2 = tk.Label(self.faciliteiten2, width=4, bg="lightgray")
        self.faciliteiten2_3 = tk.Label(self.faciliteiten2, width=4, bg="lightgray")
        self.faciliteiten2_0.grid(row=0, column=0, sticky="NESW")
        self.faciliteiten2_1.grid(row=0, column=1, sticky="NESW")
        self.faciliteiten2_2.grid(row=1, column=0, sticky="NESW")
        self.faciliteiten2_3.grid(row=1, column=1, sticky="NESW")

        self.faciliteiten3 = tk.Frame(self.frame, borderwidth=1, relief="solid")
        self.faciliteiten3_0 = tk.Label(self.faciliteiten3, width=5)
        self.faciliteiten3_1 = tk.Label(self.faciliteiten3, width=5)
        self.faciliteiten3_2 = tk.Label(self.faciliteiten3, width=5)
        self.faciliteiten3_3 = tk.Label(self.faciliteiten3, width=5)
        self.faciliteiten3_0.grid(row=0, column=0, sticky="NESW")
        self.faciliteiten3_1.grid(row=0, column=1, sticky="NESW")
        self.faciliteiten3_2.grid(row=1, column=0, sticky="NESW")
        self.faciliteiten3_3.grid(row=1, column=1, sticky="NESW")

        self.faciliteiten4 = tk.Frame(self.frame, borderwidth=1, relief="solid", bg="lightgray")
        self.faciliteiten4_0 = tk.Label(self.faciliteiten4, width=5, bg="lightgray")
        self.faciliteiten4_1 = tk.Label(self.faciliteiten4, width=5, bg="lightgray")
        self.faciliteiten4_2 = tk.Label(self.faciliteiten4, width=5, bg="lightgray")
        self.faciliteiten4_3 = tk.Label(self.faciliteiten4, width=5, bg="lightgray")
        self.faciliteiten4_0.grid(row=0, column=0, sticky="NESW")
        self.faciliteiten4_1.grid(row=0, column=1, sticky="NESW")
        self.faciliteiten4_2.grid(row=1, column=0, sticky="NESW")
        self.faciliteiten4_3.grid(row=1, column=1, sticky="NESW")

        self.faciliteiten0.grid(row=0, column=3, sticky="NESW")
        self.faciliteiten1.grid(row=1, column=3, sticky="NESW")
        self.faciliteiten2.grid(row=2, column=3, sticky="NESW")
        self.faciliteiten3.grid(row=3, column=3, sticky="NESW")
        self.faciliteiten4.grid(row=4, column=3, sticky="NESW")
        self.frame.pack(pady=50)
        self.window.mainloop()

    def test(self, option):

        url = f"https://api.openweathermap.org/data/2.5/weather?q={option}&units=metric&appid=f8c6ec40fa12b97fb7772e85d0c2516c"
        r = requests.get(url=url)
        cursor.execute("SELECT * FROM BERICHT INNER JOIN station ON bericht.stationid = station.stationid AND goedgekeurd = true ORDER by datum DESC, tijd DESC")
        info = cursor.fetchall()
        print(info)
        print(len(info))
        self.img0 = ImageTk.PhotoImage(Image.open("icons/0.png").resize((35, 35)))
        self.img1 = ImageTk.PhotoImage(Image.open("icons/1.png").resize((35, 35)))
        self.img2 = ImageTk.PhotoImage(Image.open("icons/2.png").resize((35, 35)))
        self.img3 = ImageTk.PhotoImage(Image.open("icons/3.png").resize((35, 35)))
        if len(info) > 0:
            self.tijd0['text'] = f"{info[0][1]}\n{info[0][2]}"
            self.station0['text'] = info[0][8]
            self.bericht0['text'] = info[0][0]
            if info[0][9]:
                self.faciliteiten0_0.configure(image=self.img0, width=35)
            if info[0][10]:
                self.faciliteiten0_1.configure(image=self.img1, width=35)
            if info[0][11]:
                self.faciliteiten0_2.configure(image=self.img2, width=35)
            if info[0][12]:
                self.faciliteiten0_3.configure(image=self.img3, width=35)
        else:
            self.tijd0['text'] = ""
            self.station0['text'] = ""
            self.bericht0['text'] = ""
            self.faciliteiten0_0.configure(image="")
            self.faciliteiten0_1.configure(image="")
            self.faciliteiten0_2.configure(image="")
            self.faciliteiten0_3.configure(image="")
        if len(info) > 1:
            self.tijd1['text'] = f"{info[1][1]}\n{info[1][2]}"
            self.station1['text'] = info[1][8]
            self.bericht1['text'] = info[1][0]
            if info[1][9]:
                self.faciliteiten1_0.configure(image=self.img0, width=35)
            if info[1][10]:
                self.faciliteiten1_1.configure(image=self.img1, width=35)
            if info[1][11]:
                self.faciliteiten1_2.configure(image=self.img2, width=35)
            if info[1][12]:
                self.faciliteiten1_3.configure(image=self.img3, width=35)
        else:
            self.tijd1['text'] = ""
            self.station1['text'] = ""
            self.bericht1['text'] = ""
            self.faciliteiten1_0.configure(image="")
            self.faciliteiten1_1.configure(image="")
            self.faciliteiten1_2.configure(image="")
            self.faciliteiten1_3.configure(image="")
        if len(info) > 2:
            self.tijd2['text'] = f"{info[2][1]}\n{info[2][2]}"
            self.station2['text'] = info[2][8]
            self.bericht2['text'] = info[2][0]
            if info[2][9]:
                self.faciliteiten2_0.configure(image=self.img0, width=35)
            if info[2][10]:
                self.faciliteiten2_1.configure(image=self.img1, width=35)
            if info[2][11]:
                self.faciliteiten2_2.configure(image=self.img2, width=35)
            if info[2][12]:
                self.faciliteiten2_3.configure(image=self.img3, width=35)
        else:
            self.tijd2['text'] = ""
            self.station2['text'] = ""
            self.bericht2['text'] = ""
            self.faciliteiten2_0.configure(image="")
            self.faciliteiten2_1.configure(image="")
            self.faciliteiten2_2.configure(image="")
            self.faciliteiten2_3.configure(image="")
        if len(info) > 3:
            self.tijd3['text'] = f"{info[3][1]}\n{info[3][2]}"
            self.station3['text'] = info[3][8]
            self.bericht3['text'] = info[3][0]
            if info[3][9]:
                self.faciliteiten3_0.configure(image=self.img0, width=35)
            if info[3][10]:
                self.faciliteiten3_1.configure(image=self.img1, width=35)
            if info[3][11]:
                self.faciliteiten3_2.configure(image=self.img2, width=35)
            if info[3][12]:
                self.faciliteiten3_3.configure(image=self.img3, width=35)
        else:
            self.tijd3['text'] = ""
            self.station3['text'] = ""
            self.bericht3['text'] = ""
            self.faciliteiten3_0.configure(image="")
            self.faciliteiten3_1.configure(image="")
            self.faciliteiten3_2.configure(image="")
            self.faciliteiten3_3.configure(image="")
        if len(info) > 4:
            self.tijd4['text'] = f"{info[4][1]}\n{info[4][2]}"
            self.station4['text'] = info[4][8]
            self.bericht4['text'] = info[4][0]
            if info[4][9]:
                self.faciliteiten4_0.configure(image=self.img0, width=35)
            if info[4][10]:
                self.faciliteiten4_1.configure(image=self.img1, width=35)
            if info[4][11]:
                self.faciliteiten4_2.configure(image=self.img2, width=35)
            if info[4][12]:
                self.faciliteiten4_3.configure(image=self.img3, width=35)
        else:
            self.tijd4['text'] = ""
            self.station4['text'] = ""
            self.bericht4['text'] = ""
            self.faciliteiten4_0.configure(image="")
            self.faciliteiten4_1.configure(image="")
            self.faciliteiten4_2.configure(image="")
            self.faciliteiten4_3.configure(image="")


        # print(r.json())

GUI()