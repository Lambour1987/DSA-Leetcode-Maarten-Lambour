naam = "Jan"
leeftijd = 25

zin = "Mijn naam is %10s en ik ben %3d jaar oud" % (naam, leeftijd)
print(zin)

naam = "Jan"
leeftijd = 25

zin = "Mijn naam is {:>10} en ik ben {:3} jaar oud". format(naam, leeftijd)
print(zin)
