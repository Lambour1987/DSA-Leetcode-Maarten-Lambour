tafel = int(input("Welke tafel wilt u printen?: "))

print(f"de tafel van {tafel}:")

for i in range(0,10):
    for j in range(0,5):
        i = i + 1
        uitkomst = tafel * i
        print(uitkomst, end=" ")
    print()