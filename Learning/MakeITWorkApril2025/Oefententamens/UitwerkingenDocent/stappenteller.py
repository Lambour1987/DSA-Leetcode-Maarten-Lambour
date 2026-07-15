"""
Dit programma kan op basis van het aantal stappen dat  de gebruiker in een weerk heeft gelopen,
berekenen hoeveel kilocalorieën iemand heeft verbrand. Tevens geeft het programma aan op
welke dagen de gebruiker minder heeft gelopen dan het minimaal aantal stappen.
Dit minimale aantal stappen kan de gebruiker zelf invoeren.
Auteur: Jetty Schenk
"""

# print naam, studentnummer en klas.
print("Dit programma is gemaakt door student X, MIW, 5008123456\n")

# definieer een functie voor het berekenen van kilocalorieën.
def bereken_kcal(aantalstappen):
    verbrande_calorieen = 0.03 * aantalstappen
    return verbrande_calorieen

# Vraag de gebruiker om het minimale aantal stappen hij wilt lopen en zorg dat het minimaal 5000 is.
minimum_stappen = int(input("Hoeveel stappen wil je minimaal lopen per dag? "))
while minimum_stappen < 5000:
    print("\tStel je doel hoger, minimaal 5000 stappen per dag!")
    minimum_stappen = int(input("Hoeveel stappen wil je minimaal lopen per dag? "))

# Vul een array met de dagen van de week en maak een array een voor de gelopen stappen.
dagen_van_de_week = ["maandag","dinsdag","woensdag","donderdag","vrijdag","zaterdag","zondag"]
gelopen_stappen_week = []

# Vraag de gebruiker  m.b.v een for loop om de stappen in te vullen en vul array gelopen_stappen_week.
print("Voer het aantal stappen per dag in:")
for i in range(7):
    stappen_per_dag = int(input("\t%s: " % dagen_van_de_week[i]))
    gelopen_stappen_week.append(stappen_per_dag)

# Bereken m.b.v loop het totale aantal stappen
totaal_aantal_stappen = 0
for i in range(7):
    totaal_aantal_stappen = totaal_aantal_stappen + gelopen_stappen_week[i]

# Print het totale aantal stappen
print("\nJe hebt deze week in totaal %d stappen gelopen." % totaal_aantal_stappen)

# Print m.b.v. functie het totale aantal verbrande calorieën.
print("Je hebt hiermee %f kCal verbrand." % bereken_kcal(totaal_aantal_stappen))

# print m.b.v. loop de dagen van de week waarop minder dan het minimum aantal stappen is gelopen
print("Je hebt deze week te weinig stappen gelopen op: ",end="")
for i in range(7):
    if gelopen_stappen_week[i] < minimum_stappen:
        print(dagen_van_de_week[i],end=" ")

# Print boodschap als de gebruiker alle dagen genoeg stappen heeft gezet.
genoeg_stappen = True
for i in range(7):
    if gelopen_stappen_week[i] < minimum_stappen:
        genoeg_stappen = False

if genoeg_stappen:
    print("\nJe hebt alle dagen genoeg gelopen, ga zo door!")
