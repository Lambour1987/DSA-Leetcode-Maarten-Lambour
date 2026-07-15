from typing import Optional


class ListNode:
  def __init__(self, val=0, next=None):
      self.val = val
      self.next = next

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

# Voorbeeldgebruik:
# Maak een gekoppelde lijst: 1 -> 2 -> 3 -> 4 -> 5
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))

# Maak een instantie van de Solution klasse
oplossing = Solution()

# Vind het middelste knooppunt in de gekoppelde lijst
middelste_knooppunt = oplossing.middleNode(head)

# Print het waarde van het middelste knooppunt
print(middelste_knooppunt.val)