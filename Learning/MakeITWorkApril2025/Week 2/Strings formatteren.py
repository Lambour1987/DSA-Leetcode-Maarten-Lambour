#3 Manieren om het print statement aan te passen
from tempfile import template

print("Methode:\nVoornaam:\nAchternaam:\n")


#Druk naam en leeftijd af
naam = "Maarten"
leeftijd = 37

zin = f"Mijn naam is {naam} en mijn leeftijd is {leeftijd}"
print(zin)

#Afronden variabele pi
pi = 3.14159

afrpi = round(pi,2)
print(f"De waarde van pi is ongeveer {afrpi}")

intpi=int(pi)
print("de waarde van pi is ongeveer", intpi)

#Jan zegt wat (nog doen met dubbele aanhalingstekens)
print(f"Jan zegt: Hallo!")

#Oldskool + Format methode gebruikt om te printen
stad = "Amsterdam"
temperatuur = 20

zin = "Het is %d graden in %s" %(temperatuur, stad)
print(zin)

zin = "Het is {} graden in {}".format(temperatuur, stad)
print(zin)


#Druk de fruit en groente gecentreerd af
fruit = "Appel"
groente = "Broccoli"

print(f"{fruit:^40}\n{groente:^40}")

#Python is leuk (moet nog met functie denk ik)
print("Python is leuk")

#Afspraak
dag = "vrijdag"
tijd = "16.00"

print(f"Onze afspraak is {dag} om {tijd}")

#Tabel Arjen Lubach
Voornaam = "Arjen"
Achternaam = "Lubach"
Titel = "De Avondshow"

print("Voornaam  ","Achternaam  ","Titel  ")
print(f"{Voornaam:<5}{Achternaam:^18}{Titel:>13}")