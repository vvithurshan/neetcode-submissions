from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        n = len(s1)
        l, r = 0, n
        target = Counter(s1)

        while r <= len(s2):
            if Counter(s2[l:r]) == target:
                return True

            l += 1
            r += 1

        return False