#2nd Approach: Pointer & Ascii Code. Shift pointers by increment or decrement pointers. Pointer passes.
# Time:
# Space:

#Zelf: Bucket?


class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s)-1

        while l < r:
            while l < r and not self.alphaNum(s[l]):
                l += 1
            while r > l and not self.alphaNum(s[r]):
                r -= 1
            if s[l].lower() != s[r].lower():
                return False

            l, r = l + 1, r -1
        return True


    def alphaNum(self, c):
        return ('A' <= c <= 'Z') or \
               ('a' <= c <= 'z') or \
               ('0' <= c <= '9')

# Voorbeeld van gebruik:
solution = Solution()
print(solution.isPalindrome("A man, a plan, a canal: Panama")) # Output: True
print(solution.isPalindrome("race a car")) # Output: False
print(solution.isPalindrome("Able was I ere I saw Elba"))  # Output: True