# Importeer de dobbelsteen1 functie

#import KOPIE_7_Dobbelsteen1

#def toon_worp(aantal_karakter):

karakter = input("Kies een karakter. Kies uit een van de volgende: @ # $ % ^ & * ")

if karakter in "@#$%^&*":
    print("Juist karakter: Het gekozen karakter is", karakter)
    k = karakter

else:
    print("Onjuist karakter")


def worp():
    aantalogen = int(input("Wat heb je gegooid met je dobbelsteen? "))

    if aantalogen <1 or aantalogen >=7:
        print("Ongeldige worp")
    if aantalogen == 1:
        print("\n  k")
    elif aantalogen == 2:
        print("\nk\n\n k")
    elif aantalogen == 3:
        print("\nk\n","k\n"," k")
    elif aantalogen == 4:
        print("\n k k\n","\n","k k")
    elif aantalogen == 5:
        print("\nk k\n","k","\nk k")
    elif aantalogen == 6:
        print("\nk k\nk k\nk k")


worp()


#def main()
#karakter = input("Geef het karakter aan, u heeft keuze tussen:")










