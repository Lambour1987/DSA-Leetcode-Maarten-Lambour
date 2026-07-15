import random

def karakter_mogelijkheden():
    karakters = ["!","@","#","$","%","^","&","*"]
    while True:
        karakter = input("welk karakter2 moet ik gebruiken voor het oog: ")
        if karakter in karakters:
            print("goed zo")
            return karakter
        else:
            print("opnieuw")

def toon_worp_1(aantal, karakter):
    if aantal == 1:
        print(f"{karakter}")
    if aantal == 2:
        print(f"{karakter}{karakter}")
    if aantal == 3:
        print(f"{karakter}{karakter}{karakter}")
    if aantal == 4:
        print(f"{karakter}{karakter}{karakter}{karakter}")
    if aantal == 5:
        print(f"{karakter}{karakter}{karakter}{karakter}{karakter}")
    if aantal == 6:
        print(f"{karakter}{karakter}{karakter}{karakter}{karakter}{karakter}")

def toon_worp_2(aantal,karakter):
    print(karakter*aantal)


karakter = karakter_mogelijkheden()
aantal= random.randrange(1,7)

toon_worp_1(aantal, karakter)
toon_worp_2(aantal, karakter)



