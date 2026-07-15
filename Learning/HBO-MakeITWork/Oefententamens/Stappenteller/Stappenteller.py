#Nog uitwerken: studentnaam, nr etc, doel


#Declareren en initaliseren van de variabelen:
#Lijst met weekdagen
#Lijst met werkelijke stappen
#Lijst met dagen waarin te weinig is gelopen
week_dagen = ["maandag","dinsdag","woensdag", "donderdag", "vrijdag", "zaterdag", "zondag"]
week_dag_stappen = []
dagen_te_weinig_stappen = []

#Constante met minimaal in te voeren stappen
MINIMAAL_STAPPEN = 5000

#T.b.v. stappen per week berekenen, initaliseer op 0
totaal_week_stappen =0

#T.b.v stappen per dag berekenen, initaliseer op 0
stappen_per_dag = 0

#functie voor het berekenen van calorien
def verbrandt(totaal_week_stappen):
    kCal = totaal_week_stappen * 0.03
    return kCal

#while loop om opnieuw te vragen als te weinig is ingevoerd
vraag_min_stap_per_dag = int(input("Hoeveel stappen wil je minimaal lopen per dag? "))
while vraag_min_stap_per_dag<MINIMAAL_STAPPEN:
    print(f"     Stel je doel hoger, minimaal {MINIMAAL_STAPPEN} stappen per dag!")
    vraag_min_stap_per_dag = int(input("Hoeveel stappen wil je minimaal lopen per dag? "))

#op de weekdagen de stappen per dag invoeren
print("Voer het aantal stappen per dag in: ")
for dag in week_dagen:
    werkelijke_stappen_per_dag = int(input(f"{dag}: "))
    totaal_week_stappen = totaal_week_stappen + werkelijke_stappen_per_dag
    if werkelijke_stappen_per_dag < vraag_min_stap_per_dag:
        dagen_te_weinig_stappen.append(dag)
        #print(te_weinig_stappen)

#Beoordeel of er voldoende stappen zijn gezet o.b.v. eigen input stappen per dag

print()

print(f"Je hebt deze week in totaal {totaal_week_stappen} stappen gelopen.")
kCal = verbrandt(totaal_week_stappen)
print(f"Je hebt hiermee {kCal} kCal verbrand")

#Beoordeel of er dagen zijn waarin te weinig is gelopen
if len(dagen_te_weinig_stappen) > 0:
    print("Je hebt te weinig gelopen op: " + ", ".join(dagen_te_weinig_stappen))
else:
    print("Je hebt op alle dagen genoeg gelopen, ga zo door!")



