#1st Approach:
# Time:
# Space:

from collections import deque

class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        dom = list(dominoes)
        q = deque()

        for i, d in enumerate(dom):
            if d != ".":
                q.append((i, d))

        while q:
            i, d = q.popleft()

            if d == "L" and i > 0 and dom[i - 1] == ".":
                q.append((i - 1, "L"))
                dom[i - 1] = "L"
            elif d == "R" and i + 1 < len(dom) and dom[i + 1] == ".":
                if i + 2 < len(dom) and dom[i + 2] == "L":
                    q.append((i + 1, "R"))
                    dom[i + 1] = "R"
                else:
                    q.append((i + 1, "R"))
                    dom[i + 1] = "R"

        return "".join(dom)

# Voorbeeldgebruik:
dominoes_example = ".L.R...LR..L.."
solution_instance = Solution()
result = solution_instance.pushDominoes(dominoes_example)
print(result)