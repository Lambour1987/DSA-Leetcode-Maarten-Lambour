#1st Approach: Recursive Solution
# Time:
# Space:

#Subproblems (namelijk 2[a3[bc]]. 3[bc] is een subproblem
# Wel lastig maar wel een goede

class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for i in range(len(s)): #(zelf index nu wel belangrijk daarom range?)
            if s[i] != "]":
                stack.append(s[i])
            else:
                substr = ""
                while stack[-1] != "[":
                    substr = stack.pop() + substr
                stack.pop()

                k = ""
                while stack and stack[-1].isdigit():
                    k = stack.pop() + k
                stack.append(int(k) * substr)

        return "".join(stack)


# Voorbeeld van het gebruik van de decodeString-methode
solution = Solution()

# Voorbeeld invoer
encoded_string = "3[a2[b]c]"

# Roep de methode decodeString aan
decoded_string = solution.decodeString(encoded_string)

print("Gecodeerde string:", encoded_string)
print("Gedecodeerde string:", decoded_string)




