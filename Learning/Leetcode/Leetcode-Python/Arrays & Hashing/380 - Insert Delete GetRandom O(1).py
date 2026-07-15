import random

class RandomizedSet:

    def __init__(self):
        self.numMap = {}
        self.numList = []

    def insert(self, val: int) -> bool:
        res = val not in self.numMap
        if res:
            self.numMap[val] = len(self.numList)
            self.numList.append(val)
        return res

    def remove(self, val: int) -> bool:
        res = val in self.numMap
        if res:
            idx = self.numMap[val]
            lastVal = self.numList[-1]
            self.numList[idx] = lastVal
            self.numList.pop()
            self.numMap[lastVal] = idx
            del self.numMap[val]
        return res

    def getRandom(self) -> int:
        return random.choice(self.numList)

# Voorbeeldgebruik
randomizedSet = RandomizedSet()
print(randomizedSet.insert(1))  # True
print(randomizedSet.remove(2))  # False
print(randomizedSet.insert(2))  # True
print(randomizedSet.getRandom())  # Kan 1 of 2 zijn
print(randomizedSet.remove(1))  # True
print(randomizedSet.insert(2))  # False, omdat 2 al aanwezig is
print(randomizedSet.getRandom())  # Altijd 2