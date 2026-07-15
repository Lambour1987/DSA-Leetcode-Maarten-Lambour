#1st Approach: Two Pointers: Previous & Current
# Time:
# Space:

class ListNode:
  def __init__(self, val=0, next=None):
      self.val = val
      self.next = next

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        dummy = ListNode(next=head)
        prev, curr = dummy, head

        while curr:
            nxt = curr.next

            if curr.val == val:
                prev.next = nxt
            else:
                prev = curr

            curr = nxt
        return dummy.next


# Voorbeeldgebruik:
# Maak een gekoppelde lijst: 1 -> 2 -> 6 -> 3 -> 4 -> 5 -> 6
head = ListNode(1, ListNode(2, ListNode(6, ListNode(3, ListNode(4, ListNode(5, ListNode(6)))))))

# Maak een instantie van de Solution klasse
oplossing = Solution()

# Verwijder alle knooppunten met de waarde 6 uit de gekoppelde lijst
nieuw_hoofd = oplossing.removeElements(head, 6)

# Print de aangepaste gekoppelde lijst
while nieuw_hoofd:
    print(nieuw_hoofd.val, end=" ")
    nieuw_hoofd = nieuw_hoofd.next
