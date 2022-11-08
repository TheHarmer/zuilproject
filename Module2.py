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

    # Vragen of het een nieuwe of bestaande moderator is
    acc = input("Nieuw of bestaande moderator? ")
    print(acc == "bestaand")
    if acc.lower() != "bestaand" and acc.lower() != "nieuw":
        print("Ongeldige input")
        return

    # Info van de moderator vragen
    naam = input("Wat is uw naam: ")
    email = input("Wat is uw email adres: ")

    # Als de moderator al bestaat
    if acc.lower() == "bestaand":

        cursor.execute("SELECT moderatorid FROM moderator WHERE email = %s", [email])
        info = cursor.fetchone()

        # Checken of de moderator ook echt bestaat
        if not info:
            print("Email bestaat niet")
            return

        moderatorId = info[0]

    # Als de moderator nog niet bestaat
    if acc.lower() == "nieuw":

        cursor.execute("SELECT naam FROM moderator WHERE email = %s", [email])
        info = cursor.fetchone()

        # Checken of de moderator al bestaat
        if info:
            print("Email bestaat al")
            return

        cursor.execute("INSERT INTO moderator(naam, email) VALUES(%s,%s)", [naam, email])
        cursor.execute("SELECT moderatorid FROM moderator WHERE email = %s", [email])
        moderatorId = cursor.fetchone()[0]

    # Zet alle berichten uit de CSV in een list
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


moderatie()