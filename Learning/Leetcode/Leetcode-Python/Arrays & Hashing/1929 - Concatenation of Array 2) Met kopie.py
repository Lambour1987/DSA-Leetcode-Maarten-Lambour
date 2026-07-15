#1th approach: BF?
# Time:
# Space:

#2th approach: Create OutputArray (=Dynamic Array)
# Time: O(1): O(n+n). Input is n. Concatenation is also n.
# Space: O(n)

#Zelf: clone/ copy?

#2th approach: Create OutputArray (=Dynamic Array)

from typing import List

class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]: #zelf: dus een array of integers
        ans = []

        for i in range(0,2): #zelf '0,' neergezet. De lus wordt 2x doorlopen. Probeer die 2 eens te veranderen naar een 1 of een 3 dan zie je het verschil.
            #2 betekent hier: 2x de lus doorlopen.
            for n in nums: #voor iedere iteratie in de buitenste lus, wordt de gehele lijst nums doorlopen
                ans.append(n)
        return(ans)

solution_instance = Solution()
nums = solution_instance.getConcatenation([1, 2, 3]) #hier geef je de waarden aan.
print(nums)