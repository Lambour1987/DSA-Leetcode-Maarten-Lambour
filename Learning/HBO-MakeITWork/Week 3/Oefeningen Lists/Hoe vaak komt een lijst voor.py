import random

for i in range(0,1000):
    list_1 = random.randint(0, 50)
    print(list_1, end=" ")

for j in range(list_1):
    count = 0
    if list_1[j]==23:
        count = count + 1
        print(count)

