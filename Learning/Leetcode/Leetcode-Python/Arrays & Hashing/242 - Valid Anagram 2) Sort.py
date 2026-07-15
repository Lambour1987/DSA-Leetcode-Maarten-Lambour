#2th approach: Sorted
# Time: O(n^2) met Bubblesort of O(nlogn)
# Space: O(n): usually met sorting methods. Optimized sometimes O(1)

#Zelf: Bucket?, # Geen BF

#Cheat approach with Counter. niet gedaan.
#class Solution:
    # def isAnagram(self, s: str, t= str) -> bool:
    #     return Counter(s) == Counter(t)

class Solution:
    def isAnagram(self, s: str, t= str) -> bool:
        return sorted(s) == sorted(t)


        if len(s) !=len(t):
            return False
        countS, countT = {}, {}

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)

        for c in countS: #c is de keyvalues van de Hashmap. c is de key
            if countS[c] != countT.get(c, 0):
                return False

        return True

solution_instance = Solution()

word1 = "listen"
word2 = "silent"

result = solution_instance.isAnagram(word1, word2)

print(result)