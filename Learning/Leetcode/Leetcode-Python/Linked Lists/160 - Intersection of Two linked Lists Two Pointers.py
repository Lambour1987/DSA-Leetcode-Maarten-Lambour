#2nd Approach: Two pointers
# Time: O(n+m)
# Space: O(1)
from typing import Optional


#2nd Approach: Two pointers

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        l1, l2 = headA, headB
        while l1 !=l2:
            l1 = l1.next if l1 else headB
            l2 = l2.next if l2 else headA
        return l1

# Voorbeelduitwerking
# Creëer gekoppelde lijsten
listA = ListNode(1)
listA.next = ListNode(2)
listA.next.next = ListNode(8)
listA.next.next.next = ListNode(9)
listA.next.next.next.next = ListNode(10)

listB = ListNode(3)
listB.next = listA.next.next  # Verbind met knooppunt 8 in lijst A

# Maak instanties van de Solution-klassen
solution_two_pointers = Solution()

# Roep de getIntersectionNode-functie aan voor beide benaderingen
result_two_pointers = solution_two_pointers.getIntersectionNode(listA, listB)

# Print de resultaten
if result_two_pointers:
    print(f"Intersectie gevonden met Two Pointers-benadering op knooppunt met waarde {result_two_pointers.val}")
else:
    print("Geen intersectie gevonden met Two Pointers-benadering")