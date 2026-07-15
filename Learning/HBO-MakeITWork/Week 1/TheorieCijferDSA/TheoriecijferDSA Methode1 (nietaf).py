
dt1 = int(input("Geef aantal punten voor DT1: "))
dt2 = int(input("Geef aantal punten voor DT2: "))

aantal_voldoendes = 0

if dt1<0 or dt1>20:
    print("Onjuist ingevoerd")
elif dt1 >= 12:
    aantal_voldoendes = aantal_voldoendes + 1
    cijfer_dt1 = float(dt1 / 2)
    print(f"Voldoende, uw cijfer is {cijfer_dt1}")
elif dt1 <=12:
    cijfer_dt1=float((dt1-1.5) / 2)
    print(f"Onvoldoende, uw cijfer is {cijfer_dt1}")

if dt2<0 or dt2>20:
    print("Onjuist ingevoerd")
elif dt2 >= 12:
    aantal_voldoendes = aantal_voldoendes + 1
    cijfer_dt2 = float(dt2 / 2)
    print(f"Voldoende, uw cijfer is {cijfer_dt2}")
elif dt1 <=12:
    cijfer_dt2=float((dt1-1.5) / 2)
    print(f"Onvoldoende, uw cijfer is {cijfer_dt2}")

print(f"u heeft {aantal_voldoendes} voldoende behaald")