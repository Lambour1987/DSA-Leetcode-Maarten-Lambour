#1st Approach: Brute Force (niet uitgewerkt)
# Time: O(n^2)
# Space:

#2nd Approach: Two Pointers
# Time: O(N)
# Space:

#Zelf: probeer met Hashmap zie LC1

class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        l, r = 0, len(numbers) - 1

        while l < r:
            curSum = numbers[l] + numbers[r]

            if curSum > target:
                r -= 1
            elif curSum < target:
                l += 1
            else:
                return [l+1, r +1]
        return []


# Een instantie van de Solution-klasse maken
solution = Solution()

# Voorbeeldlijst en doel
numbers = [2, 7, 11, 15]
target = 9

# Testen van de twoSum-methode
resultaat = solution.twoSum(numbers, target)
print(f"Indices van de twee getallen die de som {target} vormen: {resultaat}")