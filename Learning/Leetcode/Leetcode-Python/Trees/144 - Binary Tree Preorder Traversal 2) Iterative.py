#2st Approach:
# Time: O(n)
# Space:

#Pointer bijhouden
#Zelf: wat je doet; je doet pre- order: eerst linkerchild, dan rechter. en tegelijkertijd
#doe je een (call) stack bijhouden. dat is eerste de rechter child en dan de linker
#zie filmpje best lastig

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> list[int]:
        cur, stack = root, [] #current pointer verwijst naar root, stack is leeg
        res = [] #result is een lege array
        while cur or stack:
            if cur: #dus als cur niet nul is
                res.append(cur.val) #dan voeg je de waarde van de node toe waar de pointer op staat
                stack.append(cur.right) #daarnaast de rechterchild toevoegen aan de stack
                cur = cur.left #vervolgens naar de pointer naar de linkernode
            else:
                cur = stack.pop()
        return res

example_tree = TreeNode(1)
example_tree.left = TreeNode(2)
example_tree.right = TreeNode(3)
example_tree.left.left = TreeNode(4)
example_tree.left.right = TreeNode(5)

solution = Solution()
result = solution.preorderTraversal(example_tree)
print(result)  # Output: [1, 2, 4, 5, 3]