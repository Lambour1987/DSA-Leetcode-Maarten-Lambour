from typing import Optional

#Swap

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return None

        #swap the children
        tmp = root.left
        root.left = root.right
        root.right = tmp

        #Recursive invert subtrees
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root

# Voorbeeldgebruik
def print_tree_inorder(node):
    if node:
        print_tree_inorder(node.left)
        print(node.val, end=" ")
        print_tree_inorder(node.right)

# Maak een voorbeeldboom
example_tree = TreeNode(1)
example_tree.left = TreeNode(2)
example_tree.right = TreeNode(3)
example_tree.left.left = TreeNode(4)
example_tree.left.right = TreeNode(5)

# Maak een instantie van de Solution-klasse
solution = Solution()

# Omgekeerde boom verkrijgen
inverted_tree = solution.invertTree(example_tree)

# Inorder afdrukken van de originele boom
print("Inorder van originele boom:")
print_tree_inorder(example_tree)
print()

# Inorder afdrukken van de omgekeerde boom
print("Inorder van omgekeerde boom:")
print_tree_inorder(inverted_tree)