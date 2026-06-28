class Solution:
    def isValid(self, s: str) -> bool:
        
        map = {
            '(' : ')',
            '{' : '}',
            '[' : ']'
        }

        closed = list(map.values())

        stack = []

        for c in s:

            if c in map:
                stack.append(c)

            elif c in closed:
                if stack:
                    val = stack.pop()

                    if c != map[val]:
                        return False

                else:
                    return False
        
        if stack:
            return False
        
        return True