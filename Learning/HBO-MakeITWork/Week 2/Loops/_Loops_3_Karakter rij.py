def geldigheid_karakter(karakter):
    toegestane_tekens = ["!","@","#","$","%","^","&","*"]
    if karakter in toegestane_tekens:
        return True
    else:
        return False

def toon_char_rij(karakter, aantal):
    for i in range(aantal):
        print(karakter, end="")


karakter= input("Welk karakter wil je dit keer gebruiken?: ")

geldigheid_karakter(karakter)

if geldigheid_karakter(karakter) == True:
    aantal = int(input("Hoe vaak wil je het zien?: "))
    toon_char_rij(karakter,aantal)
else:
    print("Dit karakter is niet toegestaan")