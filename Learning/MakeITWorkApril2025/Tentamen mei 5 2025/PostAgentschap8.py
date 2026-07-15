print("Dit is de uitwerking van Maarten Lambour, 500978379")
# Aantekening Maarten: Werkt voor gegeven input maar niet alles geprobeert
# Korting nog niet verwerkt


#List met gegevens over de bundel
gewicht_in_gram_lijst = []
aantal_brieven_lijst = []
track_and_trace_lijst = []
kosten_per_bundel_lijst = []

#Vraag de gebruiker het aantal bundels in te voeren
#Gebruik een while loop om steeds opnieuw te vragen als het aantal ingevoerde bundels onjuist is.
aantal_bundels = int(input("Hoeveel bundels wil je laten versturen?: "))
while aantal_bundels > 1000 or aantal_bundels < 1:
    print("Je mag tussen 1 en 1000 bundels invoeren.")
    aantal_bundels = int(input("Voer een geldig aantal bundels in: "))

# Functie om kosten per bundel te berekenen: als parameters gebruikt zoals in de opgave aangegeven
def bereken_bundelkosten(gewicht, aantal, is_trackntrace):
    if is_trackntrace:
        return 8.15 * aantal
    else:
        if gewicht <= 20:
            return 0.93 * aantal
        elif gewicht <= 100:
            return 2.00 * aantal
        else:
            return 3.00 * aantal


# Functie om totale kosten te berekenen
def bereken_totale_bundelkosten(kostenlijst):
    return sum(kostenlijst)


# Gegevens verzamelen per bundel
for bundel in range(aantal_bundels):
    print(f"\nBundel {bundel + 1}")

    gewicht = int(input("Gewicht in gram: "))
    while gewicht <= 0:
        print("Het gewicht moet meer dan 0 gram zijn.")
        gewicht = int(input("Voer een geldig gewicht in gram in: "))

    aantal = int(input("Aantal brieven: "))
    while aantal < 1 or aantal > 1000:
        if aantal < 1:
            print("Het aantal brieven moet minimaal 1 zijn.")
        else:
            print("Het aantal brieven mag maximaal 1000 zijn.")
        aantal = int(input("Aantal brieven: "))

    tracktrace = input("Wilt u track en trace j/n: ").lower()

    # Als invoer ongeldig is, 1x extra kans geven
    if tracktrace not in ['j', 'n']:
        print("Vul j of n in!")
        tracktrace = input("Wilt u track en trace j/n: ").lower()
        if tracktrace not in ['j', 'n']:
            print("Tweede invoer ook ongeldig. Track & Trace wordt op 'nee' gezet.")
            tracktrace = 'n'

    is_trackntrace = (tracktrace == 'j')
    kosten = bereken_bundelkosten(gewicht, aantal, is_trackntrace)

    # Voeg toe aan lijsten
    gewicht_in_gram_lijst.append(gewicht)
    aantal_brieven_lijst.append(aantal)
    track_and_trace_lijst.append("Ja" if is_trackntrace else "Nee")
    kosten_per_bundel_lijst.append(kosten)

# Overzicht van alle bundels: gebruik gemaakt van afsnijden om tabelvorm te krijgen
print("Overzicht van alle bundels")
print("\n{:<15} {:<10} {:<5} {:<10}".format("gewicht in gram", "aantal", "T&T", "kosten"))
for i in range(aantal_bundels):
    print("{:<15} {:<10} {:<5} €{:<.2f}".format(
        gewicht_in_gram_lijst[i],
        aantal_brieven_lijst[i],
        track_and_trace_lijst[i],
        kosten_per_bundel_lijst[i]
    ))

# Totale kosten
totaal_kosten = bereken_totale_bundelkosten(kosten_per_bundel_lijst)
print(f"\nTotale kosten voor alle bundels: €{totaal_kosten:.2f}")
