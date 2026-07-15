#1st Approach: Hashset
# Time:
# Space:

class Solution:
    def partitionString(self, s: str) -> int:
        cur_set = set()
        res = 1

        for c in s:
            if c in cur_set:
                res += 1
                cur_set = set()
            cur_set.add(c)

        return res

# Voorbeeldgebruik:
example = Solution()
input_string = "abac"
result = example.partitionString(input_string)
print(result)