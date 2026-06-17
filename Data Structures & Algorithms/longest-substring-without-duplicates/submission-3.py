class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        l, r = 0, 0
        longest = 0
        seen = set()

        while r < len(s):
            if s[r] not in seen:
                seen.add(s[r])
                r += 1
                longest = max(longest, r - l)
            else:
                l += 1
                r = l
                seen = set()

        return longest