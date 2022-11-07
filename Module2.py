from datetime import datetime
import psycopg2
import csv


# Connection with the database
connection = psycopg2.connect(
    host = "localhost",
    database = "stationszuil",
    user = "postgres",
    password = "123")

cursor = connection.cursor()


def moderatie():

    # Loop om de moderator te krijgen
    while True:

        naam = input("Wat is uw naam: ")
        email = input("Wat is uw email adres: ")

        cursor.execute("SELECT naam FROM moderator WHERE email = %s", [email])
        info = cursor.fetchone()

        # Checkt of de naam en de email bij elkaar kloppen
        if not info or naam == info[0]:
            break
        print("Naam/Email incorrect")

    # Inserts moderator in de database als de email nog niet bestaat
    cursor.execute("INSERT INTO moderator(naam, email) VALUES(%s,%s) ON CONFLICT DO NOTHING", [naam, email])
    cursor.execute("SELECT moderatorid FROM moderator WHERE email = %s", [email])
    moderatorId = cursor.fetchone()[0]

    with open("zuil.csv", "r") as file:
        reader = csv.reader(file)
        lines = []
        for row in reader:
            lines.append(row)

    # Lijst voor alle gekeurde berichten
    lst = []
    for i in lines:

        # Stript alle info in verschillende variabelen
        print(f"{i[0]}-{i[1]}\n{i[2]}\n{i[3]}\n{i[4]}")

        while True:

            # Keuring van het bericht
            goedkeuring = input("Type \"stop\" om the stoppen\nBericht goedgekeurd (y/n): ")

            # Checkt of de input geldig is
            if goedkeuring == "stop":
                break
            elif goedkeuring == "y" or goedkeuring == "n":
                lst.append(i)
                break
            print("Ongelidge input")


        if goedkeuring != "stop":
            if goedkeuring == "y":
                goedkeuring = True
            else:
                goedkeuring = False

            cursor.execute("SELECT stationid FROM station WHERE locatie = %s", [i[2]])
            stationId = cursor.fetchone()[0]

            # Het bericht met alle informatie in de database zetten
            cursor.execute("INSERT into bericht(bericht, schrijfdatum, schrijftijd, BeoordelingDatum, BeoordelingTijd, goedgekeurd, moderatorid, stationid, reiziger) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s)",
                           [i[4], i[0], i[1], datetime.now().strftime('%d/%m/%Y'), datetime.now().strftime('%H:%M:%S') ,goedkeuring, moderatorId, stationId, i[3]])


    # Het verwijderen van de berichten die gekeurd zijn
    with open("zuil.csv", "w", newline='') as file:
        writer = csv.writer(file)
        for a in lines:
            if a not in lst:
                writer.writerow(a)


    connection.commit()