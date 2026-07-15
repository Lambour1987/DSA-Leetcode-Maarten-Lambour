#1st Approach:
# Time:
# Space:

#2nd Approach:
# Time:
# Space:

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        l, r = 0, 1 #left = buy, right =sell
        maxP = 0

        while r < len(prices):
            #profitable?
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxP = max(maxP, profit)
            else:
                l = r
            r += 1
        return maxP

# Een instantie van de Solution-klasse maken
solution = Solution()

# Voorbeeldprijzen van aandelen
stock_prices = [7, 1, 5, 3, 6, 4]

# Testen van de maxProfit-methode
max_winst = solution.maxProfit(stock_prices)
print(f"De maximale winst is: {max_winst}")