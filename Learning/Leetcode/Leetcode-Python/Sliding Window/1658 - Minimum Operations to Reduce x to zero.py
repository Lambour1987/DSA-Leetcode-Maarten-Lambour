class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:
        target = sum(nums) - x
        cur_sum = 0
        max_window = -1
        l = 0
        for r in range(len(nums)):
            cur_sum += nums[r]

            while l <= r and cur_sum > target:
                cur_sum -= nums[l]
                l += 1

            if cur_sum == target:
                max_window = max(max_window, r - l + 1)

        return -1 if max_window == -1 else len(nums) - max_window

# Een instantie van de Solution-klasse maken
solution = Solution()

# Voorbeeld lijst en doelwaarde
nums = [1, 1, 4, 2, 3]
x = 5

# De minOperations-methode aanroepen
result = solution.minOperations(nums, x)

# Het resultaat afdrukken
print(result)