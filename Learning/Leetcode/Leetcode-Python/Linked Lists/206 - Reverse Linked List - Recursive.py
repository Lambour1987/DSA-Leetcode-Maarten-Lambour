#2nd Approach: Recursively: Subproblem
# Time: O(n)
# Space: O(n)


#Recursive: in stead of reverse entire linked list. Reverse remainder of linked list.
#Subproblem.

class ListNode:
  def __init__(self, val=0, next=None):
      self.val = val
      self.next = next

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        # recursive: T O(n), M O(n)

        if not head:
            return None

        newHead = head
        if head.next:
            newHead = self.reverseList(head.next)
            head.next.next = head
        head.next = None
        return newHead

# Example usage:
# Create a linked list: 1 -> 2 -> 3 -> 4 -> 5
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))

# Create a solution instance
solution = Solution()

# Reverse the linked list
reversed_head = solution.reverseList(head)

# Print the reversed linked list
while reversed_head:
    print(reversed_head.val, end=" ")
    reversed_head = reversed_head.next


