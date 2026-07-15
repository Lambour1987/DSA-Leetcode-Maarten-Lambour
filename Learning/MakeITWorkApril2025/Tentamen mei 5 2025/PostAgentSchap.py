#Student & studentnummer


gewicht_in_gram = []
aantal = []
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
    gewicht_in_gram = int(input("Gewicht in gram: "))
    aantal = int(input("Aantal: "))
    tracktrace = input("Wilt u track en trace j/n")
    if track_and_trace == "j":
        track_and_trace = True
        track_and_trace_kosten = 0
    elif track_and_trace == "n":
        if gewicht_in_gram > 0 and gewicht_in_gram <= 20:
            track_and_trace_kosten = 0.93
        elif gewicht_in_gram > 20 and gewicht_in_gram <=100:
            track_and_trace_kosten = 2.00
        elif gewicht_in_gram > 100:
            track_and_trace_kosten = 3.00
    else: #wanneer geen ja of nee bij track en trace wordt ingevoerd:
        print("Vul j of n in")



