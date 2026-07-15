#1st Approach: Pointers
# Time: O(n)
# Space:

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        dummy = ListNode(0, head)
        prev, curr = dummy, head

        while curr and curr.next:
            # save ptrs
            nxtPair = curr.next.next
            second = curr.next

            #reverse this pair
            second.next = curr
            curr.next = nxtPair
            prev.next = second

            # update ptrs
            prev = curr
            curr = nxtPair

        return dummy.next

# Voorbeeld van een gelinkte lijst: 1 -> 2 -> 3 -> 4
gelinkte_lijst = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))

# Maak een instantie van de Solution-klasse
oplossing = Solution()

# Roep de swapPairs-functie aan
aangepaste_lijst = oplossing.swapPairs(gelinkte_lijst)

# Print de aangepaste gelinkte lijst
current = aangepaste_lijst
while current:
    print(current.val, end=" -> ")
    current = current.next