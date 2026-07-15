#1st Approach:
# Time: O(sqrt(n))
# Space:

class Solution:
    def isPerfectSquare(self, num: int) -> bool:

        # O(sqrt(n))
        for i in range(1, num + 1):
            if i*i == num:
                return True
            if i*i > num:
                return False

        # O(logn)
        l, r = 1, num
        while l <= r:
            mid = (l + r) // 2
            if mid * mid > num:
                r = mid -1
            elif mid * mid < num:
                l = mid + 1
            else:
                return True
        return False

# Maak een instantie van Solution
solution = Solution()

# Voorbeeld 1
num1 = 16
result1 = solution.isPerfectSquare(num1)
print(f"Is {num1} een perfect vierkant? {result1}")  # Dit zou True moeten afdrukken

# Voorbeeld 2
num2 = 14
result2 = solution.isPerfectSquare(num2)
print(f"Is {num2} een perfect vierkant? {result2}")  # Dit zou False moeten afdrukken

# Voorbeeld 3
num3 = 25
result3 = solution.isPerfectSquare(num3)
print(f"Is {num3} een perfect vierkant? {result3}")  # Dit zou True moeten afdrukken