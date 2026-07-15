#1st Approach: Hashset
# Time:
# Space:

from typing import Optional

#1st Approach: Hashset

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class SolutionHashset:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        visited_nodes = set()

        # Loop door de eerste lijst en voeg elk knooppunt toe aan de set
        while headA:
            visited_nodes.add(headA)
            headA = headA.next

        # Loop door de tweede lijst en kijk of een knooppunt al in de set zit
        while headB:
            if headB in visited_nodes:
                return headB
            headB = headB.next

        return None

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
solution_hashset = SolutionHashset()

# Roep de getIntersectionNode-functie aan voor beide benaderingen
result_hashset = solution_hashset.getIntersectionNode(listA, listB)

# Print de resultaten
if result_hashset:
    print(f"Intersectie gevonden met Hashset-benadering op knooppunt met waarde {result_hashset.val}")
else:
    print("Geen intersectie gevonden met Hashset-benadering")
