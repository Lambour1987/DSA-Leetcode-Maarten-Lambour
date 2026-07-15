#1st Approach: Bruteforce
# Time: O(n^3): n^2 substrings. decide if palindrome N^3
# Space:

#2nd Approach: Beide richtingen op bewegen
# Time: O (n^2)
# Space:

#Two pointers gebruiken. Increment count.

class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0

        for i in range(len(s)):
            res += self.countPali(s, i, i)
            res += self.countPali(s, i, i+1)

        return res

    def countPali(self, s, l, r):
        count = 0
        while l>=0 and r< len(s) and s[l] == s[r]:
            count += 1
            l -= 1
            r +=1
        return count


solution = Solution()
example_string = "abc"
result = solution.countSubstrings(example_string)
print(result)  # Output: 3 (palindromen: "a", "b", "c")