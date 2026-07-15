waarde = int(input('Wat heb je gegooid met je dobbelsteen? '))
print()
# print per waarde het specifieke dobbelsteenpatroon obv #
if waarde == 1:
    print()
    print(" " + "#")
    print()
elif waarde == 2:
    print("#")
    print()
    print("  " + "#")
elif waarde == 3:
    print("#")
    print(" " + "#")
    print("  " + "#")
elif waarde == 4:
    print("#" + " " + "#")
    print()
    print("#" + " " + "#")
elif waarde == 5:
    print("#" + " " + "#")
    print(" " + "#")
    print("#" + " " + "#")
elif waarde == 6:
    print("#" + " " + "#")
    print("#" + " " + "#")
    print("#" + " " + "#")
else:
    print('Ongeldige worp')
