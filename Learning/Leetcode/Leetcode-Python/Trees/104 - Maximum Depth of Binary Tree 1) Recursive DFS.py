#1st Approach: Recursive Depth First Search
# Time: wc O(n)
# Space:
from idlelib.tree import TreeNode

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0

        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))


# Definieer de TreeNode-klasse
class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

# Maak een instantie van Solution
solution = Solution()

# Voorbeeldboom
#       3
#      / \
#     9  20
#        / \
#       15  7
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

# Bereken de maximale diepte van de boom
result = solution.maxDepth(root)
print(f"De maximale diepte van de boom is: {result}")  # Dit zou 3 moeten