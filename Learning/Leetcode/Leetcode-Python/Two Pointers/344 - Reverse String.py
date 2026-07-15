#1st Approach: Iterative Solution: Two pointers
# Time: O(n) because we iterate through entire string
# Space: O(1) no extra space

#2nd Approach: Stack Solution: Stack Less efficient
# Time: O(n)
# Space: O(n)

#3nd Approach: Recursive Solution: Recursion on call stack
# Time: O(n)
# Space: O(n)

#swap. Zelf: deep copy?

from typing import List

# class Solution:
#     def reverseString(self, s: List[str]) -> None:
#         """
#         Do not return anything, modify s in-place instead
#         """
#         l, r = 0, len(s) - 1
#         while l < r:
#             s[l], s[r] = s[r], s[l]
#             l, r = l + 1, r - 1
#
# solution = Solution()
# my_list = ["a", "b", "c", "d"]
# solution.reverseString(my_list)
# print(my_list)

#2nd Approach
# from typing import List
#
# class Solution:
#     def reverseString(self, s: List[str]) -> None:
#         stack = []
#         for c in s:
#             stack.append(c)
#         i = 0
#         while stack:
#             s[i] = stack.pop()
#             i = i + 1
#
# solution = Solution()
# my_list = ["a", "b", "c", "d"]
# solution.reverseString(my_list)
# print(my_list)

#3nd Approach
from typing import List

class Solution:
    def reverseString(self, s: List[str]) -> None:
        def reverse(l, r):
            if l < r:
                s[l], s[r] = s[r], s[l]
                reverse(l + 1, r - 1)
        reverse(0, len(s)-1)

solution = Solution()
my_list = ["a", "b", "c", "d"]
solution.reverseString(my_list)
print(my_list)