#1st Approach: Brute Force: Triple Loop
# Time: O(n^3)
# Space:

#2nd Approach: Sort, Hashset (zelf; als input niet gesorteerd is)
# Time: O(n logn) + O(n^2) -> O(n^2). Dus
# Space: O(1) of O(n). Hangt van library af. sorteren kan O(n) zijn.

#3nd Approach: Two Pointers (zelf: als input wel gesorteerd is)
# Time:
# Space:

#Wat is handiger: sorteren en two pointers of niet sorteren en hashmap

class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        res = [] #dus een list als output
        nums.sort()

        for i, a in enumerate(nums):
            if i > 0 and a == nums[i-1]:
                continue #dit stuk voorkomt duplicates

            l, r = i + 1, len(nums) -1 #initialiseer pointers
            while l < r:
                threeSum = a + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l-1] and l <r:
                        l += 1
        return res

# Een instantie van de Solution-klasse maken
solution = Solution()

# Voorbeeldlijst
nums = [-1, 0, 1, 2, -1, -4]

# Testen van de threeSum-methode
resultaat = solution.threeSum(nums)
print(f"Unieke tripletten met som gelijk aan nul: {resultaat}")