#1st Approach: BFS
# Time: O(N)
# Space:

import collections

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root:TreeNode) -> list[list[int]]:
        res = []

        q = collections.deque() #dit geeft ons een queue
        q.append(root) #hier beginnen we onze queue mee. met de rootnode

        while q: #run BFS terwijl queue niet leeg is
            qLen = len(q)
            level = []
            for i in range(qLen):
                node = q.popleft()
                if node:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if level:
                res.append(level)

        return res

# Voorbeeldboom
#       3
#      / \
#     9   20
#        /  \
#       15   7
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

# Maak een instantie van Solution
solution = Solution()

# Roep de levelOrder-methode aan om de niveaureeksen te verkrijgen
resultaat = solution.levelOrder(root)

# Druk het resultaat af
print("Niveaureeksen van de boom:")
for niveau, waarden in enumerate(resultaat, 1):
    print(f"Niveau {niveau}: {waarden}")