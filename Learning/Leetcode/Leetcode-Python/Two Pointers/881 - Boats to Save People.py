#1st Approach: Greedy, sort
# Time:
# Space:

class Solution:
    def numRescueBoats(self, people: list[int], limit: int) -> int:
        people.sort()

        res = 0 #boats
        l, r = 0, len(people) -1
        while l <= r:
            remain = limit - people[r]
            r -= 1
            res += 1
            if l <=r and remain >= people[l]:
                l += 1

        return res

solution = Solution()
people_example = [3, 2, 2, 1]
limit_example = 3
result = solution.numRescueBoats(people_example, limit_example)
print(result)