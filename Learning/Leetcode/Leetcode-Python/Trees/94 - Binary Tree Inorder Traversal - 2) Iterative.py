#2nd Approach: Iterative, call stack
# Time:
# Space:

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> list[int]:
        res = []
        stack = []
        cur = root

        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            res.append(cur.val)
            cur = cur.right
        return res

example_tree = TreeNode(1)
example_tree.left = TreeNode(2)
example_tree.right = TreeNode(3)

solution = Solution()
result = solution.inorderTraversal(example_tree)
print(result)