#1st Approach: Hashset
# Time: O(n*M)
# Space:

class Solution:
    def numUniqueEmails(self, emails: list[str]) -> int:
        unique = set()

        for e in emails:
            local, domain = e.split("@")
            local = local.split("+")[0] #we nemen alles wat voor het eerste + teken komt daarom [0]
            local = local.replace(".", "")# dus volgens mij de punt verplaatsen met "", dus eigenlijk wissen
            unique.add((local, domain))
        return len(unique)


emails = ["john.doe@example.com", "jane.doe@example.com", "john.doe+spam@example.com", "johndoe@example.com"]

solution = Solution()
result = solution.numUniqueEmails(emails)
print(result)