


while True:
    aantal_cijfers = int(input("Hoeveel cijfers wilt u invoeren? "))

    if aantal_cijfers == 0:
        print("Aantal cijfers moet groter zijn dan 0!")
        continue

    i = 0
    aantal_ingevoerd = 0
    som_cijfers = 0
    aantal_voldoendes = 0

    for studentnummer in range(0,aantal_cijfers):
        studentnummer = studentnummer + 1
        cijfer_student = int(input(f"Cijfer student {studentnummer}: "))
        aantal_ingevoerd = aantal_ingevoerd + 1
        som_cijfers = som_cijfers + cijfer_student
        if cijfer_student>5.5:
            aantal_voldoendes = aantal_voldoendes + 1
    break


gemiddelde = som_cijfers/aantal_ingevoerd

print(f"Aantal cijfers:{aantal_ingevoerd}")
print(f"Gemiddelde cijfer: {gemiddelde}")
print(f"Aantal voldoendes: {aantal_voldoendes}")
