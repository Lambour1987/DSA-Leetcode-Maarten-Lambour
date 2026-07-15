#1st Approach: Array
# Time: O(n)
# Space: O(n)

class ListNode:
  def __init__(self, val=0, next=None):
      self.val = val
      self.next = next


class Solution:
    def isPalindrome(self, head:ListNode) -> bool:
        nums = []

        while head:
            nums.append(head.val)
            head = head.next

        l, r = 0, len(nums) - 1
        while l <= r:
            if nums[l] != nums[r]:
                return False
            l += 1
            r -= 1
        return True

# Voorbeeldgebruik:
# Maak een palindroom gekoppelde lijst: 1 -> 2 -> 3 -> 2 -> 1
palindroom_lijst = ListNode(1, ListNode(2, ListNode(3, ListNode(2, ListNode(1)))))

# Maak een instantie van de Solution klasse
oplossing = Solution()

# Controleer of de gekoppelde lijst een palindroom is
resultaat = oplossing.isPalindrome(palindroom_lijst)

# Print het resultaat
print(resultaat)  # Dit zou True moeten zijn, omdat de lijst een palindroom is