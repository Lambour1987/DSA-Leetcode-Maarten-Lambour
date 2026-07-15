#1st Approach:
# Time:
# Space:

import heapq

class Solution:
    def isNStraightHand(self, hand: list[int], groupSize: int) -> bool:
        if len(hand) % groupSize: #% is modulo operator
            return False

        count = {}
        for n in hand:
            count[n] = 1 + count.get(n,0) #n ophalen uit dict. Verhogen met 1. Als die niet bestaat dan 0. Daar wordt dan 1 opgeteld.

        minH = list(count.keys())
        heapq.heapify(minH)
        while minH:
            first=minH[0] #geeft kleinste element uit heap

            for i in range(first, first + groupSize):
                if i not in count:
                    return False
                count[i] -= 1 #waarde van element wordt verlaagd met 1
                if count[i] == 0:
                    if i != minH[0]:
                        return False
                    heapq.heappop(minH)
        return True

solution = Solution()
hand_example = [1,2,3,6,2,3,4,7,8]
groupSize_example = 3
result = solution.isNStraightHand(hand_example, groupSize_example)
print(result)