def toon_rij_sterren(aantal):
    for i in range(0, aantal):
        print("*", end = " ")

def sterren_vierkant(aantal):
    for i in range(aantal):
        toon_rij_sterren(aantal)
        print()

toon_rij_sterren(5)
sterren_vierkant(5)
