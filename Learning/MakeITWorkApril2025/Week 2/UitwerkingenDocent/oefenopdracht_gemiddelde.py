"""
Deze applicatie rekent het gemiddelde uit van twee of meer getallen.
:author: Frank Oberndorff

"""
def wiljedoorgaan():
    """
    Deze functie vraagt de gebruiker of hij door wil gaan met het toevoegen
    van getallen. Als de gebruiker 'ja' intypt is de returnwaarde True, als
    hij 'nee' intypt is de returnwaarde False
    :return: True of False (boolean)
    """
    doorgaan = input('Wil je van meer getallen het gemiddelde bepalen (ja/nee)?')
    # Geef aan dat input niet geaccepteerd wordt als het antwoord niet 'ja' en
    # niet 'nee' is
    while doorgaan != 'ja' and doorgaan != 'nee':
        print("Je moet met 'ja' of 'nee' antwoorden.")
        doorgaan = input('Wil je van meer getallen het gemiddelde bepalen (ja/nee)?')

    # Als de input 'ja' is return True, als hij 'nee' is return False
    if doorgaan == 'ja':
        return True
    else:
        return False
#einde functie wiljedoorgaan()

# de variabele som bevat de optelling van alle ingevoerde getallen
som = int(input("Dit programma berekent het gemiddelde van "
                "twee of meer\ngetallen. Geef het eerste getal: "))
som = som + int(input("Geef het tweede getal: "))

# de variabele aantal bevat het aantal ingevoerde getallen
aantal = 2

# zolang de gebruiker wilt doorgaan met het toevoegen van getallen,
# tel de invoer op bij de som en hoog het aantal op met 1
while wiljedoorgaan():
    som = som + int(input("Geef het volgende getal: "))
    aantal = aantal + 1

print("Het gemiddelde van jouw", aantal, "getallen is", som / aantal)