#1st Approach:
# Time:
# Space:

class MinStack:
    def __init__(self):
        self.stack = [] #not an ordinary array
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        val = min(val, self.minStack[-1] if self.minStack else val)
        self.minStack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]

# Maak een instantie van MinStack
minStack = MinStack()

# Voeg elementen toe aan de stack
minStack.push(3)
minStack.push(5)
minStack.push(2)
minStack.push(1)

# Bekijk de minimale waarde op dit moment
print("Minimale waarde op dit moment:", minStack.getMin())  # Dit zou 1 moeten afdrukken

# Verwijder het bovenste element van de stack
minStack.pop()

# Bekijk de top van de stack en de minimale waarde op dit moment
print("Bovenste element van de stack:", minStack.top())  # Dit zou 2 moeten afdrukken
print("Minimale waarde op dit moment:", minStack.getMin())  # Dit zou 2 moeten afdrukken

# Voeg meer elementen toe
minStack.push(0)
minStack.push(4)

# Bekijk de minimale waarde op dit moment
print("Minimale waarde op dit moment:", minStack.getMin())  # Dit zou 0 moeten afdrukken