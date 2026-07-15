#1st Approach:
# Time:
# Space:
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        prev, res = None, float("inf")

        def dfs(node):
            if not node:
                return

            dfs(node.left)
            nonlocal prev, res
            if prev:
                res = min(res, node.val - prev.val)
            prev = node

            dfs(node.right)
        dfs(root)
        return res

# Voorbeeldboom
#       4
#      / \
#     2   6
#    / \
#   1   3
root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(6)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)

# Maak een instantie van Solution
solution = Solution()

# Roep de minDiffInBST-methode aan om het minimale verschil te verkrijgen
resultaat = solution.minDiffInBST(root)

# Druk het resultaat af
print("Minimaal verschil tussen knopen in de BST:", resultaat)