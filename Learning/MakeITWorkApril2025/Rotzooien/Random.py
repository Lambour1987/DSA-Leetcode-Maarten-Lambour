import random
# 1 Random getallen

getal1 = random.randrange(0,4) #0 tm 3
getal2 = random.randint(0,4) # 0 tm 4
getal3 = random.random()
print(getal1)
print(getal2)
print(getal3)



# 5 willekeurige getallen tussen 1 en 10
getallen_tuple = tuple(random.randint(1, 10) for _ in range(5))

print(getallen_tuple)


