#1st Approach: Brute Force
# Time: O(n^2)
# Space: O(1)

#Zie LC 2BF, 217BF

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]: #of gewoon: def twoSum(self, nums, target):
        n = len(nums)

        for i in range(0, n): #zelf '0,' erbij gezet. Er staat dus for i in range(len(0, nums)).
            for j in range(i + 1, n): #i+1: beginnen met element na Huidige element (niet per se beginnen met het 2e element)
                if nums[i] + nums[j] == target:
                    return [i, j]

# Voorbeeldgebruik
solution_instance = Solution()
nums = [2, 7, 11, 15]
target = 9
result = solution_instance.twoSum(nums, target)
print(result)