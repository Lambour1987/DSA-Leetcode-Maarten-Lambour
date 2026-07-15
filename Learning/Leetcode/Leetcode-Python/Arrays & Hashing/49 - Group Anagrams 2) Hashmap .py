#2st Approach: Hashmap (in de loop van de uitwerking wordt de dictionary gewijzigd in een default hashmap
# Time: O(m*n) -> m is number of strings we are given. n is average length
# Space:
from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: list[str])-> list[list[str]]:
        res = defaultdict(list) #mapping charCount to list of Anagrams.

        for s in strs: #zelf: dus voor elk woord in de lijst met stringst
            count = [0] * 26 #a ... z

            for c in s: #zelf: voor elk karakter in elk woord in de lijst van strings
                count[ord(c)-ord("a")] += 1    #map a tm z in 0 tm 25

            res[tuple(count)].append(s)

        return res.values()


solution = Solution()
example_strings = ["eat", "tea", "tan", "ate", "nat", "bat"]
result = solution.groupAnagrams(example_strings)
print(result)