# "RECEPT" / "STAPPENPLAN"
"""
Maak een applicatie...
Stap 1...
Stap 2...
Stap 3...

"""


# # IMPORTS
# importeer hier modules die je nodig hebt voor je applicatie (bijv. datetime of math)

# # CONSTANTEN = variabelen die niet gewijzigd worden

# # LIJSTEN: als workaround omdat je nog geen verbinding met een SQL Database hebt
klantenlijst = [
                ["Voornam", "Achternaam", "Woonplaats"],
                ["Julian", "Wolff", "Zutphen"],
                ["Joey", "van den Berg", "Den Haag"],
                ["Vera", "Cremers", "Ede"]
            ]

def toon_menu():
    print('\n' * 2)
    print('+---------------------------+')
    print('|                           |')
    print('|   1 print klant           |')
    print('|   2 wijzigen klant        |')
    print('|                           |')
    print('|                           |')
    print('|                           |')
    print('|      "stop" = stoppen     |')
    print('+---------------------------+')

while True:
    toon_menu()
    menukeuze = input("Maak je keuze: ")
    if menukeuze == "stop":
        print("Doei")
        break
    elif menukeuze == "1":
        print("Menukeuze 1")
    elif menukeuze == "2":
        print("Menukeuze 2")
    else:
        print("Ongeldige keuze, voer een geldig nummer of 'stop' in")






print("Programma beëindigd.")


