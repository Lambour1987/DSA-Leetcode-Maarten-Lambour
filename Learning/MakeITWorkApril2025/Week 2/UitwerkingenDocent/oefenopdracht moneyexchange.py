"""
Dit programma berekent de waarde van dollars, ponden en yen
omgerekend naar euro's
@author: Frank Oberndorff
"""
# Vastleggen van de koersen. Dit getal legt vast hoeveel euro je krijgt
# als je 1 eenheid van de betreffende munt betaalt.
# constanten voor de wisselkoersen
USD_RATE = 0.9551
GBP_RATE = 1.2059
YEN_RATE = 0.006436
# constanten voor de namen van de valuta
USD = "US dollar"
GBP = "GB pounds"
YEN = "Yen"
# constante voor het percentage van de transactiekosten
PERCENTAGE_TRANSACTIEKOSTEN = 0.015


def bereken_bedrag_euros(valutacode, bedrag):
    """
    Deze functie berekent de eurowaarde van een bepaald bedrag
    in buitenlandse valuta
    :param valutacode: naam van de valuta obv constanten (str)
    :param bedrag: bedrag van valuta (int)
    :return: eurowaarde
    """
    if valutacode == USD:
        euros = bedrag * USD_RATE
    elif valutacode == GBP:
        euros = bedrag * GBP_RATE
    elif valutacode == YEN:
        euros = bedrag * YEN_RATE
    return euros


def bereken_transactiekosten(bedrag):
    """
    Deze functie berekent de transactiekosten van het omwisselen van een
    bepaald eurobedrag dat omgewisseld wordt
    :param eurobedrag: eurobedrag dat omgewisseld wordt
    :return: transactiekosten
    """
    MINIMUM_KOSTEN = 2
    MAXIMUM_KOSTEN = 15
    kosten = bedrag * PERCENTAGE_TRANSACTIEKOSTEN
    if kosten < MINIMUM_KOSTEN:
        kosten = MINIMUM_KOSTEN
    elif kosten > MAXIMUM_KOSTEN:
        kosten = MAXIMUM_KOSTEN
    return kosten


# lees de valutakeuze en het aantal om te wisselen valuta in
valuta_keuze = input(f"Valuta (1 = {USD}, 2 = {GBP}, 3 = {YEN}): ")
aantal = int(input("In te wisselen bedrag (alleen gehele getallen): "))

# zet de keuze om in de naam van het valuta (obv een constante)
if valuta_keuze == "1":
    valuta = USD
elif valuta_keuze == "2":
    valuta = GBP
elif valuta_keuze == "3":
    valuta = YEN

# bereken het eurobedrag en de transactiekosten
eurobedrag = bereken_bedrag_euros(valuta, aantal)
transactiekosten = bereken_transactiekosten(eurobedrag)

# print alle resultaten op het scherm
print()
print(f"Voor {aantal} {valuta} krijgt u {round(eurobedrag, 2)} Euro.")
print(f"De transactiekosten bedragen {round(transactiekosten, 2)} Euro.")
print(f"U ontvangt {round(eurobedrag, 2) - round(transactiekosten, 2)} Euro.")
