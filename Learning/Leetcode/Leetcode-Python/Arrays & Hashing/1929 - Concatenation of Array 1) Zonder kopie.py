#1th approach: Door chatGPT
# Time:
# Space:

from typing import List

class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = []

        # Voeg alle elementen van nums toe aan ans
        for n in nums:
            ans.append(n) #toevoegen aan een list dus met ans.append(n): je voegt n toe aan de list

        # Voeg alle elementen van nums opnieuw toe aan ans
        # Zelf je kan dit oneindig kopieren
        for n in nums:
            ans.append(n)

        return ans

# Test de functie
solution_instance = Solution()
nums = solution_instance.getConcatenation([1, 2, 3])
print(nums)