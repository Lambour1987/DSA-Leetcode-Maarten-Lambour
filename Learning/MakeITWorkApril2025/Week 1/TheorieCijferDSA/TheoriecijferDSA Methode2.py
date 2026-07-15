
VAK_NAAM = "Datastructures"

print(f"Voer behaalde punten in voor het vak {VAK_NAAM}: ")

punten_deeltoets1 = int(input("Datastructures Deeltoets 1: "))

while punten_deeltoets1 < 0 or punten_deeltoets1 > 20:
    print("Onjuist aantal punten voor Deeltoets 1 ingevoerd")
    punten_deeltoets1 = int(input("Typ Opnieuw Datastructures Deeltoets 1 (0-20): "))


punten_deeltoets2 = int(input("Datastructures Deeltoets 2: "))

while punten_deeltoets2 < 0 or punten_deeltoets2 > 20:
    print("Onjuist aantal punten voor Deeltoets 2 ingevoerd")
    punten_deeltoets2 = int(input("Typ Opnieuw Datastructures Deeltoets 2 (0-20): "))


if punten_deeltoets1 >= 12: #Deeltoets 1 voldoende
    cijfer_deeltoets1 = punten_deeltoets1 / 2
    if punten_deeltoets2 >= 12 : # Deeltoets 2 voldoende
        cijfer_deeltoets2 = punten_deeltoets2 / 2
        eindcijfer = round((cijfer_deeltoets1+cijfer_deeltoets2)/2,1)
        print(f"Datastructures Deeltoets 1: {cijfer_deeltoets1:<5} {"Voldoende":<12}")
        print(f"Datastructures Deeltoets 2: {cijfer_deeltoets2:<5} {"Onvoldoende":<12}")
        print("Je hebt een voldoende voor het vak datastructures")
        print(f"Je cijfer is een {eindcijfer}")
    else:
        cijfer_deeltoets2 = (punten_deeltoets2 - 1.5) / 2
        eindcijfer = round(cijfer_deeltoets2,1)
        print(f"Datastructures Deeltoets 1: {cijfer_deeltoets1:<5} {"Voldoende":<12}")
        print(f"Datastructures Deeltoets 2: {cijfer_deeltoets2:<5} {"Onvoldoende":<12}")
        print("Je hebt een onvoldoende voor het vak datastructures")
        print(f"Je cijfer is een {eindcijfer}")

else: #Deeltoets 1 onvoldoende
    cijfer_deeltoets1 = (punten_deeltoets1 - 1.5)/2
    print("Deeltoets 1 is onvoldoende")
    if punten_deeltoets2 >= 12 :
        cijfer_deeltoets2 = punten_deeltoets2 / 2
        eindcijfer = round(cijfer_deeltoets1,1)
        print(f"Datastructures Deeltoets 1: {cijfer_deeltoets1} {"Voldoende":<12}")
        print(f"Datastructures Deeltoets 2: {cijfer_deeltoets2} {"Onvoldoende":<12}")
        print(f"Je cijfer is een {eindcijfer}")
    else:
        cijfer_deeltoets2 = (punten_deeltoets2 - 1.5) / 2
        if cijfer_deeltoets1>cijfer_deeltoets2:
            eindcijfer = cijfer_deeltoets1
        else:
            eindcijfer = round(cijfer_deeltoets2,1)
        print(f"Datastructures Deeltoets 1: {cijfer_deeltoets1} {"Voldoende":<12}")
        print(f"Datastructures Deeltoets 2: {cijfer_deeltoets2} {"Onvoldoende":<12}")
        print(f"Je cijfer is een {eindcijfer}")



