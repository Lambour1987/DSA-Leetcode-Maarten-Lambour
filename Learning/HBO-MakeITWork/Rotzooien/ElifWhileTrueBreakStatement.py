while True:
    aantal_ogen = int(input("Wat heb je gegooid met je dobbelsteen? "))

    if aantal_ogen in [1,2,3,4,5,6]:
        break
    else:
        print("Ongeldige worp. Probeer opnieuw")

if aantal_ogen == 1:
    print("\n # \n ")
elif aantal_ogen == 2:
    print("# \n \n #")
elif aantal_ogen == 3:
    print("# \n # \n  #")
elif aantal_ogen == 4:
    print(" # # \n \n # #")
elif aantal_ogen == 5:
    print("# # \n # \n# #")
elif aantal_ogen == 6:
    print('# # #\n # # #')
else:
    print("Ongeldige worp")