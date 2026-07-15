#1st Approach: Dutch Flag Algorime (chatgpt)
# Time:
# Space:

class Solution:
    def sortColors(self, nums: list[int]) -> None:

        l, r = 0, len(nums) -1
        i = 0

        def swap(i, j):
            tmp = nums[i] #opslaan in tijdelijke variabele
            nums[i] = nums[j] #dan nums op index j opslaan in index i
            nums[j] = tmp #dan tmp in j opslaan

        while i <= r:
            if nums[i] == 0:
                swap(l, i)
                l+= 1 #l = l+1
            elif nums[i] == 2:
                swap(i, r)
                r-= 1 #r = r-1
            i += 1

# Voorbeeld gebruik:
solution = Solution()
colors = [2, 0, 1, 2, 1, 0, 2, 1, 0]
solution.sortColors(colors)
print(colors)