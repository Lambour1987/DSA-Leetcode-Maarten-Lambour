
aantal = int(input("Hoeveel cijfers wilt u invoeren?: "))
student_nummer = 1

if aantal == 0:
    print("Aantal cijfers moet groter zijn dan 0!")
else:
    for i in range(0,aantal):
        i = i + 1
        cijfer = int(input(f"Cijfer student {i}: "))

#print(f"Aantal cijfers: {i}("/")(aantal)")

