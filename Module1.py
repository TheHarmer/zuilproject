import random
from datetime import datetime
import csv


def zuil():

    # Naam vragen, anoniem als het leeg is
    naam = input("Wat is uw naam (laat leeg voor anoniem): ").strip()
    if not naam:
        naam = "Anoniem"

    # Loop voor het invullen van het bericht. Checkt of het ingevoerde bericht geldig is
    while True:

        bericht = input("Voer uw bericht in: ")
        if len(bericht) < 140 and len(bericht) != 0:
            break
        print("Ongeldige lengte")

    # Kiest een van de 3 stations
    station = random.choice(["Amsterdam","Utrecht","Den Haag"])

    # Schrijft de informatie in het tekst bestand
    with open("zuil.csv", "a", newline='') as file:
        writer = csv.writer(file)
        writer.writerow([datetime.now().strftime('%d/%m/%Y'),datetime.now().strftime('%H:%M:%S'),station,naam,bericht])


zuil()