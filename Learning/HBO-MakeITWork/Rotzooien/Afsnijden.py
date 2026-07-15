import random

aantal = random.random(0,3)

karakter = "#"

links = f'{karakter}'
rechts = f'{karakter:>5}'
midden = f'{karakter:^5}'
links_rechts = f'{karakter:<4}{karakter}'
# print per waarde het specifieke dobbelsteenpatroon obv oog
if aantal == 1:
    print()
    print(midden)
    print()
elif aantal == 2:
    print(links)
    print()
    print(rechts)
else:
    print(links)
    print()
    print(links_rechts)

