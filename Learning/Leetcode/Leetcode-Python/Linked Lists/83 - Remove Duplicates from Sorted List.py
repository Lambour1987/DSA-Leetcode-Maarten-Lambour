#1st Approach:
# Time:
# Space:
from typing import Optional


class ListNode:
  def __init__(self, val=0, next=None):
      self.val = val
      self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head

        while cur:
            while cur.next and cur.next.val == cur.val:
                cur.next = cur.next.next
            cur = cur.next
        return head

# Voorbeeldgebruik:
# Maak een gekoppelde lijst: 1 -> 2 -> 3 -> 3 -> 4 -> 4 -> 5
head = ListNode(1, ListNode(2, ListNode(3, ListNode(3, ListNode(4, ListNode(4, ListNode(5)))))))

# Maak een instantie van de Solution klasse
oplossing = Solution()

# Verwijder duplicaten uit de gekoppelde lijst
aangepast_hoofd = oplossing.deleteDuplicates(head)

# Print de aangepaste gekoppelde lijst
while aangepast_hoofd:
    print(aangepast_hoofd.val, end=" ")
    aangepast_hoofd = aangepast_hoofd.next