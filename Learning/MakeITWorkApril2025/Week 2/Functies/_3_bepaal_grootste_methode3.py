#Methode 3: makkelijke if else statemnets en and operations

def grootste_getal(getal1,getal2,getal3):
    if getal1 >= getal2 and getal1 >= getal3:
        return getal1
    elif getal2 >=getal1 and getal2 >=getal3:
        return getal2
    elif getal3 >=getal1 and getal3 >=getal2:
        return getal3


getal1=int(input("voer getal 1 in: "))
getal2=int(input("Voer getal 2 in: "))
getal3=int(input("Voer getal 3 in: "))

grootste=grootste_getal(getal1, getal2, getal3)
print(f"Het grootste getal is {grootste}")

