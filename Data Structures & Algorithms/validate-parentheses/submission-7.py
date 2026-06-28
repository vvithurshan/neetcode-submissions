class Solution:
    def isValid(self, s: str) -> bool:
        
        map = {
            '(' : ')',
            '{' : '}',
            '[' : ']'
        }

        stack = []

        for c in s:

            if c in map:
                stack.append(c)

            else:
                if stack:
                    val = stack.pop()

                    if c != map[val]:
                        return False

                else:
                    return False
        
        if stack:
            return False
        
        return True