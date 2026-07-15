from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> list[int]:
        stack = [root]
        visit = [False] #wel of niet bezocht door de poitner. Mogelijk wel in stack al opgenomen
        res = []

        while stack:
            cur, v = stack.pop(), visit.pop()
            if cur:
                if v:
                    res.append(cur.val)
                else:
                    stack.append(cur)
                    visit.append(True)
                    stack.append(cur.right)
                    visit.append(False)
                    stack.append(cur.left)
                    visit.append(False)
        return res


example_tree = TreeNode(1)
example_tree.left = TreeNode(2)
example_tree.right = TreeNode(3)
example_tree.left.left = TreeNode(4)
example_tree.left.right = TreeNode(5)

solution = Solution()
result = solution.postorderTraversal(example_tree)
print(result)  # Output: [4, 5, 2, 3, 1]