# 2st Approach: Reverse order, basecase (zelf: DP?, soort van greedy ook zie chatgpt)
# Time: O(n)
# Space:

#zelf kan ook met 2 pointers?

class Solution:
    def replaceElements(self, arr: list[int]) -> list[int]:
        # initial max = -1
        # reverese iteration
        # new max = max(oldmax, arr[i])

        rightMax = -1

        for i in range(len(arr) -1, -1, -1): #eerste -1 is de laatste index, 2e -1 is beginpunt(tm index 0), 3e is stapgrootte
            newMax = max(rightMax, arr[i]) # bereken maximale waarde tussen rightMax en de plek waar de i nu is
            arr[i] = rightMax
            rightMax = newMax
        return arr

solution_instance = Solution()

# Voorbeeldlijst
arr = [17, 18, 5, 4, 6, 1]

# Roep de methode aan om de elementen te vervangen
result = solution_instance.replaceElements(arr)

# Print de resulterende lijst
print("Resultaat:", result)