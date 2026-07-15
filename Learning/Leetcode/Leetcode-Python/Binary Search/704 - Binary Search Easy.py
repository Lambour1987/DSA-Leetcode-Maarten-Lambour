class Solution:
    def search(self, nums: list[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            m = l + ((r-1)//2)
            if nums[m] > target:
                r = m - 1
            elif nums[m] < target:
                l = m + 1
            else:
                return m
        return - 1

# Een instantie van de Solution-klasse maken
solution = Solution()

# Voorbeeldlijst en doelwit
voorbeeld_nums = [-1, 0, 3, 5, 9, 12]
doelwit = 9

# Testen van de search-methode
resultaat = solution.search(voorbeeld_nums, doelwit)
print(f"Het doelwit {doelwit} is op index: {resultaat}")