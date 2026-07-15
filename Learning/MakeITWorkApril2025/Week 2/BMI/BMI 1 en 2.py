

import math

def bereken_bmil(lengte, gewicht):
    lengte = lengte/100

    bmi = round(gewicht/math.pow(lengte,2),1)

    return bmi

def bepaal_categorie(bmi):
    if bmi <18.5:
        categorie = "Ondergewicht"
    elif bmi >= 18.5 and bmi <25.0:
        categorie = "Gezond Gewicht"
    elif bmi >= 25.0 and bmi <30.0:
        categorie = "Overgewicht"
    else:
        categorie = "Obesitas"
    return categorie



gewicht = float(input("Wat is uw gewicht?: "))
lengte = int(input("Wat is uw lengte in centimeters?: "))
print(f"Gewicht in kilogram: {gewicht}")
print(f"Lengte in centimeter: {lengte}")
bmi = bereken_bmil(lengte, gewicht)
categorie = bepaal_categorie(bmi)
print(f"BMI: {bmi}")
print(categorie)