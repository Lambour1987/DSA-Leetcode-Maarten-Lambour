# vraag of het programma gestart moet worden

doorgaan = input('Wil je strafregels laten schrijven? (ja/nee) ')
while (doorgaan == 'ja'):
    aantal = int(input('Hoeveel strafregels moet je schrijven? '))
    zin = input('Welke strafregel moet je schrijven? ')
    for i in range(aantal):
        # print de strafregel het opgegeven aantal keer
        print(zin)
    # vraag of het programma moet blijven draaien
    doorgaan = input('Wil je nog meer strafregels laten schrijven? ')
# sluit het programma af met een bodoschap
print('Je wilt geen strafregels meer schrijven, dus het programma stopt.')