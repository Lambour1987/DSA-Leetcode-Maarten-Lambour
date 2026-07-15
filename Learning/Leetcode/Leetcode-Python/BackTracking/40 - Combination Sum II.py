#1st Approach:
# Time:
# Space:

#2nd Approach:
# Time:
# Space:

class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        candidates.sort()
        res = []

        def backtrack(cur, pos, target):
            if target == 0:
                res.append(cur.copy())
            if target <= 0:
                return

            prev = -1
            for i in range(pos, len(candidates)):
                if candidates[i] == prev:
                    continue
                cur.append(candidates[i])
                backtrack(cur, i +1, target - candidates[i])
                cur.pop()
                prev = candidates[i]

        backtrack([], 0, target)
        return res

# Voorbeeldgebruik
solution = Solution()
candidates_list = [10,1,2,7,6,1,5]
target_value = 8
result = solution.combinationSum2(candidates_list, target_value)
print(result)