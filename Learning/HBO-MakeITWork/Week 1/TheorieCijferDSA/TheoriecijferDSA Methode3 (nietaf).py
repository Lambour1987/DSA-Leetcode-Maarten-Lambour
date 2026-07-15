#Klopt nog niet helemaal maar begin is er


DATASTRUCTURES = 0
Eindcijfer = 0

print("Voer de behaalde punten in voor het vak Datastructures: ")
punten_deeltoets_1 = int(input("Datastructures deeltoets 1: "))
punten_deeltoets_2 = int(input("Datastructures deeltoets 2: "))

deeltoets1_voldoende = False
deeltoets2_voldoende = False

if punten_deeltoets_1 > 12:
    cijfer_deeltoets1 = punten_deeltoets_1/2
    deeltoets1_voldoende = True
elif punten_deeltoets_1 <12:
    cijfer_deeltoets2 = (punten_deeltoets_2-1.5)/2
if punten_deeltoets_2 > 12:
    cijfer_deeltoets2 = punten_deeltoets_2/2
    deeltoets2_voldoende = True
elif punten_deeltoets_2 <12:
    cijfer_deeltoets2 = (punten_deeltoets_2-1.5)/2

if deeltoets1_voldoende == True:
    if deeltoets2_voldoende == True:
        eindcijfer = (cijfer_deeltoets1 + cijfer_deeltoets2)/2
    elif deeltoets2_voldoende == False:
        eindcijfer = (cijfer_deeltoets2)
elif deeltoets1_voldoende == False:
    if deeltoets2_voldoende == True:
        eindcijfer = cijfer_deeltoets1
    elif deeltoets2_voldoende == False:
        eindcijfer == (cijfer_deeltoets1+cijfer_deeltoets2)/2


print(f"Cijfer datastructures Deeltoets 1: {cijfer_deeltoets1}: Voldoende {deeltoets1_voldoende}")
print(f"Cijfer datastructures Deeltoets 2: {cijfer_deeltoets2}: Voldoende {deeltoets2_voldoende}")
print(f"Het eindcijfer is {eindcijfer}")