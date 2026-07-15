#1st Approach: Two Pointers
# Time: O(n)
# Space: O(1)

#Zelf kan je ook eerst het aantal stijgingen en dalingen bepalen en vervolgens de
# het algoritme uitvoeren.

#Keep track with boolean

class Solution:
    def checkPossibility(self, nums: list[int]) -> bool:
        changed = False

        for i in range(len(nums) -1): #zelf: had ook met enumerate gekund
            if nums[i] <= nums[i+1]: #bekijk of element kleiner is dan het volgende element
                continue
            if changed:
                return False

            #We want to decrease left element
            if i == 0 or nums[i+1] >= nums[i-1]:
                nums[i] = nums[i+1] #dus waarde op index i wordt vervangen door de waarde rechts hiervan indien de waarde links lager is dan de rechter.
            else:
                nums[i+1] = nums[i]
            changed = True
        return True

# Voorbeeldgebruik:
nums_example1 = [4, 2, 3]
solution_instance = Solution()
result1 = solution_instance.checkPossibility(nums_example1)
print(f"Kan worden aangepast met hoogstens één wijziging: {result1}")

nums_example2 = [4, 2, 1]
result2 = solution_instance.checkPossibility(nums_example2)
print(f"Kan worden aangepast met hoogstens één wijziging: {result2}")




