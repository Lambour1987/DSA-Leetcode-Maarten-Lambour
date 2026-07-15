#1st Approach: Stack, List
# Time: O(2*n) --> O(n)
# Space:

class Solution:
    def evalRPN(self, tokens:list[str]) -> int:
        stack = []
        for c in tokens:
            if c == "+":
                stack.append(stack.pop() + stack.pop())
            elif c == "-":
                a, b = stack.pop(), stack.pop()
                stack.append(b - a)
            elif c == "*":
                stack.append(stack.pop()*stack.pop())
            elif c == "/":
                a, b = stack.pop(), stack.pop()
                stack.append(int(b / a))
            else:
                stack.append(int(c))
        return stack[0]

# Een voorbeeld van een lijst met RPN-tokens
rpn_tokens = ["2", "1", "+", "3", "*"]

# Maak een instantie van de Solution-klasse
oplossing = Solution()

# Roep de evalRPN-methode aan met de lijst met tokens
resultaat = oplossing.evalRPN(rpn_tokens)

# Druk het resultaat af
print(resultaat)