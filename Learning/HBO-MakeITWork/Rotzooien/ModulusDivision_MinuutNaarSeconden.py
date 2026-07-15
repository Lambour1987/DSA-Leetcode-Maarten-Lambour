def zet_om_naar_minuten(seconden):
    minuten = seconden // 60
    seconden = seconden % 60
    return minuten, seconden

min, sec = zet_om_naar_minuten(114)
print(f"Dit is {min} minuut en {sec} seconden")