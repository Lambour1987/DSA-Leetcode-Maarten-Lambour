#1st Approach: Recursive Solution
# Time:
# Space:

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)
        if val > root.val:
            root.right = self.insertIntoBST(root.right, val)
        else:
            root.left = self.insertIntoBST(root.left, val)
        return root

# Maak een instantie van Solution
solution = Solution()

# Voorbeeldboom
#       4
#      / \
#     2   7
#    / \
#   1   3
root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(7)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)

# Voeg een nieuwe knoop met waarde 5 toe aan de boom
new_val = 5
result_tree = solution.insertIntoBST(root, new_val)

# Functie om de inorder-traversie van de boom af te drukken
def inorder_traversal(node):
    if not node:
        return []
    return inorder_traversal(node.left) + [node.val] + inorder_traversal(node.right)

# Druk de inorder-traversie van de oorspronkelijke en gewijzigde boom af
print("Inorder-traversie van oorspronkelijke boom:", inorder_traversal(root))
print("Inorder-traversie van gewijzigde boom:", inorder_traversal(result_tree))