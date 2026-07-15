#1st Approach:
# Time: O(n^2)
# Space:

#remainder
#Subarrays: Try every subarray
#Sliding window werkt niet goed
#Oplossing. Mod per subarray en tel restwaarden op die gelijk aan k zou zijn

class Solution:
    def checkSubarraySum(self, nums: list[int], k:int) -> bool:
        remainder = {0: -1} # map remainder -> end index
        total = 0

        for i, n in enumerate(nums):
            total += n
            r = total % k
            if r not in remainder:
                remainder[r] = i
            elif i - remainder[r] > 1:
                return True


# Voorbeeldgebruik:
nums_example1 = [23, 2, 4, 6, 7]
k_example1 = 6
solution_instance = Solution()
result1 = solution_instance.checkSubarraySum(nums_example1, k_example1)
print(f"Heeft een subarray met een som die een veelvoud is van {k_example1}: {result1}")

nums_example2 = [23, 2, 6, 4, 7]
k_example2 = 8
result2 = solution_instance.checkSubarraySum(nums_example2, k_example2)
print(f"Heeft een subarray met een som die een veelvoud is van {k_example2}: {result2}")