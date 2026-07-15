def zeg_hallo():
    print("Hallo!")

while True:
    keuze = input("1 = Hallo zeggen, 2 = Overslaan, 3 = Stoppen: ")

    if keuze == "1":
        zeg_hallo()
    elif keuze == "2":
        print("Deze ronde wordt overgeslagen.\n")
        continue #Ga meteen naar het begin van de while-loop
    elif keuze == "3":
        print("Het Programma Stopt")
        break # stop de while-loop
    else:
        print("Ongeldige keuze .\n")

print("Nu dus gestopt")

