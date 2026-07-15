#1st Approach: Hashset
# Time: O(n*M)
# Space:

class Solution:
    def numUniqueEmails(self, emails: list[str]) -> int:
        unique = set()

        for e in emails:
            i, local = 0, "" #Index i start op 0, local op "", dus lege string
            while e[i] not in ["@","+"]:
                if e[i] != ".":
                    local += e[i]
                i += 1

            while e[i] != "@":
                i += 1
            domain = e[i+1:]
            unique.add((local, domain))

        return len(unique)

emails = ["john.doe@example.com", "jane.doe@example.com", "john.doe+spam@example.com", "johndoe@example.com"]

solution = Solution()
result = solution.numUniqueEmails(emails)
print(result)

