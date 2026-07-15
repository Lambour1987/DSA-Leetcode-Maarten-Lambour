
naam_teamA = input("Naam van team 1: ")
naam_teamB = input("Naam van team 2: ")

score_team_A = []
score_team_B = []

punten_team_A=0
punten_team_B=0

aantal_gespeelde_wedstrijden = 0

team_heeft_gewonnen = False

wedstrijden = 0

while not team_heeft_gewonnen:
    wedstrijden = wedstrijden + 1
    print(f"Uitslag wedstrijd {wedstrijden}")
    score_team_A = int(input(f"Aantal punten (KANWEG: SCORE) {naam_teamA}: "))
    score_team_B = int(input(f"Aantal punten (KANWEG: SCORE) {naam_teamB}: "))

    aantal_gespeelde_wedstrijden = aantal_gespeelde_wedstrijden +1

    if score_team_A>score_team_B:
        punten_team_A = punten_team_A + 1
        print(f"Punten team A: {punten_team_A}")
    elif score_team_B>score_team_A:
        punten_team_B = punten_team_B + 1
        print(f"Punten team B: {punten_team_B}")

    if punten_team_A == 4:
        print("KANWEG: TeamA heeft gewonnen")
    elif punten_team_B == 4:
        print("KANWEG: TEAMB heeft gewonnen")

    print(f"Aantal gespeelde wedstrijden {aantal_gespeelde_wedstrijden}")
    print(f"Totaal aantal gespeelde wedstrijden {aantal_gespeelde_wedstrijden}")

