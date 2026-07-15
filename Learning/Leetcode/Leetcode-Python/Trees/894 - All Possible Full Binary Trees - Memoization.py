from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def allPossibleFBT(self, n:int) -> list[Optional[TreeNode]]:
        dp = {}  # map n: list of FBT

        # Return de lijst van FBT's met n nodes
        def backtrack(n):
            if n == 0:
                return []
            if n == 1:
                return [TreeNode()]

            res = []
            for l in range(n):  # 0 - (n-1)
                r = n - 1 - l
                leftTrees, rightTrees = backtrack(l), backtrack(r)

                for t1 in leftTrees:
                    for t2 in rightTrees:
                        res.append(TreeNode(0, t1, t2))
            return res

        return backtrack(n)

# Voorbeeldgebruik
solution = Solution()

# Genereer alle mogelijke volledige binaire bomen (FBT) met 3 knooppunten
result = solution.allPossibleFBT(3)

# Hier kun je de gegenereerde FBT's afdrukken of andere bewerkingen uitvoeren
for tree in result:
    # Hier afdrukken van de waarden van de knooppunten
    def print_tree(node):
        if node:
            print_tree(node.left)
            print(node.val)
            print_tree(node.right)

    print_tree(tree)
    print("------")