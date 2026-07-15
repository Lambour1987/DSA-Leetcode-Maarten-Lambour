#Handmatig sorteren. Zeer omslachtig. Lijkt het meest op selection sort
#Voor 5 getallen zou je 5! = 120 mogelijkheden moeten hebben

#gebruik getallen 10,20,30
def sorteren(getal1, getal2, getal3):
    if getal1>getal2: #True bij: 30,20,10/30,10,20/20,10,30
        if getal1>getal3: #True bij: 30,20,10/30,10,20
            if getal2>getal3: #True bij 30,20,10
                print(getal3,getal2,getal1)
            else: #False bij 30,10,20
                print(getal2,getal3,getal1)
        else:#False bij 20,10,30
            print(getal2,getal1,getal3)
    elif getal1>getal3:
        if getal2>getal3:
            print(getal3,getal1,getal2)
        else:
            print(getal1,getal2,getal3)
    else:
        if getal2>getal3:
            print(getal1,getal3,getal2)
        else:
            print(getal1,getal2,getal3)

i = 0
getal1 = 0
getal2 = 0
getal3 = 0

for i in range(0,3):
    getal = int(input("Geef een getal: "))
    if i == 0:
        getal1 = getal
    elif i==1:
        getal2 = getal
    elif i==2:
        getal3=getal

sorteren(getal1,getal2,getal3)

