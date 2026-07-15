#1st Approach: Lineair Time Algoritm
# Time:
# Space:

class Solution:
    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:
        if sum(gas) < sum(cost):
            return -1

        total = 0
        res = 0
        for i in range(len(gas)):
            total += (gas[i] - cost[i]) # betekent: total = total + (gas[i] - cost[i]).

            if total < 0:
                total = 0
                res = i + 1
        return res

# Een instantie van de Solution-klasse maken
solution = Solution()

# Voorbeeld met benzine- en kostengegevens voor elk pompstation
gas = [1, 2, 3, 4, 5]
cost = [3, 4, 5, 1, 2]

# Testen van de canCompleteCircuit-methode
resultaat = solution.canCompleteCircuit(gas, cost)
print(f"Het startpunt om een volledige ronde te maken is: {resultaat}")