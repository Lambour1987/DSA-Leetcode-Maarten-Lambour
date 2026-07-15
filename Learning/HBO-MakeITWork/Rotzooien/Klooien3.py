import random

# 5 willekeurige getallen tussen 1 en 10
getallen_tuple = tuple(random.randint(1, 10) for _ in range(5))

print(getallen_tuple)
