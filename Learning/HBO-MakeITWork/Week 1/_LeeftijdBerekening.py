""""
Dit programma heeft tot doel de leeftijd te berekenen van
de gebruiker te berekenen en een boodschap te geven afhankelijk
van zijn leeftijd. Gemaakt door Maarten Lambour
"""

naam = input("Hoe heet je: ")
geboortejaar = int(input("Wat is je geboortejaar?: "))
JAAR = 2025

#Deze functie berekent de leeftijd o.b.v. het geboortejaar
def leeftijd(JAAR, geboortejaar):
    leeftijd = JAAR-geboortejaar
    return(leeftijd)

#Deze functie bepaalt een boodschap o.b.v. de leeftijd
def boodschap_leeftijd(leeftijd):
    if leeftijd >= 50:
        boodschap = "Ondank je leeftijd zie je er nog best goed uit!"
    else:
        boodschap = "Je bent nog lang niet toe aan pensioen."
    return boodschap

uitkomst_leeftijd = leeftijd(JAAR, geboortejaar)
boodschap = boodschap_leeftijd(uitkomst_leeftijd)

print(f"Beste {naam}, in 2018 zal je leeftijd {uitkomst_leeftijd} zijn. {boodschap}")








