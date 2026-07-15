import random
import statistics
getallen_lijst = []

som = 0
minimum = 100

for i in range(0,20):
    getal = random.randint(1,100)
    som = som + getal
    getallen_lijst.append(getal)
    if getallen_lijst[i]<minimum:
        minimum = getallen_lijst[i]

lengte_lijst = len(getallen_lijst)
gemiddelde = float(som/lengte_lijst)

gemiddelde2 = statistics.mean(getallen_lijst)

print(getallen_lijst)
print(som)
print("het gemiddelde is:", gemiddelde)
print(sum(getallen_lijst))
print("het minimnum is ", minimum)
print("het gemiddelde volgens import statistics is", gemiddelde2)
