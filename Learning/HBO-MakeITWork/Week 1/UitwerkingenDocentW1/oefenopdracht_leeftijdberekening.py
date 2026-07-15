"""
Dit programma berekent de leeftijd van de gebruiker obv zijn geboortejaar.
@author: Frank Oberndorff

"""
# Vraag de gebruiker naar zijn naam en geboortejaar TODO
naam_gebruiker = input("Hoe heet je? ")
geboortejaar = int(input("Wat is je geboortejaar? "))
HUIDIG_JAAR = 2025

# Bereken de leeftijd door het geboortejaar af te trekken van het huidige jaar
leeftijd = HUIDIG_JAAR - geboortejaar

# Print een lege regel
print()
# Print de leeftijd van de gebruiker in dit jaar
print("Beste", naam_gebruiker, ", in ", HUIDIG_JAAR, "zal je leeftijd", leeftijd, "zijn.")

# Print een boodschap afhankelijk van de leeftijd van de gebruiker
if leeftijd >= 50:
    print("Ondanks je leeftijd zie je er nog best goed uit!")
else:
    print("Je bent nog lang niet toe aan je pensioen.")