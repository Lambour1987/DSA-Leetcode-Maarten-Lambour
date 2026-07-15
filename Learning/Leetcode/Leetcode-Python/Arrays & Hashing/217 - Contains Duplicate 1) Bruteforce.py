#1st Approach: Brute Force (ChatGPT)
#Time: O(n^2): n is size of array
#Space: O(1): no extra memory

#Zie LC 2BF, 217BF

class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        n = len(nums) #kan ook: dit weghalen en dan neerzetten for i in range(len(nums)) en for j in range(i+1, len(nums))

        for i in range(0, n): #voor iedere indice binnen de index (=range(n)) of dus for i in range(len(nums))
            for j in range(i + 1, n): #zelf: dit is dus BF. de i begon op het eerste element van de lijst, en i + 1 op dus het tweede element tot het einde van nums (=n)
                if nums[i] == nums[j]:
                    return True

        return False

solution_instance = Solution()
example_nums = [1,2,3,4,1]
result = solution_instance.containsDuplicate(example_nums)
print(result)

