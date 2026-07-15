#1st Approach:
# Time: O(n)
# Space: (1)


from typing import Optional

class ListNode:
  def __init__(self, val=0, next=None):
      self.val = val
      self.next = next

class Solution:
    def swapNodes(self, head: Optional[ListNode], k:int) -> Optional[ListNode]:
        cur = head
        for i in range(k-1):
            cur = cur.next

        left = cur
        right = head
        while cur.next:
            cur = cur.next
            right = right.next
        left.val, right.val = right.val, left.val

        # Voorkom dat left en right dezelfde knooppunt zijn (zelf 3/12/23: door chat gpt erbij gezet)
        if left != right:
            left.val, right.val = right.val, left.val
        return head


# Voorbeeld gebruik van de swapNodes-functie
# Maak een gelinkte lijst: 1 -> 2 -> 3 -> 4 -> 5
gelinkte_lijst = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))

# Maak een instantie van de Solution-klasse
oplossing = Solution()

# Roep de swapNodes-functie aan om het eerste en het laatste knooppunt te verwisselen
aangepaste_lijst = oplossing.swapNodes(gelinkte_lijst, 2)

# Print de aangepaste gelinkte lijst
current = aangepaste_lijst
while current:
    print(current.val, end=" -> ")
    current = current.next