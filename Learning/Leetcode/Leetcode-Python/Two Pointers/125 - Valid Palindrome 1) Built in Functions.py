#1st Approach: 'cheat' function uses lot of build in functions
# Time:
# Space: Extra memory by creating new str and by reversing str

class Solution:
    def isPalindrome(self,s: str) ->bool:
        newstr = "" #removes al non alpha characters (maar kost extra space)

        for c in s:
            if c.isalnum(): #build in function. Heeft string alpha numerical strings
                newstr += c.lower() # convert to lowercase.
        return newstr == newstr[::-1] # is nieuwe string gelijk aan gereverde string. Reverse: [::-1]

solution = Solution()
print(solution.isPalindrome("A man, a plan, a canal: Panama"))  # Output: True
print(solution.isPalindrome("race a car"))  # Output: False