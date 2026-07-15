print("Dit is de uitwerking van Maarten Lambour, 500978379")
# Aantekening Maarten: Werkt voor gegeven input maar niet alles geprobeerd
# Korting nu wel verwerkt

# List met gegevens over de bundel c.f. opdracht
gewicht_in_gram_lijst = []
aantal_brieven_lijst = []
track_and_trace_lijst = []
kosten_per_bundel_lijst = []

# Vraag de gebruiker het aantal bundels in te voeren
# Gebruik een while loop om steeds opnieuw te vragen als het aantal ingevoerde bundels onjuist is.
aantal_bundels = int(input("Hoeveel bundels wil je laten versturen?: "))
while aantal_bundels > 1000 or aantal_bundels < 1:
    print("Je mag tussen 1 en 1000 bundels invoeren.")
    aantal_bundels = int(input("Voer een geldig aantal bundels in: "))

# Functie om de korting per pakket te berekenen
def bereken_bundelkosten(gewicht, aantal, is_trackntrace):
    if is_trackntrace:
        prijs_per_stuk = 8.15
    else:
        if gewicht <= 20:
            prijs_per_stuk = 0.93
        elif gewicht <= 100:
            prijs_per_stuk = 2.00
        else:
            prijs_per_stuk = 3.00

    totaal = prijs_per_stuk * aantal

    # 20% korting bij 100 of meer brieven. Dan 80% betalen. (1-20%)
    if aantal >= 100:
        totaal = totaal * 0.8

    return totaal

# Functie om totale kosten te berekenen (argument is kosten_per_bundel zie beneden)
def bereken_totale_bundelkosten(kostenlijst):
    return sum(kostenlijst)

# Verzamel gegevens per bundel
for bundel in range(aantal_bundels):
    print(f"\nBundel {bundel + 1}")
    print("    Gewicht in gram:", end=" ")

    gewicht = int(input())
    while gewicht <= 0:
        print("    Het gewicht moet meer dan 0 gram zijn.")
        print("    Gewicht in gram:", end=" ")
        gewicht = int(input())

    print("    Aantal brieven:", end=" ")
    aantal = int(input())
    while aantal < 1 or aantal > 1000:
        if aantal < 1:
            print("    Het aantal brieven moet minimaal 1 zijn.")
        else:
            print("    Het aantal brieven mag maximaal 1000 zijn.")
        print("    Aantal brieven:", end=" ")
        aantal = int(input())

    # track en trace aanzetten met ja of nee.
    # Als er met hoofdletters wordt ingevuld 'J' of 'N' dan opnieuw vragen. Dus lowercase toegepast.
    print("    Wilt u track en trace j/n:", end=" ")
    tracktrace = input().lower()
    while tracktrace not in ['j', 'n']:
        print("    Vul j of n in!")
        print("    Wilt u track en trace j/n:", end=" ")
        tracktrace = input().lower()

    is_trackntrace = (tracktrace == 'j')
    kosten = bereken_bundelkosten(gewicht, aantal, is_trackntrace)

    gewicht_in_gram_lijst.append(gewicht)
    aantal_brieven_lijst.append(aantal)
    # Gebruik traditionele if-else voor track en trace
    if is_trackntrace:
        track_and_trace_lijst.append("Ja")
    else:
        track_and_trace_lijst.append("Nee")
    kosten_per_bundel_lijst.append(kosten)

# Overzicht van alle bundels: gebruik gemaakt van {<:15} afsnijden om tabelvorm
# te krijgen net als bij Arjen Lubach opdracht
print("Overzicht van alle bundels")
print("\n{:<15} {:<10} {:<5} {:<10}".format("Gewicht in gram", "Aantal", "T&T", "Kosten"))
for i in range(aantal_bundels):
    print("{:<15} {:<10} {:<5} €{:<.2f}".format(
        gewicht_in_gram_lijst[i],
        aantal_brieven_lijst[i],
        track_and_trace_lijst[i],
        kosten_per_bundel_lijst[i]
    ))

# De kosten per bundel worden hier als argument doorgegeven aan de functie bereken_totale_bundelkosten.
# De parameter aldaar heet kostenlijst
# Het resultaat wordt vervolgens opgeslagen in de variabele totaal_kosten om straks de korting te berekenen
totaal_kosten = bereken_totale_bundelkosten(kosten_per_bundel_lijst)


# Hier het totaal van de kosten bepaalt
# 5% korting bij totaal > 800 euro

korting_toegepast = False
if totaal_kosten > 800:
    totaal_kosten *= 0.95
    korting_toegepast = True

# Print totale kosten afgerond op decimalen
print(f"\nTotale kosten voor alle bundels: €{totaal_kosten:.2f}")
