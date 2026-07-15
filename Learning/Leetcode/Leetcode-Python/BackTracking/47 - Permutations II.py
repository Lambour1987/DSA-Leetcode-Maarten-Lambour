#1st Approach:
# Time:
# Space:

#2nd Approach:
# Time:
# Space:

#3nd Approach:
# Time:
# Space:


class Solution:
    def permuteUnique(self, nums: list[int]) -> list[list[int]]:
        res = []
        perm = []
        count = {n:0 for n in nums}
        for n in nums:
            count[n] += 1

        def dfs():
            if len (perm) == len(nums):
                res.append(perm.copy())
                return

            for n in count:
                if count[n] > 0:
                    perm.append(n)
                    count[n] -= 1

                    dfs() #zelf: recursive call dfs again

                    count[n] += 1
                    perm.pop()

        dfs()
        return res

# Een instantie van de Solution-klasse maken
solution = Solution()

# Voorbeeld van het genereren van unieke permutaties voor nums = [1, 1, 2]
nums = [1, 1, 2]
resultaat = solution.permuteUnique(nums)
print(f"Unieke permutaties voor {nums}: {resultaat}")