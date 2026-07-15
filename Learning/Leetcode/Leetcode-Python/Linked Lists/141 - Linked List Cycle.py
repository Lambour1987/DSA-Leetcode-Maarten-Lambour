#1st Approach:
# Time:
# Space:

from typing import Optional

#1st Approach:

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

# Voorbeeld van een gelinkte lijst met een lus
# 1 -> 2 -> 3 -> 4 -> 5 -> 6
#            ^         |
#            |_________|
gelinkte_lijst_met_lus = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)
node6 = ListNode(6)

gelinkte_lijst_met_lus.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6
node6.next = node3  # Lus gecreëerd

# Maak een instantie van de Solution-klasse
oplossing = Solution()

# Controleer of de gelinkte lijst een lus heeft
heeft_lus = oplossing.hasCycle(gelinkte_lijst_met_lus)

# Print het resultaat
print("Heeft de gelinkte lijst een lus:", heeft_lus)