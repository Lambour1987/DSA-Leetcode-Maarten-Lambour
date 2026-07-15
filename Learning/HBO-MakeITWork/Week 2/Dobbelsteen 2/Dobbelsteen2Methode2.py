import random

def karakter():
    karakter = str(input("Welk karakter moet ik gebruiken voor het oog: "))

    while karakter not in ["!","@","#","$","%","^","&","*","_"]:
        karakter = str(input("Klopt niet, probeer opnieuw: "))
        print("Het gekozen karakter is", karakter)
    return karakter

def random_ogen():
    aantal_ogen = random.randrange(1,6)
    print("het aantal ogen is", aantal_ogen)
    return aantal_ogen


def toon_worp(aantal, gekozen_karakter):

    k = gekozen_karakter

    if aantal== 1:
        print(f"\n {k} \n ")
    elif aantal == 2:
        print(f"{k} \n \n {k}")
    elif aantal == 3:
        print(f"{k} \n {k} \n  {k}")
    elif aantal == 4:
        print(f" {k} {k} \n \n {k} {k}")
    elif aantal == 5:
        print(f"{k} {k} \n {k} \n{k} {k}")
    elif aantal == 6:
        print(f'{k} {k} {k}\n {k} {k} {k}')
    else:
        print("Ongeldige worp")


gekozen_karakter = karakter()
aantal = random_ogen()
toon_worp(aantal, gekozen_karakter)
