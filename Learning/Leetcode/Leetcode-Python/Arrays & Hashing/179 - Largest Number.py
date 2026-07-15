#1st Approach: Greedy, Sort, Compare Values
# Time: n(logn)
# Space:

class Solution:
    def largestNumber(self, nums:list[int]) -> str:
        for i, n in enumerate(nums):
            nums[i] = str(n) #convert every number in the list to a a string

        def compare(n1, n2):
            if n1 + n2 > n2 + n1:
                return -1
            else:
                return 1

        nums = sorted(nums, key=cmp_to_key(compare)) #dit is iets wat je niet kan weten

        return str(int("".join(nums)))

# Een voorbeeld van een lijst met getallen
num_list = [3, 30, 34, 5, 9]

# Maak een instantie van de Solution-klasse
oplossing = Solution()

# Roep de largestNumber-methode aan met de lijst met getallen
resultaat = oplossing.largestNumber(num_list)

# Druk het resultaat af
print(resultaat)