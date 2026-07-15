import random

def welkom():
    print("Welkom bij Casino Roulette!")
    print("Je hebt 100 fiches. Zet je fiches in op een nummer tussen 0 en 36.")
    print("Als je wint, verdien je 36 keer je inzet. Je verliest je inzet als je verliest.\n")


def plaats_inzet(fiches):
    while True:
        inzet = input(f"Je hebt {fiches} fiches. Hoeveel fiches wil je inzetten: ")
        if not inzet.isdigit():
            print("Ongeldige invoer. Voer een geldig getal in.")
        elif int(inzet) > fiches:
            print("Je kunt niet meer inzetten dan je hebt. Probeer opnieuw.")
        else:
            return int(inzet)


def speel_roulette(inzet):
    winnend_nummer = random.randint(0, 36)
    print(f"Het roulette wiel draait... het winnende nummer is {winnend_nummer}!")

    if inzet == winnend_nummer:
        return 36 * inzet
    else:
        return -inzet


def main():
    welkom()
    fiches = 100

    while fiches > 0:
        inzet = plaats_inzet(fiches)
        resultaat = speel_roulette(inzet)
        fiches += resultaat

        if resultaat > 0:
            print(f"Gefeliciteerd! Je hebt {resultaat} fiches gewonnen.")
        else:
            print(f"Jammer! Je hebt {abs(resultaat)} fiches verloren.")

        print(f"Je hebt nu {fiches} fiches over.\n")

    print("Bedankt voor het spelen!")


if __name__ == "__main__":
    main()