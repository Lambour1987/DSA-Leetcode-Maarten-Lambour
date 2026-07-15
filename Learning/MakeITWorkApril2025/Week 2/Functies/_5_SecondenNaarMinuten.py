def zet_om_naar_seconden(seconden):
    minuten = seconden//60
    rest_seconden = seconden%60
    print(f"Het gaat om {minuten} minuten en {rest_seconden} seconden")


seconden = int(input("Voer het aantal seconden in: "))
zet_om_naar_seconden(seconden)
