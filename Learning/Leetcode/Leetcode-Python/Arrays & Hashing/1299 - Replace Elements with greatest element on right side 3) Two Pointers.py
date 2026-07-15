# 3st Approach: Bruteforce
# Time: O(n)
# Space:

class Solution:
    def replaceElements(self, arr: list[int]) -> list[int]:
        n = len(arr)
        right_max = -1

        for i in range(n - 1, -1, -1):  # Loop achteruit door de lijst
            temp = arr[i]  # Tijdelijk opslaan van het huidige element
            arr[i] = right_max  # Vervang het huidige element door het rechter maximum
            right_max = max(right_max, temp)  # Update het rechter maximum

        return arr


solution_instance = Solution()

# Voorbeeldlijst
arr = [17, 18, 5, 4, 6, 1]

# Roep de methode aan om de elementen te vervangen
result = solution_instance.replaceElements(arr)

# Print de resulterende lijst
print("Resultaat:", result)