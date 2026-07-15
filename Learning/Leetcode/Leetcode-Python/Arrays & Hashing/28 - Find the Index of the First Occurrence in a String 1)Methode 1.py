#1st Approach: Bruteforce: Nested Forloops
# Time:
# Space:

#lijkt op 438

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == "":
            return 0

        for i in range(len(haystack) + 1 - len(needle)):
            for j in range(len(needle)):
                if haystack[i+j] !=needle[j]: #start at i. j is incrementer
                    break
                if j == len(needle) -1:
                    return i

            return -1

# Een instantie van de Solution-klasse maken
solution = Solution()

# Voorbeeld strings
haystack_example = "hello"
needle_example = "ll"

# Index van het eerste voorkomen van de substring vinden
result = solution.strStr(haystack_example, needle_example)

# Het resultaat afdrukken
print("Index van het eerste voorkomen:", result)


