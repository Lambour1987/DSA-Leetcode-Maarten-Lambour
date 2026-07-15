#1st Approach: Recursively
# Time: O(n)
# Space:
from idlelib.tree import TreeNode
from typing import Optional


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def dfs(root):
            if not root: return [True, 0]

            left, right = dfs(root.left), dfs(root.right)
            balanced = (left[0] and right[0] and
                       abs(left[1] - right[1]) <= 1)

            return [balanced, 1 + max(left[1], right[1])]

        return dfs(root)[0]

# Definieer de TreeNode-klasse
class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

# Maak een instantie van Solution
solution = Solution()

# Voorbeeldboom (gebalanceerd)
#       1
#      / \
#     2   3
#    / \
#   4   5
balanced_tree = TreeNode(1)
balanced_tree.left = TreeNode(2)
balanced_tree.right = TreeNode(3)
balanced_tree.left.left = TreeNode(4)
balanced_tree.left.right = TreeNode(5)

# Voorbeeldboom (ongebalanceerd)
#       1
#      /
#     2
#    /
#   3
unbalanced_tree = TreeNode(1)
unbalanced_tree.left = TreeNode(2)
unbalanced_tree.left.left = TreeNode(3)

# Test gebalanceerde boom
result_balanced = solution.isBalanced(balanced_tree)
print(f"Is de gegeven boom gebalanceerd? {result_balanced}")  # Dit zou True moeten afdrukken

# Test ongebalanceerde boom
result_unbalanced = solution.isBalanced(unbalanced_tree)
print(f"Is de gegeven boom gebalanceerd? {result_unbalanced}")  # Dit zou False moeten afdrukken