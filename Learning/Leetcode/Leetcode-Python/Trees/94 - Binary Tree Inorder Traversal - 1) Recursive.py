#1st Approach: Recursive, zonder call stack?
# Time: O(n)
# Space: O(n) -> Because of Function Call Stack


from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val #waarde van het knooppunt
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> list[int]:
        res = [] #global variable

        def inorder(root):
            if not root: #basecase. If root does not exist, return
                return
            inorder(root.left) #eerst links
            res.append(root.val) #toevoegen aan resultaat
            inorder(root.right) #dan rechter root
        inorder(root) #functie wordt weer aangeroepen
        return res

example_tree = TreeNode(1)
example_tree.left = TreeNode(2)
example_tree.right = TreeNode(3)

solution = Solution()
result = solution.inorderTraversal(example_tree)
print(result)