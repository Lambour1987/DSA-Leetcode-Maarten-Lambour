track_and_trace = False

bundels = 0

gewicht_in_gram_lijst = []
aantal_brieven_lijst = []
track_and_trace_lijst = []
kosten_per_bundel = 0

aantal_bundels = int(input("Hoeveel bundels wil je laten versturen?: "))
while aantal_bundels > 1000:
    print("Je mag niet meer dan 1000 bundels invoeren.")
    aantal_bundels = int(input("Voer een geldig aantal bundels in (max 1000): "))

for bundel in range(aantal_bundels):
    bundels += 1
    print(f"\nBundel {bundels}")

    geef_gewicht_in_gram = int(input("Gewicht in gram: "))
    gewicht_in_gram_lijst.append(geef_gewicht_in_gram)
    geef_aantal_brieven = int(input("Aantal: "))
    aantal_brieven_lijst.append(geef_aantal_brieven)
    tracktrace = input("Wilt u track en trace j/n: ").lower()

    if tracktrace != 'j' and tracktrace != 'n':
        print("Ongeldige invoer. Vul j of n in.")
        tracktrace = input("Wilt u track en trace j/n: ").lower()

def bereken_bundelkosten(gewicht, aantal, is_trackntrace):
    for bundel in bundels:
        if tracktrace == 'j':
            track_and_trace = True
            kosten_per_bundel = 8.15
            track_and_trace_lijst.append("Ja")
        elif tracktrace == 'n':
            track_and_trace_lijst.append("Nee")
            if geef_gewicht_in_gram > 0 and geef_gewicht_in_gram <= 20:
                kosten_per_bundel = 0.93

            elif geef_gewicht_in_gram > 20 and geef_gewicht_in_gram <= 100:
                kosten_per_bundel = 2.00
            elif geef_gewicht_in_gram > 100:
                kosten_per_bundel = 3.00
        else:
            print("Tweede poging ongeldig. Er worden geen kosten berekend.")

        print(f"Kosten voor deze bundel: €{kosten:.2f}")


print("Overzicht van alle bundels: ")
print(f"gewicht in gramlijstOverzicht {gewicht_in_gram_lijst}")
print(f"aantal in gramlijstOverzicht {aantal_brieven_lijst}")
print(f"T&T {track_and_trace_lijst}")