#1st Approach:
# Time:
# Space:

from typing import Optional

#1st Approach: Hashset

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        left, right = ListNode(), ListNode()
        ltail, rtail = left, right

        while head:
            if head.val < x:
                ltail.next = head
                ltail = ltail.next
            else:
                rtail.next = head
                rtail = rtail.next
            head = head.next

        ltail.next = right.next
        rtail.next = None
        return left.next

# Voorbeeld van een gelinkte lijst: 1 -> 4 -> 3 -> 2 -> 5 -> 2
ongesorteerde_lijst = ListNode(1, ListNode(4, ListNode(3, ListNode(2, ListNode(5, ListNode(2))))))

# Maak een instantie van de Solution-klasse
oplossing = Solution()

# Roep de partition-methode aan
gepartitioneerde_lijst = oplossing.partition(ongesorteerde_lijst, 3)

# Print de gepartitioneerde gelinkte lijst
current = gepartitioneerde_lijst
while current:
    print(current.val, end=" -> ")
    current = current.next