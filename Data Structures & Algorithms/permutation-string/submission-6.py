from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        freqS1 = Counter(s1)
        l = 0

        for r in range(len(s1), len(s2) + 1):

            freq = Counter(s2[l:r])

            if freqS1 == freq:
                return True

            l += 1


        return False