"""
Dit programma vraagt de gebruiker om de cijfers van semester 1 in toe voeren, waarna hij een overzicht geeft van de
studievoortgang. Tevens kan het programma voorspellen of de student een positief of negatief BSA zal krijgen.
"""

# Definieer een array vaknamen waarin de namen van vakken en projecten komen.
lijst_vaknamen = ["Fasten Your Seatbelts","Programming","Business","Personal skills","Project skills",
                  "Management & Organisatie","Databases"]
aantal_vakken = len(lijst_vaknamen)

# Definieer een array voor de punten van de vakken en projecten.
lijst_te_behalen_punten = [12,3,3,2,2,3,3]

# Definieer een array voor vakcijfers
lijst_vakcijfers = []

# Vraag de gebruikers om zijn cijfers in te voeren (alleen geldige getallen tussen 1.0 en 10.0)
# Sla mb.v. een for loop de ingevoerde cijfers op in de array vakcijfers
print("Voer behaalde cijfers in:")
for i in range(aantal_vakken):
    # cijfer = float(input('%s: ' % lijst_vaknamen[i]))
    cijfer = float(input(f"{lijst_vaknamen[i]} : "))
    # Zolang het ingevoerde cijfer niet tussen 1 en 10 ligt, vraag opnieuw een cijfer in te voeren
    while cijfer < 1 or cijfer > 10:
        print("Voer een cijfer in tussen 1 en 10:")
        cijfer = float(input('%s: ' % lijst_vaknamen[i]))
    lijst_vakcijfers.append(cijfer)

# Bepaal welke vakken zijn behaald en ken de juiste punten toe
lijst_vak_punten_behaald = []
for i in range(aantal_vakken):
    if lijst_vakcijfers[i] >= 5.5:
        lijst_vak_punten_behaald.append(lijst_te_behalen_punten[i])
    else:
        lijst_vak_punten_behaald.append(0)

# Tel alle behaalde studiepunten bij elkaar op en sla deze ook op onder de variabelen totaalpunten
totaal_behaalde_punten = 0
for i in range(aantal_vakken):
    totaal_behaalde_punten = totaal_behaalde_punten + lijst_vak_punten_behaald[i]

totaal_te_behalen_punten = 0
for i in range(aantal_vakken):
    totaal_te_behalen_punten = totaal_te_behalen_punten + lijst_te_behalen_punten[i]
# Je kunt voor het optellen van een lijst ook de Python functie sum() gebruiken :
# totaal_te_behalen_punten = sum(lijst_te_behalen_punten)

# Print de resultaten per vak op het scherm
print()
for i in range(aantal_vakken):
    print("Vak/project: %-30s Cijfer: %2.1f Behaalde punten: %d" % (lijst_vaknamen[i], lijst_vakcijfers[i], lijst_vak_punten_behaald[i]))

# Print het aantal behaalde studiepunten
print("\nTotaal behaalde studiepunten: %d/%d" % (totaal_behaalde_punten, totaal_te_behalen_punten))

# Print als de gebruiker minder dan 5/6 van de punten heeft behaald een melding
if totaal_behaalde_punten < 5 / 6 * totaal_te_behalen_punten:
    print("PAS OP: je ligt op schema voor een negatief BSA!")