import klanten

#
# HOOFDPROGRAMMA
#
keuze = klanten.toon_menu()

if keuze == 0:
    print("Dit is het einde")

if keuze == 1:
    klanten.klant_toevoegen()

if keuze == 2:
    klanten.klant_wijzigen()

if keuze == 3:
    klanten.klant_verwijderen()
