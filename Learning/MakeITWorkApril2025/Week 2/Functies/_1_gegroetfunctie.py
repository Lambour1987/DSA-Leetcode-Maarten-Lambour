import sys

def groet(naam, gekozen_dagdeel):
    print(f"Goeden{gekozen_dagdeel}, {naam}")

def vraag_dagdeel():
    invoer_dagdeel = int(input("Wat is het dagdeel? (morgen(1), middag(2), avond(3))"))
    if invoer_dagdeel == 1:
        return "morgen"
    elif invoer_dagdeel ==2:
        return "middag"
    elif invoer_dagdeel ==3:
        return "avond"
    else:
        print("Onjuiste dagdeel ingevoerd. Het moet tussen 1 en 3 liggen")
        sys.exit() # programma stopt hier

naam = input("Voer uw naam in: ")
gekozen_dagdeel = vraag_dagdeel()
groet(naam,gekozen_dagdeel)
