#1th approach: Hashmap
# Time: O(n^2): n is number of rows
# Space:
#2th approach: Sorted
# Time:
# Space:

#Two Pointers

from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]] #begin met waarde 1 uit de bovenste rij. is 2d Array

        for i in range(numRows -1): #zelf: dus nu is for i in range itererern door het aantal rijen minus de bovenste (want die staat al bij res = [[1]])
            temp = [0] + res[-1] + [0] #zelf nieuwe rij bouwen: 0 aan het begin toevoegen en 0 aan het eind toevoegen
            row = []
            for j in range(len(res[-1])+1): #Volgende rij. Aantal uit de vorige rij + 1
                row.append(temp[j] + temp[j+1]) #bijhouden van pointers
            res.append(row) #rij toevoegen
        return res

solution = Solution()
result = solution.generate(3)  # Vervang 5 door het gewenste aantal rijen
print(result)
