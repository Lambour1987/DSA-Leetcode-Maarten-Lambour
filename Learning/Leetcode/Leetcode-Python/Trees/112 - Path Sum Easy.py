#1st Approach: helper funtion DFS
# Time: O(n) where n nodes in tree
# Space: wc O(n) where n is height or O(log n) bij balanced tree

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:


        def dfs(node, curSum):
            if not node:
                return

            curSum += node.val
            if not node.left and not node.right:
                return curSum == targetSum

            return (dfs(node.left, curSum) or
                    dfs(node.right, curSum))

        return dfs(root, 0)


# Maak een instantie van Solution
solution = Solution()

# Voorbeeldboom
#       5
#      / \
#     4   8
#    /   / \
#   11  13  4
#  /  \      \
# 7    2      1
root = TreeNode(5)
root.left = TreeNode(4)
root.right = TreeNode(8)
root.left.left = TreeNode(11)
root.left.left.left = TreeNode(7)
root.left.left.right = TreeNode(2)
root.right.left = TreeNode(13)
root.right.right = TreeNode(4)
root.right.right.right = TreeNode(1)

# Test of er een pad is met de som gelijk aan 22
target_sum = 22
result = solution.hasPathSum(root, target_sum)
print(f"Heeft de boom een pad met de som van {target_sum}? {result}")  # Dit zou True moeten afdrukken