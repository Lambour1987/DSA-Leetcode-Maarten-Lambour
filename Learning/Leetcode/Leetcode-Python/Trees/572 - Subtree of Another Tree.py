class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        if not t: return True
        if not s: return False

        if self.sameTree(s, t):
            return True

        return (self.isSubtree(s.left, t) or
                self.isSubtree(s.right, t))

    def sameTree(self, s, t):
        if not s and not t:
            return True

        if s and t and s.val == t.val:
            return (self.sameTree(s.left, t.left) and
                    self.sameTree(s.right, t.right))
        return False


# Maak een instantie van Solution
solution = Solution()

# Voorbeeldbomen
# Boom 's'
#       3
#      / \
#     4   5
#    / \
#   1   2
s = TreeNode(3)
s.left = TreeNode(4)
s.right = TreeNode(5)
s.left.left = TreeNode(1)
s.left.right = TreeNode(2)

# Boom 't' (een subboom van 's')
#     4
#    / \
#   1   2
t = TreeNode(4)
t.left = TreeNode(1)
t.right = TreeNode(2)

# Test of 't' een subboom is van 's'
result = solution.isSubtree(s, t)
print(f"Is 't' een subboom van 's'? {result}")  # Dit zou True moeten afdrukken
