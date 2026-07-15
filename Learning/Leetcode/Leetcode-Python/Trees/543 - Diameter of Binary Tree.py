from idlelib.tree import TreeNode


class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        res = [0]

        def dfs(root):
            if not root:
                return -1
            left = dfs(root.left)
            right = dfs(root.right)
            res[0] = max(res[0], 2 + left + right)

            return 1 + max(left, right)

        dfs(root)

        return res[0]

# Definieer de TreeNode-klasse

class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

# Maak een instantie van Solution
solution = Solution()

# Voorbeeldboom
#       1
#      / \
#     2   3
#    / \
#   4   5
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

# Bereken de diameter van de boom
result = solution.diameterOfBinaryTree(root)
print(f"De diameter van de boom is: {result}")