"""
Dit programma berekent de Body Mass Index (BMI) o.b.v. het gewicht
en de lengte van de gebruiker
"""
GRENS_GEZOND_GEWICHT = 25
# Vraag de gebruiker naar zijn gewicht en lengte
gewicht = float(input("Gewicht in kilogram: "))
lengte_in_cm = int(input("Lengte in centimeter: "))
# Zet de ingevoerde lengte (in cm's) om in meters
lengte_in_m = lengte_in_cm/100

bodymassindex = gewicht / (lengte_in_m * lengte_in_m)

# Print een lege regel en de BMI van de gebruiker
print()
print("BMI:", bodymassindex)

if bodymassindex <= GRENS_GEZOND_GEWICHT:
    print("Je bent goed op gewicht.")
else:
    print(("Je hebt overgewicht!"))