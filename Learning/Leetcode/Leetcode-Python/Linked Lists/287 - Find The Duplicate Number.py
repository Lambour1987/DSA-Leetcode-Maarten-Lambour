#1st Approach: Tortoise & Haze
# Time: O(n)
# Space: O(1)

class ListNode:
  def __init__(self, val=0, next=None):
      self.val = val
      self.next = next

class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        slow, fast = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                break
        return slow

# Voorbeeld van een lijst met duplicaat: [1, 3, 4, 2, 2]
duplicaat_lijst = [1, 3, 4, 2, 2]

# Maak een instantie van de Solution-klasse
oplossing = Solution()

# Roep de findDuplicate-functie aan
duplicaat = oplossing.findDuplicate(duplicaat_lijst)

# Print het resultaat
print("Duplicaat in de lijst:", duplicaat)