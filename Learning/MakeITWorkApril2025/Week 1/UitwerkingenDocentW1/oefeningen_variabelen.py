# 1. Schrijf een programma dat de gebruiker om drie getallen vraagt en print het grootste getal. Invoer en printen met duidelijke begeleidende tekst.
getal1 = float(input("Voer het eerste getal in: "))
getal2 = float(input("Voer het tweede getal in: "))
getal3 = float(input("Voer het derde getal in: "))

grootste_getal = max(getal1, getal2, getal3)
print(f"Het grootste getal is: {grootste_getal}")


# 2. Schrijf een programma dat de gebruiker om een getal vraagt en print het getal, het kwadraat en de wortel van het getal. Invoer en printen met duidelijke begeleidende tekst.
import math

getal = float(input("Voer een getal in: "))
print(f"Het getal is: {getal}")
print(f"Het kwadraat van het getal is: {getal**2}")
print(f"De wortel van het getal is: {math.sqrt(getal)}")

