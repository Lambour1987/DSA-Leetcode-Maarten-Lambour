#1st Approach: Array:
# Time:
# Space:

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right:int) -> Optional:
        dummy = ListNode(0, head)

        # 1) reach node at position "Left"
        leftPrev, cur = dummy, head
        for i in range(left - 1):
            leftPrev, cur = cur, cur.next

        # Now cur="left", leftPrev="node before left"
        # 2) reverse from left to right
        prev = None
        for i in range(right - left + 1):
            tmpNext = cur.next
            cur.next = prev
            prev, cur = cur, tmpNext

        # 3) Update pointers
        leftPrev.next.next = cur # cur is node after "right"
        leftPrev.next = prev # prev is "right"
        return dummy.next

# Voorbeeld van een gelinkte lijst: 1 -> 2 -> 3 -> 4 -> 5
gelinkte_lijst = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))

# Maak een instantie van de Solution-klasse
oplossing = Solution()

# Roep de reverseBetween-methode aan om knooppunten van positie 2 tot 4 om te keren
aangepaste_lijst = oplossing.reverseBetween(gelinkte_lijst, 2, 4)

# Print de aangepaste gelinkte lijst
current = aangepaste_lijst
while current:
    print(current.val, end=" -> ")
    current = current.next