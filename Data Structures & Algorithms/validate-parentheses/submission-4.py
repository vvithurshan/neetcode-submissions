class Solution:
    def isValid(self, s: str) -> bool:
        
        brackets = {
            "(" : ")",
            "[" : "]",
            "{" : "}"
        }

        keys = brackets.keys()

        stack = []

        for c in s:
            if c in keys:
                stack.append(c)

            else:
                if not stack:
                    return False
                if brackets[stack.pop()] != c:
                    return False

        return not stack