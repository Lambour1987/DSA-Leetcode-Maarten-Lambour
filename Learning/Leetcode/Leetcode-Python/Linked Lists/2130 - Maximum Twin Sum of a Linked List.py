#1st Approach:
# Time:
# Space:

from typing import Optional

class ListNode:
  def __init__(self, val=0, next=None):
      self.val = val
      self.next = next

class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow, fast = head, head
        prev = None
        while fast and fast.next:
            fast = fast.next.next
            tmp = slow.next
            slow.next = prev
            prev = slow
            slow = tmp

        res = 0
        while slow and prev:
            res = max(res, prev.val + slow.val)
            prev = prev.next
            slow = slow.next

        return res


# Voorbeeld gebruik van de pairSum-functie
# Maak een gelinkte lijst: 1 -> 2 -> 3 -> 4 -> 5
gelinkte_lijst = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))

# Maak een instantie van de Solution-klasse
oplossing = Solution()

# Roep de pairSum-functie aan
resultaat = oplossing.pairSum(gelinkte_lijst)

# Print het resultaat
print("Maximale paar som:", resultaat)