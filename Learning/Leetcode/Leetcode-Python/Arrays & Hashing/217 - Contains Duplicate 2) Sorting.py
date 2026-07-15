#2nd Approach: Sorting (ChatGPT)
# Time: O(n) -> (1 pass)
# Space: O(nlogn): Sorting. Voor de rest O(1) (dus geen extra space behalve het sorteren)

class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        nums.sort() #sorteren

        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                return True
        return False

solution_instance = Solution()
example_nums = [1,2,3,4,1]
result = solution_instance.containsDuplicate(example_nums)
print(result)