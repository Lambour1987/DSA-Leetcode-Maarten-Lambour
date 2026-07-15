# # SIMPEL VOORBEELD F-STRING MET VARIABELE IN EEN STRING
#
print("# OUTPUT: SIMPEL VOORBEELD F-STRING MET VARIABELE IN EEN STRING:")
naam = "Hannah"             # variabele naam
leeftijd = 12               # variabele leeftijd
message = f"Ik ben {naam} en ik ben {leeftijd} jaar oud." # variabele message met f-string
print(message)
print()
print()
#
#
# IETS DIRECT BINNEN EEN F-STRING BEREKENEN
print("OUTPUT: IETS DIRECT IN EEN F-STRING BEREKENEN:")
x = 10
y = 5
print(f"{x} keer {y} is {x * y}")
print()
print()

# UITLIJNEN IN KOLOMMEN
print("OUTPUT: UITLIJNEN IN KOLOMMEN:")
print()
voornaam = "voornaam"
achternaam = "achternaam"
stad = "stad"
print(f"{voornaam:<10} {achternaam:<20}{stad:<20}")
print(f"{voornaam:<10} {achternaam:<20}{stad:<20}")
print(f"{voornaam:<10} {achternaam:<20}{stad:<20}")
print(f"{voornaam:<10} {achternaam:<20}{stad:<20}")
print(f"{voornaam:<10} {achternaam:<20}{stad:<20}")
print(f"{voornaam:<10} {achternaam:<20}{stad:<20}") # in de volgende oefening zie je hoe je
                                                    # de hardcoded "20" met een variabele op basis van
                                                    # het langste woord per kolom in de studentenlijst kunt vervangen.

print()
print()


# # VOORBEELD VAN TABELSTRUCTUUR (f-string en lists)
# # Je hebt hier een  lijst van lijsten met in elke rij de gegevens van een student

print("# VOORBEELD VAN TABELSTRUCTUUR (f-string en lists):")

studenten = [                                   # een lijst met sublijsten
    ["Alice", 30, "Amsterdam"],
    ["Bob", 25, "Rotterdam"],
    ["Charlie", 35, "Utrecht"],
    ["Linda", 59, "Bussum"]
]
print() # een lege regel

# Nu bepaal je met "max" en "len" de maximale lengte van de woordjes die in de sublijsten staan.
# Daar komt een getal uit dat vervolgens nog met "+2" wordt verhoogd (een soort 'padding').
# student[0] adresseert de 1e positie in de sublijst, de naam van de student dus.
# student[2] adresseert de 3e positie in de sublijst, de stad waar de student woont dus.
naam_width = max(len(student[0]) for student in studenten) + 2
leeftijd_width = (len("leeftijd")) + 2          # hier wordt de lengte van het woord "leeftijd" als maatstaf genomen
stad_width = max(len(student[2]) for student in studenten) + 2

# De headers (kopregel) in hardcode (dus gewoon ingetikt)
# de '<' betekent dat de tekst naar links wordt uitgelijnd.

print(f"{'NAAM':<{naam_width}}{'LEEFTIJD':<{leeftijd_width}}{'PLAATS':<{stad_width}}")

# Nu loop je de lijst "studenten" met een for-loop af en print je de rijen.
# Eerst pack je de sublist "student" uit in 3 variabelen: naam, leeftijd, stad
# Daarmee ken je het eerste element uit de sublist toe aan "naam", het tweede aan "leeftijd"
# en het deerde aan "stad"

for student in studenten:
    naam, leeftijd, stad = student                  # dit is een manier om meerdere variabelen in een klap te vullen
    print(f"{naam:<{naam_width}}{leeftijd:<{leeftijd_width}}{stad:<{stad_width}}")
