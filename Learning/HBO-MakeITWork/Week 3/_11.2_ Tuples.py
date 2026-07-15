#Gegevens met een logisch verband, bijv. coordinaat.
# In c, gebruik struct

point = (3,4)
print(point)
print(point[1])

print("\n")

fibonacci = (1,1,2,3,5,8)

for getal in fibonacci:
    print(getal)

# tupel met twee items in de variabele 'vormen'
vormen = ('cirkel', 'vierkant')
print(f"Tuple: {vormen}")

# de variabele vormen kan naar het type list worden gecast
vormen = list(vormen)
print(f"List: {vormen}")

#een item toevoegen aan de list
vormen.append('driehoek')
print(f"List met toegevoegd item: {vormen}")

#list terugzetten naar tupel
vormen = tuple(vormen)
print(f"Tuple: {vormen}")




