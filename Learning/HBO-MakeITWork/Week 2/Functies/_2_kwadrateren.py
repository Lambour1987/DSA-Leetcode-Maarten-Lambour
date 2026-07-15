#Kwadrateren van een getal

def kwadrateer(getal):
    kwadraat = getal * getal
    return kwadraat

getal = int(input("voer een getal in: "))
kwadraat = kwadrateer(getal)
print(kwadraat)