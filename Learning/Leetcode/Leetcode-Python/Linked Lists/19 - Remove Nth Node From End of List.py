#1st Approach:
# Time: O(n)
# Space:

class ListNode:
  def __init__(self, val=0, next=None):
      self.val = val
      self.next = next

class Solution:
    def removeNthFromEnd(self, head: ListNode, n:int) -> ListNode:
        dummy = ListNode(0, head)
        left = dummy
        right = head

        while n > 0 and right:
            right = right.next
            n-= 1

        while right:
            left = left.next
            right = right.next

        #delete
        left.next = left.next.next
        return dummy.next

# Voorbeeld gebruik van de removeNthFromEnd-functie
# Maak een gelinkte lijst: 1 -> 2 -> 3 -> 4 -> 5
gelinkte_lijst = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))

# Maak een instantie van de Solution-klasse
oplossing = Solution()

# Roep de removeNthFromEnd-functie aan om het 2e knooppunt vanaf het einde te verwijderen
aangepaste_lijst = oplossing.removeNthFromEnd(gelinkte_lijst, 2)

# Print de aangepaste gelinkte lijst
current = aangepaste_lijst
while current:
    print(current.val, end=" -> ")
    current = current.next