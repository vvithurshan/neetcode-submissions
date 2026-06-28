class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        oprs = set(["+", "-", "*", "/"])

        stack = []

        for t in tokens:

            if t in oprs:
                res = 0
                val2 = stack.pop() 
                val1 = stack.pop()

                if t == "+":
                    res = val1 + val2

                elif t == "-":
                    res = val1 - val2

                elif t == "*":
                    res = val1 * val2

                else:
                    res = int(val1 / val2)

                stack.append(res)

            else:
                stack.append(int(t))

        return stack[-1]