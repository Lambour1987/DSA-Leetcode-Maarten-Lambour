# Gemiddelde
# Door Maarten Lambour
# Bereken het gemiddelde van minimaal 2 getallen

#recursief of iteratief

def eerste_getallen():
    print("Dit programma berekent het gemiddelde van twee of meer getallen")
    aantal = 0
    eerste_getal = int(input("Geef het eerste getal: "))
    tweede_getal = int(input("Geef het tweede getal: "))
    vraag(eerste_getal, tweede_getal)

def vraag(eerste_getal, tweede_getal):
    antwoord = input("Wil je van meer getallen het gemiddelde bepalen (ja/nee)? ")

    if antwoord == 'ja':
        volgende_getallen()
    elif antwoord == 'nee':
        bereken_gemiddelde(eerste_getal, tweede_getal)
    else:
        print("Onjuist gegeven")


def volgende_getallen(antwoord):
    aantal = 2
    while (antwoord == 'ja'):
        getal = input("geef een getal")
        aantal = aantal + 1




def bereken_gemiddelde(eerste getal,tweede getal):
    for getal in range(aantal):
        getal = int(input("geef getal: "))
        totaal = getal + totaal
        print(totaal)
        i = i+1
        gemiddelde = totaal/aantal

        print(gemiddelde)

#def main():

eerste_getallen()


