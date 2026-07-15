import math
"""
Dit programma berekent de Body Mass Index (BMI) o.b.v. het gewicht
en de lengte van de gebruiker
"""
# constanten voor de grenzen van de categoriën
GRENS_ONDERGEWICHT = 18.5
GRENS_GEZOND_GEWICHT = 25
GRENS_OBESITAS = 30


def bereken_bmi(lengte, gewicht):
    """
    :param gewicht: in kg als float
    :param lengte: in meters als float
    :return: de bodymassindex afgerond
    """
    bodymassindex = gewicht / math.pow(lengte, 2)
    return round(bodymassindex, 1)


def bepaal_categorie(bmi):
    """
    :param bmi: waarde van de bodymassindex
    :return: de categorie als string op basis van grenswaarden
    """
    if bmi < GRENS_ONDERGEWICHT:
        categorie = "Ondergewicht"
    elif bmi <= GRENS_GEZOND_GEWICHT:
        categorie = "Gezond gewicht"
    elif bmi <= GRENS_OBESITAS:
        categorie = "Overgewicht"
    else:
        categorie = "Obesitas"
    return categorie


# Vraag de gebruiker naar zijn gewicht en lengte
gewicht = float(input("Gewicht in kilogram : "))
lengte_in_cm = int(input("Lengte in centimeter: "))

# Zet de ingevoerde lengte (in cm's) om in meters
lengte_in_m = lengte_in_cm / 100

bmi = bereken_bmi(lengte_in_m, gewicht)

# Print een lege regel en de BMI van de gebruiker
print()
print(f"BMI: {bmi} ({bepaal_categorie(bmi)})")
