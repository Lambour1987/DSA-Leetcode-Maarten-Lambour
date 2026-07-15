#Insert en Append functie

colors = ['red', 'green', 'blue', 'yellow']
print(colors)

colors.append('black')
print(colors)

print(f"Item met index nummer [0] is: {colors[0]}")

print(f"Item met index nummer [4] is: {colors[4]}")

colors = ['red', 'green', 'blue', 'yellow']
print(f"De oorspronkelijke lijst: \n{colors}\n")

colors.insert(1, 'white')

print(f"Lijst met 'white' op indexpositie 1:\n{colors}")
