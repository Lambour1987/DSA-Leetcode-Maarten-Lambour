
def som_lijst(getallen_rij,lengte_rij):

    som = 0

    for i in range(0,lengte_rij):
        som = som + getallen_rij[i]
        print(som)

getallen_rij=[1,2,3,4,5]
lengte_rij = len(getallen_rij)
som_lijst(getallen_rij, lengte_rij)