class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        if len(s) == 1:
            return 1
        maxL = 0
        i = 0
        l = 1

        while l < len(s):
            if len(set(s[i:l+1])) == len(s[i:l+1]):
                maxL = max(maxL, l - i)
                l += 1
            elif i < l:
                i += 1
                l += 1
        return maxL + 1
        