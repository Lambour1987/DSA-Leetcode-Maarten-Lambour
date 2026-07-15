#BSA Monitor


vaknamen = ["Project Fasten your Seatbelts","Programming","Business", "Personal Skills", "Project Skills", "Management & Organization", "Databases"]
vakpunten = [12,3,3,2,2,3,3]
vakcijfers = []
aantal_behaalde_vakpunten =  []
aantal_vakken = len(vaknamen)

print("Voer het behaalde cijfer in: ")
for vak in vaknamen:
    cijfer = float(input(f"{vak}: "))
    if cijfer<=0 or cijfer > 10.00:
        print("cijfer niet geldig")
    vakcijfers.append(cijfer)

print(vakcijfers)

som_punten=0
for i in range(aantal_vakken):
    if vakcijfers[i]>5.5:
        aantal_behaalde_vakpunten.append(vakpunten[i])
        som_punten = som_punten + 1
    else:
        aantal_behaalde_vakpunten.append(0)

print(aantal_behaalde_vakpunten)

for vak in vaknamen:
    print(f"Vak/project: {vak}", f"Cijfer: {vakcijfers}", f"Behaalde punten: {aantal_behaalde_vakpunten}")

print("Het aantal behaalde punten is", som_punten)

