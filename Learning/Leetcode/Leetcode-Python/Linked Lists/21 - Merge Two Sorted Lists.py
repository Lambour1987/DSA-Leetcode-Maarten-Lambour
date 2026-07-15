#1st Approach:
# Time:
# Space:

#Dummy Node

class ListNode:
  def __init__(self, val=0, next=None):
      self.val = val
      self.next = next

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode()
        tail = dummy

        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next

        if l1:
            tail.next = l1
        elif l2:
            tail.next = l2

        return dummy.next

# Voorbeeldgebruik:
# Maak twee gesorteerde lijsten: 1 -> 3 -> 5 en 2 -> 4 -> 6
l1 = ListNode(1, ListNode(3, ListNode(5)))
l2 = ListNode(2, ListNode(4, ListNode(6)))

# Maak een instantie van de Solution klasse
oplossing = Solution()

# Voeg de twee gesorteerde lijsten samen
samengevoegd_hoofd = oplossing.mergeTwoLists(l1, l2)

# Print de samengevoegde lijst
while samengevoegd_hoofd:
    print(samengevoegd_hoofd.val, end=" ")
    samengevoegd_hoofd = samengevoegd_hoofd.next