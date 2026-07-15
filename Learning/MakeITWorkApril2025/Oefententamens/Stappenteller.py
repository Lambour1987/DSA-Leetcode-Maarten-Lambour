#Nog uitwerken: studentnaam, nr etc, doel


#Declareren en initaliseren van de variabelen:
#Lijst met weekdagen
#Lijst met werkelijke stappen
#Lijst met dagen waarin te weinig is gelopen
week_dagen = ["maandag","dinsdag","woensdag", "donderdag", "vrijdag", "zaterdag", "zondag"]
week_dag_stappen = []
te_weinig_stappen = []

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
    werk_stappen_per_dag = int(input(f"{dag}: "))
    totaal_week_stappen = totaal_week_stappen + werk_stappen_per_dag
    if werk_stappen_per_dag < vraag_min_stap_per_dag:
        te_weinig_stappen = te_weinig_stappen.append(week_dagen)
        print(te_weinig_stappen)
    elif werk_stappen_per_dag > vraag_min_stap_per_dag:
        print("Je hebt op alle dagen genoeg gelopen ga zo door! ")
    kCal = verbrandt(totaal_week_stappen)

#Beoordeel of er voldoende stappen zijn gezet o.b.v. eigen input stappen per dag


print()

print(f"Je hebt deze week in totaal {totaal_week_stappen} stappen gelopen.")
print(f"Je hebt hiermee {kCal} kCal verbrand")
print(f"Je hebt te weinig stappen gelopen op ,{te_weinig_stappen}")