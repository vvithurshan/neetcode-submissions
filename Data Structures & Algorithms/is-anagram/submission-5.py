class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        d = {}

        for c in s:
            d[c] = d.get(c, 0) + 1

        for c in t:
            
            if c in d and d[c] != 0:
                d[c] -= 1

                if d[c] == 0:
                    del d[c]
            else:
                return False

        if d:
            return False
        # for k, v in d.items():
        #     if v != 0:
        #         return False

        return True