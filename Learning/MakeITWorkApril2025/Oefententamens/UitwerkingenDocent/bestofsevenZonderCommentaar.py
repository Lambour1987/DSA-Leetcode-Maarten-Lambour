def printwinnaar(naamteam1, naamteam2, aantalwinstteam1, aantalwinstteam2):
    if aantalwinstteam1 > aantalwinstteam2:
        print(naamteam1, "heeft gewonnen met", aantalwinstteam1, "-", aantalwinstteam2)
    else:
        print(naamteam2, "heeft gewonnen met", aantalwinstteam2, "-", aantalwinstteam1)

print("Dit programma is gemaakt door Frank Oberndorff, 5007123456")

naamteam1 = input("Naam van team 1: ")
naamteam2 = input("Naam van team 2: ")

puntenteam1array = []
puntenteam2array = []

eriseenwinnaar = False
wedstrijdnr = 0

while not eriseenwinnaar:
    gewonnen_team1 = 0
    gewonnen_team2 = 0
    print()
    wedstrijdnr += 1
    print("Uitslag wedstrijd", wedstrijdnr)

    puntenteam1 = int(input("   Aantal punten " + naamteam1 + ": "))
    puntenteam2 = int(input("   Aantal punten " + naamteam2 + ": "))

    puntenteam1array.append(puntenteam1)
    puntenteam2array.append(puntenteam2)

    for i in range(len(puntenteam1array)):
        if puntenteam1array[i] > puntenteam2array[i]:
            gewonnen_team1 += 1
        else:
            gewonnen_team2 += 1

    if gewonnen_team1 == 4 or gewonnen_team2 == 4:
        eriseenwinnaar = True

print()
print("Aantal gespeelde wedstrijden is:", wedstrijdnr)
printwinnaar(naamteam1, naamteam2, gewonnen_team1, gewonnen_team2)
print()
for i in range(len(puntenteam1array)):
    print("wedstrijd", i + 1, ":", naamteam1, "-", naamteam2,
          puntenteam1array[i], "-", puntenteam2array[i])
