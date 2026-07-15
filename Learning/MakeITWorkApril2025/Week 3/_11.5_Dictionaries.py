# Vergelijkbaar met hashmap in c

ages = {'John': 25, 'Mary': 30, 'Bob': 20}

print(ages)
print(ages['Mary'])

# haal 1-voor-1 elke key op en stop die telkens in variabele p
for person in ages:
    #print de key
    print(person)

print()

#haal 1-voor-1 elke key op en stop die telkens in variabele p
for person in ages:
    #print de value die hoort bij de key in de dictionary ages
    print(ages[person])

