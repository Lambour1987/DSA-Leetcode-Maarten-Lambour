# range(5) is gelijk aan de reeks 0,1,2,3,4

for i in range(5):
    # print het woord 'herhaling' en de waarde i+10
    print('herhaling', i+10)

#vraag om het aantal
aantal = int(input('Hoeveel strafregels moet je schrijven? '))
zin = input('Welke strafregel moet je schrijven? ')
for i in range(aantal):
    # print de strafregel het opgegeven aantal keer
    print(zin)
