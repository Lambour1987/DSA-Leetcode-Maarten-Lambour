
def validatie_aantal():
    aantal_cijfers = int(input("Hoeveel cijfers wilt u invoeren?: "))
    while aantal_cijfers<=0:
        print("Aantal cijfers moet groter zijn dan 0! ")
        aantal_cijfers = int(input("Hoeveel cijfers wilt u invoeren?: "))
    return aantal_cijfers

def cijferlijst(aantal_cijfers):
    cijfer_lijst = []
    for i in range(aantal_cijfers):
        i = i + 1
        cijfer = float(input(f"Cijfer student {i}: "))
        cijfer_lijst.append(cijfer)
    print("\n")
    return cijfer_lijst

def krijg_gemiddelde(cijfer_lijst, aantal_cijfers):
    totaal_som_cijfers = 0
    for cijfer in cijfer_lijst:
        totaal_som_cijfers = totaal_som_cijfers + cijfer
    gemiddelde_cijfer = totaal_som_cijfers/ aantal_cijfers
    return gemiddelde_cijfer

def krijg_aantal_voldoendes(cijferlijst):
    aantal_voldoendes = 0
    aantal_onvoldoendes = 0
    for cijfer in cijferlijst:
        if cijfer>5.5:
            aantal_voldoendes = aantal_voldoendes + 1
        else:
            aantal_onvoldoendes = aantal_onvoldoendes + 1
    return (aantal_voldoendes)

def krijg_hoogste_cijfer(cijfer_lijst):
    hoogste_cijfer = 0
    for cijfer in cijfer_lijst:
        if cijfer>hoogste_cijfer:
            hoogste_cijfer = cijfer
    return hoogste_cijfer

def outputfunctie(aantal_cijfers, gemiddelde, voldoendes, hoogste):
    print(f"Aantal cijfers     : {aantal_cijfers}\n"
          f"Gemiddelde cijfer  : {gemiddelde}\n"
          f"Aantal voldoendes  : {voldoendes}\n"
          f"Hoogste cijfer     : {hoogste}")

aantal_cijfers = validatie_aantal()
cijfer_lijst = cijferlijst(aantal_cijfers)
gemiddelde = krijg_gemiddelde(cijfer_lijst, aantal_cijfers)
voldoendes = krijg_aantal_voldoendes(cijfer_lijst)
hoogste = krijg_hoogste_cijfer(cijfer_lijst)
outputfunctie(aantal_cijfers, gemiddelde, voldoendes, hoogste)



