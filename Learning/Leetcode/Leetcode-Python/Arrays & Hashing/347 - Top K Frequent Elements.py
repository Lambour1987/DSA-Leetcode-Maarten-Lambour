#1st Approach: Bucket Sort, Max Heap/ Heapify
# Time: k*logn is beter dan n logn of O(n) bij bucket sort
# Space: O(1) volgens mij of O(n) bij Bucket sort

#Zelf: kan een hashset ook? Aantal tellen in de max set

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        count = {} #hashmap
        freq = [[] for i in range(len(nums)+1)]

        for n in nums:
            count[n] = 1 + count.get(n,0)
        for n, c in count.items(): #dit is de items uit de hashmap halen
            freq[c].append(n)

        res = []
        for i in range(len(freq) -1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res

example = Solution()
nums = [1, 1, 1, 2, 2, 3]
k = 2

result = example.topKFrequent(nums, k)
print(result)