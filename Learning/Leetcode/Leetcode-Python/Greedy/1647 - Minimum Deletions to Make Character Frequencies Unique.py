#1st Approach:
# Time: O(n): Iterate through array
# Space: O(n) -> O(1): Map every single character to frequency, but only 26 characters so O(1)

import collections

class Solution:
    def minDeletions(self, s: str) -> int:
        count = collections.Counter(s)
        used_freq = set()
        res = 0

        for c, freq in count.items():
            while freq > 0 and freq in used_freq:
                freq -= 1
                res += 1

            used_freq.add(freq)  # freq = either unique or 0

        return res

# Voorbeeldgebruik
solution = Solution()
s_example = "aaabbbcccc"
result = solution.minDeletions(s_example)
print(result)