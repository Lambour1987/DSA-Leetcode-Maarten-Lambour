import random

computer_getal = random.randint(1,10)
print(computer_getal)
gebruiker_getal = int(input("Voer een getal tussen 1 en 10 in: "))


if computer_getal == gebruiker_getal:
    print("Goed geraden")
else:
    print("Probeer opnieuw")

