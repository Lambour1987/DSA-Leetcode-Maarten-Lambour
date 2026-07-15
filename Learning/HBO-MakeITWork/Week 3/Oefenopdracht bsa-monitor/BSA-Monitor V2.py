#Opieuw doen, gaat al redelijk


#Maak een lijst met vakken
vak_namen_lijst = ["Fasten your Seatbelts","Programming","Business","Perosnal Skills", "Project Skills", "Management & Organization", "Databases"]
vak_punten_lijst = [12,3,3,2,0,3,0]
vak_cijfer_lijst = []

totaal_punten = 0

#Voer per vak het cijfer in, validatie geldigheid
def cijfer_per_vak():
    print("Voer behaalde cijfers in: ")
    for vak in vak_namen_lijst:
        cijfer = float(input(f"{vak}: "))
        while cijfer <1 or cijfer>10:
            print("cijfer moet tussen 1 en 10 liggen")
            cijfer = float(input(f"{vak}: "))
        vak_cijfer_lijst.append(cijfer)

def behaalde_punten(cijfer):
    behaald_lijst = []
    for i in rante(len(vak_cijfer_lijst)):
        if cijfer >5.5:
            behaald_lijst.append(vak_punten_lijst[cijfer])
        else:
            behaald_lijst.append(0)

cijfer = cijfer_per_vak()
behaalde_punten(cijfer)




