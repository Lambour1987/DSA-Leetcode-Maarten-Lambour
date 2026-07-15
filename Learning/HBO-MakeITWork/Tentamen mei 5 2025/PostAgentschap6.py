print("Dit is de uitwerking van Maarten Lambour, 500978379")

gewicht_in_gram_lijst = []
aantal_brieven_lijst = []
track_and_trace_lijst = []
kosten_per_bundel_lijst = []

aantal_bundels = int(input("Hoeveel bundels wil je laten versturen?: "))
while aantal_bundels > 1000 or aantal_bundels < 1:
    print("Je mag tussen 1 en 1000 bundels invoeren.")
    aantal_bundels = int(input("Voer een geldig aantal bundels in: "))

# Functie om kosten per bundel te berekenen
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

# Gegevens verzamelen per bundel
for bundel in range(aantal_bundels):
    print(f"\nBundel {bundel + 1}")
    gewicht = int(input("Gewicht in gram: "))

    aantal = int(input("Aantal brieven: "))
    while aantal < 1 or aantal > 1000:
        print("Het aantal brieven moet minimaal 1 en maximaal 1000 zijn.")
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

# Overzicht
print("\nOverzicht van alle bundels:")
for i in range(aantal_bundels):
    print(f"Bundel {i+1}: Gewicht = {gewicht_in_gram_lijst[i]}g, "
          f"Aantal = {aantal_brieven_lijst[i]}, "
          f"Track&Trace = {track_and_trace_lijst[i]}, "
          f"Kosten = €{kosten_per_bundel_lijst[i]:.2f}")
