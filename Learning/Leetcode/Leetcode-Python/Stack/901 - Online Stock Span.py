#1st Approach:
# Time:
# Space:

class StockSpanner:
    def __init__(self):
        self.stack = []  # pair: (price, span)

    def next(self, price: int) -> int:
        span = 1
        while self.stack and self.stack[-1][0] <= price:
            span += self.stack[-1][1]
            self.stack.pop()
        self.stack.append((price, span))
        return span


# Gebruik de StockSpanner-klasse
spanner = StockSpanner()

# Prijzen
prices = [100, 80, 60, 70, 60, 75, 85]

# Bereken de span voor elke prijs en print het resultaat
for price in prices:
    print(spanner.next(price), end=" ")  # Output: 1 1 1 2 1 4 6