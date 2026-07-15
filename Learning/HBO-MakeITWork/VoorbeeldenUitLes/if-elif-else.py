# score = 1000
#
# if score < 50:
#     print("Helaas!")
# elif 50 <= score < 70:
#     print("Goed gedaan!")
# else:
#     print("Uitstekend!")

temperatuur = 15            # De temperatuur in graden Celsius
weertype = "regenachtig"    # Type weer: zonnig, bewolkt of regenachtig

if temperatuur > 20:
    if weertype == "zonnig":
        print("Trek een T-shirt en shorts aan.")
    else:
        print("Trek lichte kleding aan, maar neem een jas mee.")
else:
    if weertype == "regenachtig":
        print("Trek een warme trui en een regenjas aan.")
    else:
        print("Het is koel; draag een lange broek en een trui.")



    temperatuur = 15  # De temperatuur in graden Celsius
    weertype = "regenachtig"  # Type weer: zonnig, bewolkt of regenachtig

    if temperatuur > 20 and weertype == "zonnig":
        print("Trek een T-shirt en shorts aan.")
    elif temperatuur > 20 and weertype != "zonnig":
        print("Trek lichte kleding aan, maar neem een jas mee.")
    elif temperatuur <= 20 and weertype == "regenachtig":
        print("Trek een warme trui en een regenjas aan.")
    else:
        print("Het is koel; draag een lange broek en een trui.")




















