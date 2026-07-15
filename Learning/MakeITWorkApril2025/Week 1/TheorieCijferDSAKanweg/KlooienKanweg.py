# Eigen variant gemaakt met meerdere mogelijke deeltoetsen
# Regels dat (net als opdracht) alles voldoende moet zijn en bij onvoldoende het hoogste onvoldoende cijfer telt.

VAK_NAAM = "Datastructures"

eindcijfer = 0

def punten_deeltoetsen():
    aantal_deeltoetsen = int(input("Voer het aantal deeltoetsen in: "))

    puntenlijst = []

    #Hier voor iedere deeltoets het cijfer aangeven. Dit kan alleen zolang dit cijfer tussen 0 en 20 ligt anders opnieuw invoeren
    for deeltoetsnr in range(1, aantal_deeltoetsen+1):
        while True:
            punten_deeltoets = int(input(f"Voer aantal punten deeltoets {deeltoetsnr} opnieuw in: "))
            if punten_deeltoets >0 and punten_deeltoets <20:
                puntenlijst.append(punten_deeltoets)
                break
            else:
                print("ongeldig aantal punten, probeer opnieuw")
    print(puntenlijst)
    return puntenlijst

def bepaal_voldoende(puntenlijst):
    lijst_voldoendes = []
    lijst_onvoldoendes = []
    for deeltoetsnr in puntenlijst:
        if puntenlijst[deeltoetsnr] >12:
            print(f"Deeltoetsnummer {deeltoetsnr} gehaald")
            lijst_voldoendes.append(puntenlijst[deeltoetsnr])
        elif puntenlijst[deeltoetsnr] <12:
            print(f"Deeltoetsnummer {deeltoetsnr} gehaald")
            lijst_onvoldoendes.append(puntenlijst[deeltoetsnr])
        print(f"lijst met voldoendes {lijst_voldoendes}")
        print(f"lijst met onvoldoendes {lijst_onvoldoendes}")



puntenlijst = punten_deeltoetsen()
bepaal_voldoende(puntenlijst)
