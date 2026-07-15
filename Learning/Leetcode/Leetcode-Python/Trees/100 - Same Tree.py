#1st Approach: DFS, Recursive
# Time: O(p+q)
# Space:

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:
            return True
        if not p or not q or p.val != q.val:
            return False

        return (self.isSameTree(p.left, q.left) and
                self.isSameTree(p.right, q.right))


# Maak een instantie van Solution
solution = Solution()

# Voorbeeldboom 1
#       1
#      / \
#     2   3
tree1 = TreeNode(1)
tree1.left = TreeNode(2)
tree1.right = TreeNode(3)

# Voorbeeldboom 2 (identiek aan boom 1)
#       1
#      / \
#     2   3
tree2 = TreeNode(1)
tree2.left = TreeNode(2)
tree2.right = TreeNode(3)

# Voorbeeldboom 3 (verschillend van boom 1)
#       1
#        \
#         2
#          \
#           3
tree3 = TreeNode(1)
tree3.right = TreeNode(2)
tree3.right.right = TreeNode(3)

# Test identieke bomen
result1 = solution.isSameTree(tree1, tree2)
print(f"Zijn boom 1 en boom 2 identiek? {result1}")  # Dit zou True moeten afdrukken

# Test verschillende bomen
result2 = solution.isSameTree(tree1, tree3)
print(f"Zijn boom 1 en boom 3 identiek? {result2}")  # Dit zou False moeten zijn