student = input("Geef uw naam: ")
klas = int(input("geef uw klas: "))
studentnummer = int(input("geef uw studentnummer: "))
print(f"Dit programma is gemaakt door {student}, {klas}, {studentnummer}")


team_naam1 = input("Wat is de naam van team 1: ")
team_naam2 = input("Wat is de naam van team 2: ")

punten_team1 = []
punten_team2 = []

tussenstand_team1 = 0
tussenstand_team2 = 0

aantal_wedstrijden = 7
aantal_gespeeld = 0

for wedstrijd in range(aantal_wedstrijden-1):
    wedstrijd = wedstrijd + 1
    aantal_gespeeld = aantal_gespeeld + 1
    print(f"Uitslag wedstrijd {wedstrijd}")
    score_wedstrijd_team1= int(input(f"   Aantal punten {team_naam1}: "))
    punten_team1.append(score_wedstrijd_team1)
    score_wedstrijd_team2 = int(input(f"   Aantal punten {team_naam2}: "))
    punten_team2.append(score_wedstrijd_team2)
    #print("Kanweg: punten team 1", punten_team1)
    #print("Kanweg: punten team 2", punten_team2)
    #print(f"Kanweg: aantal wedstrijden gespeeld {aantal_gespeeld}")
    if score_wedstrijd_team1>score_wedstrijd_team2:
        tussenstand_team1 = tussenstand_team1 + 1
    elif score_wedstrijd_team2>score_wedstrijd_team1:
        tussenstand_team2 = tussenstand_team2 + 1
    else:
        print("Gelijkspel")

print()
#print(punten_team1)
#print(punten_team2)

#Hoeveel gespeeld
print(f"Aantal gespeelde wedstrijden: {aantal_gespeeld}")

#Wie heeft er uiteindelijk gewonnen
if tussenstand_team1 > tussenstand_team2:
    print(f"{team_naam1} heeft gewonnen met {tussenstand_team1} - {tussenstand_team2}")
elif tussenstand_team1 < tussenstand_team2:
    print(f"{team_naam2} heeft gewonnen met {tussenstand_team2} - {tussenstand_team1}")
else:
    print(f"Gelijkspel: aan beide partijen worden geen punten toegekend")

print()

for wedstrijd in range(aantal_wedstrijden-1):
    print(f"wedstrijd {wedstrijd+1}: {team_naam1} - {team_naam2} {punten_team1[wedstrijd]} - {punten_team2[wedstrijd]}")


