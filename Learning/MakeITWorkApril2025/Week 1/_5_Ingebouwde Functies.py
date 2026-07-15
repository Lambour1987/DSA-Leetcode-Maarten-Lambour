#Ingebouwde functies door Maarten Lambour
#Doel: Leeftijd berekening gebruiker en print getallen

#Voer naam in en stop resultaat in variabele
voornaam = input("Typ je naam: ")
print("Hallo", voornaam)

#Vraag leeftijd en converteer naar integer
leeftijd = int(input("Wat is je leeftijd: "))

#Bereken leeftijd over 10 jaar en print het resultaat
leeftijd_toekomst = leeftijd+10
print(f"Hallo {voornaam}, je leeftijd over 10 jaar is {leeftijd_toekomst}")

print("Voer 3 getallen in: ")

getal1 = int(input("Voer getal 1 in "))
getal2 = int(input("Voer getal 2 in "))
getal3 = int(input("Voer getal 3 in "))

print(getal1,"...",getal2,"...",getal3)