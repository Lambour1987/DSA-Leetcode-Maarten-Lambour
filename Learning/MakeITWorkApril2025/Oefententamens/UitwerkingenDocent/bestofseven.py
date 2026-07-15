"""
Dit programma registreert de uitslagen van een Best of Seven
reeks van basketbalwedstrijden.
Het eerste team dat 4 wedstrijden heeft gewonnen, is de winnaar.
"""

def printwinnaar(naamteam1, naamteam2, aantalwinstteam1, aantalwinstteam2):
    """
    Deze functie print de uitslag van de best of seven reeks. In de uitslag wordt
    het aantal gewonnen wedstrijden van de winnaar het eerst genoemd.
    :param naamteam1: (str) de naam van team1
    :param naamteam2: (str) de naam van team2
    :param aantalwinstteam1: (int) het aantal gewonnen wedstrijden van team 1
    :param aantalwinstteam2: (int) het aantal gewonnen wedstrijden van team 1
    :return: geen returnwaarde
    """
    if aantalwinstteam1 > aantalwinstteam2:
        print(naamteam1,"heeft gewonnen met",aantalwinstteam1,"-",aantalwinstteam2)
    else:
        print(naamteam2,"heeft gewonnen met",aantalwinstteam2,"-",aantalwinstteam1)
    # Einde van de functie printwinnaar


# Hier begint het hoofdprogramma

print("Dit programma is gemaakt door Frank Oberndorff, 5007123456")

# Vraag de gebruiker om de namen van de teams
naamteam1 = input("Naam van team 1: ")
naamteam2 = input("Naam van team 2: ")

# Maak twee lege arrays om de scores van de teams in op te slaan.
puntenteam1array = []
puntenteam2array = []

# Zet variabele eriseenwinnaar op Falsezodat bij de start van de loop er nog
# geen winnaar is.
eriseenwinnaar = False

# Zet het aantal wedstrijden en de gewonnenwedstrijden op 0 bij de start van
# het programma
wedstrijdnr = 0


while eriseenwinnaar == False:
    gewonnen_team1 = 0
    gewonnen_team2 = 0
    print()
    wedstrijdnr = wedstrijdnr + 1
    print("Uitslag wedstrijd", wedstrijdnr)

    # Vraag de punten van iedere wedstrijd
    puntenteam1 = int(input("   Aantal punten "+naamteam1+": "))
    puntenteam2 = int(input("   Aantal punten "+naamteam2+": "))

    # Bepaal wie de wedstrijd gewonnen heeft en hoog het aantal gewonnen
    # wedstrijden op
    # if puntenteam1 > puntenteam2:
    #     gewonnen_team1 = gewonnen_team1 + 1
    # else:
    #     gewonnen_team2 = gewonnen_team2 + 1

    # Stop de punten in de array van het bijbehorende team
    puntenteam1array.append(puntenteam1)
    puntenteam2array.append(puntenteam2)

    # Als een van beide teams 4 gewonnen wedstrijden heeft bereikt, dan is er
    # een winnaar
    for i in range(len(puntenteam1array)):
        if (puntenteam1array[i] > puntenteam2array[i]):
            gewonnen_team1 = gewonnen_team1 +1
        else:
            gewonnen_team2 = gewonnen_team2 +1


    if gewonnen_team1 == 4 or gewonnen_team2 == 4:
        eriseenwinnaar = True

# Print de uitslag van de best of seven reeks en de uitslagen van de wedstrijden.
print()
# Print het aantal wedstrijden
print("Aantal gespeelde wedstrijden is: ", wedstrijdnr)
# Print de uitslag van de best of seven reeks
printwinnaar(naamteam1, naamteam2, gewonnen_team1, gewonnen_team2)
print()
# Print de uitslag van iedere wedstrijd mbv een loop door de arrays met punten
for i in range(len(puntenteam1array)):
    # print i+1 omdat de range loopt van 0 tot len(puntenteam1array)
    # en we willen bijv. niet 'wedstrijd 0' printen maar 'wedstrijd 1'
    print("wedstrijd",i+1,":",naamteam1,"-",naamteam2,
            puntenteam1array[i],"-",puntenteam2array[i])