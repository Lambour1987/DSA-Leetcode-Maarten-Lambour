#1st Approach: More of a Medium Question
# Time: n(logn)? of O(logn?)
# Space:

class Solution:
    def arrangeCoins(self, n: int) -> int:
        l, r = 1, n
        res = 0

        while l <= r:
            mid = (l + r) // 2 #integer division
            coins = (mid / 2) * (mid + 1) #decimal division
            if coins > n:
                r = mid - 1
            else:
                l = mid + 1
                res = max(mid, res)
        return res
            



