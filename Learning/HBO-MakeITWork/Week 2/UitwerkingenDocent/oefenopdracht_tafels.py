tafel = int(input("Welke tafel wilt u printen (0=stoppen)? "))
hoeveelgetallen = int(input("Hoeveel getallen wilt u printen? "))

while tafel!=0:
    print ("De tafel van", tafel,":")

    for x in range(1, (hoeveelgetallen+1)):
        print("%6d" % (x*tafel), end='')
        if x % 5 == 0: # of x % 5 == 0 and x != hoeveelgetallen
            print()
    print()
    tafel = int(input("Welke tafel wilt u printen (0=stoppen)? "))
    hoeveelgetallen = int(input("Hoeveel getallen wilt u printen? "))
