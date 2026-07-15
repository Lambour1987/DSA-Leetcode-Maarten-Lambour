#Vergelijkbaar met hashset in c

# een nieuwe set met 4 kleuren
colors = {'red', 'green', 'blue', 'yellow'}

#print een voor een alle items uit de set
for c in colors:
    print(c)

# een nieuwe set met 4 kleuren
colors = {'red', 'green', 'blue', 'yellow'}
print(colors)

# de kleur 'yellow' verwijderen met discard
colors.discard('yellow')
print(colors)

# de kleur 'black' toevoegen
colors. add('black')
print(colors)

#de kleur 'red' nogmaals toevoegen
colors.add('red')

#bij het printen van 'colors' blijkt de laatste toevoeging
# 'red' niet zijn gedaan omdat er al een kleur 'red' was
print(colors)