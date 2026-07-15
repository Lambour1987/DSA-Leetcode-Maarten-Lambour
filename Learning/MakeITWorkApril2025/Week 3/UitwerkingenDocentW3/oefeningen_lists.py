# Functie voor het maken van een rij willekeurige getallen
import random


def maak_random_rij_getallen(aantal, maximum):
    rij = []
    for teller in range(aantal):
        getal = random.randint(1, maximum)  # Bij randint is het eindgetal wel inclusief, bij randrange niet.
        rij.append(getal)
    return rij


def som_lijst(getallenrij):
    som = 0
    for i in range(len(getallenrij)):
        som = som + getallenrij[i]
    return som


def bepaal_minimum(rij):
    minimum = rij[0]
    for i in range(1, len(rij)):
        if rij[i] < minimum:
            minimum = rij[i]
    return minimum


def gemiddelde_van_rij(rij):
    return sum(rij) / len(rij)


def tel_voorkomens_in_rij(check_getal, rij):
    aantal = 0
    for getal in rij:
        if getal == check_getal:
            aantal += 1
    return aantal


def tel_voorkomens_getallen_in_rij(maximum, rij):
    resultaat_rij = []
    for getal in range(1, maximum + 1):
        # de loop gaat van 1 tot en met maximum.
        resultaat_rij.append((getal, tel_voorkomens_in_rij(getal, rij)))
    return resultaat_rij


# Hier start het hoofdprogramma

# Range en lists
lijst1 = list(range(9))
print(lijst1)
lijst2 = list(range(1, 10))
print(lijst2)
lijst3 = list(range(2, 11, 2))
print(f'De lijst {lijst3} bevat {len(lijst3)} getallen.')
print()
# Rij van random getallen maken
aantal = int(input("Hoeveel getallen wil je genereren? "))
maximum = int(input("Wat is het grootste getal dat mag voorkomen? "))
rij = maak_random_rij_getallen(aantal, maximum)
for getal in rij:
    print(getal, end=' ')
print()

# Gemiddelde van een rij bepalen
print(f"De som is: {som_lijst(rij)}")
print(f"Het gemiddelde is: {gemiddelde_van_rij(rij)}")
print()

# Hoe vaak komt een getal voor.
rij = maak_random_rij_getallen(1000, 50)
getal = 23
print(f"Het getal {getal} komt {tel_voorkomens_in_rij(23, rij)} keer in de rij voor.")
print()

print(f"Het kleinste getal in de rij is {bepaal_minimum(rij)}")

# Tel voorkomens van getallen 1 tot 50
eind_rij = 50
rij_voorkomens = tel_voorkomens_getallen_in_rij(eind_rij, rij)
for getal, aantal in rij_voorkomens:
    print(f"Getal {getal} komt {aantal} keer voor.")

