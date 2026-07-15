print('1. Klant toevoegen')
print('2. Klant wijzigen')

keuze = input("Maak uw keuze: ")
keuze = int(keuze)

uitkomsten = [11,12,13,14,15,16,17,18,19,20,21]

print('Zoeken mbv een for')
for uitkomst in uitkomsten:
    print(uitkomst)
    if keuze == uitkomst:
        print('Goede keuze')

print('Zoeken mbv een while')
niet_gevonden = True
positie = 0
while niet_gevonden:
    print(uitkomsten[positie])
    uitkomst = uitkomsten[positie]
    if keuze == uitkomst:
        print('Goede keuze')
        niet_gevonden = False
    else:
        positie = positie + 1
        if positie == len(uitkomsten):
            niet_gevonden = False







