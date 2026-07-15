track_and_trace = False
kosten_per_pakket = 0
bundels = 0
kosten_per_bundel = 0

gewicht_in_gram_lijst = []
aantal_bundels_lijst = []
track_and_trace_lijst = []

aantal_bundels = int(input("Hoeveel bundels wil je laten versturen?: "))
while aantal_bundels > 1000:
    print("Je mag niet meer dan 1000 bundels invoeren.")
    aantal_bundels = int(input("Voer een geldig aantal bundels in (max 1000): "))

print(f"KANWEG: aantal bundels is {aantal_bundels}")

for bundel in range(aantal_bundels):
    bundels += 1
    print(f"\nBundel {bundels}")

    geef_gewicht_in_gram = int(input("Gewicht in gram: "))
    gewicht_in_gram_lijst.append(geef_gewicht_in_gram)
    print(f'KANWEG lijst gewichten in gram {gewicht_in_gram_lijst}')
    geef_aantal_bundels = int(input("Aantal: "))
    aantal_bundels_lijst.append(geef_aantal_bundels)
    print(f'KANWEG lijst aantallen {geef_aantal_bundels}')
    tracktrace = input("Wilt u track en trace j/n: ").lower()

    if tracktrace != 'j' and tracktrace != 'n':
        print("Ongeldige invoer. Vul j of n in.")
        tracktrace = input("Wilt u track en trace j/n: ").lower()

    if tracktrace == 'j':
        track_and_trace = True
        kosten = 8.15
        track_and_trace_lijst.append("Ja")
    elif tracktrace == 'n':
        track_and_trace_lijst.append("Nee")
        if geef_gewicht_in_gram > 0 and geef_gewicht_in_gram <= 20:
            track_and_trace_kosten = 0.93
        elif geef_gewicht_in_gram > 20 and geef_gewicht_in_gram <= 100:
            track_and_trace_kosten = 2.00
        elif geef_gewicht_in_gram > 100:
            track_and_trace_kosten = 3.00
    else:
        print("Tweede poging ongeldig. Er worden geen kosten berekend.")

    print(f"Kosten voor deze bundel: €{kosten:.2f}")

def bereken_bundelkosten(gewicht, aantal, is_trackntrace):
    for bundel in bundels:



print("Overzicht van alle bundels: ")
print(f"gewicht in gramlijstOverzicht {gewicht_in_gram_lijst}")
print(f"aantal in gramlijstOverzicht {aantal_bundels_lijst}")
print(f"T&T {track_and_trace_lijst}")