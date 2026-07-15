class Solution:
    def numOfSubarrays(self, arr:list[int], k: int, threshold:int) -> int:
        res = 0
        curSum = sum(arr[:k-1])

        for L in range(len(arr) - k + 1):
            curSum += arr[L + k - 1]
            if (curSum / k) >= threshold:
                res += 1
            curSum -= arr[L]
        return res

# Voorbeeldarray
arr = [2, 1, 3, 4, 1, 2, 5, 3]
# Parameters
k = 3
threshold = 3

# Maak een instantie van Solution
solution = Solution()

# Roep de numOfSubarrays-methode aan om het aantal subarrays te verkrijgen
resultaat = solution.numOfSubarrays(arr, k, threshold)

# Druk het resultaat af
print(f"Aantal subarrays waarvan het gemiddelde groter is dan of gelijk is aan {threshold}: {resultaat}")