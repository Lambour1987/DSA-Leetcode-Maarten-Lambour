#1st Approach: BruteForce
# Time:
# Space:

#2nd Approach: Greedy
# Time:
# Space:

class Solution:
    def canJump(self, nums: list[int]) -> bool:
        goal = len(nums)-1 #zelf bij andere LCs definieer je hier een poitner

        for i in range(len(nums)-1,-1,-1): #doorlopen range van rechts naar links met stappen van 1 (min 1)
            if i + nums[i] >=goal:
                goal = i

        return True if goal == 0 else False

solution = Solution()

# Voorbeeld 1
nums1 = [2, 3, 1, 1, 4]
result1 = solution.canJump(nums1)
print(result1)  # Output: True

# Voorbeeld 2
nums2 = [3, 2, 1, 0, 4]
result2 = solution.canJump(nums2)
print(result2)  # Output: False