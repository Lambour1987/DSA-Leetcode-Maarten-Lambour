class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val #waarde van het knooppunt
        self.left = left
        self.right = right

from typing import Optional

class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.stack = []
        while root:
            self.stack.append(root)
            root = root.left

    def next(self) -> int:
        res = self.stack.pop()
        cur = res.right
        while cur:
            self.stack.append(cur)
            cur = cur.left
        return res.val

    def hasNexst(self) -> bool:
        return self.stack != []


# Definieer een paar knooppunten voor een eenvoudige binaire boom
node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)

# Stel de ouder-kindrelaties in om een eenvoudige boom te vormen:
#       1
#        \
#         2
#          \
#           3
node1.right = node2
node2.right = node3

# Je kunt nu deze boom traverseren of andere bewerkingen uitvoeren op basis van je behoeften.
# Bijvoorbeeld, je kunt de waarde van een knooppunt afdrukken:
print(node1.val)  # Output: 1

# Je kunt de kinderen van een knooppunt verkrijgen:
left_child = node2.left  # Dit zal None zijn, omdat we het niet hebben ingesteld

# Of je kunt de waarde van een kindknoop afdrukken als het bestaat:
if left_child:
    print(left_child.val)
else:
    print("Left child is None.")

# Als je de hele boom wilt afdrukken, kun je een diepte-eerste zoektocht (DFS) gebruiken:
def print_tree(node):
    if node:
        print_tree(node.left)
        print(node.val)
        print_tree(node.right)

print_tree(node1)
# Output:
# 1
# 2
# 3