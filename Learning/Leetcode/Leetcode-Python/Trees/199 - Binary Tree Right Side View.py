#1st Approach: Recursive, basecase
# Time:
# Space:
import collections


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rightSideView(self, root: TreeNode) -> list[int]:
        res = []
        q = collections.deque([root])

        while q:
            rightSide = None
            qLen = len(q)

            for i in range(qLen):
                node = q.popleft()
                if node:
                    rightSide = node
                    q.append(node.left)
                    q.append(node.right)
            if rightSide:
                res.append(rightSide.val)
        return res

# Voorbeeldboom
#       1
#      / \
#     2   3
#      \
#       5
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.right = TreeNode(5)

# Maak een instantie van Solution
solution = Solution()

# Roep de rightSideView-methode aan om de waarden aan de rechterkant te verkrijgen
resultaat = solution.rightSideView(root)

# Druk het resultaat af
print("Waarden aan de rechterkant van elk niveau:")
print(resultaat)
