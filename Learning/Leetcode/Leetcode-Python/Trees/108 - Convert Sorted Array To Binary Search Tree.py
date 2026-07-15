class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sortedArrayToBST(self, nums: list[int]) -> TreeNode:


        def helper(l, r):
            if l > r:
                return None

            m = (l + r) // 2
            root = TreeNode(nums[m])
            root.left = helper(l, m - 1)
            root.right = helper(m + 1, r)
            return root

        return helper(0, len(nums) - 1)



# Maak een instantie van Solution
solution = Solution()

# Voorbeeld van een gesorteerde lijst
sorted_nums = [-10, -3, 0, 5, 9]

# Converteer de gesorteerde lijst naar een gebalanceerde zoekboom (BST)
result_tree = solution.sortedArrayToBST(sorted_nums)

# Functie om de diepte van de boom te berekenen (niet noodzakelijk voor de conversie)
def maxDepth(root: TreeNode) -> int:
    if not root:
        return 0
    left_depth = maxDepth(root.left)
    right_depth = maxDepth(root.right)
    return max(left_depth, right_depth) + 1

# Druk de gesorteerde lijst en de diepte van de geconverteerde BST af
print("Gesorteerde lijst:", sorted_nums)
print("Diepte van de BST:", maxDepth(result_tree))
