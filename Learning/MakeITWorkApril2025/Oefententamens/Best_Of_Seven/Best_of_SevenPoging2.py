

print(f"Maarten Lambour Spring School 7123479")

naam_team_A = str(input("Voer de naam van het eerste team in: "))
naam_team_B = str(input("Voer de naam van het tweede team in: "))

punten_team_A = []
punten_team_B = []

winnend_team = False
aantal_wedstrijden = 0

gewonnen_team1 = 0
gewonnen_team2 = 0

while winnend_team == False:

    aantal_wedstrijden = aantal_wedstrijden + 1
    print()
    print("Uitslag wedstrijd")

    punten_team_A.append(int(input(f"Voer punten {naam_team_A} in: ")))
    punten_team_B.append(int(input(f"Voer punten {naam_team_B} in: ")))

    if punten_team_A[-1] > punten_team_B[-1]:
        gewonnen_team1 = gewonnen_team1 + 1
    else:
        gewonnen_team2 = gewonnen_team2 + 1

    if gewonnen_team1 == 4 or gewonnen_team2 == 4:
        winnend_team = True
