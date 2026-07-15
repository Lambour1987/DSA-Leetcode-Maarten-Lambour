#1st Approach: Bruteforce
# Time: O(n^2)
# Space:

class Solution:
    def replaceElements(self, arr: list[int]) -> list[int]:
        result = []
        n = len(arr) #zelf: niet minus 1 want we hebben het over de waarden uit de array

        for i in range(n - 1):  # Loop over alle elementen behalve de laatste. arr heeft lengte 6. Dat is indices 0 t/m 5.
            # Maar we doen nu indices 0 t/m 4. Want laatste niet nodig. Dus voor de indices minus 1. (dat is op einde array minus 2)
            max_right = max(arr[i + 1:]) if i < n - 1 else -1  # Vind het maximale element aan de rechterkant
            result.append(max_right)  # Voeg het maximale element toe aan het resultaat

        result.append(-1)
        # Voeg -1 toe voor het laatste element, aangezien er geen elementen rechts van de laatste zijn
        return result


solution_instance = Solution()

# Voorbeeldlijst
arr = [17, 18, 5, 4, 6, 1]

# Roep de methode aan om de elementen te vervangen
result = solution_instance.replaceElements(arr)

# Print de resulterende lijst
print("Resultaat:", result)