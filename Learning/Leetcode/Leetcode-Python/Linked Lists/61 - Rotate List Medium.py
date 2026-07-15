#1st Approach:
# Time:
# Space:

class ListNode:
  def __init__(self, val=0, next=None):
      self.val = val
      self.next = next

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return head

        #Get length
        length, tail = 1, head
        while tail.next:
            tail = tail.next
            length += 1

        k = k % length
        if k == 0:
            return head

        # Move to the pivot and rotate
        cur = head
        for i in range(length - k - 1):
            cur = cur.next
        newHead = cur.next
        cur.next = None
        tail.next = head
        return newHead


# Voorbeeld van een gelinkte lijst: 1 -> 2 -> 3 -> 4 -> 5
gelinkte_lijst = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))

# Maak een instantie van de Solution-klasse
oplossing = Solution()

# Roep de rotateRight-methode aan om de gelinkte lijst naar rechts te roteren met k=2
geroteerde_lijst = oplossing.rotateRight(gelinkte_lijst, 2)

# Print de geroteerde gelinkte lijst
current = geroteerde_lijst
while current:
    print(current.val, end=" -> ")
    current = current.next