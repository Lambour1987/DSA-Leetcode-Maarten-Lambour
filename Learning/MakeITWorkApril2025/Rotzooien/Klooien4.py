#Random getallen met for loop. Duplicaten mogelijk. Check met if statements hoeveel gelijk

import random

list_A = []
list_B = []

for i in range(0,3):
    getal = random.randrange(0,3)
    list_A.append(getal)

for j in range(0,3):
    getal = random.randrange(0, 3)
    list_B.append(getal)

print(list_A)
print(list_B)

list_A = sorted(list_A)
list_B = sorted((list_B))

print(list_A)
print(list_B)

if list_A[0]==list_B[0]:
    print("1e getal gelijk")
    if list_A[1] == list_B[1]:
        print("2e getal gelijk")
    else:
        print("2e getal ongelijk")
        if list_A[2] == list_B[2]:
            print("3e getal gelijk")
        else:
            print("3e getal ongelijk")