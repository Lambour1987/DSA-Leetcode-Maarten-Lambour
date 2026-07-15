#Student & studentnummer


gewicht_in_gram = []
aantal_bundels = []
track_and_trace_list =[]
track_and_trace = False
track_and_trace_kosten = 0
bundels = 0
kosten_per_bundel = 0


# eventueel nog lowercase
aantal_bundels = int(input("Hoeveel bundels wil je laten versturen?: "))
print(f"KANWEG: aantal bundels is {aantal_bundels}")

for bundel in range(0, aantal_bundels):
    bundels = bundels + 1
    print(f"Bundel {bundels}")
    geef_gewicht_in_gram = int(input("Gewicht in gram: "))
    gewicht_in_gram.append(geef_gewicht_in_gram)
    print(f"gewicht in gramlijst {gewicht_in_gram}")
    geef_aantal = int(input("Aantal: "))
    aantal_bundels.append(geef_aantal)
    print(f"aantal in lijst {aantal_bundels}")
    tracktrace = input("Wilt u track en trace j/n")

    if tracktrace == 'ja':
        track_and_trace = True
        track_and_trace_kosten = 0
        if gewicht_in_gram > 0 and gewicht_in_gram <= 20:
            track_and_trace_kosten = 0.93
        elif gewicht_in_gram > 20 and gewicht_in_gram <=100:
            track_and_trace_kosten = 2.00
        elif gewicht_in_gram > 100:
            track_and_trace_kosten = 3.00





