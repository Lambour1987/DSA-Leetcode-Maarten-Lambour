#2st Approach: Recursive DFS
# Time:

#Update Boundaries

from typing import Optional




class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val #waarde van het knooppunt
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:

        def valid(node, left, right):
            if not node:
                return True

            if not (node.val < right and node.val > left):
                return False

            return (valid(node.left, left, node.val) and
                    valid(node.right, node.val, right))
        return valid(root, float("-inf"), float("inf"))

# Een voorbeeld van een geldige BST:
#       2
#      / \
#     1   3
root_valid = TreeNode(2)
root_valid.left = TreeNode(1)
root_valid.right = TreeNode(3)

# Een voorbeeld van een ongeldige BST:
#       5
#      / \
#     1   4
#        / \
#       3   6
root_invalid = TreeNode(5)
root_invalid.left = TreeNode(1)
root_invalid.right = TreeNode(4, left=TreeNode(3), right=TreeNode(6))

solution = Solution()

# Controleren of de BST geldig is
print(solution.isValidBST(root_valid))    # Output: True
print(solution.isValidBST(root_invalid))  # Output: False