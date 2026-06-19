class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack = []
        opr = set(["+", "-", "*", "/"])

        for token in tokens:
            if token not in opr:
                stack.append(int(token))

            else:
                val2 = stack.pop()
                val1 = stack.pop()

                res = None
                if token == "+":
                    res = val1 + val2

                elif token == "-":
                    res = val1 - val2

                elif token == "*":
                    res = val1 * val2

                else:
                    res = val1 / val2

                stack.append(int(res))

        return stack[-1]