#1st Approach: Recursive Problem, Basecase, Dynamic Programming
# Time: O(n^2):
# Space: O(n)

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val #waarde van het knooppunt
        self.left = left
        self.right = right

class Solution:
    def numTrees(self, n: int) -> int:
        # numTree[4] = numTree[0] * numTree[3] +
        #              numTree[1] * numTree[2] +
        #              numTree[2] * numTree[1] +
        #              numTree[3] * numTree[1]
        numTree = [1] * (n + 1)

        # 0 nodes = 1 tree
        # 1 nodes = 1 tree
        for nodes in range(2, n + 1):
            total = 0
            for root in range(1, nodes + 1):
                left = root - 1
                right = nodes - root
                total += numTree[left] * numTree[right]
            numTree[nodes] = total
        return numTree[n]


# Voorbeeldgebruik
solution = Solution()

# Aantal unieke binaire zoekbomen voor 3 knooppunten
result = solution.numTrees(3)
print(result)  # Output: 5

# Aantal unieke binaire zoekbomen voor 5 knooppunten
result = solution.numTrees(5)
print(result)  # Output: 42
