#1st Approach: Recursive, basecase
# Time:
# Space:

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if not t1 and not t2:
            return None

        v1 = t1.val if t1 else 0
        v2 = t2.val if t2 else 0
        root = TreeNode(v1 + v2)

        root.left = self.mergeTrees(t1.left if t1 else None, t2.left if t2 else None)

        root.right = self.mergeTrees(t1.right if t1 else None, t2.right if t2 else None)

        return root

# Maak een instantie van Solution
solution = Solution()

# Voorbeeldbomen
# Boom 't1'
#       1
#      / \
#     3   2
#    /
#   5
t1 = TreeNode(1)
t1.left = TreeNode(3)
t1.right = TreeNode(2)
t1.left.left = TreeNode(5)

# Boom 't2'
#       2
#      / \
#     1   3
#      \
#       4
t2 = TreeNode(2)
t2.left = TreeNode(1)
t2.right = TreeNode(3)
t2.left.right = TreeNode(4)

# Voeg de bomen samen
result_tree = solution.mergeTrees(t1, t2)

# Functie om de diepte van de boom te berekenen (niet noodzakelijk voor de samenvoeging)
def maxDepth(root: TreeNode) -> int:
    if not root:
        return 0
    left_depth = maxDepth(root.left)
    right_depth = maxDepth(root.right)
    return max(left_depth, right_depth) + 1

# Druk de samengevoegde boom en de diepte ervan af
print("Diepte van de samengevoegde boom:", maxDepth(result_tree))