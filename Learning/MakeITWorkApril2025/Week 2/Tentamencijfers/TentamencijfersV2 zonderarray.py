aantal_cijfers = int(input("Hoeveel cijfers wilt u invoeren?: "))
cijfer_student = 0
cijfer_totaal = 0
aantal_voldoendes = 0
aantal_onvoldoendes = 0
hoogste_cijfer = 0

if aantal_cijfers == 0:
    print("Aantal cijfers moet groter zijn dan 0!")

else:
    for i in range(0, aantal_cijfers):
        i = i + 1
        cijfer_student = int(input(f"Cijfer van studentnummer {i}: "))
        if cijfer_student>5.5:
            aantal_voldoendes +=1
        else:
            aantal_onvoldoendes +=1
        if cijfer_student>hoogste_cijfer:
            hoogste_cijfer = cijfer_student
        cijfer_totaal = cijfer_totaal + cijfer_student
        huidig_gemiddelde = cijfer_totaal / i

    print(f"Het huidig totaal is {cijfer_totaal}\n"
        f" Het gemiddelde cijfer is {huidig_gemiddelde}\n"
        f" Het aantal voldoendes is {aantal_voldoendes}\n"
        f" Het aantal onvoldoendes is {aantal_onvoldoendes}\n"
        f" Het hoogste cijfer is een {hoogste_cijfer}")

