tafel = int(input("Welke tafel wilt u printen?: "))
tot_aan = int(input("Hoeveel getallen wilt u printen?: "))

totaal = 0
i = 0

print(f"De tafel van {tafel}:")

for i in range(1, tot_aan+1):
    totaal = i * tafel
    print(totaal, end=" ")

    if i % 5 ==0:
        print()