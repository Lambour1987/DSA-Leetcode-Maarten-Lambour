"""
Dit programma berekent de beoordeling van het vak Datastructures
author: Frank Oberndorff en Gerke de Boer`
"""

# Constante voor de naam van het vak
VAKNAAM = "Datastructures"
CESUUR = 12
# print inleidende tekst op scherm
print("Voer behaalde punten in voor het vak " + VAKNAAM + ":")

# vraag de gebruiker om de behaalde punten voor de deeltoetsen
punten_deeltoets1 = int(input(VAKNAAM + " Deeltoets 1: "))
punten_deeltoets2 = int(input(VAKNAAM + " Deeltoets 2: "))

# bepaal het cijfer en de beoordeling voor beide deeltoetsen
if punten_deeltoets1 >= CESUUR:
    beoordeling_deeltoets1 = 'Voldoende'
    cijfer_deeltoets1 = punten_deeltoets1 / 2
else:
    beoordeling_deeltoets1 = 'Onvoldoende'
    cijfer_deeltoets1 = (punten_deeltoets1 - 1.5) / 2

if punten_deeltoets2 >= CESUUR:
    beoordeling_deeltoets2 = 'Voldoende'
    cijfer_deeltoets2 = punten_deeltoets2 / 2
else:
    beoordeling_deeltoets2 = 'Onvoldoende'
    cijfer_deeltoets2 = (punten_deeltoets2 - 1.5) / 2

# print de cijfers en beoordelingen van de beide deeltoetsen
print()
print("Cijfer " + VAKNAAM + " Deeltoets 1: " + str(cijfer_deeltoets1) + "\t\t" + beoordeling_deeltoets1)
print("Cijfer " + VAKNAAM + " Deeltoets 2: " + str(cijfer_deeltoets2) + "\t\t" + beoordeling_deeltoets2)

# print de beoordeling en het cijfer van het gehele vak
if beoordeling_deeltoets1 == 'Voldoende' and beoordeling_deeltoets2 == 'Voldoende':
    print("Je hebt een voldoende voor het vak", VAKNAAM)
    print("Je cijfer is", round((cijfer_deeltoets2 + cijfer_deeltoets1) / 2, 1))
else:
    print("Je hebt een onvoldoende voor het vak", VAKNAAM)
    print("Je cijfer is", round(min(cijfer_deeltoets1, cijfer_deeltoets2), 1))