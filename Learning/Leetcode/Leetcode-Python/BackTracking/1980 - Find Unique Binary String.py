#1st Approach:
# Time:
# Space:

#2^n possibilities

class Solution:
    def findDifferentBinaryString(self, nums: list[str]) -> str:
        strSet = {s for s in nums}

        def backtrack(i, cur):
            if i == len(nums):
                res = "".join(cur)
                return None if res in strSet else res

            res = backtrack(i+1, cur)
            if res: return res

            cur[i] = "1"
            res = backtrack(i+1, cur)
            if res: return res


        return backtrack(0, ["0" for s in nums])


# Voorbeeldgebruik:
nums_example = ["00", "01", "10"]
solution_instance = Solution()
result = solution_instance.findDifferentBinaryString(nums_example)
print(f"Een binair getal dat verschilt van de gegeven lijst: {result}")