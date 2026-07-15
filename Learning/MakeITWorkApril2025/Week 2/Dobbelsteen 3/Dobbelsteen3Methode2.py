import random


#Bereken de geldigheid van het karakter. Indien niet geldig probeer opnieuw
def karakter():
    karakter = str(input("Welk karakter moet ik gebruiken voor het oog: "))

    while karakter not in ["!","@","#","$","%","^","&","*","_"]:
        karakter = str(input("Klopt niet, probeer opnieuw: "))

    return karakter

#Op basis van het gekozen karakter wordt er een willekeurig aantal ogen tussen de 1 en 7 gegeven (1 tm 6)
def toon_worp(gekozen_karakter):
    aantal = random.randrange(1, 7)

    while aantal !=6:
        k = gekozen_karakter
        print("Het aantal klopt nu niet, dat is namelijk: ", aantal)
        if aantal== 1:
            print(f"\n {k} \n ")
            print()
        elif aantal == 2:
            print(f"{k} \n \n {k}")
            print()
        elif aantal == 3:
            print(f"{k} \n {k} \n  {k}")
            print()
        elif aantal == 4:
            print(f" {k} {k} \n \n {k} {k}")
            print()
        else:
            print(f"{k} {k} \n {k} \n{k} {k}")
            print()

        aantal = random.randrange(0, 7)
    print("Het aantal klopt nu wel, dat is namelijk: ", aantal)
    print(f'{k} {k}\n{k} {k} \n{k} {k}')

gekozen_karakter = karakter()
toon_worp(gekozen_karakter)
