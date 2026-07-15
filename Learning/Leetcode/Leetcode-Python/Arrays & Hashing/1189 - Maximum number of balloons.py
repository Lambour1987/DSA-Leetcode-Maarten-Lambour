#1st Approach:
# Time: O(n)
# Space:

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        countText = Counter(text)
        balloon = Counter("balloon") #kan ook met forloop maar Counter is eigenlijk build in

        res = len(text) #or float("inf")
        for c in balloon:
            res = min(countText[c] // balloon[c]) #// is integer division
        return res



