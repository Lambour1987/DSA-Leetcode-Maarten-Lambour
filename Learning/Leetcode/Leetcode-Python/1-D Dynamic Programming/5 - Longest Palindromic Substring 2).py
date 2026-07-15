#2nd Approach: Start vanuit het midden naar links en rechts
# Time: O(n^2) -> n*n
# Space:

#3nd Approach:
# Time:
# Space:

class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        resLen = 0

        for i in range(len(s)):
            # odd lenght
            l, r = i, i #2 pointers, beide op i, wat het midden is
            while l >= 0 and r < len(s) and s[l] == s[r]: #dit laatste: s[l] == s[r]. Zolang de karakters van de string s links en rechts gelijk zijn.
                if (r - l + 1) > resLen: #lengte van een substring. Index begint bij 0 daarom '+1'
                    res = s[l:r+1]
                    resLen = r-l +1
                l -=1
                r +=1

            #even lenght
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r-l+1) > resLen:
                    res = s[l:r+1]
                    resLen = r-l+1
                l -= 1
                r +=1

        return res

solution = Solution()
example_string = "babad"
result = solution.longestPalindrome(example_string)
print(result)  # Output: "bab" or "aba"