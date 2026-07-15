from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        res = []

        def preorder(root):
            if not root:
                return

            res.append("(")
            res.append(str(root.val))

            if not root.left and root.right:
                res.append("()")
            preorder(root.left)
            preorder(root.right)
            res.append(")")

        preorder(root)
        return "".join(res)[1:-1] #chop of first & last character


# Maak een instantie van Solution
solution = Solution()

# Voorbeeldboom
#       1
#      / \
#     2   3
#    /
#   4
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)

# Converteer de boom naar een string
result = solution.tree2str(root)
print("De geconverteerde string van de boom is:", result)