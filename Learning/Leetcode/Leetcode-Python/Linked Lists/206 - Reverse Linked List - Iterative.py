#1st Approach: Iteratively: Tow Pointers: Current & Previous pointer
# Time: O(n)
# Space: O(1) -> Using pointers

#2nd Approach: Recursively
# Time:
# Space:

#1st Approach: Iteratively: Pointers

#Shift, current, previous, null node, head

# Defenition for singly linked list.
class ListNode:
  def __init__(self, val=0, next=None):
      self.val = val
      self.next = next

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev, curr = None, head

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev

# Example usage:
# Create a linked list: 1 -> 2 -> 3 -> 4 -> 5
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
solution = Solution()
reversed_head = solution.reverseList(head)

# Print the reversed linked list
while reversed_head:
    print(reversed_head.val, end=" ")
    reversed_head = reversed_head.next