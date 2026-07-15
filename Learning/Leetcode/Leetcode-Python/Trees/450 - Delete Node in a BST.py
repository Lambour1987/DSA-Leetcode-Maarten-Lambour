#1st Approach: Recursive, base case
# Time: O(2*h)
# Space:
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def deleteNode(self, root: Optional[TreeNode], key:int) -> Optional[TreeNode]:
        if not root:
            return root

        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        else:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left

            # Find the min from right subtree
            cur = root.right
            while cur.left:
                cur = cur.left
            root.val = cur.val
            root.right = self.deleteNode(root.right, cur.val)
        return root

# Functie om de inorder-traversie van de boom af te drukken
def inorder_traversal(node):
    if not node:
        return []
    return inorder_traversal(node.left) + [node.val] + inorder_traversal(node.right)

# Voorbeeldboom
#       5
#      / \
#     3   8
#    / \
#   2   4
root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(8)
root.left.left = TreeNode(2)
root.left.right = TreeNode(4)

# Maak een instantie van Solution
solution = Solution()

# Verwijder knoop met waarde 3
new_tree = solution.deleteNode(root, 3)

# Inorder-traversie van de oorspronkelijke en gewijzigde boom
print("Inorder-traversie van oorspronkelijke boom:", inorder_traversal(root))
print("Inorder-traversie van gewijzigde boom:", inorder_traversal(new_tree))