eerste_getal = int(input("Dit programma berekent het gemiddelde van twee of meer getallen. Geef het eerste getal: "))
tweede_getal = int(input("Geeft het tweede getal: "))
aantal = 2
print("KANWEG: het aantal is", aantal)
som = eerste_getal+tweede_getal
print("KANWEG: de som is ", som)
antwoord = input("Wil je van meer getallen het gemiddelde bepalen (ja/nee)? ")

while antwoord == "ja":
    volgende_getal=int(input("Geef het volgende getal: "))
    som = som + volgende_getal
    print("KANWEG: Som is", som)
    aantal = aantal + 1
    print("KANWEG: Aantal is", aantal)

    antwoord = input("Wil je meer getallen het gemiddelde bepalen (ja/nee)? ")

if antwoord == "nee":
    gemiddelde = som / aantal
    print(f"Het gemiddelde van jouw {aantal} getallen is {gemiddelde}")

else:
    print("Je moet 'ja' of 'nee' antwoorden.")



