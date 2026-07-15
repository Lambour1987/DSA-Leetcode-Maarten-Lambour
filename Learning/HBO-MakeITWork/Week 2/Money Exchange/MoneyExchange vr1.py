
# Koers 15-4-2025
#1 EURO = 161,60 yen
#1 EURO = 1,13 dollar
#1 EURO = 0.8554 pond

YEN = EURO_YEN = 161      # Yen
DOLLAR = EURO_DOLLAR = 1.13     # Dollar
POND = EURO_POND = 0.8554   # Pond


def Money_Exchange(valuta, vreemd_bedrag):
    if valuta == 1:
        eur_bedrag = round(float(vreemd_bedrag/EURO_DOLLAR),2)

        valuta = "dollar"
    elif valuta == 2:
        eur_bedrag = round(float(vreemd_bedrag/EURO_POND),2)
        valuta = "pond"
    elif valuta == 3:
        eur_bedrag = round(float(vreemd_bedrag/EURO_YEN),2)
        valuta = "yen"
    else:
        print("onjuist ingevoerd")
        return

    print(f"Voor {vreemd_bedrag} {valuta} krijgt u {eur_bedrag} Euro.")


valuta = int(input("1=US dollar, 2=GB pounds, 3=Yen "))
vreemd_bedrag = int(input("In te wisselen bedrag (gehele getallen): "))

Money_Exchange(valuta, vreemd_bedrag)



