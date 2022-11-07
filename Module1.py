import random
from datetime import datetime


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