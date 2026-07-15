"""
Dit programma bepaalt van een cijferlijst het aantal ingevoerde cijfers, het gemiddelde cijfer
het aantal voldoendes en het hoogste cijfer
@author: Frank Oberndorff
"""
def bepaalaantalvoldoendes(cijferlijst):
    """

    :param cijferlijst: Een array van tentamencijfers
    :return: Het aantal cijfers in de array dat groter is dan 5.5
    """
    aantalvoldoendes = 0
    for cijfer in cijferlijst:  # ga 1 voor 1 langs alle elementen in de array
        if cijfer>= 5.5:
            aantalvoldoendes = aantalvoldoendes + 1
    return aantalvoldoendes

def bepaalhoogstecijfer(cijferlijst):
    """
    :param cijferlijst: Een array van tentamencijfers
    :return: het hoogste cijfer van de array
    """
    # Zet het maximum op 0 aan het begin van de functie
    maxcijfer = 0
    # Ga 1 voor 1 langs alle elementen in de array
    for cijfer in cijferlijst:
        # Als het cijfer in het element van de array groter is dan het maximum
        if cijfer> maxcijfer:
            # Maak het maximum dan gelijk aan het cijfer in het element van
            # de array
            maxcijfer = cijfer
    # Als je de hele array gehad hebt, is maxcijfer gelijk aan het maximum
    # van de hele array
    return maxcijfer

def bepaalgemiddeldecijfer(cijferlijst):
    """

    :param cijferlijst: Een array van tentamencijfers
    :return: Het gemiddelde van alle cijfers in de cijferlijst
    """
    totaal = 0
    aantal = 0
    for cijfer in cijferlijst:
        totaal = totaal + cijfer
        aantal = aantal +1
    gemiddelde = totaal/aantal
    return gemiddelde


# HIER BEGINT HET HOOFDPROGRAMMA

#Vraag het aantal cijfers dat de gebruiker wilt invoeren
aantalcijfers = int(input("Hoeveel cijfers wilt u invoeren? "))

# Controleer of de gebruiker een geldige waarde (>0) heeft ingevoerd
while aantalcijfers <= 0:
    print("Aantal cijfes moet groter zijn dan 0!")
    aantalcijfers = int(input("Hoeveel cijfers wilt u invoeren? "))

# Maak een array aan en vul deze met de invoer van de gebruiker
cijfers = []
for i in range(aantalcijfers):
    ingevoerdcijfer = int(input("Cijfer student "+str(i)+": "))
    cijfers.append(ingevoerdcijfer)

# Print het aantal cijfers, het gemiddelde, het aantal voldoendes en
# en het hoogste cijfer
print()
print("Aantal cijfers    : ", aantalcijfers)
print("Gemiddelde cijfer : ", bepaalgemiddeldecijfer(cijfers))
print("Aantal voldoendes : ", bepaalaantalvoldoendes(cijfers))
print("Hoogste cijfer    : ", bepaalhoogstecijfer(cijfers))

