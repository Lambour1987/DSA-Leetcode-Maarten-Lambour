#Oppervlakteberekening door Maarten Lambour
#Berekenen van de oppervlakte van een cirkel, rechthoek, vierkant en driehoek

def cirkel():
    pi = 3.14
    hoogte_cm = int(input("Wat is de hoogte in cm? "))
    breedte_cm = int(input("Wat is de breedte in cm? "))
    oppervlakte = hoogte_cm*breedte_cm
    print(f"De oppervlakte van jouw rechthoek is {oppervlakte} vierkante centimeter ")

def rechthoek():
    hoogte_cm = int(input("Wat is de hoogte in cm? "))
    breedte_cm = int(input("Wat is de breedte in cm? "))
    oppervlakte = hoogte_cm * breedte_cm
    print(f"De oppervlakte van jouw rechthoek is {oppervlakte} vierkante centimeter ")

def vierkant():
    zijde_cm = int(input("Wat is de zijde in cm? "))
    oppervlakte = zijde_cm*zijde_cm
    print(f"De oppervlakte van jouw rechthoek is {oppervlakte} vierkante centimeter ")

def driehoek():
    hoogte_cm = int(input("Wat is de hoogte in cm? "))
    breedte_cm = int(input("Wat is de breedte in cm? "))
    oppervlakte = (hoogte_cm * breedte_cm)/2
    print(f"De oppervlakte van jouw rechthoek is {oppervlakte} vierkante centimeter")



def vraag():
    antwoord = ""
    while antwoord !=" ":
        antwoord = int(input("Van welke figuur wil je de oppervlakte laten uitrekenen? "))
        if antwoord == 1:
            cirkel()
        elif antwoord == 2:
            rechthoek()
        elif antwoord == 3:
            vierkant()
        elif antwoord == 4:
            driehoek()
        elif antwoord == 0:
            print("Het programma wordt nu gestopt.")
vraag()

