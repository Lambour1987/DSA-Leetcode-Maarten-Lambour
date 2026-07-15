def menu():
    while True:
        keuze = input("1 = Hallo, 2 = Overslaan, 3 = Stoppen: ")

        if keuze == "1":
            print("Hallo!")
        elif keuze == "2":
            print("Ronde overgeslagen.\n")
        elif keuze == "3":
            print("Programma stopt.")
            return  # stopt de hele functie, en dus de loop ook
        else:
            print("Ongeldige keuze.\n")

menu()