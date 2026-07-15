#1th approach: Count with Array or Hashmap. Here Hashmap
# Time: O(s+t): iterate through both of string
# Space: O(s+t): 2 hashmaps

#Zelf: Bucket?, # Geen BF
#Zelf: samenvoegen en kijken of ieder getal even vaak voorkomt kan ook
#Zie ook LC169,242,392

#Uitwerking 1th approach: Hashmap


class Solution:
    def isAnagram(self, s: str, t= str) -> bool:
        if len(s) !=len(t): # Van tevoren checken of de lengte van maps hetzelfde zijn
            return False

        countS, countT = {}, {} #hier worden de hashmaps gemaakt

        for i in range(len(s)): #itereer door indices (niet door karakters, dat zou zijn for i in s)
            countS[s[i]] = 1 + countS.get(s[i], 0) #waarde van s ophalen op index i. toevoegen aan hashmap. 0 is default argument (hashmap = leeg)
            countT[t[i]] = 1 + countT.get(t[i], 0)


        for c in countS: #c is de keyvalues van de Hashmap.
            if countS[c] != countT.get(c, 0): #default value is 0
                return False

        return True

solution_instance = Solution()

word1 = "listen"
word2 = "silent"

result = solution_instance.isAnagram(word1, word2)

print(result)

