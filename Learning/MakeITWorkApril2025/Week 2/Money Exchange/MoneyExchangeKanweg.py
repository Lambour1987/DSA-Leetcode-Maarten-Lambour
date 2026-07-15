
USD_RATE = 0.9551
GBP_RATE = 1.2059
YEN_RATE = 0.006436

def valutakeuze():
    keuze  = int(input("Valuta (1= US dollar, 2 = GB pounds, 3 = Yen): "))
    bedrag = int(input("In te wisselen bedrag(alleen gehele getallen): "))
    if keuze == 1:
        omgerekend_bedrag = bedrag * (1/USD_RATE)
    elif keuze == 2:
        omgerekend_bedrag = bedrag * (1/GBP_RATE)
    elif keuze == 3:
        omgerekend_bedrag = bedrag * (1/YEN_RATE)
    else:
        print("keuze onjuist")
        return None, None

    return bedrag, omgerekend_bedrag

def transactiekosten(omgerekend_bedrag):
    kosten = omgerekend_bedrag * 0.0015
    if kosten >= 15:
        kosten = 15
    elif kosten <= 2:
        kosten = 2
    return kosten



bedrag, omgerekend_bedrag = valutakeuze()
extra_kosten=transactiekosten(omgerekend_bedrag)
totale_kosten = omgerekend_bedrag + extra_kosten


print(f"voor {bedrag} bedrag krijgt u {omgerekend_bedrag} Euro.")
print(f"de transactiekosten bedrag {extra_kosten}, de totale kosten bedragen {totale_kosten}")

