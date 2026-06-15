class Solution:
    def isValid(self, s: str) -> bool:
        n = len(s)
        if n % 2 != 0:
            return False
        reverse = {
            '(' : ')',
            '[' : ']',
            '{' : '}',
        }
        start = ['(', '[', '{']
        end = [')', ']', '}']

        stack = []

        for ch in s:
            if ch in start:
                stack.append(ch)
            elif ch in end:
                if stack:
                    last = stack.pop()
                    if reverse[last] != ch:
                        return False
                else:
                    return False
        if not stack:
            return True
        return False
                    
