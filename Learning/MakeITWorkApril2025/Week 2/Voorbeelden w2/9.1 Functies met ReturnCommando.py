# Aan het begin van een programma definieer je een functie

def optellen(a, b):
    uitkomst = a + b
    return uitkomst

# Aanroepen van de functie (voorbeeld 1)
print('de som van 10 en 20 is')
print(optellen(10, 20))
print()

# Aanroepen van dezelfde functie met andere argumenten
# (voorbeeld 2)

x=25
y=30
som=optellen(x, y)

print('de som van x en y is',som)
