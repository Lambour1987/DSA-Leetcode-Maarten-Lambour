class NumArray:

    def __init__(self, nums: list[int]):
        self.prefix = []
        cur = 0
        for n in nums:
            cur += n
            self.prefix.append(cur)

    def sumRange(self, left: int, right: int) -> int:
        rightSum = self.prefix[right]
        leftSum = self.prefix[left-1] if left > 0 else 0
        return rightSum - leftSum

# Voorbeeld
nums = [-2, 0, 3, -5, 2, -1]
numArray = NumArray(nums)

# Het bereikssom oproepen
result = numArray.sumRange(0, 2)
print(result)  # Het resultaat zou 1 moeten zijn, omdat nums[0] + nums[1] + nums[2] = -2 + 0 + 3 = 1