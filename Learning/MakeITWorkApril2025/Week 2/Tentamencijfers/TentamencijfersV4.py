aantal_invoeren = 0

while aantal_invoeren <= 0:
    aantal_invoeren = int(input("Hoeveel cijfers wilt u invoeren? "))
    if aantal_invoeren <= 0:
        print("Aantal cijfers moet groter zijn dan 0!")

reeds_ingevoerd = 0
som_cijfers = 0
studentencijfers = []

for studentnummer in range(0,aantal_invoeren):
    studentnummer = studentnummer + 1
    cijfer_student = int(input(f"Cijfer student {studentnummer}: "))
    studentencijfers.append(cijfer_student)
    som_cijfers = som_cijfers + cijfer_student
    reeds_ingevoerd = reeds_ingevoerd + 1
    print(f"Reeds ingevoerd {reeds_ingevoerd} van de {aantal_invoeren}")

gemiddelde = som_cijfers/aantal_invoeren

voldoendes = 0

for cijfer_student in studentencijfers:
    if cijfer_student>5.5:
        voldoendes = voldoendes + 1

hoogste = studentencijfers[0]

for cijfer in studentencijfers:
    if cijfer > hoogste:
        hoogste = cijfer

print(f"Aantal cijfers: {aantal_invoeren}")
print(f"Gemiddelde cijfer: {gemiddelde}")
print(f"aantal voldoendes: {voldoendes}")
print(f"hoogste cijfer {hoogste}")



