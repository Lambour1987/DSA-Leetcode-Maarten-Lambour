#Naam: BMI berekening
#Doel: Bereken BMI op basis van gewicht (kg) en lengte in (cm)

gewicht_kg = float(input("Gewicht in kg: "))
lengte_cm = int(input("Lengte in cm: "))
lengte_mtr = lengte_cm/100

#print("Gewicht in kilogram:", gewicht_kg)
#print("Lengte in centimemeter", lengte_mtr)

BMI = float(gewicht_kg/(lengte_mtr*lengte_mtr))
print('BMI: ', BMI)

if BMI >= 25:
    print("Er is sprake van overgewicht.")
else:
    print("Je bent goed op gewicht.")
