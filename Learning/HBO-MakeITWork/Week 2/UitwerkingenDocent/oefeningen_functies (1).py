def groet(naam, dagdeel):
    print(f'Goede{dagdeel} {naam}')


def kwadrateer(getal):
    return getal * getal


def bepaal_grootste(getal1, getal2, getal3):
    grootste = getal1
    if getal2 > grootste:
        grootste = getal2
    if getal3 > grootste:
        grootste = getal3
    return grootste


def sorteer(getal1, getal2, getal3):
    if getal1 < getal2:
        eerste = getal1
        tweede = getal2
    else:
        eerste = getal2
        tweede = getal1
    if getal3 < eerste:
        derde = tweede
        tweede = eerste
        eerste = getal3
    elif getal3 < tweede:
        derde = tweede
        tweede = getal3
    else:
        derde = getal3
    print(eerste, tweede, derde)


def zet_om_naar_minuten(seconden):
    minuten = seconden // 60
    seconden = seconden % 60
    return minuten, seconden


groet('Julian', 'morgen')
print(kwadrateer(3))
print(bepaal_grootste(34, 79, 78))
sorteer(84, 79, 78)
min, sec = zet_om_naar_minuten(114)
print(f"Dit is {min} minuut en {sec} seconden")



