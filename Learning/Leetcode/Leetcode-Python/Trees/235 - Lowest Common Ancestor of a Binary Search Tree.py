class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        cur = root

        while cur:
            if p.val > cur.val and q.val > cur.val:
                cur = cur.right
            elif p.val < cur.val and q.val < cur.val:
                cur = cur.left
            else:
                return cur

# Maak een instantie van Solution
solution = Solution()

# Voorbeeldboom
#       6
#      / \
#     2   8
#    / \ / \
#   0  4 7  9
#     / \
#    3   5
root = TreeNode(6)
root.left = TreeNode(2)
root.right = TreeNode(8)
root.left.left = TreeNode(0)
root.left.right = TreeNode(4)
root.right.left = TreeNode(7)
root.right.right = TreeNode(9)
root.left.right.left = TreeNode(3)
root.left.right.right = TreeNode(5)

# Zoek het laagste gemeenschappelijke voorouder van 2 en 8
p_node = root.left  # knoop met waarde 2
q_node = root.right  # knoop met waarde 8
result = solution.lowestCommonAncestor(root, p_node, q_node)
print(f"Het laagste gemeenschappelijke voorouder van {p_node.val} en {q_node.val} is: {result.val}")