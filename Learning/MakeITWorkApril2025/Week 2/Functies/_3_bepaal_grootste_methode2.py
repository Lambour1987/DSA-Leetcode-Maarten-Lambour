# doe met variabele maximum en for loop

def invoeren():
    getallenreeks = []
    aantal_invoeren = int(input(f"Hoeveel getallen wilt u invoeren? "))
    for i in range(0,aantal_invoeren):
        i = i + 1
        getal = int(input(f"voer getal {i} in: "))
        getallenreeks.append(getal)
    return getallenreeks


def bepaal_grootste(reeks):
    maximum = 0
    for getal in reeks:
        if getal > maximum:
            maximum = getal
    return maximum

reeks = invoeren()
maximum = bepaal_grootste(reeks)
print(f"Het grootste getal is {maximum}")




