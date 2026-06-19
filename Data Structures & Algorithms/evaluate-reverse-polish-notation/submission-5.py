class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack = []
        opr = set(["+", "-", "*", "/"])

        for token in tokens:
            if token not in opr:
                stack.append(token)

            else:
                val2 = int(stack.pop())
                val1 = int(stack.pop())

                res = None
                if token == "+":
                    res = val1 + val2

                elif token == "-":
                    res = val1 - val2

                elif token == "*":
                    res = val1 * val2

                else:
                    res = val1 / val2

                stack.append(res)

        return int(stack[-1])