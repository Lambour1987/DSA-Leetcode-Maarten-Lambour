class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0: return False

        div = 1
        while x > 10 * div:
            div *= 10

        while x:
            right = x % 10
            left = x // div

            if left != right: return False

            x = (x % div) // 10
            div = div / 100

        return True

# Een instantie van de Solution-klasse maken
solution = Solution()

# Voorbeeld van het controleren van een palindroom voor x = 121
x1 = 121
resultaat1 = solution.isPalindrome(x1)
print(f"Is {x1} een palindroom? {resultaat1}")

# Voorbeeld van het controleren van een palindroom voor x = -121
x2 = -121
resultaat2 = solution.isPalindrome(x2)
print(f"Is {x2} een palindroom? {resultaat2}")

# Voorbeeld van het controleren van een palindroom voor x = 10
x3 = 10
resultaat3 = solution.isPalindrome(x3)
print(f"Is {x3} een palindroom? {resultaat3}")
