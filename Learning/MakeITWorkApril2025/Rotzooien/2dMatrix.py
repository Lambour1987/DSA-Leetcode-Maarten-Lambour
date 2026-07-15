def test(m,n):
    for i in range(m):
        for j in range(n):
            print("*",end=" ")
        print()

m= int(input("Geef de hoogte met m: "))
n= int(input("Geef de breedte met n: "))

test(m,n)
