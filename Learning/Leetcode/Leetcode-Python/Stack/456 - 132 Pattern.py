#1st Approach:
# Time: O(n*2)
# Space:

#monotonicly decreasing order: maakt het makkelijker om maximum te vinden.

class Solution:
    def find132pattern(self, nums: list[int]) -> bool:
        stack = [] #pair [num, minLeft]. Dus er wordt een paartje bijgehouden.Je kan in plaats daarvan ook 2 stacks bijhouden. 1tje van de waarde van de stack en 1tje voor de minimumwaarde links van de waarde uit de eerste stack
        curMin = nums[0] #dus minimum bijhouden

        for n in nums[1:]: #dit omdat we de index niet hoeven te weten. Eerste waarde skippen we want dat is niet de k value.
            while stack and n >= stack[-1][0]: #stack[-1] is het laatste element op de lijst. [0] is het eerste element van curMin volgens mij
                stack.pop()
            if stack and n > stack[-1][1]: #[
                return True

            stack.append([n, curMin])
            curMin = min(curMin, n)

        return False

# Voorbeeld van het gebruik van find132pattern-methode
solution = Solution()

# Voorbeeld invoer
nums = [3, 1, 4, 2]

# Roep de methode find132pattern aan
pattern_found = solution.find132pattern(nums)

if pattern_found:
    print("Het 132-patroon is gevonden in de lijst.")
else:
    print("Het 132-patroon is niet gevonden in de lijst.")