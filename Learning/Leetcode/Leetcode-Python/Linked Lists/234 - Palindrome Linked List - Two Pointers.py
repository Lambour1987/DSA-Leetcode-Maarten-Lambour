#2nd Approach: Slow & Fase Pointers
# Time: O(n)
# Space: O(1)

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def Palindrome(self, head: ListNode) -> bool:
        fast = head
        slow = head

        # find middle(slow)
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        # reverse second half
        prev = None
        while slow:
            tmp = slow.next
            slow.next = prev
            prev = slow
            slow = tmp

        # check palindrome
        left, right = head, prev
        while right:
            if left.val !=right.val:
                return False
            left = left.next
            right = right.next

# Example usage:
# Create a palindrome linked list: 1 -> 2 -> 3 -> 2 -> 1
palindrome_list = ListNode(1, ListNode(2, ListNode(3, ListNode(2, ListNode(1)))))

# Create an instance of the Solution class
solution = Solution()

# Check if the linked list is a palindrome
result = solution.Palindrome(palindrome_list)

# Print the result
print(result)  # This should print True, as the list is a palindrome