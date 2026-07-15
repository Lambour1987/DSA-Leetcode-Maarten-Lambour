import math

#Naam: BMI Vervolg
#Doel: Bereken BMI en bepaal categorie

def bereken_bmil(lengte_cm, gewicht_kg):

#BMI = Gewicht in kilogram/ (Lengte in meter^2)

    lengte_m = lengte_cm/100

    print("Gewicht in kilogram: ", gewicht_kg)
    print("Lengte in centimers: ", lengte_m)

    bmi = gewicht_kg/math.pow(lengte_m,2)
    bmi = round(bmi,1)

    return bmi


def bepaal_categorie(bmi):
    if bmi < 18.5:
        return("(ondergewicht)")
    elif bmi >= 18.5 or bmi <25.0:
        return("(gezond gewicht)")
    elif bmi >= 25.0 or 30.0:
        return("(overgewicht)")
    elif bmi >=30.0:
        return("(obesitas)")


## als string teruggeven

#def main():
lengte_cm = float(input("Voer je lengte in cm in: "))
gewicht_kg = float(input("Voer je gewicht in kg in: "))
uitkomst_BMI =bereken_bmil(lengte_cm, gewicht_kg)
uitkomst_cat = bepaal_categorie(uitkomst_BMI)
print("BMI:", uitkomst_BMI, uitkomst_cat)
