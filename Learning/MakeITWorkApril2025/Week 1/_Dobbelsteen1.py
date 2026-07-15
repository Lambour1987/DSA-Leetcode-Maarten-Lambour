from xml.dom.minidom import ElementInfo

aantalogen = int(input("Wat heb je gegooid met je dobbelsteen? "))

if aantalogen <1 or aantalogen >=7:
    print("Ongeldige worp")
if aantalogen == 1:
    print("\n  #")
elif aantalogen == 2:
    print("\n#\n\n #")
elif aantalogen == 3:
    print("\n#\n","#\n"," #")
elif aantalogen == 4:
    print("\n # #\n","\n","# #")
elif aantalogen == 5:
    print("\n# #\n","#","\n# #")
elif aantalogen == 6:
    print("\n# #\n# #\n# #")


