#1st Approach: Brute Force: Hashmap/ Hashset
# Time:
# Space:

#2nd Approach: Sliding Window
# Time: O(n): never add same element to hashset more than once
# Space: O(n) or more accurate O(k)

class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        window = set()
        L = 0

        for R in range(len(nums)):
            if R - L > k:
                window.remove(nums[L])
                L += 1
            if nums[R] in window:
                return True
            window.add(nums[R])
        return False

# Een instantie van de Solution-klasse maken
solution = Solution()

# Voorbeeld array en afstand
nums = [1, 2, 3, 1, 2, 3]
k = 2

# Testen van de containsNearbyDuplicate-methode
resultaat = solution.containsNearbyDuplicate(nums, k)
print(f"Bevat de array duplicaten binnen een afstand van {k}? {resultaat}")