import random
from datetime import datetime
import psycopg2


connection = psycopg2.connect(
    host = "localhost",
    database = "stationszuil",
    user = "postgres",
    password = "123")

cursor = connection.cursor()


def zuil():


    naam = input("Wat is uw naam: ").strip()
    if not naam:
        naam = "Anoniem"

    while True:

        bericht = input("Voer uw bericht in: ")
        if len(bericht) < 140 and len(bericht) != 0 and ";" not in bericht:
            break
        print("Ongeldig bericht")

    station = random.choice(["Amsterdam","Utrecht","Den Haag"])
    with open("zuil.txt","a") as file:
        file.write(f"{datetime.now().strftime('%d/%m/%Y-%H:%M:%S')};{station};{naam};{bericht}\n")


def moderatie():


    while True:

        naam = input("Wat is uw naam: ")
        email = input("Wat is uw email adres: ")

        cursor.execute("SELECT naam FROM moderator WHERE email = %s", [email])
        info = cursor.fetchone()

        if not info or naam == info[0]:
            break
        print("Naam/Email incorrect")

    cursor.execute("INSERT INTO moderator(naam, email) VALUES(%s,%s) ON CONFLICT DO NOTHING", [naam, email])
    cursor.execute("SELECT moderatorid FROM moderator WHERE email = %s", [email])
    moderatorId = cursor.fetchone()[0]

    with open("zuil.txt","r") as file:
        lines = file.readlines()

    lst = []
    for i in lines:

        info = i.strip("\n").split(";")
        print(f"{info[0]}\n{info[1]}\n{info[2]}\n{info[3]}")

        while True:

            goedkeuring = input("Bericht goedgekeurd (y/n): ")
            if goedkeuring == "stop":
                break
            if goedkeuring == "y" or goedkeuring == "n":
                lst.append(i)
                break
            print("Ongelidge input")

        if goedkeuring == "y":
            goedkeuring = True
        else:
            goedkeuring = False

    with open("zuil.txt", "w") as file:
        for a in lines:
            if a not in lst:
                file.write(a)

        cursor.execute("SELECT stationid FROM station WHERE locatie = %s", [info[1]])
        stationId = cursor.fetchone()[0]

        cursor.execute("INSERT into bericht(bericht, datum, tijd, goedgekeurd, moderatorid, stationid, reiziger) VALUES(%s, %s, %s, %s, %s, %s, %s)", [info[3], info[0].split("-")[0], info[0].split("-")[1], goedkeuring, moderatorId, stationId, info[2]])
    connection.commit()


moderatie()