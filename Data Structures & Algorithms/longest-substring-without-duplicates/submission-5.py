class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        res = 0

        l, r = 0, 0
        n = len(s)

        while r < n:

            numSet = set()
            
            while r < n and s[r] not in numSet:
                numSet.add(s[r])
                r += 1
            res = max(res, (r - l))
            l += 1 # I previously used l = r
            r = l

        return res