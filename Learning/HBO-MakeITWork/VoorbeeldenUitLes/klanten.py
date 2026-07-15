def klant_toevoegen():
    klantnummer = input("Wat is het klantnummer? ")
    klantnaam = input("Wat is de naam van de klant? ")

def klant_wijzigen():
    klantnummer = input("Welke klant wil je wijzigen? ")

def klant_verwijderen():
    klantnummer = input("Welke klant wil je verwijderen? ")

def toon_menu():
    print("1. Klant toevoegen")
    print("2. Klant wijzigen")
    print("3. Klant verwijderen")
    print("0. Stop programma")

    # Controleer de keuze van de gebruiker
    # en vraag net zo lang om een keuze totdat deze correct is
    gemaakte_keuze = int(input("Maak uw keuze: "))

    return gemaakte_keuze
