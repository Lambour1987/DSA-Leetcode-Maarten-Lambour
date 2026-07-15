#1st Approach:
# Time: O(n)
# Space: O(1): alleen een single variable di

#Keep track, reset by space, Eliminate white spaces

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        i, length = len(s) -1, 0 #In eerste instantie leest python dit als 2 variabelen toewijzen (niet per se een index en een variabele).
        # bij de volgende regels weet python de context (bij de while loops). hier blijkt dat i een index moet zijn.

        while s[i] == " ":
            i -= 1 #dus i = i - 1
        while i >= 0 and s[i] != " ":
            length += 1
            i -= 1
        return length

solution = Solution()
example_string = "Hello World      "
result = solution.lengthOfLastWord(example_string)
print(result)  # Output: 5 (length of the last word "World")