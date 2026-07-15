#1st Approach:
# Time:
# Space:
from collections import deque


class MyStack:

    def __init__(self):
        self.q = deque()

    def push(self, x:int) -> None:
        self.q.append(x)

    def pop(self) -> int:
        for i in range(len(self.q) -1):
            self.push(self.q.popleft())
        return self.q.popleft()


    def top(self) -> int:
        return self.q[-1]

    def empty(self) -> bool:
        return len(self.q) ==0

# Maak een instantie van MyStack
stack = MyStack()

# Voeg elementen toe aan de stack
stack.push(1)
stack.push(2)
stack.push(3)

# Controleer of de stack leeg is
print("Is de stack leeg?", stack.empty())  # Dit zou False moeten afdrukken

# Bekijk het bovenste element van de stack
print("Bovenste element van de stack:", stack.top())  # Dit zou 3 moeten afdrukken

# Verwijder het bovenste element van de stack
print("Verwijderd element:", stack.pop())  # Dit zou 3 moeten afdrukken

# Controleer opnieuw of de stack leeg is
print("Is de stack leeg?", stack.empty())  # Dit zou False moeten afdrukken

# Voeg meer elementen toe
stack.push(4)
stack.push(5)

# Verwijder en print alle elementen van de stack
while not stack.empty():
    print("Verwijderd element:", stack.pop())

# Controleer opnieuw of de stack leeg is
print("Is de stack leeg?", stack.empty())  # Dit zou True moeten afdrukken