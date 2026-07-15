#Random getallen met for loop. Geen dubplicaten mogelijk

import random

list_A = random.sample(range(0,9),3)
list_B = random.sample(range(0,9),3)

print("Ongeordend: ")
print(list_A)
print(list_B)

list_A = sorted(list_A)
list_B = sorted(list_B)

print("Gesorteerd:")
print(list_A)
print(list_B)

