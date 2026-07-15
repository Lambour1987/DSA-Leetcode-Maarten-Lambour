import math

def berekenoppervlaktecircel(straalcircel):
    oppervlakte = math.pi * math.pow(straalcircel,2)
    return int(oppervlakte)

def berekenoppervlakterechthoek(hoogterechthoek, breedterechthoek):
    oppervlakte = hoogterechthoek * breedterechthoek
    return int(oppervlakte)

def berekenoppervlaktevierkant(zijdevierkant):
    oppervlakte = math.pow(zijdevierkant, 2)
    return int(oppervlakte)

def berekenoppervlaktedriehoek(basisdriehoek, hoogtedriehoek):
    oppervlakte = basisdriehoek * hoogtedriehoek / 2
    return int(oppervlakte)

def printResultaat(figuur, oppervlakte):
    print("De oppervlakte van jouw", figuur,"is",oppervlakte,"vierkante cm.")

gewenstefiguur = ''

while gewenstefiguur != '0':
    print()
    print("Van welke figuur wil je de oppervlakte uit laten rekenen?")
    gewenstefiguur = input("(cirkel = 1; rechthoek = 2; vierkant = 3; driehoek = 4; stoppen = 0): ")
    print()
    if gewenstefiguur == '1':
        straal = int(input("Wat is de straal van de circel in cm? "))
        printResultaat('circel',berekenoppervlaktecircel(straal))
    elif gewenstefiguur == '2':
        hoogte = int(input("Wat is de hoogte in cm? "))
        breedte = int(input("Wat is de breedte in cm? "))
        printResultaat('rechthoek',berekenoppervlakterechthoek(hoogte, breedte))
    elif gewenstefiguur == '3':
        zijde = int(input("Wat is de zijde in cm? "))
        printResultaat('vierkant',berekenoppervlaktevierkant(zijde))
    elif gewenstefiguur =='4':
        basis = int(input("Wat is de basis in cm? "))
        hoogte = int(input ("Wat is de hoogte in cm? "))
        printResultaat('driehoek',berekenoppervlaktedriehoek(basis, hoogte))
