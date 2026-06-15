class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = 0
        ans = 0
        hash = set()

        for r in range(len(s)):
            
            while s[r] in hash:
                hash.remove(s[l])
                l += 1
            hash.add(s[r])
            ans = max(r - l + 1, ans)

        return ans