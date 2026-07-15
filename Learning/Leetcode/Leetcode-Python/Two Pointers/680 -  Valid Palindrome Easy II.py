#1st Approach:
# Time: O(n) -> 2N
# Space: Extra memory by using str and by reversing str

class Solution:
    def validPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1

        while l < r:
            if s[l] !=s[r]:
                skipL, skipR = s[l+1:r+1], s[l:r]
                return (skipL == skipR[::-1]
                or skipR == skipR[::-1])
            l, r = l + 1, r - 1

        return True

solution = Solution()
print(solution.validPalindrome("aba"))  # Output: True
print(solution.validPalindrome("abca"))  # Output: True
print(solution.validPalindrome("racecar"))  # Output: True
print(solution.validPalindrome("abc"))  # Output: False