#1st Approach: Bruteforce (start helemaal links en helemaal rechts)
# Time: O(n^3): n * n^2
# Space:

class Solution:
    def longestPalindrome(self, s: str) -> str:
        def is_palindrome(substring):
            return substring == substring[::-1]#alle elementen van begin ':' tot eind ':' met stappen van minus 1, maar omgekeerd

        res = ""
        resLen = 0

        for i in range(len(s)):
            for j in range(i, len(s)):
                substring = s[i:j+1] # dus vanaf i t/m j met stappen van 1
                if is_palindrome(substring) and len(substring) > resLen:
                    res = substring
                    resLen = len(substring)

        return res

solution = Solution()
example_string = "babad"
result = solution.longestPalindrome(example_string)
print(result)  # Output: "bab" or "aba"