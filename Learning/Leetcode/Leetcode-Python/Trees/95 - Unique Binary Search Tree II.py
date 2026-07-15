#1st Approach:
# Time:
# Space:
from typing import Optional

from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        dp = {}

        def generate(left, right):
            if left > right:
                return [None]

            if (left, right) in dp:
                return dp[(left, right)]

            res = []
            for val in range(left, right + 1):
                for leftTree in generate(left, val - 1):
                    for rightTree in generate(val + 1, right):
                        root = TreeNode(val, leftTree, rightTree)
                        res.append(root)

            dp[(left, right)] = res
            return res

        if n == 0:
            return []

        return generate(1, n)


# Voorbeeldgebruik
solution = Solution()

# Genereer alle mogelijke unieke binaire zoekbomen met 3 knooppunten
result = solution.generateTrees(3)

# Hier kun je de gegenereerde binaire zoekbomen afdrukken of andere bewerkingen uitvoeren
for tree in result:
    print(tree)