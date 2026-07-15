def tel_aantal_te_sommeren_getallen(grens):

    som = 0
    i = 1

    while som + i < grens:
        som = som + i
        i = i + 1
        print(i, som)

    print(f"De eerste {i} getallen bij elkaar zijn net geen {grens}")


grens = int(input("Tot hoeveel moeten we optellen: "))
tel_aantal_te_sommeren_getallen(grens)